n = int(input('Digite o numero de posições: '))
v = []
for i in range(n):
    valor = int(input('Digite o valor: '))
    v.append(valor)

menor = v[0]
for i in range(n):
    if v[i] < menor:
        menor = v[i]

print('O menor valor é: ', menor)

        
