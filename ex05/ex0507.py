#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(0.50) 7 - Faça um programa que leia 5 números e informe o maior número.'''
maior = 0
for n in range(1, 6):
    numero = int(input('Digite o número {}: '.format(n)))
    if numero > maior:
        maior = numero
print('O maior número digitado foi {}.'.format(maior))
