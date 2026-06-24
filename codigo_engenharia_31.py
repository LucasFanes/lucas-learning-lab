contador = 0
notatotal = 0

while True:
    contador += 1
    nota1 = float(input(f"Digite a 1ª nota do aluno {contador}: "))
    nota2 = float(input(f"Digite a 2ª nota do aluno {contador}: "))
    
    if not (0 <= nota1 <= 10) or not (0 <= nota2 <= 10):
        print("Nota inválida digitada. Encerrando programa...")
        break
    
    notadoaluno = (nota1 + nota2) / 2
    notatotal += notadoaluno
    print(f"Média do aluno {contador}: {notadoaluno:.2f}")
    print(f"Média acumulada da turma: {notatotal / contador:.2f}\n")