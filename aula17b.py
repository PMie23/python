valores = list(range(4, 11))            # Comando 'list' tambem cria lista.
                                        # O 'range' vai criar elementos de 4 até antes do 11.

desordenados = [8, 2, 5, 3, 7, 9, 1]
desordenados.sort()                     # Comando que ordena os valores da lista
desordenados.sort(reverse=True)         # Comando que ordena ao contrario
len(desordenados)                       # Comando que informa quantos elementos tem na lista

print(valores)
print(desordenados)
print(f'A lista "Desordenados" tem {len(desordenados)} itens.')