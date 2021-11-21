from removecaractere import removcaract
from removedigito import removdig
from quantidade import qtd
from primeirodigito import calculo
from segundodigito import calculo2

while True:
    cnpj = input('Digite o CNPJ: ')
    cnpj = removcaract(cnpj)
    digito = cnpj[-2:]
    cnpj = removdig(cnpj)
    verificacao_1 = qtd(cnpj)
    if not verificacao_1:
        print('\n'*100)
        print('Verifique os digitos e tente novamente.')
        continue
    else:
        digito_1 = calculo(cnpj)
        digito_2 = calculo2(cnpj, digito_1)
        if digito == str(digito_1)+str(digito_2):
            print('CNPJ válido!')
        else:
            print('CNPJ inválido')
    continua = input("deseja continuar? [s/n] ")
    if continua in 'Nn':
        break
