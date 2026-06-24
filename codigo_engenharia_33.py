from random import randrange

linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))

A = [[randrange(1, 11) for _ in range(colunas)] for _ in range(linhas)]
B = [[randrange(1, 11) for _ in range(colunas)] for _ in range(linhas)]

abaixoDP = 0
acimaDP = 0

for i in range(linhas):
    for j in range(colunas):
        if i > j:
            abaixoDP += A[i][j]
        if i < j:
            acimaDP += B[i][j]

print("\nMatriz A:")
for row in A:
    print(*(f"{x:4}" for x in row))

print("\nMatriz B:")
for row in B:
    print(*(f"{x:4}" for x in row))

print(f"\nSoma acumulada (Abaixo DP de A + Acima DP de B) = {abaixoDP + acimaDP}")