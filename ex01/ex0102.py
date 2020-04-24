#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 01
#---
#2 - Sabendo que a cotação atual do dólar americano é R$ 4,47, receba um valor em reais do usuário e converta para dólares. Exemplo de saída: $ 1.00
reais = float(input('Digite o valor total em reais que deseja converter para dólares: '))
dolares = reais * 4.47
print('R${:.2f} = US${:.2f}'.format(reais, dolares))
