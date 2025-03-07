n = int(input('Me diga um número qualquer: '))
num = n % 2
if num == 0:
    print('O número {} é PAR.'.format(n))
else:
    print('O número {} é ÍMPAR.'.format(n))