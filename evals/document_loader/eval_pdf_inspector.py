import pdf_inspector

# INPUT_PATH = "data/VenuedigitalBrochure.pdf"
# INPUT_PATH = "data/new-tata-punch-brochure.pdf"
INPUT_PATH = "data/Nexon-brochure-may.pdf"
# INPUT_PATH = "data/xpres-brochure.pdf"
OUTPUT_PATH = "evals/document_loader/output/pdf_inspector-2.txt"

result = pdf_inspector.process_pdf(INPUT_PATH)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:

    f.write("=" * 80 + "\n")
    f.write("MARKDOWN CONTENT\n")
    f.write("=" * 80 + "\n\n")

    f.write(result.markdown or "")

print(f"Output saved to: {OUTPUT_PATH}")