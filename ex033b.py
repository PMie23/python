a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando que é menor
# Já coloca 'a' como menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}.'.format(menor))
#Verificando quem é maior com o 'a' já como maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}.'.format(maior))