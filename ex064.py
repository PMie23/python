num = 0
cont = 0
soma = 0
#No ex. b tem como fazer tudo o que tem em cima em uma linha só
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma += num
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont - 1, soma - 999))
#No ex. b tem a maneira um pouco melhor de se fazer o format sem precisa do "-1" e do "-999"