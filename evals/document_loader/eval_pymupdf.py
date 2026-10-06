import pymupdf

INPUT_PATH = "data/xpres-brochure.pdf"
OUTPUT_PATH = "evals/document_loader/output/pymupdf.txt"

pdf = pymupdf.open(INPUT_PATH)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:

    f.write(f"Total Pages: {len(pdf)}\n\n")

    for i, page in enumerate(pdf):
        f.write("=" * 80 + "\n")
        f.write(f"PAGE {i + 1}\n")
        f.write("=" * 80 + "\n\n")

        f.write("CONTENT:\n")
        f.write(page.get_text())
        f.write("\n\n")

pdf.close()