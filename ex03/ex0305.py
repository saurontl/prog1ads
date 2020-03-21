#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
#5 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
# aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input('Digite o valor da nota 1: '))
if nota1 > 10:
    print(f'Você digitou "{nota1:.2f}" e a nota máxima é 10. Por favor, verifique.')
    exit()
nota2 = float(input('Digite o valor da nota 2: '))
if nota2 > 10:
    print(f'Você digitou "{nota2:.2f}" e a nota máxima é 10. Por favor, verifique.')
    exit()
media = (nota1 + nota2) / 2
if media >= 7 and media < 10:
    print('Oba, o aluno foi aprovado!')
elif media < 7:
    print('Más notícias, o aluno foi reprovado!')
else:
    print('Parabéns, você passou com 10!')