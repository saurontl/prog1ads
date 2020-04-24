#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 01
#---
#3 - Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos 45 litros de água. Sabendo que em 1 m3 de água há 1.000 litros,
#calcule quantos banhos de 5 minutos são necessários para consumir 1 metro cúbico de água?
consumo = float(input('Digite quantos litros de água são consumidos por banho: '))
total = int(1000 / consumo)
print('Em {:.0f} banhos você gastará 1m3 de água.'.format(total))
