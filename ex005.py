# 5. Dados 3 números verificar qual é o maior;

x = float(input('Insira um primeiro número: '))
y = float(input('Insira um segundo número: '))
z = float(input('Insira um terceiro número: '))

if x >= y and x >= z:
    print('O maior valor é {}'.format(x))
elif y >= x and y >= z:
    print('O maior valor é {}'.format(y))
else:
    print('O maior valor é {}'.format(z))

sair = input('\nDigite ENTER para sair...')