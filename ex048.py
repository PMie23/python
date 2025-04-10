soma = 0
# Temos que utilizar um acumulador.
cont = 0
# Utilizaremos também um contador para saber quantos números estão no resultado da soma.
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont += 1
        # Ou 'cont = cont + 1'
        soma += n
        # Ou 'soma = soma + n'
print('A soma de todos os {} números solicitados é {}.'.format(cont, soma))
