totM18 = totM = totF20 = 0
print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if i > 18:
        totM18 += 1
    if s == 'M':
        totM += 1
    if s == 'F' and i < 20:
        totF20 += 1
    print('-' * 20)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-' * 20)
print(f'Total de pessoas com mais de 18 anos: {totM18}.')
print(f'Ao todo temos {totM} homens cadastrados.')
print(f'E temos {totF20} mulheres com menos de 20 anos.')