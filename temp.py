from src.document_loader import load_document
from src.chunking import chunking
from src.embeddings import create_embeddings

pages = load_document(r"C:\Users\SOFT LAPTOP\OneDrive - Faculty Of Engineering (Tanta University)\Desktop\self-study\courses\legal-document-intelligence-rag\Legal_Document\integralversionprinciples2010-e.pdf")

chunks = chunking(pages)
print(len(chunks))
print(chunks[:2])
create_embeddings(chunks)