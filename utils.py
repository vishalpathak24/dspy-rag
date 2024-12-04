from typing import List
from langchain_community.embeddings import LlamaCppEmbeddings

# NOTE: Need this fix GUFF files of LLAMA-3

# json.dumps(embd['data'][0]['embedding'])

class LlamaCppEmbeddingsFix(LlamaCppEmbeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = self.client.create_embedding(texts)
        return [ list(map(float, d['embedding'][0])) for d in embeddings['data']]

    def embed_query(self, text: str) -> List[float]:
        embedding = self.client.embed(text)[0]
        return list(map(float, embedding))