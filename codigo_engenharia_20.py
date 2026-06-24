Estatura1 = float(input("Digite a primeira estatura: "))
Estatura2 = float(input("Digite a segunda estatura: "))
Estatura3 = float(input("Digite a terceira estatura: "))

if Estatura1 == Estatura2 or Estatura1 == Estatura3 or Estatura2 == Estatura3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")
else:
    maior = max(Estatura1, Estatura2, Estatura3)
    print(f"A maior estatura é {maior:.2f}")