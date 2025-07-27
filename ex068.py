from random import randint
v = 0
print('-=-' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 10)
while True:
    n = int(input('Diga um valor: '))
    comput = randint(0, 10)
    s = n + comput
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print('-' * 30)
    print(f'Você jogou {n} e o computador {comput}. Total de {s}.')
    print('DEU PAR!' if s % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if s % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if s % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('-' * 30)
    print('Vamos jogar novamente...')
    print('-' * 30)
print(f'GAME OVER! Você venceu {v} vezes.')
