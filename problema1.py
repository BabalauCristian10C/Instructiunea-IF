
n_e_1 = int(input("Introduceti numarul curent al elevului:"))
print("punctajul elevului", n_e_1, ":", end="")
pnct_1 = int(input())
n_e_2 = int(input("Introduceti numarul curent al elevului:"))
print("punctajul elevului", n_e_2, ":", end="")
pnct_2 = int(input())
n_e_3 = int(input("introduceti elevul cu numarul :"))
print("punctajul elevului ", n_e_3, ":", end=" ")
pnct_3 = int(input())


list = [pnct_1, pnct_2,pnct_3 ]
max_pnct = max(list)


if max_pnct == pnct_1:
    print(f'evelul {n_e_1} are cele mai multe puncte {pnct_1}')
elif max_pnct == pnct_2:
    print(f'evelul {n_e_2} are cele mai multe puncte {pnct_2}')
else:
    print(f'evelul {n_e_3} are cele mai multe puncte {pnct_3}')