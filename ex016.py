import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))
# nesse caso, como não está especificado o "trunc" no import, precisa colocar o import "math.trunc" total