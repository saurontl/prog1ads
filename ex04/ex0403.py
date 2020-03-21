# José Everton da Silva Filho
# Exercício 04 - AdS - P1 - Unifip - Patos/PB
#####
'''
3 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
'''
n = int(input('Por favor, digite um número de 1 a 7: '))
if n == 0 or n > 7: print('Você precisa digitar um número entre 1 e 7.')
if n == 1: print('1 - Domingo')
if n == 2: print('2 - Segunda-feira')
if n == 3: print('3 - Terça-feira')
if n == 4: print('4 - Quarta-feira')
if n == 5: print('5 - Quinta-feira')
if n == 6: print('6 - Sexta-feira')
if n == 7: print('7 - Sábado')

