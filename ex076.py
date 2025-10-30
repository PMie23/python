def linha():
    print('-' * 40)

linha()
print(f'{"LISTA DE MATERIAL ESCOLAR":^40}')
linha()

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Mochila', 120.3,
            'Caneta', 10.53)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:                            # Vai mostrar os itens que são pares primeiros
        print(f'{listagem[pos]:.<30}', end='')  # Vai mostrar com formatação de pontos até 30 espaços ":.<30"
    else:                                       # Vai mostrar depois do comando acima, os itens ímpares
        print(f'R${listagem[pos]:>7.2f}')       # Vai mostrar com formatação para finalizar com 7 espaços depois do "R$"
linha()
