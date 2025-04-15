pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
décimo = pt + (10 - 1) * r
# Fórmula do enésimo termo de uma função
for c in range(pt, décimo + r, r):
    print('{} '.format(c), end='-> ')
print('ACABOU')