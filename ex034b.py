sal = float(input('Qual é o valor do salário do funcionário? R$'))
saln = sal + (sal * 0.10) if sal > 1250  else sal + (sal * 0.15)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, saln))