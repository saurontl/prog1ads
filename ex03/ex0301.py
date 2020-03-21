#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
#1 - Faça um Programa que peça dois números e imprima o maior deles.
numero1 = int(input("Digite o valor 1: "))
numero2 = int(input("Digite o valor 2: "))
if numero1 == numero2:
    print('Você comparou os mesmos números.')
    exit()
if numero1 > numero2:
    print(f"{numero1} é maior do que {numero2}.")
else:
    print(f"{numero2} é maior do que {numero1}.")