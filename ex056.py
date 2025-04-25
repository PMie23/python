somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher20 = 0
for pess in range (1, 4):
    print('----- {}ª pessoa -----'.format(pess))
    nome = str(input('Nome da pessoa: ')).strip()
    idade = int(input('Idade da pessoa: '))
    sexo = str(input('Sexo da pessoa [M/F]: ')).strip()
    somaidade += idade
    if pess == 1 and sexo in 'Mm':
        #Utilizamos tanto o M maiusculo qnt o minusculo para não ter problema caso digite M ou m.
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 3
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomemaisvelho))
print('Ao todo temos {} mulheres com menos de 20 anos.'.format(totmulher20))