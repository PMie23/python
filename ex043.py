peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
# Ou 'peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('CUIDADO! Você está com BAIXO PESO!')
elif imc <= 24.9:
    print('PARABÉNS! Você está no PESO NORMAL!')
elif imc <= 29.9:
    print('Você está com EXCESSO DE PESO!')
elif imc <= 34.9:
    print('CUIDADO! Você está com OBESIDADE - GRAU I!')
elif imc <= 39.9:
    print('CUIDADO! Você está com OBESIDADE - GRAU II!')
elif imc >= 40:
    print('CUIDADO! Você está com OBESIDADE MÓRBIDA!')