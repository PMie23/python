listaA = [5, 1, 8, 3]
listaB = listaA             # Quando de iguala listas, o Python cria uma ligação entre elas, deixando ambas identicas
listaB[2] = 4               # Mudando em uma lista, muda na outra tambem

# Para criar uma copia de uma lista dentro de outra (e não ter a ligação citada acima):

listaC = [7, 4, 2, 9]
listaD = listaC[:]
listaD[1] = 6               # Nesse caso, só mudou na lista D pq criou uma cópia e não tem ligação entre as listas
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')

print(f'Lista C: {listaC}')
print(f'Lista D: {listaD}')