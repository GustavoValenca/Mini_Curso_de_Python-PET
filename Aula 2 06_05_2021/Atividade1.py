coefA = int(input("Coeficiente A: "))
coefB = int(input("Coeficiente B: "))
coefC = int(input("Coeficinete C: "))

delta = (coefB ** 2) - (4 * coefA * coefC)

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    r = (- coefB + (delta ** 0.5)) / (2 * coefA)
    print("A equação possui 1 raiz real: {}"
          .format(r))
else:
    r = (- coefB + (delta ** 0.5)) / (2 * coefA)
    r2 = (- coefB - (delta ** 0.5)) / (2 * coefA)
    print("A equação possui 2 raízes reais: {} e {}"
          .format(r, r2))
