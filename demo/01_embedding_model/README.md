# 01. Azure OpenAI Embedding Model

텍스트를 숫자 벡터로 바꿔보는 가장 작은 예제입니다.

## 실행 방법

```bash
pip install -r ../requirements.txt
python embedding_demo.py
```

## 코드에서 채울 값

`embedding_demo.py` 맨 위의 값만 바꾸면 됩니다.

```python
AZURE_OPENAI_ENDPOINT = "https://YOUR-RESOURCE-NAME.openai.azure.com/"
AZURE_OPENAI_API_KEY = "YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = "text-embedding-3-large"
```

주의: `AZURE_OPENAI_EMBEDDING_DEPLOYMENT`는 모델명이 아니라 Azure에서 직접 만든 **배포 이름**입니다.

## 공식 튜토리얼

- Azure OpenAI Embeddings 사용법  
  https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/embeddings

- Azure OpenAI Embeddings 튜토리얼  
  https://learn.microsoft.com/en-us/azure/foundry/openai/tutorials/embeddings
