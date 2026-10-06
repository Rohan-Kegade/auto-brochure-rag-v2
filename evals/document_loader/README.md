# PDF Loader Evaluation

## Objective

Evaluate different PDF loaders for extracting content from car brochure PDFs.

## Candidates

- PyPDFLoader
- PyMuPDF
- PDFPlumber
- PDFMuse
- PDF Inspector

## Evaluation Criteria

1. Text extraction
2. Table extraction
3. Page-level metadata
4. Layout preservation
5. Processing time

## Results

After testing the document loaders on multiple car brochures:

- **PyPDFLoader** and **PyMuPDF** provide good text extraction, but do not preserve table structure well. This is important for extracting car specifications and comparing variants.

- **PDF Inspector** provides good text and structured Markdown output in some cases, but its table extraction is not reliable or consistent. It also does not provide reliable page-level metadata for extracted content, which is important for citations.

- **PDFMuse** provides good results for some tables and useful metadata such as source, page number, category, and bounding box. However, its extraction is not consistent across different PDF files and can encounter extraction issues with some documents.

- **PDFPlumber** performed the most consistently across the tested documents. It provides useful page-level information and performs well at extracting both text and table data relevant to this application.

## Why Not OCR or Multimodal?

OCR or multimodal approaches were not used because car brochures mainly contain **car images and textual information** such as features, specifications, and variant details.

Extracting car images is not necessary because users primarily ask about **features, specifications, and variant differences**, rather than the car's visual appearance. Text within images was also successfully extracted using text-based loaders, making OCR or multimodal processing unnecessary for the current use case.

## Conclusion

Based on the tested documents, **PDFPlumber was selected as the document extraction approach** for the current RAG pipeline because it provided the most consistent combination of text extraction, table extraction, and page-level information.