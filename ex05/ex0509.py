#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(1.50) 9 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.'''
print('Início da contagem dos números ímpares de 1 a 50:')
print('#############################')
total = 0
for n in range(1, 51, 2):
    print(n, end=' ')
    total += 1
print(' ')
print('############ FIM ############')
print('Entre 1 e 50 existem {} números ímpares.'.format(total))
