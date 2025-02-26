from math import hypot
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
hi = hypot(c1, c2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))