from  sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle as pkl


model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    text=[chunk["text"] for chunk in chunks]
    embeddings=model.encode(text)
    embeddings_np=np.array(embeddings).astype("float32")
    faiss.normalize_L2(embeddings_np)
    dimension=embeddings_np.shape[1]

    index=faiss.IndexFlatIP(dimension)

    index.add(embeddings_np)

    faiss.write_index(index,"vectorstore/legal_index.faiss")
    with open("vectorstore/chunks.pkl","wb") as f:
        pkl.dump(chunks,f)

    print("DONE EMBEDDINGS....")



