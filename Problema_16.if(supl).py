#calcularea ecuatiilor de gradul2 
import math

print("Forma ecuatiei de gr2 : ax**2 + bx + c")
a = int(input("Introduceti a = "))
b = int(input("Introduceti b = "))
c = int(input("Introduceti c = "))
print(f'Ecutia formata {a}x**2 + ({b}x) + ({c})')
x = "x"

def rez(a,b,c):
    disc = b**2 - 4*a*c
    if disc < 0:
        print(f'Discriminantul este ngativ, ecuatia nu are solutii {disc}')
    elif disc == 0:
        sol_0 = (b**2) / (2 * a)
        print("Unica solutie este", sol_0)
    else:
        sol_1 = int((-1 * b - math.sqrt(disc)) / 2 * a)
        sol_2 = int((-1 * b + math.sqrt(disc)) / 2 * a)
        print(f'Solutiile sunt {sol_1} si {sol_2}')
print(rez(a, b, c))