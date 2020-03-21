#José Everton da Silva Filho
#Exercício 04 - AdS - P1 - Unifip - Patos/PB
#####
'''
1 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver
o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
seguinte critério, baseado no salário atual:
-- salários até R$ 280,00 (incluindo) : aumento de 20%
-- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-- o salário antes do reajuste;
-- o percentual de aumento aplicado;
-- o valor do aumento;
-- o novo salário, após o aumento.
'''
salario = float(input('Qual o valor do salário a ser reajustado? R$' ))
if salario <= 280:
    aumento = ((20 * salario) / 100)
    salario_novo = salario + aumento
    print(f'O salário de R${salario:.2f} teve um reajuste de R${aumento:.2f} referente a 20% de aumento, totalizando R${salario_novo:.2f}.')
if salario > 280 and salario <= 700:
    aumento = ((15 * salario) / 100)
    salario_novo = salario + aumento
    print(f'O salário de R${salario:.2f} teve um reajuste de R${aumento:.2f} referente a 15% de aumento, totalizando R${salario_novo:.2f}.')
if salario > 700 and salario <= 1500:
    aumento = ((10 * salario) / 100)
    salario_novo = salario + aumento
    print(f'O salário de R${salario:.2f} teve um reajuste de R${aumento:.2f} referente a 10% de aumento, totalizando R${salario_novo:.2f}.')
if salario > 1500:
    aumento = ((5 * salario) / 100)
    salario_novo = salario + aumento
    print(f'O salário de R${salario:.2f} teve um reajuste de R${aumento:.2f} referente a 5% de aumento, totalizando R${salario_novo:.2f}.')