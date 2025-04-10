for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou!')
#Nesse caso, existe uma quantidade maior de interações do range que no exercício passado pq ele testa 50x o laço.
# No passado, ele testava com o intervalo de 2 em 2, testando menos o laço e sendo mais rapido e economico.