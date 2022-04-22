# 8. Coletar 3 ângulos e verificar se formam um triângulo;

x = float(input('Qual o valor do primeiro ângulo? '))
y = float(input('Qual o valor do segundo ângulo? '))
z = float(input('Qual o valor do terceiro ângulo? '))

if x+y+z == 180:
    print('Os ângulos formam um triângulo!!!')
else:
    print('Os ângulos {}, {}, {}, não formam um triângulo!!!'.format(x,y,z))

sair = input('\nDigite ENTER para sair...')