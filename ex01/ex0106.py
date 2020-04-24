#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 01
#---
#6 - Escreva um programa que leia uma temperatura em graus Fahrenheit, transforme-a em graus Celsius e exiba o resultado.
fahr = float(input('Digite o valor em Fahrenheit que você deseja converter em Celsius: '))
celsius = (fahr - 32) / 1.8
print('{:.2f} Fahrenheit = {:.2f} Celsius.'.format(fahr, celsius))
