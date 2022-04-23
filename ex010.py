# 10. Coletar uma letra e verificar se é uma consoante ou vogal.

nome = input('Qual seu nome? ')
letra = input('{}, por favor insira apenas UMA LETRA '.format(nome))



if letra.lower() == 'a' or letra.lower() == 'i' or letra.lower() == 'u' or letra.lower() == 'e' or letra.lower() == 'o':
    print('A letra {}, é uma vogal'.format(letra))
else:
    print('A letra {}, é uma consoante'.format(letra))
sair = input('\nDigite ENTER para sair...')