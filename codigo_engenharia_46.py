# Módulo de Banco de Dados de Recursos Humanos Local

dicionario_funcionarios = {}

def obter_dados_funcionario():
    global dicionario_funcionarios
    while True:
        
        # Validação de Matrícula
        while True:
            matricula_input = input("\nDigite seu número de matrícula (ou 'fim' para fechar): ")
            if matricula_input.lower() == "fim":
                matricula = "fim"
                break
            try:
                matricula = int(matricula_input)
                if matricula <= 0:
                    print("Matrícula inválida! Deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("Por favor, insira um valor numérico inteiro.")

        if matricula == "fim":
            break

        nome = input("Digite seu nome completo: ")

        # Validação de Gênero
        while True:
            sexo = input("Digite seu sexo [F/M]: ").lower()
            if sexo in ["f", "m"]:
                break
            else:
                print("Opção inválida! Escreva apenas 'F' ou 'M'.")

        departamento = input("Digite seu departamento/setor: ")

        # Validação de Tempo de Serviço
        while True:
            temps_input = input("Digite seu tempo de serviço (anos inteiros): ")
            try:
                tempo_servico = int(temps_input)
                if tempo_servico <= 0:
                    print("Tempo inválido! Deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("Digite um número inteiro válido.")

        # Validação de Salário
        while True:
            salario_input = input("Digite seu salário bruto: R$ ")
            try:
                salario = float(salario_input)
                if salario <= 0:
                    print("Salário inválido! Deve ser maior que zero.")
                else:
                    break
            except ValueError:
                print("Digite um valor financeiro real.")

        # Alocação estruturada na tabela hash (Dicionário)
        dicionario_funcionarios[matricula] = (nome, sexo, departamento, tempo_servico, salario)

    # Exibição do relatório geral
    print("\n--- Funcionários Cadastrados ---")
    if not dicionario_funcionarios:
        print("Nenhum registro encontrado.")
    else:
        for m, d in sorted(dicionario_funcionarios.items()):
            print(f"Matrícula: {m} | Nome: {d[0]} | Gênero: {d[1].upper()} | Setor: {d[2]} | Tempo: {d[3]} anos | Salário: R$ {d[4]:.2f}")

def buscar_por_tempo_servico():
    if not dicionario_funcionarios:
        return
        
    while True:
        filtro = input("\nDeseja filtrar buscas por 'tempo de serviço'? (sim/sair): ").lower()
        if filtro != "sim":
            break
            
        try:
            min_tempo = int(input("Exibir funcionários com tempo de serviço acima de (anos): "))
            print(f"\n--- Resultados (Tempo de Serviço > {min_tempo} anos) ---")
            encontrado = False
            
            for m, dados in dicionario_funcionarios.items():
                if dados[3] > min_tempo:
                    print(f"Matrícula: {m} | Nome: {dados[0]} | Setor: {dados[2]} | Tempo: {dados[3]} anos")
                    encontrado = True
            if not encontrado:
                print("Nenhum funcionário cumpre este requisito.")
        except ValueError:
            print("Digite um número inteiro válido.")

obter_dados_funcionario()
buscar_por_tempo_servico()