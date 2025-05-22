from pydoc import stripid

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
# O [] do final é para indicar que so precisa pegar a primeira letra, caso a pessoa escreva mais de uma.
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))