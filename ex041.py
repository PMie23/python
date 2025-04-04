from datetime import date
niver = int(input('Ano de Nascimento: '))
idade = date.today().year - niver
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('O atleta é MIRIM.')
elif 9 < idade <= 14:
    print('O atleta é INFANTIL.')
elif 14 < idade <= 19:
    print('O atleta é JUNIOR.')
elif 19 < idade <= 25:
    print('O atleta é SÊNIOR.')
elif idade > 25:
    #poderia ser 'else:'
    print('O atleta é MASTER.')