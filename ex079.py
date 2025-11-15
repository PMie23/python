valores = []
while True:                                     # Dando loop até o usuário pedir para parar
    num = int(input('Digite um valor: '))
    if num not in valores:                      # Add valores
        valores.append(num)
        print('Valor adicionado com sucesso.')
    else:                                       # Bloqueando os valores iguais
        print('Valor duplicado. Não será adicionado.')
    resp = str(input('Você gostaria de continuar? [S/N] ').lower().strip())     # Escolha do usuário se continua
    if resp in 'Nn':                            # Quando ele não quiser mais, para o programa
        break
print('-=' * 30)
valores.sort()                                  # Comando para ordenar os números
print(f'Você digitou os valores {valores}.')