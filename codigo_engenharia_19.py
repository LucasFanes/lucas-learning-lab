Nome = input("Digite o sobrenome do apresentador: ").lower()

if Nome in ["pinheiro", "araújo"]:
    print("O Nome do programa de televisão é Bom dia Nação")
elif Nome in ["bonner", "vasconcelos"]:
    print("O nome do programa é Jornal Brasileiro")
else:
    print("Apresentador(a) desconhecido(a).")