def dobra(lista):                   # Essa função servirá para dobrar os valores da lista
    pos = 0                         # E nesse caso não é desempacotamento
    while pos < len(lista):
        lista[pos] *= 2             # Significa que os valores da lista irão ser multip. por 2
        pos += 1


valores = [6, 4, 2, 7, 0, 9]
dobra(valores)
print(valores)