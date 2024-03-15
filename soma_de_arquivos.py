with open("numeros100.txt", "r") as arquivo:
    conteudo = arquivo.readlines()

soma = 0

for linha in conteudo:
    linha = float(linha)
    soma += linha

print('A soma dos números do arquivo txt: {:.2f}'.format(soma))

