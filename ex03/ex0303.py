#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.
letra = str(input('Qual o seu sexo? Digite F para Feminino ou M para Masculino: '))
if letra in ['f', 'F']:
    print('Você é do sexo Feminino.')
elif letra in ['m', 'M']:
    print('Você é do sexo Masculino.')
else:
    print(f'Sexo inválido, você digitou "{letra}". Digite F ou M.')