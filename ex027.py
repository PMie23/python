n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
#Dividiu cada nome como item de uma lista
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(nome[0]))
print('Seu último nome é {}.'.format(nome[len(nome)-1]))
# Usou o len para que o codigo contasse qnts posições tem na lista e depois retirasse 1.
# O len conta a partir de 1 e não a partir de 0.