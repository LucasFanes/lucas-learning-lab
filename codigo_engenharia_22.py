preco = float(input("Digite o preço do produto: "))
formadepag = input("Digite a forma de pagamento (a vista / cartao de debito / cartao de credito): ").lower()

precpag = 1.0
if formadepag == "a vista":
    precpag = 0.85
elif formadepag == "cartao de debito":
    precpag = 0.9
elif formadepag == "cartao de credito":
    precpag = 0.95
else:
    print("Forma de pagamento não válida")

precototal = preco * precpag
print(f"O preço total é R$ {precototal:.2f}")