# AI Car Research & Comparison Assistant

A **RAG-based AI assistant** that helps car buyers and sales representatives research and compare cars using official car brochure PDFs.

## Why This Project?

Car brochures contain a large amount of information across different **models, variants, and trims**. Remembering all the **specifications, features, and variant-level differences** can be difficult.
This can be especially challenging for **car buyers** comparing multiple cars and for **sales representatives** who need to quickly answer customer questions.

## Why RAG?

Users can upload a car brochure to an LLM and ask questions, but processing the **entire document for every query** can be slow and inefficient.
RAG solves this by retrieving only the **relevant information** from the selected brochures and providing it to the LLM before generating an answer. This makes the process more efficient and allows the assistant to provide **page-level citations**.

## How This Project Works

1. Upload a **car brochure PDF**.
2. Extract and chunk the content, generate **embeddings**, and store them in a **vector database**.
3. Select one or more **previously indexed brochures** for the current chat.
4. Ask a question or compare **cars, features, specifications, or variants**.
5. Retrieve the **most relevant chunks** from the selected brochures.
6. Provide the retrieved context to the **LLM** to generate an answer with **page-level citations**.

### Overall Flow

```text
                    Upload PDF
                        ↓
                 Extract Content
                        ↓
                  Chunk Documents
                        ↓
                 Generate Embeddings
                        ↓
                 Store in Vector DB
                        ↓
              ┌─────────────────────┐
              │ Previously Indexed  │
              │      Brochures      │
              └──────────┬──────────┘
                         ↓
                Select Brochures
                    for Chat
                         ↓
                    User Query
                         ↓
                     Retrieval
                         ↓
                Relevant Chunks
                         ↓
                       LLM
                         ↓
                Answer + Citations
```

## Technology Stack

- Document Loader: PDFPlumber
- Embeddings: TBD
- Vector Database: TBD
- LLM: TBD
- Backend: TBD