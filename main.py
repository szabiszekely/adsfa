szo = 'almafa'
lista = []
talalat = False
index = 0


for betu in szo:
  print(betu)
  lista.append(betu)

bekert = None
  
while bekert != '':
  bekert = input('Kérek egy betűt: ')
  while index < len(lista) :
    if lista[index] == bekert:
    
    index = index + 1

print(szo)
print(lista)
if talalat:
  print('Volt benne ',bekert)
else:
  print('Nem volt benne ',bekert)