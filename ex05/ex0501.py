#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(0.25) 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso
o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''
valor = int(input('Digite um valor entre 0 e 10: '))
while valor < 0 or valor > 10:
    valor = int(input('Erro! Digite um valor entre 0 e 10: '))
else: print('Correto! Você digitou {}.'.format(valor))

