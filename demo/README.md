# Azure OpenAI Embedding + Azure AI Search Vector Search 튜토리얼

비전공자도 실행해볼 수 있도록 최대한 짧게 만든 Python 예제입니다.

기존 데모 전체를 올리는 대신, 핵심 흐름만 분리했습니다.

1. 텍스트를 embedding vector로 바꾸기
2. vector를 Azure AI Search에 저장하고 검색하기

## 폴더 구조

```text
azure-vector-search-python-tutorial/
├─ README.md
├─ requirements.txt
├─ 01_embedding_model/
│  ├─ README.md
│  └─ embedding_demo.py
└─ 02_vector_search/
   ├─ README.md
   └─ vector_search_demo.py
```

## 준비물

- Python 3.10 이상 권장
- Azure OpenAI 리소스
- Azure OpenAI embedding model 배포
  - 예: `text-embedding-3-large`
- Azure AI Search 서비스

## 설치

VS Code 터미널에서 실행합니다.

```bash
pip install -r requirements.txt
```

## 01. Embedding Model만 실행하기

```bash
cd 01_embedding_model
python embedding_demo.py
```

`embedding_demo.py` 맨 위의 값만 본인 Azure 값으로 바꾸면 됩니다.

```python
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com/"
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "text-embedding-3-large"
```

실행하면 문장이 몇 차원짜리 벡터로 바뀌었는지 확인할 수 있습니다.

## 02. Vector Search 실행하기

```bash
cd 02_vector_search
python vector_search_demo.py
```

`vector_search_demo.py` 맨 위의 Azure OpenAI 값과 Azure AI Search 값을 채우면 됩니다.

```python
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com/"
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "text-embedding-3-large"

AZURE_SEARCH_ENDPOINT = "https://YOUR-SEARCH-SERVICE.search.windows.net"
AZURE_SEARCH_API_KEY = "YOUR_AZURE_SEARCH_ADMIN_KEY"
```

실행하면 샘플 문서 3개가 Azure AI Search에 저장되고, 검색어와 의미가 가장 가까운 문서를 찾아줍니다.

## 주의

이 코드는 발표/수업/튜토리얼용으로 일부러 단순하게 만들었습니다.

GitHub에 공개할 때는 실제 API Key를 절대 올리면 안 됩니다.  
공개 저장소에는 아래처럼 빈 값이나 예시 값만 남겨두는 것을 권장합니다.

```python
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
AZURE_SEARCH_API_KEY = "YOUR_AZURE_SEARCH_ADMIN_KEY"
```

실제 서비스에서는 `.env`, Key Vault, GitHub Secrets 같은 방식을 사용하는 게 더 안전합니다.

## 공식 Azure 문서

### Azure OpenAI Embedding

- Azure OpenAI Embeddings 사용법  
  https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/embeddings

- Azure OpenAI Embeddings 튜토리얼  
  https://learn.microsoft.com/en-us/azure/foundry/openai/tutorials/embeddings

### Azure AI Search Vector Search

- Azure AI Search Vector Search Quickstart  
  https://learn.microsoft.com/en-us/azure/search/search-get-started-vector

- Python Vector Search 샘플  
  https://learn.microsoft.com/en-us/samples/azure-samples/azure-search-python-samples/python-vector-quickstart/

- Azure AI Search Python SDK  
  https://learn.microsoft.com/en-us/python/api/overview/azure/search-documents-readme?view=azure-python
