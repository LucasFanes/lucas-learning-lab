medicamentos = []
preco_total = 0
mais_barato_nome = ""
mais_barato_preco = float('inf')

for i in range(5):
    print(f"\nInformações para o medicamento {i+1}:")
    nome = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o preço do medicamento: "))
    
    preco_total += preco
    if preco < mais_barato_preco:
        mais_barato_preco = preco
        mais_barato_nome = nome

media_precos = preco_total / 5
print(f"\nO medicamento mais barato é: {mais_barato_nome} custando R$ {mais_barato_preco:.2f}")
print(f"A média dos preços é: R$ {media_precos:.2f}")