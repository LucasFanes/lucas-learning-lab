nome = input("Digite seu nome: ")
quantidade = int(input("Digite a quantidade de imóveis vendidos: "))
valor_vendas = float(input("Digite o valor total de suas vendas: "))
x2 = quantidade * 200
salario = (valor_vendas * 0.05) + 1500 + x2
print(f"Seu salário final é de: R$ {salario:.2f}")