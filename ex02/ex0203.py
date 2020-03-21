#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#####
#3. Faça um programa que calcule a média de consumo de combustível de um veículo. O usuário deve informar o KM inicial
#(ex. 12500 km), o KM final (ex. 12700 km) e quantos litros foram gastos no percurso.

km_inicial = int(input('Digite o KM inicial: '))
km_final = int(input('Digite o KM final: '))
km_consumo = int(km_final - km_inicial)
consumo_litros = km_consumo / 15
print(f'Levando em consideração que um carro faz 15km com 1 litro de combustível, você gastará aproximadamente {consumo_litros:.0f} litros para percorrer {km_consumo:.0f}km.')

