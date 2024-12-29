import pdfplumber as pp

# Extraire l'ensemble du text contenu dans un document PDF
with pp.open("assets/scm_mock_examples.pdf") as book:
    for page_no, page in enumerate(book.pages, start=1):
        print(f"{page_no = }")
        data = page.extract_text()
        print(data.strip())
        print("-" * 45)
