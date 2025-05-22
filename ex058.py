from random import randint
from time import sleep
comput = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == comput:
        acertou = True
    else:
        if jogador < comput:
            print('Mais... Tente mais uma vez!')
        elif jogador > comput:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas. Parabéns!'.format(palpite))