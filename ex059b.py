from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior Número
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    opção = int(input('>>>>>>>>>>>> Qual a sua opção? '))
    sleep(0.5)
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('O produto entre {} * {} é {}.'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(1.5)
print('Fim do Programa. Volte Sempre!')