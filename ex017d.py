from math import hypot
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}.'.format(hypot(c1, c2)))
#Utilizando o import de hypot e colocando o calculo dentro do format. Mais direto.