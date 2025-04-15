n = int(input('Digite um número: '))
tot = 0
# Conta quantas vezes deu o argumento
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))
# O cód acima é \n = quebra de linha e \033[m é voltar a cor normal
if tot == 2:
    print('E por isso esse número é PRIMO.')
else:
    print('E por isso esse número NÃO É PRIMO.')
