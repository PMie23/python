m = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a \n{:.4f}km \n{:.3f}hm \n{:.2f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, m*0.001, m*0.01, m*0.1, m*10, m*100, m*1000))