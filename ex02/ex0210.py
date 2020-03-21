#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#####
#10. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual
# (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).
salario = float(input('Digite o valor do salário: '))
percentual = float(input('Digite o valor do percentual a ser aplicado: '))
salario_atual = float(((salario * percentual) / 100) + salario)
print(f'O valor do salário atual é de {salario_atual:.2f}.')


