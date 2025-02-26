c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
hip = (c1 ** 2 + c2 ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hip))
# Utilizando a fórmula matem da hipot q eh "o quadrado da hipot é a soma do quadrado dos catetos".