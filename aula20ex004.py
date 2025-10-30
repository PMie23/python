def contador(* num):                    # Desempacotamento
    for valor in num:                   # Utilizando loop com definição de função.
        print(f'{valor} ', end='')
    print('FIM!')

contador(4, 7, 5, 3)
contador(2, 8)
contador(9, 1, 6, 8, 3)