#Exercicio 1
nota = 11
while nota < 0 or nota > 10:
    nota = int(input('Digite uma nota entra 0 - 10: '))

#Exercicio 2
print('Abaixo Crie Seu Login e Senha')
login = str(input('Crie Seu Login: '))
senha = str(input('Crie Sua Senha: '))
while login.lower() == senha.lower():
    print('=-'*24)
    print('ERROR - SENHA NÃO PODE SER IGUAL AO LOGIN')
    print('=-'*24)
    login = str(input('Crie Seu Login: '))
    senha = str(input('Crie Sua Senha: '))
print('CADASTRO CONCLUIDO COM SUCESSO')

#Exercicio 3
paisA = 80000
paisB = 200000
count = 0
print(f'Pais A = {paisA} Ano Inicial')
print(f'Pais B = {paisB} Ano Inicial')
while paisA < paisB:
    count += 1
    paisA = (paisA*3/100) + paisA
    paisB = (paisB*1.5/100) + paisB
    print(f'Pais A = {paisA:.2f} Ano {count}')
    print(f'Pais B = {paisB:.2f} Ano {count}')
    print('-'*12)
print(f'No Ano {count} o Pais A Sera Maior do que o Pais B, tendo {paisA:.2f} Habitantes e Pais B {paisB:.2f} Habitantes \nPais A Tendo um crescimento de 3% por ano e Pais B 1.5% ao Ano')

#Exercicio 4
print('Sequencia de Fibonacci')
a = int(input('Digite um numero para saber sua Sequencia Fibonacci: '))
n1 = a
n2 = a
count = 0
while True:
    count += 2
    print(n1)
    print(n2)
    n1 = n1 + n2
    n2 = n2 + n1
    if count > 8:
        break

#Exercicio 5
print('Para Descobrir o MDC entre 2 Numeros os digite abaixo ')
n1 = int(input('Digite o Primeiro Numero: '))
n2 = int(input('Digite o Segundo Numero: '))

while n1 != n2:
    if n1 > n2:
        n1 = n1 - n2
    elif n1 < n2:
        n2 = n2 - n1

print(f'o MDC é de {n1}')
