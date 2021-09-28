# Másodfokú képlet megoldása - 0928
import math

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

if(a == 0 or b == 0 or c == 0):
    print("Az egyenlet megoldásához nem használható a megoldóképlet.")
else:
    d = math.pow(b, 2) + 4 * a * c
    if(d < 0):
        print("A diszkrimináns értéke nem található meg a valós számok halmazán.")
    elif d == 0:
        print(f"x = {- b / (2 * a)}")
    else:
        print(f"x1 = {(- b + math.sqrt(d)) / (2 * a)}")
        print(f"x2 = {(- b - math.sqrt(d)) / (2 * a)}")

print("kész vége cső")
