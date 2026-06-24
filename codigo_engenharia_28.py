older = float('-inf')
younger = float('inf')
oldersname, youngersname = "", ""
contador_alunos = 0

while True:
    contador_alunos += 1
    nome = input(f"Digite o nome do aluno {contador_alunos}: ")
    age = float(input(f"Digite a idade de {nome} (ou número negativo para sair): "))

    if age < 0:
        break

    if age > older:
        older = age
        oldersname = nome
    if age < younger:
        younger = age
        youngersname = nome

if contador_alunos > 1:
    print(f"\nMais velho: {oldersname} ({older} anos)")
    print(f"Mais novo: {youngersname} ({younger} anos)")
    print(f"Média das idades extremas: {(older + younger) / 2:.2f}")