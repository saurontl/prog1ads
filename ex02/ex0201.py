#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#####
#1. Faça um programa que solicite ao usuário o valor do litro de combustível (ex. 4,75) e quanto em dinheiro ele deseja
# abastecer (ex. 50,00). Calcule quantos litros de combustível o usuário obterá com esses valores.

combustivel = float(input("Digite o valor em reais do litro do combustível: R$"))
dinheiro = float(input("Digite o valor em reais que você deseja abastecer: R$"))
total = combustivel * dinheiro
print(f"Você abastecerá {total:.2f} litros.")

