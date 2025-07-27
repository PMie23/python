while True:
    n1 = int(input('Você gostaria da tabuada de qual número? '))
    print('_' * 30)
    if n1 < 0:
        break
    for n2 in range(1, 11):
        print(f'{n1} x {n2} = {n1*n2}')
    print('_' * 30)
print('PROGRAMA TABUADA EXNCERRADO. Vote sempre!')