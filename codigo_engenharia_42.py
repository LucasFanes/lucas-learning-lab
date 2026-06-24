# Módulo de Calculadora Trigonométrica Interativa (POO)
from math import sin, cos, tan, radians

class CalculadoraTrigonometrica:
    def __init__(self, angulo_graus):
        self.angulo_graus = angulo_graus
        # Converte o ângulo automaticamente para radianos (necessário para a biblioteca math)
        self.angulo_radianos = radians(angulo_graus)

    def obter_seno(self):
        return sin(self.angulo_radianos)

    def obter_cosseno(self):
        return cos(self.angulo_radianos)

    def obter_tangente(self):
        try:
            # Trata o caso de tangentes indefinidas (ex: 90 graus)
            if self.angulo_graus % 180 == 90:
                raise ValueError("A tangente para este ângulo é indefinida.")
            return tan(self.angulo_radianos)
        except ValueError as e:
            return str(e)

# Loop interativo do programa
while True:
    resposta = input("\nDeseja realizar um cálculo trigonométrico? (s/n): ").lower()
    if resposta != "s":
        print("Saindo da calculadora...")
        break

    try:
        valor_angulo = float(input("Digite o valor do ângulo em graus: "))
        calc = CalculadoraTrigonometrica(valor_angulo)
        
        # Mapeamento do menu utilizando dicionário de funções (Estrutura profissional)
        operacoes = {
            "1": ("Seno", calc.obter_seno),
            "2": ("Cosseno", calc.obter_cosseno),
            "3": ("Tangente", calc.obter_tangente)
        }

        while True:
            print(f"\n--- Menu Trigonométrico (Ângulo: {valor_angulo}° ) ---")
            for chave, info in operacoes.items():
                print(f"{chave}. Calcular {info[0]}")
            print("0. Escolher outro ângulo / Sair")

            escolha = input("Sua escolha: ")

            if escolha == '0':
                break
            elif escolha in operacoes:
                nome_operacao = operacoes[escolha][0]
                resultado = operacoes[escolha][1]()
                
                # Se o resultado for número, formata; se for texto (erro da tangente), exibe direto
                if isinstance(resultado, float):
                    print(f"-> Resultado da operação {nome_operacao}: {resultado:.4f}")
                else:
                    print(f"-> {resultado}")
            else:
                print("Opção inválida! Escolha um número do menu.")

    except ValueError:
        print("Por favor, introduza um valor numérico válido para o ângulo.")