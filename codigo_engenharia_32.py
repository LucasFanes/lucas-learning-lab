A = [[2, 1, -5], [3, 7, 0], [6, 4, 8]]
tr_A = 0
soma_A = 0
lin = len(A)
col = len(A[0])

print("Estrutura da Matriz A:")
for i in range(lin):
    for j in range(col):
        if i == j:
            tr_A += A[i][j]
        soma_A += A[i][j]
        print(f"{A[i][j]:4}", end=" ")
    print()

print(f"\nTraço de A, tr(A) = {tr_A}")
print(f"Soma de todos os elementos de A = {soma_A}")