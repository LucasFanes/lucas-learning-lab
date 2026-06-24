mapa = {1: 'Enfermeiro', 2: 'Nutricionista', 3: 'Médico'}
medicosmaior4500 = 0

while True:
    print("\nCargos:", mapa)
    Cargo = int(input("Digite o código do cargo (ou 0 para sair): "))
    if Cargo <= 0 or Cargo > 3:
        break
        
    Salario = float(input("Digite o salário: "))
    nome_cargo = mapa[Cargo]
    print(f"Registrado: {nome_cargo} - R$ {Salario:.2f}")
    
    if nome_cargo == 'Médico' and Salario > 4500:
        medicosmaior4500 += 1

print(f"\nMédicos com salário acima de R$ 4.500,00: {medicosmaior4500}")