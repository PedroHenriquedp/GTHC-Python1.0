# 6. Verificar se um número é par ou ímpar;

x = int(input('Insira um valor para saber se é ímpar ou par '))

if x%2 != 0:
    print('O valor {} é ímpar'.format(x))
else:
    print('O valor {} é par'.format(x))

sair = input('\nDigite ENTER para sair...')