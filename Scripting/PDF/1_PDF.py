
import PyPDF2 as pdf 

with open('Scripting/PDF/pdfBases/marcaAgua.pdf', 'rb') as miarchivo:
    print(miarchivo)
    print(type(miarchivo))

    archivoPDF = pdf.PdfFileReader(miarchivo)
    print(archivoPDF)
    print(type(archivoPDF))

    # Número de páginas 
    print(archivoPDF.getNumPages)