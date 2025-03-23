casa = float(input('Informe o valor da casa: R$'))
salário = float(input('Informe o seu salário: R$'))
tempo = int(input('Informe em quantos anos você deseja pagar: '))
prestação = casa / (tempo*12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, tempo, prestação))
if prestação < (salário * 30 / 100):
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')