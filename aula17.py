lanche = ['pão', 'queijo', 'salame', 'catchup']     # As listas são escritas com [].

# Diferente das tuplas, as listas são mutáveis
lanche[3] = 'catchups'                              # Comando que pode modificar o item de uma lista

lanche.append('roupa')                              # Esse comando add itens no FIM  da lista

lanche.insert(0, 'maionese')         # Comando para inserir na localização informada

del lanche[2]                                       # Comando para eliminar itens
# Ou
lanche.pop(4)                                       # Se usado sem indicação, apaga o último elemento
# Ou
lanche.remove('salame')                             # Esse tem que indicar o valor que quer eliminar

# Se tentar remover algo que não esteja na lista, vai dar erro no output
# Ex: lanche.remove('roupa')

# Para remover o item, apenas se ele esteja nos itens, fazer:
if 'roupa' in lanche:
    lanche.remove('roupa')

print(lanche)