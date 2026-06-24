# Módulo de Avaliação Escolar Utilizando Classes (POO)

class Disciplina:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas # Deve receber uma lista/tupla com 2 notas

    def calcular_media(self):
        return (self.notas[0] + self.notas[1]) / 2

    def exibir_situacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return 'Aprovado'
        elif media >= 3.0:
            return 'Em Recuperação'
        else:
            return 'Reprovado'

# Exemplo rápido de teste da classe:
materia = Disciplina("Cálculo Diferencial I", [5.5, 7.0])
print(f"Matéria: {materia.nome}")
print(f"Média Final: {materia.calcular_media():.2f}")
print(f"Situação do Aluno: {materia.exibir_situacao()}")