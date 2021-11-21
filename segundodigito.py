def calculo2(documento, digito):
    sequencia = iter('6543298765432')
    soma = 0
    for x in documento:
        soma += int(x) * int(next(sequencia))
    soma += digito * int(next(sequencia))
    soma = 11 - (soma % 11)
    if soma > 9:
        soma = 0
    return soma