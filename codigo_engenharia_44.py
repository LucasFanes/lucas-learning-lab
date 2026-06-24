# Módulo de Álgebra Linear: Geração de Matrizes e Multiplicação por Escalar Constante
from random import shuffle, choice

lista_numeros = []
item_escolhidos_global = []
historico_matrizes = []

def gerar_matriz_aleatoria():
    while True:
        print("\n--- Bem vindo ao gerador de matrizes aleatórias ---")
        lista_numeros.clear()
        
        intervalo_inicial = int(input("Digite o valor inicial do intervalo: "))
        intervalo_final = int(input("Digite o valor final do intervalo: "))
        
        for i in range(intervalo_inicial, intervalo_final + 1):
            lista_numeros.append(i)
        shuffle(lista_numeros)
        
        while True:
            colunas = int(input("Digite o número de colunas da matriz: "))
            linhas = int(input("Digite o número de linhas da matriz: "))
            if linhas <= 0 or colunas <= 0:
                print("O número de linhas e colunas deve ser maior que zero.")
            else:
                break

        num_elementos = colunas * linhas
        elemento_inicial = len(item_escolhidos_global)
        
        while len(item_escolhidos_global) < elemento_inicial + num_elementos:
            item = choice(lista_numeros)
            item_escolhidos_global.append(item)

        print("\nSua matriz aleatória:")
        matriz_atual = []
        for i in range(linhas):
            linha_matriz = []
            for j in range(colunas):
                elemento = item_escolhidos_global[elemento_inicial + i * colunas + j]
                print(f"{elemento:<4}", end=" ")
                linha_matriz.append(elemento)
            matriz_atual.append(linha_matriz)
            print()

        historico_matrizes.append(matriz_atual)
        print(f"Matriz gerada com sucesso. Histórico possui {len(historico_matrizes)} matriz(es).")

        continuar = input("Deseja gerar outra matriz? (s/n): ").lower()
        if continuar != 's':
            break

def multiplicar_por_constante():
    if not historico_matrizes:
        print("Erro: Nenhuma matriz foi gerada no histórico ainda.")
        return

    print("\n--- Multiplicador de Matriz por Constante Escalar ---")
    opcao = input("Deseja multiplicar a última matriz por uma constante? (s/n): ").lower()
    
    if opcao == "s":
        constante_input = input("Digite o valor da constante numérica (ou 'fim' para sair): ")
        if constante_input.lower() == "fim":
            return
            
        try:
            constante = float(constante_input)
            matriz_alvo = historico_matrizes[-1]
            
            matriz_multiplicada = []
            for r_idx in range(len(matriz_alvo)):
                nova_linha = []
                for c_idx in range(len(matriz_alvo[0])):
                    nova_linha.append(matriz_alvo[r_idx][c_idx] * constante)
                matriz_multiplicada.append(nova_linha)

            print(f"\nMatriz Resultante da Multiplicação por {constante}:")
            for row in matriz_multiplicada:
                print(row)
                
            historico_matrizes.append(matriz_multiplicada)
        except ValueError:
            print("Entrada inválida! Por favor, insira um número real.")

# Teste sequencial
gerar_matriz_aleatoria()
multiplicar_por_constante()