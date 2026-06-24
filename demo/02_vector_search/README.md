# 02. Azure AI Search Vector Search

샘플 문서 3개를 벡터로 저장하고, 질문과 의미가 가까운 문서를 찾는 예제입니다.

## 실행 방법

```bash
pip install -r ../requirements.txt
python vector_search_demo.py
```

## 코드에서 채울 값

`vector_search_demo.py` 맨 위의 값만 바꾸면 됩니다.

```python
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com/"
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "text-embedding-3-large"

AZURE_SEARCH_ENDPOINT = "https://YOUR-SEARCH-SERVICE.search.windows.net"
AZURE_SEARCH_API_KEY = "YOUR_AZURE_SEARCH_ADMIN_KEY"
```

## 실행 흐름

1. 문서 내용을 Azure OpenAI Embedding Model로 벡터화합니다.
2. Azure AI Search에 벡터 필드가 있는 인덱스를 만듭니다.
3. 샘플 문서를 업로드합니다.
4. 검색어도 벡터로 바꾼 뒤, 가장 가까운 문서를 찾습니다.

## 차원 설정

```python
EMBEDDING_DIMENSIONS = 3072
```

- `text-embedding-3-large` 기본 차원: 3072
- `text-embedding-3-small` 기본 차원: 1536

사용하는 embedding 모델 차원과 Search 인덱스의 `EMBEDDING_DIMENSIONS` 값이 다르면 오류가 납니다.

## 공식 튜토리얼

- Azure AI Search Vector Search Quickstart  
  https://learn.microsoft.com/en-us/azure/search/search-get-started-vector

- Python Vector Search 샘플  
  https://learn.microsoft.com/en-us/samples/azure-samples/azure-search-python-samples/python-vector-quickstart/
