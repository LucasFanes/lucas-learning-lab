# Módulo de cadastro e consulta de séries/protagonistas
series_dict = {}

# Cadastro inicial fixo
series_dict["Branquinas"] = ["1", "2"]

while True:
    print("\n------ Lista de séries ------")
    for chave, valores in series_dict.items():
        print(f"{chave}: {valores[0]} e {valores[1]}")
        
    print("\nMenu:")
    print("1. Cadastrar nova série")
    print("2. Escolher/Buscar uma série por índice")
    print("3. Sair")
    
    escolha_menu = input("Escolha uma opção (1/2/3): ")
    
    if escolha_menu == "3":
        print("Encerrando programa...")
        break
        
    elif escolha_menu == "1":
        nome_serie = input("Digite o nome da série (ou 'fim' para encerrar): ")
        if nome_serie.lower() == 'fim':
            break
        protagonista1 = input("Digite o primeiro protagonista: ")
        protagonista2 = input("Digite o segundo protagonista: ")
        series_dict[nome_serie] = [protagonista1, protagonist2]
        
    elif escolha_menu == "2":
        deseja_escolher = input("Deseja escolher uma série? (s/n): ").lower()
        if deseja_escolher == "s":
            chaves_lista = list(series_dict.keys())
            print("\nSéries disponíveis:")
            for idx, nome in enumerate(chaves_lista):
                print(f"{idx}: {nome}")
                
            try:
                indice = int(input("Digite o número da série que deseja escolher: "))
                if 0 <= indice < len(chaves_lista):
                    serie_escolhida = chaves_lista[indice]
                    print(f"Você escolheu a série: {serie_escolhida}")
                else:
                    print("Escolha inválida. Por favor, escolha um número válido.")
            except ValueError:
                print("Por favor, digite um número inteiro válido.")