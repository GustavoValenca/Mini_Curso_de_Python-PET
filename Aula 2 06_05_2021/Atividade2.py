n = 0
while n == 0:
    n = int(input("Digite um número: "))

if n == 1:
    print("1 elefante incomoda muita gente.")
else:
    print("{} elefantes".format(n), end=' ')
    for i in range(0, n):
        print("incomodam", end=' ')
    print("muito mais.")
