a = int(input("Ano: "))
m = int(input("Mês: "))
d = int(input("Dia: "))

af = int(input("Ano f: "))
mf = int(input("Mês f: "))
df = int(input("Dia f: "))

ad = af - a
md = mf - m
dd = df - d

dias = (365 * ad) + (30 * md) + (1 * dd)

print(dias)
