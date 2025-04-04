print('{:=^40}'.format(' LOJAS TAVARES '))
preco = int(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista - dinheiro/cheque
[ 2 ] à vista - cartão de crédito
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    valor = preco - (preco * 10 / 100)
elif opcao == 2:
    valor = preco - (preco * 5 / 100)
elif opcao == 3:
    valor = preco
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4:
    valor = preco + (preco * 20 / 100)
    parcela = int(input('Em quantas parcelas gostaria de dividir? '))
    vlrfinal = valor / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, vlrfinal))
else:
    print('OPÇÃO INVÁLIDA. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, valor))
