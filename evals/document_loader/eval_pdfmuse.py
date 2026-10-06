from langchain_pdfmuse import PdfmuseLoader

INPUT_PATH = "data/VenuedigitalBrochure.pdf"
# INPUT_PATH = "data/new-tata-punch-brochure.pdf"
OUTPUT_PATH = "evals/document_loader/output/pdfmuse-4.txt"

loader = PdfmuseLoader(INPUT_PATH, mode="elements")

docs = loader.load()

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:

    f.write(f"Total Documents: {len(docs)}\n\n")

    for i, doc in enumerate(docs):
        f.write("=" * 80 + "\n")
        f.write(f"DOCUMENT {i + 1}\n")
        f.write("=" * 80 + "\n\n")

        f.write("METADATA:\n")
        f.write(str(doc.metadata))
        f.write("\n\n")

        f.write("CONTENT:\n")
        f.write(doc.page_content)
        f.write("\n\n")

print(f"Output saved to: {OUTPUT_PATH}")