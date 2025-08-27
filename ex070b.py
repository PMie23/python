total = cont = prod1000 = menor = 0
barato = ' '
print('-' * 30)
print('{:-^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
while True:
    prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    cont +=1
    total += preco
    if preco > 1000:
        prod1000 += 1
    if cont == 1:
        menor = preco
        barato = prod
    else:
        if preco < menor:
            menor = preco
            barato = prod
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if tipo == 'N':
        break
print('-' * 30)
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {prod1000} produtos custando mais de R$1.000,00.')
print(f'O produto mais barato foi {barato}, que custa R${menor:.2f}.')
