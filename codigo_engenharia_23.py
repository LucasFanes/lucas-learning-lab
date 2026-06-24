peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura**2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade 1º Grau")
elif 35 <= imc < 40:
    print("Obesidade 2º Grau")
else:
    print("Obesidade 3º Grau")
print(f"Seu IMC é: {imc:.2f}")