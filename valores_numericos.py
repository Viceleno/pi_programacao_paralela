v=[]
for i in range(10):
  num = float(input("Digite o número {}: ".format(i+1)))
  v.append(num)
  
with open('numeros.txt', 'w') as f:
  for num in v:
    f.write(str(num) + '\n')
    
menor_numero = min(v)
print(f"O menor número na lista é: {menor_numero}")