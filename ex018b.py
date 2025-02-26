from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}. '
      '\nO ângulo de {} tem o COSSENO de {:.2f}. '
      '\nO ângulo de {} tem TANGENTE de {:.2f}.'
      .format(ang, sen, ang, cos, ang, tang))