n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
        #Se o usuário colocar qq núm, continua eternamente até colocar 999 que sai do laço e para a repetição
    s += n
print(f'A soma vale {s}')
# print('A soma vale {}.'.format(s))
# O comando acima serve do mesmo jeito. Essa escrita é chamada de "F String" e é utilizada a partir do Python 3.6