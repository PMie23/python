def teste(b):
    global a                # Esse comando informa que não é para utilizar o a do escopo global,
    a = 8                   #mas sim utilizar o a do local como global
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


a = 5                           # Não irá usar esse a, mas sim o a local como global
teste(a)
print(f'A fora vale {a}')