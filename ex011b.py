l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}mx{}m e sua área é de {}m2. \nPara pintar essa parede, você precisará de {}l de tinta.'.format(l, a, l*a, (l*a/2)))