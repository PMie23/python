valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor : ')))    # Pediu para o usuário digitar os 5 valores

for c, v in enumerate(valores):                         # Criou as posições dos valores digitados
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')