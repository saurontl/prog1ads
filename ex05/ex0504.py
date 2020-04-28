#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(1.50) 4 - Suponha que a população de um país A seja da ordem de 80.000 habitantes com uma
taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa
de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
necessários para que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.'''
a = 80000
b = 200000
ano = 0
while b > a:
    a = (a + ((a * 3) / 100))
    b = (b + ((b * 1.5) / 100))
    ano += 1
print('Foram necessários {} anos para A ficar maior ou igual a B.'.format(ano))
print('População A: {:.0f}'.format(a))
print('População B: {:.0f}'.format(b))
