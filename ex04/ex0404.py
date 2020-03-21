# José Everton da Silva Filho
# Exercício 04 - AdS - P1 - Unifip - Patos/PB
#####
'''
4 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem "APROVADO" se o conceito
for A, B ou C ou "REPROVADO" se o conceito for D ou E.
'''
nota1 = float(input('Por favor, insira o valor da primeira nota: '))
if nota1 < 0 or nota1 > 10:
    print('Você precisa digitar um valor entre 0 e 10.')
    exit()
nota2 = float(input('Por favor, insira o valor da segunda nota: '))
if nota2 < 0 or nota2 > 10:
    print('Você precisa digitar um valor entre 0 e 10.')
    exit()
media = (nota1 + nota2) / 2
if media >= 9: conceito = 'A'
if media >= 7.5 and media < 9: conceito = 'B'
if media >= 6 and media < 7.5: conceito = 'C'
if media >= 4 and media < 6: conceito = 'D'
if media < 4 and media >= 0: conceito = 'E'
print(f'Nota 1: {nota1:.2f}')
print(f'Nota 2: {nota2:.2f}')
print(f'Média: {media:.2f}')
print(f'Conceito: {conceito}')
if conceito == 'A' or conceito == 'B' or conceito == 'C': print('APROVADO!')
else: print('REPROVADO!')

