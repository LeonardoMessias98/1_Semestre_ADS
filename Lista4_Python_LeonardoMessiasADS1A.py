#Exercicio 1
from random import randint
vet = []
for i in range(10):
    n1 = randint(1,100)
    vet.append(n1)
maior = vet[0]
menor = vet[0]
for c in range(10):
    if maior < vet[c]:
        maior = vet[c]
    if menor > vet[c]:
        menor = vet[c]
print(f'Da lista {vet}')
print(f'O maior mumero é {maior} e o menor é {menor}\n')

#Exercicio 2

from random import randint
par = []
impar = []
vet = []
for i in range(20):
    n1 = randint(1,100)
    vet.append(n1)
for c in range(20):
    if vet[c] % 2 == 0:
        par.append(vet[c])
    else:
        impar.append(vet[c])
print(f'Da lista {vet} \nSão pares {par} \nSão impares {impar}\n')

#Exercicio 3

from random import randint
vet = []
vet2 = []
vet3 = []
for i in range(10):
    n1 = randint(1,100)
    n2 = randint(1,100)
    vet.append(n1)
    vet2.append(n2)
    vet3.append(vet[i])
    vet3.append(vet2[i])
print(f'Lista 1 {vet} \nLista 2 {vet2} \nLista 3 {vet3}\n')

#Exercicio 4

vet = []
x = ('The Python Software Foundation and the global Python '
            'community welcome and encourage participation by everyone. Our community is based on'
            'mutual respect, tolerance, and encouragement, and we are working to help each other live up '
            'to these principles. We want our community to be more diverse: whoever you are, and '
            'whatever your background, we welcome you.')
x = x.lower()
x = x.replace('.',' ').replace(',',' ').replace("'",' ')
vet = x.split()
lis = []
for i in vet:
    if i[0] in 'python' or i[-1] in 'python':
        lis.append(i)
print(f'Palavras que contem letras que começam ou terminam em PYTHON\n{lis}')

#Exercicio 5

vet = []
x = ('The Python Software Foundation and the global Python '
            'community welcome and encourage participation by everyone. Our community is based on'
            'mutual respect, tolerance, and encouragement, and we are working to help each other live up '
            'to these principles. We want our community to be more diverse: whoever you are, and '
            'whatever your background, we welcome you.')
x = x.lower()
x = x.replace('.',' ').replace(',',' ').replace("'",' ')
vet = x.split()
lista = []
for i in vet:
    if len(i)> 4 and (i[0] in 'python' or i[-1] in 'python'):
        lista.append(i)
print(f'\n{len(lista)} São Maiores que 4 e começam ou terminam com alguma letra de PYTHON')
print(lista)