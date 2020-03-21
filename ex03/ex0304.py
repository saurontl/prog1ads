#José Everton da Silva Filho
#Exercício 02 - AdS - P1 - Unifip - Patos/PB
#####
# 4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = str(input('Digite um caractere: '))
if letra == 'a' or letra == 'A' or letra == 'e' or letra == 'E' or letra == 'i' or letra == 'I' or letra == 'o' or letra == 'O' or letra == 'u' or letra == 'U':
    print(f'O caractere "{letra}" é uma vogal.')
else:
    print(f'O caractere "{letra}" é uma consoante.')