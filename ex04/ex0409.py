# José Everton da Silva Filho
# Exercício 04 - AdS - P1 - Unifip - Patos/PB
#####
'''
9 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades
do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades
- Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
n = int(input('Digite um número menor do que 1000: '))
if n >= 1000:
    print('Por favor, digite um número menor do que 1000.')
    exit()
n1 = n
und = n % 10
if und > 1: und_print = 'unidades'
else: und_print = 'unidade'
n = (n - und) / 10
dez = n % 10
if dez > 1: dez_print = 'dezenas'
else: dez_print = 'dezena'
n = (n - dez) / 10
cen = n
if cen > 1: cen_print = 'centenas'
else: cen_print = 'centena'
print('O número {:.0f} tem: {:.0f} {}, {:.0f} {} e {:.0f} {}.'.format(n1, cen, cen_print, dez, dez_print, und, und_print))
