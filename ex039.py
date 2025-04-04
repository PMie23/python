from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sexo = str(input('Você é do sexo masculino ou feminino? ')).lower()
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if sexo == 'feminino':
    print('Mas como você é do sexo feminino, você não tem obrigação de se alistar no Exército. Este programa não é necessariamente para você.')
elif sexo == 'masculino':
    print('''Como você é do sexo masculino, você tem a obrigação de se alistar no Exército. 
Verifique abaixo suas informações:''')
    if idade < 18:
        print('''Ainda faltam {} anos para o alistamento.
Seu alistamento será em {}.'''.format(18-idade, atual+(18-idade)))
    elif idade > 18:
        print('''Você já deveria ter se alistado há {} anos.
Seu alistamento foi em {}.'''.format(idade-18, atual-(idade-18)))
    else:
        print('Você tem que se alistar IMEDIATAMENTE!!!')
else:
    print('Você precisa digitar seu sexo novamente. Tente outra vez.')
