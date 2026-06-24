usuario = input("Digite seu usuário: ")
cargo = input("Digite seu cargo (Analista de Sistemas/Programador de Sistemas/Analista de Banco de Dados): ").lower()
salario = float(input("Digite seu salário: "))

aumentosalario = 1.0

if cargo == "programador de sistemas":
    aumentosalario = 1.3
elif cargo == "analista de sistemas":
    aumentosalario = 1.2
elif cargo == "analista de banco de dados":
    aumentosalario = 1.15
else:
    print("Cargo não encontrado. O salário será mantido sem alteração.")

salarioap = salario * aumentosalario
print(f"Seu salário final é: R$ {salarioap:.2f}")