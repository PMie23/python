dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos kms o carro percorreu? '))
print('O valor a pagar é de R${:.2f}.'.format((dias*60) + (km*0.15)))