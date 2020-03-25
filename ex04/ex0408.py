# José Everton da Silva Filho
# Exercício 04 - AdS - P1 - Unifip - Patos/PB
#####
'''
8 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
dia = int(input('Informe o dia: '))
if dia < 1 or dia > 31:
    print('Dia inválido! Você precisa informar um dia entre 1 e 31.')
    exit()
mes = int(input('Informe o mês: '))
if mes < 1 or mes > 12:
    print('Mês inválido! Você precisa informar um mês entre 1 e 12.')
    exit()
if dia > 28 and mes == 2:
    print(f'Mês inválido para o dia {dia}, o mês {mes} só tem 28 dias.')
    exit()
if dia > 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print(f'Mês inválido para o dia {dia}, o mês {mes} só tem 30 dias.')
    exit()
ano = int(input('Informe o ano: '))
print(f'A data {dia}/{mes}/{ano} é válida.')
