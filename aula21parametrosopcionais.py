def somar(a=0, b=0, c=0):           #Colocando "=0" depois dos valores, caso na função chamada não tenha todos
    s = a + b + c                   #os valores, ele preenche com o 0.
    print(f'A soma vale {s}.')


somar(b = 4, a = 2)                 # Nesse caso eu informei fora da ordem e sem um dos valores. Sem problemas.
somar()                             # Mesmo sem valores, não dá erro no código.