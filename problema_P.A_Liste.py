prenume = ['Mihai','George', 'Ana','Dan', 'Geta','Vio']
varsta = [14,23,15,14,12,41,39]
x=0
i=0
n =list(zip(prenume, varsta))
n.append(tuple(('Andreea', 34)))
n.append(tuple(('Ioan', 23)))
for i,names in enumerate(n):
    if names == ('Ana', 15):
        n.pop(i)

for a in n:
    b = a[0]
    print(b[0:3], end = ', ')

print('''

===================
''')

for a in n[::-1]:
    print(a[0], end = ', ')

print('''

===================
''')

x = 0

for a in n:
    x+=1
    if x == 2 or x == 3:
        for text in a:
            print(text, end = ' ')

print('''

===================
''')
x = 0
for a in n:
    if x < 5:
        print(a[0], a[1], sep = ' , ', end = ' . ')
        x+=1
