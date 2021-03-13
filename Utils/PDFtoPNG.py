from pdf2image import convert_from_path

def pdf_to_png(path):
    page = convert_from_path(path)
    page[0].save('fooimage' + '.png', 'PNG')