def soma(a, b):
    print(f'A = {a} e B = {b}.')
    s = a + b
    print(f'A soma de A + B = {s}.')


# Programa Principal
soma(b = 4, a = 5)          # Prova de que se pode inverter o local dos valores qnd se explicita.
#soma(b = 7, 2)             # Se não explicitar ambos, dá erro de posicionamento do argumento.
#soma(3, 9, 5)              # Também dará erro pois não tem 3 valores e sim so 2.