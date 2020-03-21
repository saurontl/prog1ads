# José Everton da Silva Filho
# Exercício 04 - AdS - P1 - Unifip - Patos/PB
#####
'''
5 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
'''
l1 = float(input('Insira o valor do lado 1: '))
l2 = float(input('Insira o valor do lado 2: '))
l3 = float(input('Insira o valor do lado 3: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    if l1 == l2 == l3:
        print(f'{l1:.2f}, {l2:.2f} e {l3:.2f} formam um triângulo equilátero.')
    if l1 == l2 and l1 != l3:
        print(f'{l1:.2f}, {l2:.2f} e {l3:.2f} formam um triângulo isóceles.')
    if l2 == l3 and l2 != l1:
        print(f'{l1:.2f}, {l2:.2f} e {l3:.2f} formam um triângulo isóceles.')
    if l1 != l2 != l3:
        print(f'{l1:.2f}, {l2:.2f} e {l3:.2f} formam um triângulo escaleno.')
else: print(f'{l1:.2f}, {l2:.2f} e {l3:.2f} não formam um triângulo.')
