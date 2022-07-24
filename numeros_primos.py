a = int(input("Te dire si es primo o no. coloca un numero por emcima de 2: "))
b = 2
result = float
v = 0

while b < a :
    result = a % b
    b = b + 1
    if result == 0:
        v = 0
        break
    elif result >= 1:
        v = v + b


if b <= v:
    print("Tu numero es primo!")
elif v == 0:
    print("Tu numero no es primo")