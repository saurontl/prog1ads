#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
# 6 - Faça um Programa que leia três números e mostre o maior deles.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Pra finalizar, digite mais um número: '))
if n1 == n2 == n3:
    print('Todos os números digitados são iguais.')
    exit()
if n1 > n2 and n1 > n3:
    print(f'O maior número digitado foi {n1:.2f}.')
elif n2 > n1 and n2 > n3:
    print(f'O maior número digitado foi {n2:.2f}.')
else:
    print(f'O maior número digitado foi {n3:.2f}.')
