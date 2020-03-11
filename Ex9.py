#9. Escreva um programa que converte valores de polegadas em centímetros utilizando a seguinte fórmula para conversão:
#1 polegada = 2,54 cm;
polegadas = float(input('Digite o valor em polegadas: '))
cm = float(polegadas * 2.54)
print(f'{polegadas:.2f} polegadas = {cm:.2f}cm')