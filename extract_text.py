import PyPDF2

def extract_text_from_pdf(pdf_file_path):
    """
    Extract text from a PDF file.
    param:
        pdf_file_path (str): The path to the PDF file from which text will be extracted.
    return:
        str: The extracted text from the PDF file.
    """
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text
