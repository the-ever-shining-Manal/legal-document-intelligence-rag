import fitz

doc=r"C:\Users\SOFT LAPTOP\OneDrive - Faculty Of Engineering (Tanta University)\Desktop\self-study\courses\legal-document-intelligence-rag\Legal_Document\integralversionprinciples2010-e.pdf"


def load_document(document):
    file= fitz.open(document)
    pages=[]
    for page_num in range(len(file)):
        exctracted_text=fitz.get_text(file[page_num])
        pages.append([{
            'page number':page_num+1,
            'text':exctracted_text
        }])

    return pages


