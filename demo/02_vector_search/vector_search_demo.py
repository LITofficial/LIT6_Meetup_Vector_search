from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SimpleField,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
)
from azure.search.documents.models import VectorizedQuery

# 1) Azure OpenAI 설정
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com/"
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "text-embedding-3-large"  # Azure에서 만든 배포 이름
AZURE_OPENAI_API_VERSION = "2024-02-01"
EMBEDDING_DIMENSIONS = 3072  # text-embedding-3-large 기본값. small이면 보통 1536

# 2) Azure AI Search 설정
AZURE_SEARCH_ENDPOINT = "https://YOUR-SEARCH-SERVICE.search.windows.net"
AZURE_SEARCH_API_KEY = "YOUR_AZURE_SEARCH_ADMIN_KEY"
INDEX_NAME = "movie-vector-demo"

# 3) 검색해볼 샘플 데이터
DOCUMENTS = [
    {"id": "1", "title": "혼밥 브이로그", "content": "밥 먹을 때 편하게 보기 좋은 잔잔한 일상 영상"},
    {"id": "2", "title": "AI 논문 리뷰", "content": "최신 인공지능 논문을 자세히 분석하는 기술 영상"},
    {"id": "3", "title": "고양이 구조 이야기", "content": "길고양이를 구조하고 돌보는 따뜻한 동물 영상"},
]
QUERY = "밥 먹으면서 틀어놓기 좋은 영상"

openai_client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)
search_credential = AzureKeyCredential(AZURE_SEARCH_API_KEY)


def get_embedding(text):
    response = openai_client.embeddings.create(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=text,
    )
    return response.data[0].embedding


def create_index():
    fields = [
        SimpleField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(name="title", type=SearchFieldDataType.String),
        SearchableField(name="content", type=SearchFieldDataType.String),
        SearchField(
            name="content_vector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=EMBEDDING_DIMENSIONS,
            vector_search_profile_name="vector-profile",
        ),
    ]

    vector_search = VectorSearch(
        algorithms=[HnswAlgorithmConfiguration(name="hnsw")],
        profiles=[VectorSearchProfile(name="vector-profile", algorithm_configuration_name="hnsw")],
    )

    index = SearchIndex(name=INDEX_NAME, fields=fields, vector_search=vector_search)
    index_client = SearchIndexClient(AZURE_SEARCH_ENDPOINT, search_credential)
    index_client.create_or_update_index(index)


def upload_documents():
    search_client = SearchClient(AZURE_SEARCH_ENDPOINT, INDEX_NAME, search_credential)

    docs = []
    for doc in DOCUMENTS:
        docs.append({
            **doc,
            "content_vector": get_embedding(doc["content"]),
        })

    search_client.upload_documents(docs)


def search():
    search_client = SearchClient(AZURE_SEARCH_ENDPOINT, INDEX_NAME, search_credential)
    query_vector = get_embedding(QUERY)

    vector_query = VectorizedQuery(
        vector=query_vector,
        k_nearest_neighbors=3,
        fields="content_vector",
    )

    results = search_client.search(
        search_text=None,
        vector_queries=[vector_query],
        select=["title", "content"],
    )

    print("검색어:", QUERY)
    for result in results:
        print("-", result["title"], "/ score:", result["@search.score"])
        print(" ", result["content"])


create_index()
upload_documents()
search()
