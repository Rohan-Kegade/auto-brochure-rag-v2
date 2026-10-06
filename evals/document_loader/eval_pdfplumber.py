import pdfplumber

INPUT_PATH = "data/xpres-brochure.pdf"
OUTPUT_PATH = "evals/document_loader/output/pdfplumber.txt"

with pdfplumber.open(INPUT_PATH) as pdf:

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:

        f.write(f"Total Pages: {len(pdf.pages)}\n\n")

        for i, page in enumerate(pdf.pages):
            f.write("=" * 80 + "\n")
            f.write(f"PAGE {i + 1}\n")
            f.write("=" * 80 + "\n\n")

            f.write("CONTENT:\n")
            f.write(page.extract_text() or "")
            f.write("\n\n")

            f.write("TABLES:\n")

            tables = page.extract_tables()

            if tables:
                for table_num, table in enumerate(tables, start=1):
                    f.write(f"\nTABLE {table_num}:\n")

                    for row in table:
                        f.write(str(row))
                        f.write("\n")
            else:
                f.write("No tables detected.\n")

            f.write("\n\n")