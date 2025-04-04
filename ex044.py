print('{:=^40}'.format(' LOJAS GUANABARA '))
# Esse sinal dentro dos colchetes significa: com o = e o texto, centralize com 40 espaços
valor = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO: ')
print('[ 1 ] à vista - dinheiro/cheque')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual sua opção? '))
if opcao == 1:
    print('Sua compra de R${:.2f}, paga à vista, vai custar R${:.2f} no final.'.format(valor, valor - (valor * .10)))
elif opcao == 2:
    print('Sua compra de R${:.2f}, paga no cartão à vista, vai custar R${:.2f} no final.'.format(valor, valor - (valor * .05)))
elif opcao == 3:
    print('Sua compra de R${:.2f}, paga em 2x no cartão de crédito, vai custar R${:.2f} no final.'.format(valor, valor))
elif opcao == 4:
    parcela = int(input('Quantas parcelas gostaria de dividir? '))
else:
    print('OÇÃO INVÁLIDA! Tente novamente!')
    print('Sua compra de R${:.2f}, parcelado em {} vezes, vai custar R${} no final.'.format(valor, parcela, valor + (valor * .20)))
