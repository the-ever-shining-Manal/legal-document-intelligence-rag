
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle as pkl


model=SentenceTransformer("all-MiniLM-L6-v2")
index=faiss.read_index("vectorstore/legal_index.faiss")
with open("vectorstore/chunks.pkl","rb") as f:
        chunks=pkl.load(f)


def retriver(query,k=5):
    embeddings= model.encode([query])
    embeddings_np=np.array(embeddings).astype(np.float32)
    faiss.normalize_L2(embeddings_np)

    score, indices= index.search(embeddings_np,k)

    results=[]
    for idx in indices[0]:
        results.append(chunks[idx])
    return results
