print('Gerador de PA')
print('-=' * 10)
pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
termo = pt
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='-> ')
    termo = termo + rz
    cont += 1
print('FIM')