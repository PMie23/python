from random import randint
from time import sleep
# Esta função faz o computador simular uma espera
pc = randint(0, 5)
# Faz o código pensar e escolher randonicamente o número.
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if player == pc:
    print('EXATO! Este foi o número escolhido!')
else:
    print('GANHEI! Não foi esse o número. Eu pensei no número {} e não no {}.'.format(pc, player))
# O jogador tenta adivinhar o número
