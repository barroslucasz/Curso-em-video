medida = float(input('Digite uma distancia em Metros:'))
dam = medida / 10
hm = medida / 100
km = medida / 1000
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m é igual a:'.format(medida))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
