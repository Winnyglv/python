import fitz
from PyPDF2 import PdfReader

v = []
for v in range(1, 11):
    # print("/teste{}.pdf".format(v))
    arquivo = ("arquivo0{}.pdf".format(v)) # nome arquivo 
    reader = PdfReader(arquivo)
    page = reader.pages[0]
    print(page.extract_text())

    doc = fitz.open(arquivo)
    page = doc[0]

    # busca no arquivo a palavra escolhida
    for rect in page.search_for("2022"):
        a = page.add_redact_annot(rect, fill=(0, 0, 0)) #marca para remover o texto, e seleciona a cor preta 
        a.update() 
        page.apply_redactions() #apaga a palavra selecionada
       
        doc.save("funcionou{}.pdf".format(v))  # gera uma copia do(s) arquivo(s).
