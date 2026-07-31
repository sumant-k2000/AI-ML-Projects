# RAG Chatbot (Capstone Project)

## Objective

Build a Retrieval-Augmented Generation (RAG) chatbot capable of answering questions from a PDF document using LangChain, FAISS, Hugging Face Transformers, and Sentence Transformers.

## Dataset

Custom PDF document uploaded by the user.

## Technologies Used

- Python
- LangChain
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- PyPDF
- Google Colab

## Methodology

1. Upload PDF
2. Load PDF
3. Split document into chunks
4. Generate embeddings
5. Store embeddings in FAISS
6. Retrieve relevant document chunks
7. Generate answers using a language model

## Result

The chatbot successfully retrieves relevant information from the uploaded document and generates answers based on the document content.

## Conclusion

This project demonstrates how Retrieval-Augmented Generation (RAG) improves question answering by combining semantic search with a language model. Using FAISS for vector search and document embeddings enables efficient retrieval of relevant information, making the chatbot more accurate and context-aware than relying solely on a language model.
