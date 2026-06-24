numero1 = int(input("Digite o primeiro número (a): "))
numero2 = int(input("Digite o segundo número (b): "))

if numero1 < numero2:
    soma = sum(range(numero1, numero2 + 1))
    print(f"A soma dos inteiros no intervalo [{numero1}, {numero2}] é: {soma}")
else:
    print("Erro: O primeiro número deve ser menor que o segundo.")