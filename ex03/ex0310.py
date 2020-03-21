#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
#10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = str(input('Em que turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: '))
if turno in ['m', 'M']:
    print('Bom dia!')
elif turno in ['v', 'V']:
    print('Boa tarde!')
elif turno in ['n', 'N']:
    print('Bom noite!')
else:
    print('Você digitou um valor inválido. Digite M para Matutino, V para Vespertino ou N para Noturno.')
