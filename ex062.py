print('SUPER Gerador de PA')
print('-=' * 10)
pt = int(input('Digite o primeiro termo da PA: '))
rz = int(input('Digite a razão da PA: '))
termo = pt
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end='-> ')
        termo = termo + rz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')