soma = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite o {}º número: '.format(n)))
    if n % 2 == 0:
        soma += n
        # Q é a msm coisa que 'soma = soma + n'
        cont += 1
        # Que é a msm coisa que 'cont = cont + 1'
print('Você informou {} números PARES e a soma desses números é igual a {}.'.format(cont, soma))