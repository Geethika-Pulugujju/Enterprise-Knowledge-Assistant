# Enterprise Knowledge Assistant – RAG-Based Chatbot

## Project Overview

The **Enterprise Knowledge Assistant** is a Retrieval-Augmented Generation (RAG)-based chatbot designed to answer questions using information retrieved from organizational documents. Instead of relying only on a language model's general knowledge, the system retrieves relevant document passages and uses them to generate context-aware answers.

The project demonstrates how document processing, semantic search, keyword retrieval, reranking, and a Large Language Model (LLM) can work together to build a document-grounded question-answering system.

## Objectives

- Build a chatbot that answers questions based on uploaded organizational documents.
- Retrieve relevant information using semantic and keyword-based search.
- Improve retrieval quality through result fusion and reranking.
- Generate context-aware responses using a Large Language Model.
- Provide source and page references to help users verify answers.

## Technologies Used

- **Programming Language:** Python
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Vector Database:** Qdrant
- **Embeddings:** Sentence Transformers
- **Retrieval:** Dense Retrieval and BM25 Keyword Retrieval
- **Ranking:** Reciprocal Rank Fusion (RRF) and Cross-Encoder Reranking
- **LLM:** Groq API with a supported language model
- **Document Processing:** PyPDF

## System Architecture

1. **Document Ingestion:** Load organizational PDF documents.
2. **Text Extraction:** Extract text from PDF files.
3. **Text Chunking:** Divide extracted text into smaller, manageable passages.
4. **Embedding Generation:** Convert text chunks into vector embeddings.
5. **Vector Storage:** Store embeddings and associated metadata in Qdrant.
6. **Query Processing:** Convert the user's question into a searchable representation.
7. **Hybrid Retrieval:** Combine dense semantic retrieval with BM25 keyword retrieval.
8. **Result Fusion:** Apply Reciprocal Rank Fusion (RRF) to combine retrieval results.
9. **Reranking:** Use a cross-encoder to improve the relevance of retrieved passages.
10. **Answer Generation:** Send the question and relevant context to the LLM.
11. **Source References:** Return the generated answer with available source and page information.
12. **User Interface:** Allow users to interact with the chatbot through Streamlit.

## Key Features

- Document-based question answering
- PDF text extraction and chunking
- Semantic and keyword-based hybrid search
- Reciprocal Rank Fusion for combining retrieval results
- Cross-encoder reranking
- Context-grounded answer generation
- Source and page references, where available
- Modular Python implementation

## Project Structure

```text
Enterprise-Knowledge-Assistant/
├── backend/
│   └── app/
├── data/
├── frontend/
├── hybrid_retriever.py
├── index_documents.py
├── reranker.py
├── test_chunk_embeddings.py
├── test_embeddings.py
├── test_hybrid.py
├── test_reranker.py
├── test_retrieval.py
└── .gitignore
```

## How It Works

When a user asks a question, the system retrieves relevant passages from the indexed documents. Dense retrieval finds semantically similar passages, while BM25 searches for keyword matches. Reciprocal Rank Fusion combines the results, and a cross-encoder reranks the candidates. The most relevant passages are then provided as context to the language model to generate a grounded response.

## Current Status

The project repository contains the core document-processing, retrieval, and reranking components. The complete execution workflow depends on the configured environment, dependencies, API credentials, and available document data.

## Future Enhancements

- Support for additional document formats.
- Improved document upload and management.
- User authentication and access control.
- Evaluation of retrieval quality and answer accuracy.
- Conversation history and feedback collection.
- Enhanced source citations and document-level filtering.

## Author

**Geethika Pulugujju**

B.Tech – Computer Science and Engineering
