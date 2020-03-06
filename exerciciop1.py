#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#####
#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro ele deseja
# abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.
'''
combustivel = float(input("Digite o valor em reais do litro do combustível: R$"))
dinheiro = float(input("Digite o valor em reais que você deseja abastecer: R$"))
total = combustivel * dinheiro
print(f"Você abastecerá {total:.2f} litros.")
'''
#2. Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos 45 litros de água. Sabendo que em 1 m3 de
# água há 1.000 litros, calcule quantos banhos de 5 minutos são necessários para consumir 1 metro cúbico de água?
'''
consumo = float(input('Digite quantos litros de água são consumidos por banho: '))
total = int(1000 / consumo)
print(f"Em {total:.0f} banhos você gastará 1m3 de água.")
'''
#3. Faça um programa que calcule a média de consumo de combustível de um veículo. O usuário deve informar o KM inicial
#(ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.
'''
km_inicial = int(input('Digite o KM inicial: '))
km_final = int(input('Digite o KM final: '))
km_consumo = int(km_final - km_inicial)
consumo_litros = km_consumo / 15
print(f'Levando em consideração que um carro faz 15km com 1 litro de combustível, você gastará aproximadamente {consumo_litros:.0f} litros para percorrer {km_consumo:.0f}km.')
'''
#4. Escreva um programa que leia uma temperatura em graus Fahrenheit, transforme-a em graus Celsius e exiba o resultado.
'''
fahrenheit = float(input('Digite o valor em Farenheit: '))
celsius = (fahrenheit - 32) / 1.8
print(f'{fahrenheit}ºF = {celsius}ºC')
'''
#5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso. O usuário deve informar o valor original
#da dívida (ex. R$ 50,00), a quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de atraso (ex. R$ 0,25).
'''
divida = float(input('Digite o valor da dívida: '))
dias = int(input('Digite a quantidade de dias em atraso: '))
multa = float(input('Digite o valor da multa por dia de atraso: '))
divida_total = float(divida + (dias * multa))
print(f'O valor total a ser pago é de R${divida_total:.2f}.')
'''
#6. Escreva um programa que leia um valor inteiro e calcule o seu quadrado.
'''
valor_inteiro = int(input('Digite o valor inteiro a ser calculado: '))
valor_quadrado = int(valor_inteiro ** 2)
print(f'O quadrado de {valor_inteiro} é {valor_quadrado}.')
'''
#7. Faça um programa que calcule a área total (m​2​) de uma casa com 4 cômodos. O usuário deve inserir a largura e
#comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.
'''
largura_quarto1 = float(input('Digite o valor da largura do Quarto 1: '))
comprimento_quarto1 = float(input('Digite o valor do comprimento do Quarto 1: '))
largura_quarto2 = float(input('Digite o valor da largura do Quarto 2: '))
comprimento_quarto2 = float(input('Digite o valor do comprimento do Quarto 2: '))
largura_quarto3 = float(input('Digite o valor da largura do Quarto 3: '))
comprimento_quarto3 = float(input('Digite o valor do comprimento do Quarto 3: '))
largura_quarto4 = float(input('Digite o valor da largura do Quarto 4: '))
comprimento_quarto4 = float(input('Digite o valor do comprimento do Quarto 4: '))
m2_quarto1 = float(largura_quarto1 * comprimento_quarto1)
m2_quarto2 = float(largura_quarto2 * comprimento_quarto2)
m2_quarto3 = float(largura_quarto3 * comprimento_quarto3)
m2_quarto4 = float(largura_quarto4 * comprimento_quarto4)
area_total = float(m2_quarto1 + m2_quarto2 + m2_quarto3 + m2_quarto4)
print(f'O Quarto 1 tem {m2_quarto1:.2f}m2. O Quarto 2 tem {m2_quarto2:.2f}m2. O Quarto 3 tem {m2_quarto3:.2f}m2. O Quarto 4 tem {m2_quarto4:.2f}m2. A área total da casa é de {area_total:.2f}m2.')
'''
#8. Escreva um programa que leia um valor inteiro e calcule o seu cubo.
'''
valor_inteiro = int(input('Digite o valor inteiro a ser calculado: '))
valor_cubico = int(valor_inteiro ** 3)
print(f'O cubo de {valor_inteiro} é {valor_cubico}.')
'''
#9. Escreva um programa que converte valores de polegadas em centímetros utilizando a seguinte fórmula para conversão:
#1 polegada = 2,54 cm;
'''
polegadas = float(input('Digite o valor em polegadas: '))
cm = float(polegadas * 2.54)
print(f'{polegadas:.2f} polegadas = {cm:.2f}cm')
'''
#10. Faça um programa que calcula o novo valor do salário de um funcionário. O usuário informa o salário atual
# (ex. 1250,00) e o percentual do reajuste (ex. 13,5 %).
salario = float(input('Digite o valor do salário: '))
percentual = float(input('Digite o valor do percentual a ser aplicado: '))
salario_atual = float(((salario * percentual) / 100) + salario)
print(f'O valor do salário atual é de {salario_atual:.2f}.')


