l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l*a
tinta = (l*a)/2
print('Sua parede tem a dimensão de {}mx{}m e sua área é de {}m2.'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))