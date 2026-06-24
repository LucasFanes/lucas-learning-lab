ntermo = int(input("Coloque a quantidade de termos: "))
ptermo = int(input("Coloque o primeiro termo: "))
razao = int(input("Coloque a razão: "))

for i in range(1, ntermo + 1):
    an = ptermo + (i - 1) * razao
    print(f"Termo {i}: {an}")