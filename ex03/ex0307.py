#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
#7 - Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n2 == n1:
    print('Os números não podem ser iguais.')
    exit()
n3 = float(input('Pra finalizar, digite mais um número: '))
if n3 == n1 or n3 == n2:
    print('Os número não podem ser iguais.')
    exit()
#Se n1 for o menor número.
if n1 < n2 and n1 < n3:
    if n2 > n3:
        print(f'O maior número digitado foi {n2:.2f} e menor {n1:.2f}.')
    if n2 < n3:
        print(f'O maior número digitado foi {n3:.2f} e menor {n1:.2f}.')
#Se n2 for o menor número.
if n2 < n1 and n2 < n3:
    if n1 > n3:
        print(f'O maior número digitado foi {n1:.2f} e menor {n2:.2f}.')
    if n1 < n3:
        print(f'O maior número digitado foi {n3:.2f} e menor {n2:.2f}.')
#Se n3 for o menor número.
if n3 < n1 and n3 < n2:
    if n1 > n2:
        print(f'O maior número digitado foi {n1:.2f} e menor {n3:.2f}.')
    if n1 < n2:
        print(f'O maior número digitado foi {n2:.2f} e menor {n3:.2f}.')
