n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
# Abri uma contagem, começando no número que foi escolhido
print('Calculando {}! => '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    #Comando para que coloque o 'x' até o número 1 e depois o '='
    f *= c
    c -= 1
print('{}'.format(f))