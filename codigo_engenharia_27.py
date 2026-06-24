atletaentre1215 = []
melhoratleta, pioratleta = "", ""
melhortempo, piortempo = float('inf'), float('-inf')
tempototal = 0

for i in range(5):
    print(f"\nInformações para o atleta {i+1}:")
    nome = input("Digite o nome do atleta: ")
    tempo = float(input("Digite o tempo do atleta (s): "))

    tempototal += tempo
    if 12 <= tempo <= 15:
        atletaentre1215.append(nome)
    if tempo < melhortempo:
        melhortempo = tempo
        melhoratleta = nome
    if tempo > piortempo:
        piortempo = tempo
        pioratleta = nome

velocidademedia = 125 / tempototal
print(f"\nMelhor atleta: {melhoratleta} ({melhortempo}s)")
print(f"Pior atleta: {pioratleta} ({piortempo}s)")
print(f"Velocidade média geral: {velocidademedia:.2f} m/s")
print(f"Atletas com tempo entre 12s e 15s: {atletaentre1215}")