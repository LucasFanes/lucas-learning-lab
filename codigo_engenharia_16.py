idade = int(input("Digite sua idade: "))
pcd = input("Você é PCD? (sim/não): ").lower()
if idade >= 65 or pcd == "sim":
    print("Você tem direito a atendimento preferencial")
else:
    print("Você não tem direito ao atendimento preferencial")