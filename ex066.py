n = s = cont = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'VOcê digitou {cont} números e a soma deles foi {s}.')
# print('Você digitou {} números e a soma deles foi {}.'.format(cont, s)) mesmo resultado com a sintaxe diferente