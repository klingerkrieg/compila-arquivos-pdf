from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import os
pasta = '.'

blank = PdfFileReader(os.path.join("./", "blank.pdf"))
merger = PdfFileMerger()

for diretorio, subpastas, arquivos in os.walk(pasta):
    

    #nao le arquivos no root
    if (diretorio == "."):
        continue

    for arquivo in arquivos:
        if arquivo.lower().endswith(".pdf"):
            print(os.path.join(os.path.realpath(diretorio), arquivo))
            try:
                pdf = PdfFileReader(os.path.join(os.path.realpath(diretorio), arquivo), "rb")
                merger.append(pdf)

                if pdf.numPages % 2 != 0:
                    merger.append(blank)

                
            except Exception as err:
                print(Exception, err)
                print("erro:",arquivo)
                exit()

merger.write(os.path.join("./", "diarios.pdf"))