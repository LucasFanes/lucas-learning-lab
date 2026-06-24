# Módulo de cálculo de áreas geométricas interativo
from math import pi

def calcular_area_circulo(raio):
    return pi * raio ** 2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_retangulo(base, altura):
    return base * altura

while True:
    print("\nQual forma você quer calcular a área?")
    print("1 : Círculo")
    print("2 : Triângulo")
    print("3 : Retângulo")
    
    opcao = input("Digite o número da forma desejada / (Digite 'fim' para sair): ").lower()
    
    if opcao == 'fim':
        print("Saindo do programa...")
        break
        
    if opcao == "1":
        print("Você escolheu a forma: Círculo")
        raio = float(input("Digite o raio do círculo: "))
        print(f"A área do círculo é: {calcular_area_circulo(raio):.4f}")
        
    elif opcao == "2":
        print("Você escolheu a forma: Triângulo")
        base = float(input("Digite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        print(f"A área do triângulo é: {calcular_area_triangulo(base, altura):.4f}")
        
    elif opcao == "3":
        print("Você escolheu a forma: Retângulo")
        base = float(input("Digite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        print(f"A área do retângulo é: {calcular_area_retangulo(base, altura):.4f}")
        
    else:
        print("Opção inválida! Tente novamente.")