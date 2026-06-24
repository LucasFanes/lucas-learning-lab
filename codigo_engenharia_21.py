print("Calculadora de Bhaskara Python")
acoefici = int(input("Digite seu A: "))
bcoefici = int(input("Digite seu B: "))
ccoefici = int(input("Digite seu C: "))

Delta = bcoefici**2 - 4*acoefici*ccoefici

if Delta < 0:
    print("Não há raízes reais")
else:
    raizx1 = (-bcoefici + Delta**0.5) / (2*acoefici)
    raizx2 = (-bcoefici - Delta**0.5) / (2*acoefici)
    print("suas raízes são: X1", raizx1, "X2", raizx2)
    if Delta == 0:
        print("Há uma raiz dupla real")
    else:
        print("Há duas raízes diferentes reais")