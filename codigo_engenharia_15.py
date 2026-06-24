Numero1 = int(input("Digite o primeiro número: "))
Numero2 = int(input("Digite o segundo número: "))
print("\n1. Média ponderada (pesos 2 e 3)\n2. Quadrado da soma\n3. Cubo do menor número")
Respostaopcao = input("Escolha uma opção: ")

if Respostaopcao == "1":
    temp_num = (Numero1*2 + Numero2*3) / 5
    print(f"A média ponderada é: {temp_num}")
elif Respostaopcao == "2":
    temp_num2 = (Numero1 + Numero2)**2
    print(f"O quadrado da soma dos números é: {temp_num2}")
elif Respostaopcao == "3":
    temp_num3 = Numero1**3 if Numero1 < Numero2 else Numero2**3
    print(f"O cubo do menor número é: {temp_num3}")
else:
    print("Opção inválida")