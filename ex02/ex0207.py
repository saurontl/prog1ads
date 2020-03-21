#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#####
#7. Faça um programa que calcule a área total (m​2​) de uma casa com 4 cômodos. O usuário deve inserir a largura e
#comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa.
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

