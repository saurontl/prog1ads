#José Everton da Silva Filho
#AdS - P1 - Unifip - Patos/PB
#LISTA - 05
#---
'''(0.50) 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''
nome = str(input('Digite o seu nome: '))
senha = str(input('Digite a sua senha: '))
while nome == senha:
    print('Erro! A senha não pode ser igual ao nome. Tente novamente.')
    nome = str(input('Digite o seu nome: '))
    senha = str(input('Digite a sua senha: '))
else:
    print('Cadastro efetuado com sucesso.')
    print('Nome: {}'.format(nome))
    print('Senha: {}'.format(senha))
