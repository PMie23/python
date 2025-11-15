valores = list()
valores.append(8)
valores.append(4)
valores.append(1)

for c, v in enumerate(valores):                      # O comando 'enumerate' pega tanto a chave (c) quanto o valor (v)
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')