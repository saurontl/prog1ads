#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(2.00) 10 - Faça um programa que receba dois números inteiros e gere os números inteiros que
estão no intervalo compreendido por eles.'''
n1 = int(input('Digite o valor inicial: '))
n2 = int(input('Digite o valor final: '))
while n2 <= n1:
    print('Erro! O VALOR FINAL deve ser MAIOR do que o VALOR INICIAL. Tente novamente.')
    n1 = int(input('Digite o valor inicial: '))
    n2 = int(input('Digite o valor final: '))
else:
    for n in range(n1, n2+1):
        print(n, end = ' ')
print(' ')
print('##### FIM #####')
