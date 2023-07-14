largura = float(input('largura da parede:'))
altura = float(input('Altura da parede:'))
print('Sua parede tem dimensões de {}x{} e sua área é de {}m²'.format(largura, altura, largura*altura))
print('Para pintar sua parede, você precisará de {}l de tinta.'.format((largura*altura)/2))
