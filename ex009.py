# 9. Verificar se um triângulo é equilátero, isósceles ou escaleno pelas suas 3 medidas;

#Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
#Um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.

x = float(input('Qual o valor da primeira medida? '))
y = float(input('Qual o valor da segunda medida? '))
z = float(input('Qual o valor da terceira medida? '))

testeX = abs(y-z)
testeY = abs(x-z)
testeZ = abs(y-x)

if y+z > x > testeX or x+z > y > testeY or y+x > z > testeZ:
    if x == y and y == z:
        print('As três medidas {}, {}, {}, FORMAM um triângulo equilátero!!!'.format(x,y,z))
    elif x == y or y == z or z == x:
        print('As três medidas {}, {}, {}, FORMAM um triângulo isósceles!!!'.format(x,y,z))
    elif x != y and x != z or z != x and z != y or y != x and y != z:
        print('As três medidas {}, {}, {}, FORMAM um triângulo escaleno!!!'.format(x,y,z))
else:
    print('As medidas {}, {}, {}, NÃO FORMAM um triângulo'.format(x,y,z))
sair = input('\nDigite ENTER para sair...')