d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar sua viagem de {}Km.'.format(d))
if d <= 200:
    v1 = d * 0.50
    print('E o preço de sua passagem será de R${:.2f}.'.format(v1))
else:
    v2 = d * 0.45
    print('E o preço da sua passagem será de R${:.2f}.'.format(v2))