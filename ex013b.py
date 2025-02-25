s1 = float(input('Qual é o salário do funcionário? R$'))
s2 = s1 + (s1*15/100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(s1, s2))