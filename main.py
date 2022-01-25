from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage




def get_pdf_file_content(path_to_pdf):
        resource_manager = PDFResourceManager(caching=True)
        out_text = StringIO()
        laParams = LAParams()
        text_converter = TextConverter(resource_manager, out_text, laparams=laParams)
        fp = open(path_to_pdf, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, text_converter)
        for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
            interpreter.process_page(page)

        text = out_text.getvalue()
        fp.close()
        text_converter.close()
        out_text.close()




        File = open(r"D:\Coding\python projects\pdfreader\file.text", 'a+', encoding='utf8')
        File.writelines(text)
        File.close()






path_to_pdf = "./file.pdf"
get_pdf_file_content(path_to_pdf)







