#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(0.25) 5 - Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
crescimento iniciais. Valide a entrada e permita repetir a operação.'''
a = int(input('Digite o valor da população A: '))
while a <= 0:
    a = int(input('Erro! O valor deve ser maior do que 0. Digite o valor da população A: '))
b = int(input('Digite o valor da população B: '))
while b <= 0:
    b = int(input('Erro! O valor deve ser maior do que 0. Digite o valor da população B: '))
while a >= b:
    print('A população de A já é maior ou igual a população de B. Tente novamente.')
    a = int(input('Digite o valor da população A: '))
    b = int(input('Digite o valor da população B: '))
taxa_a = float(input('Digite o valor da taxa anual de crescimento de A em %: '))
taxa_b = float(input('Digite o valor da taxa anual de crescimento de B em %: '))
ano = 0
while b > a:
    a = (a + ((a * taxa_a) / 100))
    b = (b + ((b * taxa_b) / 100))
    ano += 1
print('Foram necessários {} anos para A ficar maior ou igual a B.'.format(ano))
print('População A: {:.0f}'.format(a))
print('População B: {:.0f}'.format(b))
