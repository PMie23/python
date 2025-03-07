d = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
# Este tipo de regra se chama Operação ternária (tem muito em outras linguagens)
print('E o preço da sua passagem será de R${:.2f}.'.format(preço))
