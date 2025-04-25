from datetime import date
atual = date.today().year
contmaior = 0
contmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(contmaior))
print('E também tivemos {} pessoas menores de idade.'.format(contmenor))
