#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(1.00) 6 - Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modi que o programa para que ele mostre os números um ao lado do outro.'''
show = int(input('Digite 1 para mostrar os números um abaixo do outro ou 2 para os números lado a lado: '))
while show != 1 and show != 2:
    print('Erro! Você deve digitar 1 para mostrar os números um abaixo do outro ou 2 para mostrar lado a lado. Tente novamente.')
    show = int(input('Digite 1 para mostrar os números um abaixo do outro ou 2 para os números lado a lado: '))
if show == 1:
    for n in range(1, 21):
        print(n)
if show == 2:
    for n in range(1,21):
        print(n, end = ' ')
