#Exercicio 1
print('Digite um Numero abaixo para saber se é triangular')
n = int(input('Digite 1 numero: '))

i = 1
while i * (i + 1) * (i + 2) < n:
    i += 1

if i * (i + 1) * (i + 2) == n:
    print(f'{n} é o produto {i} * {i+1} * {i+2}')
else:
    print(f' {n} não é triangular')

#Exericio 2
pag = 1
dep = 0
while pag > dep:
    pag = int(input('Informe o Valor a ser pago: '))
    dep = int(input('Informe o Valor depositado: '))
troco = dep - pag

n50 = int(troco / 50)
s50 = troco % 50
n20 = int(s50 / 20)
s20 = s50 % 20
n10 = int(s20 / 10)
s10 = s20 % 10
n5 = int(s10/5)
s5 = s10 % 5
n2 = int(s5/2)
s2 = s5 % 2
n1 = int(s2/1)

print(f'{n50} Notas de 50 Reais, \n{n20} Notas de 20 Reais, \n{n10} Notas de 10 Reais, \n{n5} Notas de 5 Reais,'
      f' \n{n2} Notas de 2 Reais, \n{n1} Notas de 1 Real')

#Exercicio 3
n1 = int(input('Para Saber se um numero é primo ou não, informe ele: '))
count = 0
c=0
for i in range(0,n1+1):
    c += 1
    if n1 % c == 0:
        count += 1
if count == 2:
    print(f'O Número {n1} é primo')
else:
    print(f'O Número {n1} não é primo')

#Exercicio 4

n = int(input('Escolha um número para saber seus divisores primos: '))

divisores = []
d = 2
while n > 1:
    if n%d == 0:
        n = n/d
        divisores.append(d)
    else:
        d += 1
print (f'Estes são os divisores {divisores}')

#Exercicio 5
numero = str(input('Insira um numero: '))
print(''.join(reversed(numero)))