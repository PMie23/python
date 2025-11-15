valores = list()
maior = 0                                             # Abre-se 2 variaveis para verificar o maior e menor numero
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {cont}: ')))
    if cont == 0:                                   # Será o primeiro número da lista
        maior = menor = valores[cont]                         # então, ele será tanto o maior quanto o menor
    else:                                           # Se não for o primeiro número
        if valores[cont] > maior:                   # E este número for maior que o maior valor
            maior = valores[cont]                   # Este número será o maior valor
        if valores[cont] < menor:                    # se esse número for menor que o menor valor
            menor = valores[cont]                   # Este número será o menor valor
print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for num, valor in enumerate(valores):               # Vai procurar nos 'valores' em looping
    if valor == maior:                              # Ai se o valor for o maior
        print(f'{num}... ', end='')                 # Ele informa
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for num, valor in enumerate(valores):
    if valor == menor:                              # Se for o menor valor,
        print(f'{num}... ', end='')                 # Vai informando também
print()