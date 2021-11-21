def removcaract(cnpj):
    documento = []
    for x in cnpj:
        if x.isnumeric():
            documento.append(x)
    documento = ''.join(documento)
    return documento

