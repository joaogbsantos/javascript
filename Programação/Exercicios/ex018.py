import math
an = float(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print ('O ângulo de {:.1f} tem o SENO de {:.2f} \n O ângulo de {:.1f} tem o COSSENO de {:.2f} \n O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(an, sen, an, cos, an, tan))