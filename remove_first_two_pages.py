import typer
from PyPDF2 import PdfFileReader, PdfFileWriter

def remove_first_two_pages(file_path: str):
    # Read the PDF file
    pdf_reader = PdfFileReader(file_path)
    
    # Create a PDF writer object
    pdf_writer = PdfFileWriter()
    
    # Iterate through the pages and add them to the writer object, starting from the third page
    for page_num in range(2, pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)
    
    # Write the new PDF to a file
    output_path = file_path.replace('.pdf', '_modified.pdf')
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)
    
    print(f'Successfully removed the first two pages. Modified file saved as: {output_path}')

def main(file_path: str):
    remove_first_two_pages(file_path)
