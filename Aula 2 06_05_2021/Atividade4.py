n = int(input("Digite um número: "))
d = 0

for i in range(1, n + 1):
    if n % i == 0:
        d += 1

if d == 2:
    print("O número {} é primo.".format(n))
else:
    print("O número {} não é primo.".format(n))
