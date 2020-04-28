#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(1.00) 3 - Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';'''

nome = str(input('Nome: '))
while len(nome) <= 3:
    print('Erro! O nome deve ter mais do que 3 caracteres. Tente novamente')
    nome = str(input('Digite o nome: '))
idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    print('Erro! A idade deve ser entre 0 e 150 anos. Tente novamente.')
    idade = int(input('Idade: '))
salario = float(input('Salário: '))
while salario <= 0:
    print('Erro! O salário deve ser maior do que 0. Tente novamente.')
    salario = float(input('Salário: '))
sexo = str(input('Sexo (F ou M): '))
#while sexo != 'M' or sexo != 'F':
while sexo not in ['F', 'f', 'M', 'm']:
    print('Erro! O sexo deve ser F para Feminino ou M para Masculino. Tente novamente.')
    sexo = str(input('Sexo (F ou M): '))
estado = str(input('Digite S, C, V ou D para o estado civil: '))
while estado not in ['S', 's', 'C', 'c', 'V', 'v', 'D', 'd']:
    print('Erro! O estado civil deve ser S (solteiro), C (casado), V (viúvo) ou D (divorciado). Tente novamente.')
    estado = str(input('Digite S, C, V ou D para o estado civil: '))
else:
    print(50*'#')
    print('Cadastro efetuado com sucesso!')
    print('Nome: {}'.format(nome))
    print('Idade: {}'.format(idade))
    print('Salário: {:.2f}'.format(salario))
    if sexo == 'f' or sexo == 'F':
        print('Sexo: Feminino')
        if estado in ['s', 'S']: print('Estado Civil: Solteira')
        if estado in ['c', 'C']: print('Estado Civil: Casada')
        if estado in ['v', 'V']: print('Estado Civil: Viúva')
        if estado in ['d', 'D']: print('Estado Civil: Divorciada')
    if sexo == 'm' or sexo == 'M':
        print('Sexo: Masculino')
        if estado in ['s', 'S']: print('Estado Civil: Solteiro')
        if estado in ['c', 'C']: print('Estado Civil: Casado')
        if estado in ['v', 'V']: print('Estado Civil: Viúvo')
        if estado in ['d', 'D']: print('Estado Civil: Divorciado')
