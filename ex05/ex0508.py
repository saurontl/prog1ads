#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(1.00) 8 - Faça um programa que leia 5 números e informe a soma e a média dos números.'''
soma = 0
for n in range(1, 6):
    numero = int(input('Digite o valor {}: '.format(n)))
    soma += numero
media = soma / 5
print('A soma dos 5 números é de {} e a média {}.'.format(soma, media))
