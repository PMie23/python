n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
#Abrindo 3 aspas, vc pode escrever quebrando linha normalmente
if opção == 1:
    print('{} convertido em BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido em OCTAl é igual a {}.'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido em HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')