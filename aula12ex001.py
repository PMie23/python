nome = str(input('Qual é o seu nome? '))
if nome == 'Isaac':
    print('Que nome bonito você tem!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Daniel':
    #Se for algum desses nomes, tera o print abaixo
    print('Esse nome é tão comum no Brasil...')
elif nome in 'Ana Paula Bianca Beatriz':
    #Se for algum desses nomes da lista acima terá o print abaixo
    print('Belo nome feminino')
else:
    #As vezes pode ficar sem else
    print('Seu nome é tão normal...')
print('Tenha um bom dia, {}.'.format(nome))