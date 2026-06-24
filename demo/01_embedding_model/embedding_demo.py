from openai import AzureOpenAI

# 1) Azure Portal에서 복사해서 여기에 붙여넣기
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com/"
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "text-embedding-3-large"  # Azure에서 만든 임베딩 모델 배포 이름
AZURE_OPENAI_API_VERSION = "2024-02-01"

# 2) 벡터로 바꿔볼 문장
TEXT = "밥 먹을 때 보기 좋은 주제"

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

response = client.embeddings.create(
    model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    input=TEXT,
)

embedding = response.data[0].embedding

print("입력 문장:", TEXT)
print("벡터 차원:", len(embedding))
print("앞부분 10개 값:", embedding[:10])
