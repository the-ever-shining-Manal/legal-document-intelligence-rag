# ⚖️ LegalRAG - Legal Document Intelligence System

A Retrieval-Augmented Generation (RAG) application for analyzing large legal documents.

This project allows users to:

- Ask questions about a legal document
- Retrieve relevant legal articles using semantic search
- Generate grounded answers with citations
- Extract Risks, Dates, and Stakeholders automatically
- Analyze 500+ page legal documents efficiently

---

## 🚀 Features

### 📄 Legal Document Processing

- PDF extraction using PyMuPDF
- Structure-aware legal chunking
- Article-level chunk generation
- Metadata preservation:
  - Chapter
  - Section
  - Article
  - Page Number

### 🧠 Semantic Search

- Sentence Transformers embeddings
- FAISS vector database
- Similarity-based retrieval

### 🤖 RAG Question Answering

- Gemini 1.5 Flash
- Grounded responses
- Page citations
- Article citations
- Hallucination reduction

### 📊 Summary Dashboard

Automatically extracts:

- Risks
- Important Dates
- Stakeholders

from retrieved legal content.

---

## 🏗️ Project Architecture

```text
PDF Document
      │
      ▼
Document Loader
      │
      ▼
Legal Chunking
      │
      ▼
Embeddings Generation
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Gemini 1.5 Flash
      │
      ▼
Answer + Dashboard
```

---

## 📂 Project Structure

```text
LegalRAG-Document-Analyzer/

├── app.py
├── requirements.txt
├── README.md

├── data/
│   └── legal_document.pdf

├── src/
│   ├── document_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retriver.py
│   ├── qa_system.py
│   └── dashboard.py

├── vectorstore/
│   ├── legal_index.faiss
│   └── chunks.pkl

└── screenshots/
```

---

## ⚙️ Technologies Used

### AI & NLP

- Google Gemini 1.5 Flash
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database

- FAISS

### PDF Processing

- PyMuPDF (fitz)

### Frontend

- Streamlit

### Programming Language

- Python

---

## 🔍 RAG Workflow

### Step 1: Document Loading

The PDF is extracted page-by-page.

### Step 2: Legal Chunking

The system identifies:

- Chapters
- Sections
- Articles
- Titles

and creates structured chunks.

### Step 3: Embedding Generation

Each chunk is converted into a vector representation using:

```python
all-MiniLM-L6-v2
```

### Step 4: Vector Storage

Embeddings are stored inside a FAISS index.

### Step 5: Retrieval

For a user query:

1. Query is embedded
2. Top-k relevant chunks are retrieved
3. Relevant legal text is returned

### Step 6: Question Answering

Gemini receives:

- User question
- Retrieved chunks

and generates a grounded answer.

### Step 7: Dashboard Extraction

Gemini extracts:

- Risks
- Dates
- Stakeholders

from the retrieved legal context.

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/LegalRAG-Document-Analyzer.git
```

Move into the project:

```bash
cd LegalRAG-Document-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Running the Project

Generate embeddings:

```bash
python create_vectorstore.py
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Question Answering

Add screenshot here.

### Retrieval Results

Add screenshot here.

### Dashboard

Add screenshot here.

---

## 🎯 Example Query

```text
What is freedom of contract?
```

Example Output:

```text
Article 1.1 (Freedom of Contract)

Page 53

The parties are free to enter into a contract and determine its content.
```

---

## 📈 Future Improvements

- Hybrid Search (BM25 + FAISS)
- Legal Entity Recognition
- Clause Classification
- Multi-document RAG
- Legal Risk Scoring
- Interactive Dashboard Visualizations

---

## 👨‍💻 Author

Developed as part of the DecodeLabs AI Internship Program.

Focus Areas:

- Retrieval-Augmented Generation (RAG)
- Legal AI
- Document Intelligence
- Large Language Models
- Semantic Search
