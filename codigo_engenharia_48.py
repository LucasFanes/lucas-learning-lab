# Módulo de Gravação/Leitura e Persistência de Arquivos JSON
import json

def salvar_dados_json(dados, nome_arquivo='funcionarios.json'):
    """Serializa estruturas de dicionários e escreve em arquivos .json."""
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print(f"Sucesso: Dados persistidos em '{nome_arquivo}'")

def carregar_dados_json(nome_arquivo='funcionarios.json'):
    """Carrega strings do arquivo .json e as converte de volta em dicionário."""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        print(f"Sucesso: Dados importados de '{nome_arquivo}'")
        return dados
    except FileNotFoundError:
        print(f"Aviso: Arquivo '{nome_arquivo}' não existe. Retornando objeto vazio.")
        return {}