#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
#8 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.
produto1 = float(input('Qual o valor do produto 1? '))
produto2 = float(input('Qual o valor do produto 2? '))
produto3 = float(input('Qual o valor do produto 3? '))
if produto1 == produto2 == produto3:
    print('Você pode comprar qualquer um, eles tem o mesmo valor.')
    exit()
if produto1 == produto2 and produto1 < produto3:
    print(f'Você pode comprar o Produto 1 ou Produto 2, pois ambos custam {produto1:.2f}.')
    exit()
if produto1 == produto3 and produto1 < produto2:
    print(f'Você pode comprar o Produto 1 ou Produto 3, pois ambos custam {produto1:.2f}.')
    exit()
if produto2 == produto3 and produto2 < produto1:
    print(f'Você pode comprar o Produto 2 ou Produto 3, pois ambos custam {produto2:.2f}.')
    exit()
if produto1 < produto2 and produto1 < produto3:
    print(f'Você deve comprar o Produto 1, pois ele é o mais barato e custa {produto1:.2f}.')
if produto2 < produto1 and produto2 < produto3:
    print(f'Você deve comprar o Produto 2, pois ele é o mais barato e custa {produto2:.2f}.')
if produto3 < produto1 and produto3 < produto2:
    print(f'Você deve comprar o Produto 3, pois ele é o mais barato e custa {produto3:.2f}.')



