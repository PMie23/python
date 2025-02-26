import math
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjajcente: '))
hip = math.hypot(c1, c2)
print('A hipotenusa vai medir {:.2f}.'.format(hip))