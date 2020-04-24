#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 01
#---
#5 - Receba do usuário o ano em que estamos, e o ano que ele nasceu, e calcule sua idade. Despreze os meses.
atual = int(input('Digite o ano atual: '))
if atual <= 0:
    print('O ano atual deve ser maior do que 0.')
    exit()
nascimento = int(input('Digite o ano que você nasceu: '))
if nascimento <= 0:
    print('O ano de nascimento deve ser maior do que 0.')
    exit()
idade = atual - nascimento
if idade == 1: print('Você tem 1 ano de idade.')
else: print('Você tem {} anos de idade.'.format(idade))
