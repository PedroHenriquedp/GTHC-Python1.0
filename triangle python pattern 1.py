# Proposta:
# Crie um programa na linguagem de programação Python
# que seja capaz de reproduzir no terminal cada umd padrões mostrados abaixo,
# de tal forma que o programa receba um inteiro N como entrada e imprima com saída na tela o
# padrão da 1° linha até a N-ésima linha, onde N pode ter o valor 1 até 99

nome = str(input('Olá! Qual o seu nome? '))
totalDeLinhas = int(input('{}, por favor insira seu valor de entrada '.format(nome)))

for linha in range(0, totalDeLinhas):
    for espaco in range(0,(totalDeLinhas - linha)):
        print(' ', end='')

    for triangulo in range(0,linha+1):
        print("* ", end='')
    print()
sair = input('\nDigite ENTER para sair...')
