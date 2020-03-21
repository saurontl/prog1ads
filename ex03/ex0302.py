#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
# 2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n1 = int(input("Digite o valor a ser conferido: "))
if n1 < 0:
    print(f"O número {n1:.2f} é negativo.")
elif n1 > 0:
    print(f"O número {n1:.2f} é positivo.")
elif n1 == 0:
    print(f"O número 0 não é positivo nem negativo, rapaz!")