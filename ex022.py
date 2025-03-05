nome = str(input('Digite seu nome completo: ')).strip()
#O strip serve para que logo de início, o cód. ja corte a...
# contagem de todos os espaços inúteis anteriores e posteriores da frase
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minpusculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
# A ideia é que o .count conte quantos espacos ' ' tem na frase e diminua...
#do numero de quantidade de letras a serem contados
separa = nome.split()
# Este comando serve para separar cada nome como item de uma lista.
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
# Pedimos para ele mostrar apenas o item '0' da lista de itens da frase