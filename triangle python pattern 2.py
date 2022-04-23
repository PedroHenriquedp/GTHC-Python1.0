# Proposta:
# Crie um programa na linguagem de programação Python
# que seja capaz de reproduzir no terminal cada umd padrões mostrados abaixo,
# de tal forma que o programa receba um inteiro N como entrada e imprima com saída na tela o
# padrão da 1° linha até a N-ésima linha, onde N pode ter o valor 1 até 99
#Padrão 3
nome = str(input('Olá! Qual o seu nome? '))
totalDeLinhas = int(input('{}, por favor insira seu valor de entrada '.format(nome)))
numero = 1
for linha in range(1, totalDeLinhas+1):
    for espaco in range(1,linha+1):
        print(numero, end=' ')
        numero = numero+1
    print()
sair = input('\nDigite ENTER para sair...')