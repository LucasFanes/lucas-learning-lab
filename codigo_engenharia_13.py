Numero1 = int(input("Digite um número inteiro positivo: "))
if Numero1 > 0:
    if Numero1 % 2 == 0:
        print(f"O quadrado de {Numero1} é {Numero1**2}")
    else:
        print(f"O cubo de {Numero1} é {Numero1**3}")
else:
    print("Por favor, digite um número maior que zero.")