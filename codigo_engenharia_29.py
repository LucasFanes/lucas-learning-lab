contador_alunos = 0
maiorestatura = float('-inf')
menorestatura = float('inf')
estaturatotal = 0.0

while True:
    estatura_input = float(input("Digite a estatura (ou um número negativo para sair): "))
    if estatura_input < 0:
        break
    
    contador_alunos += 1
    estaturatotal += estatura_input
    
    if estatura_input > maiorestatura:
        maiorestatura = estatura_input
    if estatura_input < menorestatura:
        menorestatura = estatura_input

if contador_alunos > 0:
    print(f"\nMaior estatura: {maiorestatura:.2f}m")
    print(f"Menor estatura: {menorestatura:.2f}m")
    print(f"Média de estatura: {estaturatotal / contador_alunos:.2f}m")