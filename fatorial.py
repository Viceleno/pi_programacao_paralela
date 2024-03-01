
n = int(input('Digite uma variavel: '))
fat = n
contador = 1
while contador < n:
  fat = fat * contador
  contador = contador + 1
  
print('O fatorial de', n , 'é:', fat)
