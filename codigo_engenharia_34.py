ptermo = float(input("Digite o primeiro termo da P.A: "))
ntermos = int(input("Digite a quantidade de termos da P.A: "))
razao = float(input("Digite a razão da P.A: "))

listapa = [ptermo + i * razao for i in range(ntermos)]
print(f"\nLista gerada: {listapa}")
print(f"Soma de todos os termos da P.A: {sum(listapa)}")
print(f"Menor valor contido na P.A: {min(listapa)}")
print(f"Maior valor contido na P.A: {max(listapa)}")