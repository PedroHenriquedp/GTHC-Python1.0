# 2. Coletar o nome do usuário e idade dele e mostrar na tela;
name = input('Por favor, insira seu nome de usuário: ')
idade = int(input('Qual sua idade {}? '.format(name)))
print('{}, você tem {} anos'.format(name,idade))

sair = input('\nDigite ENTER para sair...')