print("Calculadora de Bhaskara Python")
a = float(input("Digite seu A: "))
b = float(input("Digite seu B: "))
c = float(input("Digite seu C: "))
Delta = b**2-4*a*c
raizx1 = (-b+Delta**0.5)/(2*a)
raizx2 = (-b-Delta**0.5)/(2*a)
if Delta < 0:
    print("Não há raízes reais")
print("suas raízes são: X1", raizx1,"X2",raizx2)