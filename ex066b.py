n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    s += n
    cont += 1
print('Você digitou {} números e a soma deles foi {}.'.format(cont - 1, s - 999))