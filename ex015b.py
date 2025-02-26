dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos kms o carro percorreu? '))
pago = (dias * 60) + (km * 0.15)
print('O valor do aluguel do carro a pagar é R${:.2f}.'.format(pago))