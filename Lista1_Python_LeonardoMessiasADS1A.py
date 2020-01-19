#Exercicio 1
print('Bem vindo ao caculador que calcula somente uma operação')
n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o Segundo numero '))
n3 = n1+n2
print(f' A some entre {n1} e {n2} é {n3}')

#Exercicio 2
print(' Bem Vindo ao Conversor de Metros para Milimetros')
metros = float(input('Digite o numero de metros que deseja converter : '))
mili = metros *1000
print(f'{metros} metros convertidos para milimetros equivale a {mili} milimetros ')

#Exercicio 3

print('Bem vindo ao calculador de Segundos')

dias = int(input('Informe Dias '))
horas = int(input('Informe horas '))
minutos = int(input('Informe Minutos '))
seg = int(input('Informe Segundos '))

dseg = dias * 86400
hseg = horas * 3600
mseg = minutos * 60

total = dseg + hseg + mseg + seg

print(f'O Total de segundos foi {total}')

#Exercicio 4

sal = int(input('Digite o Salario'))
aum = int(input('Digite a Porcentagem do Aumento'))
aut = sal * aum / 100
nsal = sal + aut
print(f'O Novo Salario Sera de {nsal} Reais, com um aumento de {aut} Reais')

#Exercicio 5

pat = int(input('Digite o Preço Atual do produto : '))
desc = int(input('Digite a porcentagem do desconto : '))
rdesc = pat * desc / 100
pnov = pat - rdesc
print(f'O novo preço do produto sera de {pnov} Reais, com um desconto de {rdesc}Reais')

#Exercicio 6

dis = int(input('Informe a Distancia em Km : ' ))
vmed = int(input('Informe a Velocidade Media em Km/h : '))
tempo = dis/vmed
print(f'A Duração da Viagem em {dis}Km numa Velcidade Média de {vmed}Km/h sera de {tempo}Horas ')

#Exercicio 7

cel = float(input('Bora Calcular Celsius para Fahrenheit '))
fah = ((cel*9)/5)+32
print(f'{int(cel)} Graus Celsius é equivalente a {int(fah)} Graus Fahrenheit')

#Exercicio 8

fah = float(input('Bora Calcular Fahrenheit para Celsius '))
cel = ((fah-32)*5)/9
print(f'{int(fah)} Graus Fahrenheit é equivalente a {int(cel)} Graus Celsius')

#Exercicio 9

print('Bem vindo a Rentcars Python')
km = int(input('Informe quantos KM você rodou com o carro: '))
dias = int(input('Informe por quantos dias você utilizou o carro: '))
vkm = km * 0.15
vdias = dias * 60
vtotal = vdias + vkm
print(f'O Valor a ser pago é de {vtotal} Reais, Obrigado pela Preferência ')

#Exercicio 10

print('Bem vindo ao Python Health')
cdias = int(input('Informe a média de cigarros fumados por dia: '))
anos = int(input('Informe quantos anos você fuma cigarro: '))
adias = anos * 365
totalh= int((cdias * 10) / 60)
totalmin = (cdias * 10) % 60
hreais = (totalh) + (0.01 * totalmin)
totald = (hreais / 24) * adias
print (f'Com base em suas resposta, você perdeu cerca de {totald:.2f} dias ao fumar {cdias} cigarros por dias em {anos} anos')

#Exercicio 11

ler=str(2**1000000)
print(f'2 elevado a 1.000.000 tem {len(ler)} digitos')
