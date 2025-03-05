num = int(input('Informe um número: '))
u = num // 1 % 10
# Nesse caso, eu divido o núm por 1 e tira o módulo da divisão por 10 e utilizo o resto da divisão
d = num // 10 % 10
# Nesse caso, eu divido o núm por 10 e tira o módulo da divisão por 10 e utilizo o resto da divisão
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}:'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))