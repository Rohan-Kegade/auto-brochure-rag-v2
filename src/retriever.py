import pdfplumber
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

INPUT_PATH = "data/VenuedigitalBrochure.pdf"
DB_PATH = "chroma_db/"
COLLECTION_NAME = "car_brochure_collection"


def extract_text_from_pdf(pdf_path: str):

    documents = []

    with pdfplumber.open(pdf_path) as pdf:

        for i, page in enumerate(pdf.pages):

            text = page.extract_text()
            if text:
                doc = Document(
                    page_content=text,
                    metadata={
                        "source": pdf_path,
                        "page_number": i + 1,
                        "total_pages": len(pdf.pages),
                    },
                )
                documents.append(doc)

    return documents


def build_vector_store(documents: list[Document]):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
    )

    chunks = text_splitter.split_documents(documents=documents)

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=DB_PATH,
    )

    return vector_store


def build_retriever():

    docs = extract_text_from_pdf(INPUT_PATH)

    vector_store = build_vector_store(docs)

    retriever = vector_store.as_retriever(search_kwargs={"k": 5})

    return retriever


if __name__ == "__main__":

    retriever = build_retriever()

    query = "What are feature of HX5 variant"

    retrieved_docs = retriever.invoke(query)

    for idx, doc in enumerate(retrieved_docs, start=1):
        print("-"*40)
        print(doc.page_content)