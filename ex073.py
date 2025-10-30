times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Bahia', 'Botafogo',
         'Mirassol', 'São Paulo', 'Bragantino', 'Fluminense', 'Ceará',
         'Corinthians', 'Atlético-MG', 'Internacional', 'Grêmio',
         'Santos', 'Vasco', 'Vitória', 'Juventude', 'Fortaleza', 'Sport')
print('-=' * 15)
print(f'Os times do Brasileirão são: {times}.')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-=' * 15)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-=' * 15)
print(f'O clube Mirassol está na {times.index("Mirassol")+1}ª posição.')
print('-=' * 15)
