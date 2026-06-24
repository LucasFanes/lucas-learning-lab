# Módulo Geométrico da Classe Retângulo

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def calcular_area(self):
        return self.base * self.altura

# Exemplo de uso:
meu_retangulo = Retangulo(base=10.0, altura=5.0)
print(f"Retângulo de {meu_retangulo.base}x{meu_retangulo.altura}:")
print(f"Perímetro: {meu_retangulo.calcular_perimetro()}")
print(f"Área: {meu_retangulo.calcular_area()}")