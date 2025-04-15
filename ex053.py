frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
# Dividiu toda a frase em palavras dentro dos colchetes
junto = ''.join(palavras)
# Juntou todas as palavras sem espaço
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    # Comando para fazer a leitura ao contrário
if inverso == junto:
    print('A frase digitada é um PALÍNDROMO.')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO.')