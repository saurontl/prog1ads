#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
# 9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n2 == n1:
    print('Os números não podem ser iguais.')
    exit()
n3 = int(input('Pra finalizar, digite mais um número: '))
if n3 == n1 or n3 == n2:
    print('Os número não podem ser iguais.')
    exit()
list = n1, n2, n3
newlist = sorted(list, reverse=True)
print('Os números em ordem decrescente:', str(newlist).strip('[]') + '.')

