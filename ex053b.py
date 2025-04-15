frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# Macete do fatiamento: Substitui o for in do ex053, fazendo com que ele leia da primeira a ultima letra de trás pra frente
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO.')
else:
    print('Essa frase NÃO É UM PALÍNDROMO.')
# Exercício sem for