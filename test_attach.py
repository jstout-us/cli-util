from PyPDF4.pdf import PdfFileReader, PdfFileWriter

inputpath = 'meta-test-1.pdf'
outputpath = 'pypdf4-test-4.pdf'
meta_path = 'metadata.yaml'

with open(inputpath, 'rb') as pdf_in:
    reader = PdfFileReader(pdf_in)

    writer = PdfFileWriter()
    with open(meta_path, 'rb') as meta_in:
        for idx in range(reader.numPages):
            writer.addPage(reader.getPage(idx))

        writer.addAttachment('clip_meta', meta_in.read())


    with open(outputpath, 'wb') as pdf_out:
        writer.write(pdf_out)

