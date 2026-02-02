import PyPDF2

with open('[ES] Nicolas Suarez - CV.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    full_text = ''
    for page in reader.pages:
        full_text += page.extract_text() + '\n'
    
    print(full_text)
