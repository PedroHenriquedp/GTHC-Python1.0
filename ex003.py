# 3. Calcular a distância entre dois pontos;

x = float(input('Em qual ponto se encontra o A? '))
y = float(input('Em qual ponto se encontra o  B? '))
print('Obs: O programa sempre fará A - B, mas sempre retornará um valor positivo!!!')
distance = x-y

while distance < 0:
    distance = distance*-1

print('A distância entre os dois é de {}'.format(distance))
