#Exercicio 1
print('Para saber o lados de um triangulo digite o abaixo os 3 lados')
l1= int(input('Digite o Tamanho do lado 1: '))
l2= int(input('Digite o Tamanho do lado 2: '))
l3= int(input('Digite o Tamanho do lado 3: '))
if l1 == l2 == l3:
    print('O Triangulo é Equilatero')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('O Triagulo é Isosceles')
else:
    print('O Triangulo é Escaleno')

#Exercicio 2
ano=int(input('Digite o ano que deseja analisar: '))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print(f'O ano {ano} é Bissexto ')
else:
    print(f'O ano {ano} não é Bissexto ')

#Exercicio 3
print('=-'*24)
print('Bem Vindo ORDPP (ORGÃO REGULADOR DE PEIXES PESCADOS)')
print('=-'*24)
pkg = int(input('Kilos de Peixes Pescados : '))
if pkg > 50:
    kgx = pkg - 50
    print(f'Kilos Pescado: {pkg} Kg')
    print(f'Kilos Excedentes: {kgx} Kg')
    print(f'Valor da Multa {kgx*4} Reais')
else:
    kgx = 0
    print(f'Kilos Pescado: {pkg} Kg')
    print(f'Kilos Excedentes: {kgx} Kg')
    print(f'Valor da Multa {kgx*4} Reais')

#Exercicio 4
print('Informe os 3 numeros abaixos para saber qual deles é o maior ')
n1 = int(input('Digite o 1 Numero: '))
n2 = int(input('Digite o 2 Numero: '))
n3 = int(input('Digite o 3 Numero: '))
if n1 > n2 and n1 > n3:
    print(f'O Numero {n1} é o MAIOR Numero')
elif n2 > n1 and n2 > n3:
    print(f'O Numero {n2} é o MAIOR Numero')
elif n3 > n2 and n3 > n1:
    print(f'O Numero {n3} é o MAIOR Numero')

#Exercicio 5
print('Informe os 3 numeros abaixos para saber qual deles é o maior e o menor ')
n1 = int(input('Digite o 1 Numero: '))
n2 = int(input('Digite o 2 Numero: '))
n3 = int(input('Digite o 3 Numero: '))
if n1 > n2 and n1 > n3:
    print(f'O Numero {n1} é o MAIOR Numero')
    if n2 < n1 and n2 < n3:
        print(f'E {n2} é o menor Numero')
    elif n3 < n1 and n3 < n2:
        print(f'E {n3} é o menor numero')
elif n2 > n1 and n2 > n3:
    print(f'O Numero {n2} é o MAIOR Numero')
    if n1 < n2 and n1 < n3:
        print(f'E {n2} é o menor Numero')
    elif n3 < n1 and n3 < n2:
        print(f'E {n3} é o menor numero')
elif n3 > n2 and n3 > n1:
    print(f'O Numero {n3} é o MAIOR Numero')
    if n2 < n1 and n2 < n3:
        print(f'E {n2} é o menor Numero')
    elif n1 < n3 and n1 < n2:
        print(f'E {n1} é o menor numero')

#Exercicio 6
hsal = int(input('Informe Quanto ganha por hora: '))
htrab = int(input('Informe Quantos horas trabalha por dia: '))
sal = htrab * hsal
ir = 11*sal/100
inss = 8*sal/100
sind = 5*sal/100
totalimp= ir + inss + sind
sliquid = sal - totalimp
print(f'Salario Bruto: R${sal}')
print(f'IR(11%): R${ir}')
print(f'INSS(8%): R${inss}')
print(f'Sindicato(5%): R${sind}')
print(f'Salario Liquido: R${sliquid}')

#Exercicio 7
metros = int(input('Quantos Metros² ira ser pintado ?: '))
litros = metros /3
lata = int(litros / 18)
sobra = litros % 18
add=0
if sobra > 0:
    add += 1
tlatas = lata+add
print(f'Para Pintar {metros} Metros² Você Deverá comprar {tlatas} Latas, que tera um valor total de {tlatas*80} Reais')