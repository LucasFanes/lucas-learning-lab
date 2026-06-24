# Módulo de Inteligência Analítica de RH (Estatísticas de Gênero)

def lista_mulheres_por_setor(cadastro_funcionarios, departamento_alvo):
    """Retorna um sub-dicionário com as colaboradoras do setor informado."""
    mulheres_do_setor = {}
    for matricula, dados in cadastro_funcionarios.items():
        nome, sexo, departamento, temps, salario = dados
        if sexo.lower() == 'f' and departamento.lower() == departamento_alvo.lower():
            mulheres_do_setor[matricula] = dados
    return mulheres_do_setor

def calcular_media_salarial_por_genero(cadastro_funcionarios, sexo_alvo):
    """Calcula e retorna a média salarial filtrada por gênero biológico."""
    total_salario = 0
    contador_sexo = 0
    funcionarios_do_sexo = {}

    for matricula, dados in cadastro_funcionarios.items():
        if dados[1].lower() == sexo_alvo.lower():
            contador_sexo += 1
            total_salario += dados[4]
            funcionarios_do_sexo[matricula] = dados

    media_salarial = total_salario / contador_sexo if contador_sexo > 0 else 0
    return funcionarios_do_sexo, media_salarial