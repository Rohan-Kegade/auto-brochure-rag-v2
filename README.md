# AI Car Research & Comparison Assistant

A RAG-based AI assistant that helps car buyers and sales representatives research and compare cars using official car brochure PDFs.

## Why This Project?

Car brochures contain a large amount of information across different models, variants, and trims. Remembering all the specifications, features, and variant-level differences can be difficult.

This can be especially challenging for car buyers comparing multiple cars and for sales representatives who need to quickly answer customer questions.

## Why RAG?

Users can upload a car brochure to an LLM and ask questions, but processing the entire document for every query can be slow and inefficient.

RAG solves this by retrieving only the relevant information from the selected brochures and providing it to the LLM before generating an answer. This makes the process more efficient and allows the assistant to provide answers with page-level citations.

## How This Project Works

### 1. Upload Brochure

The user uploads a car brochure PDF.

### 2. Process & Store

The PDF is processed to extract its content, which is split into smaller chunks. These chunks are converted into embeddings and stored in a vector database.

### 3. Select Brochures

Users can add previously uploaded and indexed brochures to the current chat context. This allows them to research or compare cars without uploading the same brochures again.

### 4. User Query

The user asks a question about a car or compares multiple cars.

### 5. Retrieve Relevant Information

The query is used to search the selected brochures and retrieve the most relevant chunks.

### 6. Generate Answer

The retrieved information is provided to the LLM along with the user's question. The LLM generates an answer based on the retrieved context and provides relevant page-level citations.

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
              │     Brochures       │
              └──────────┬──────────┘
                         ↓
              Select Brochures for Chat
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