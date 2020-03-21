# José Everton da Silva Filho
# Exercício 04 - AdS - P1 - Unifip - Patos/PB
#####
'''
2 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
'''
valor_hora = float(input('Qual o valor da hora trabalhada? R$'))
tempo = int(input('Quantas horas são trabalhadas por mês? '))
salario = valor_hora * tempo
sindicato = (3 * salario) / 100
fgts = (11 * salario) / 100
if salario <= 900:
    ir_per = 0
    ir = (ir_per * salario) / 100
    descontos = sindicato + ir
    salario_liquido = salario - descontos
elif salario > 900 and salario <= 1500:
    ir_per = 5
    ir = (ir_per * salario) / 100
    descontos = sindicato + ir
    salario_liquido = salario - descontos
elif salario > 1500 and salario <= 2500:
    ir_per = 10
    ir = (ir_per * salario) / 100
    descontos = sindicato + ir
    salario_liquido = salario - descontos
elif salario > 2500:
    ir_per = 20
    ir = (ir_per * salario) / 100
    descontos = sindicato + ir
    salario_liquido = salario - descontos
print(f'Salário Bruto: (R${valor_hora:.2f} * {tempo:.2f}h): R${salario:.2f}')
print(f'(-) IR({ir_per:.2f}%): R${ir:.2f}')
print(f'(-) Sindicato(3%): R${sindicato:.2f}')
print(f'FGTS(11%): R${fgts:.2f}')
print(f'Total de descontos: R${descontos:.2f}')
print(f'Salário Liquido: R${salario_liquido:.2f}')