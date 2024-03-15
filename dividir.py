def dividir_arquivo(origem, destino, tamanho_maximo):
    with open(origem, 'r') as arquivo_origem:
        conteudo = arquivo_origem.readlines()

    num_partes = len(conteudo) // tamanho_maximo + (1 if len(conteudo) % tamanho_maximo != 0 else 0)

    for i in range(num_partes):
        parte = conteudo[i * tamanho_maximo: (i + 1) * tamanho_maximo]
        nome_arquivo = f"{destino}_{i + 1}.txt"
        with open(nome_arquivo, 'w') as arquivo_destino:
            arquivo_destino.writelines(parte)

    print(f"Arquivo dividido em {num_partes} partes.")

# Exemplo de uso
arquivo_origem = "numeros1000.txt"  # Nome do arquivo original
arquivo_destino = "viceleno"  # Prefixo do nome dos arquivos de destino (parte1.txt, parte2.txt, etc.)
tamanho_maximo = 100  # Tamanho máximo de linhas por arquivo

dividir_arquivo(arquivo_origem, arquivo_destino, tamanho_maximo)

