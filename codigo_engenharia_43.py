# Módulo de menu de cálculo de áreas geométricas via chaves de dicionário
from math import pi

formas_geometricas = {1: "Círculo", 2: "Triângulo", 3: "Retângulo"}

def calcular_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = pi * raio**2
    print(f"A área do círculo é: {area:.4f}")

def calcular_retangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = base * altura
    print(f"A área do retângulo é: {area:.4f}")

def calcular_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area:.4f}")

while True:
    valid_choice_made = False
    while True:
        print("\nQual forma você quer calcular a área?")
        for n, f in formas_geometricas.items():
            print(f"{n} : {f}")

        user_input_str = input("Digite o número da forma desejada / (Digite 'fim' para sair): ").lower()

        if user_input_str == "fim":
            forma_desejada = "fim"
            valid_choice_made = True
            break

        try:
            temp_int_choice = int(user_input_str)
            if temp_int_choice in formas_geometricas.keys():
                forma_desejada = temp_int_choice
                valid_choice_made = True
                break
            else:
                print("Forma inválida! Por favor, digite um número correspondente a uma forma existente.")
        except ValueError:
            print("Entrada inválida! Por favor, digite um número ou 'fim'.")

    if forma_desejada == "fim":
        print("Saindo do programa...")
        break

    forma_encontrada = formas_geometricas[forma_desejada]
    print(f"\nVocê escolheu a forma: {forma_encontrada}")
    if forma_desejada == 1:
        calcular_circulo()
    elif forma_desejada == 2:
        calcular_triangulo()
    elif forma_desejada == 3:
        calcular_retangulo()