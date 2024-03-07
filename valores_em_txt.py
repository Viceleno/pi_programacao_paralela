with open('valores.txt', 'w') as arquivo:
  for i in range(10):
    valor = float(input(f"Digite o {i+1}º valor: "))
    arquivo.write(f"{valor}\n")

print("Valores foram escritos no arquivo 'valores.txt'.")