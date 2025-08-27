total = prod1000 = menor = cont = 0
barato = ''
print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
while True:
    prod = str(input('Nome do Produto: '))
    value = float(input(('Preço: R$ ')))
    cont += 1
    total += value
    if value > 1000:
        prod1000 += 1
    if cont == 1:
        menor = value
        barato = prod
    else:
        if value < menor:
            menor = value
            barato = prod
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if tipo == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {total:.2f}.')
print(f'Temos {prod1000} produtos custando mais de R$ 1.000,00.')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}.')