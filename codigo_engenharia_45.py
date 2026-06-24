# Módulo de Álgebra Linear: Multiplicação entre duas matrizes (A x B)

def multiplicar_duas_matrizes(historico):
    if len(historico) < 2:
        print("É necessário ter pelo menos duas matrizes salvas no histórico para multiplicar.")
        return None

    print("\n--- Multiplicação entre Duas Matrizes do Histórico ---")
    for i, mat in enumerate(historico):
        print(f"Índice [{i}]: {mat}")

    try:
        idx1 = int(input("Digite o índice da primeira matriz (Matriz A): "))
        idx2 = int(input("Digite o índice da segunda matriz (Matriz B): "))
        
        if 0 <= idx1 < len(historico) and 0 <= idx2 < len(historico):
            matriz1 = historico[idx1]
            matriz2 = historico[idx2]
        else:
            print("Índices incorretos ou inexistentes.")
            return None
    except ValueError:
        print("Entrada inválida! Digite números inteiros.")
        return None

    # Validação matemática da multiplicação de matrizes
    if len(matriz1[0]) != len(matriz2):
        print("Erro matemático: O número de colunas de A deve ser idêntico ao número de linhas de B!")
        return None

    lin_a = len(matriz1)
    col_a = len(matriz1[0])
    col_b = len(matriz2[0])

    # Inicializa matriz resultante preenchida com zeros
    matriz_resultante = [[0 for _ in range(col_b)] for _ in range(lin_a)]

    # Processamento do produto de matrizes (Dot Product)
    for i in range(lin_a):
        for j in range(col_b):
            for k in range(col_a):
                matriz_resultante[i][j] += matriz1[i][k] * matriz2[k][j]

    print("\nMatriz Resultante (A x B):")
    for row in matriz_resultante:
        print(row)
        
    return matriz_resultante