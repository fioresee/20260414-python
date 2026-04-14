# Arthur Caram Fiorese Herrada RM 569578
# Gustavo Ferreira Silva RM 571675
# Felipi Bandeira de Godoy RM 573741

print("EX1 - jeito 1")

numero = 1
while numero <= 20:
    print(numero)
    numero = numero + 1

print("EX1 - jeito 2")

numero = 20
while numero >= 1:
    print(numero)
    numero = numero - 1


print("EX2 - jeito 1")

contagem = 1
while contagem <= 10:
        num = int(input("Digite um número: "))
        contagem = contagem + 1
        dobro = num * 2
        print(f"O dobro do número é {dobro}")

print("EX2 - jeito 2")

contagem = 1
while contagem <= 10:
        num = int(input("Digite um número: "))
        contagem = contagem + 1
        divisao = num / 2
        print(f"A divisão do número por 2 é {divisao:.2f}")


print("EX3 - jeito 1")

menor = 0
contagem = 1
while contagem <= 15:
        idade = int(input("Digite sua idade: "))
        contagem = contagem + 1
        if idade < 18:
            menor = menor + 1
print(f"Contagem de menores de idade: {menor}")

print("EX3 - jeito 2")

menor = 0

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1

idade = int(input("Digite sua idade: "))
if idade < 18:
    menor += 1


print(f"Contagem de menores de idade: {menor}")


print("EX4 - jeito 1")

numero_entre = 0
contagem = 1
while contagem <= 10:
    numero = int(input("Digite um número: "))
    contagem = contagem + 1
    if numero > 100 and numero < 200:
        numero_entre = numero_entre + 1
print(f"A quantidade de números que estão entre 100 e 200 é: {numero_entre}")

print("EX4 - jeito 2")

numero_entre = 0

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

numero = int(input("Digite um número: "))
if 100 <= numero <= 200:
    numero_entre += 1

print(f"A quantidade de números que estão entre 100 e 200 é: {numero_entre}")


print("EX5")

impar = 0
contagem = 1
while contagem <= 15:
    soma = int(input("Digite um número: "))
    contagem = contagem + 1
    if soma % 2 != 0:
        impar = impar + soma
print(f"A soma dos números ímpares equivale a: {impar}")

print("EX6")

soma = 0
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    else:
        soma = soma + num
print(f"A soma dos números digitados foi: {soma}")

print("EX7")

while True:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    if num1 == num2:
        print("Escolha números diferentes.")
    else:
        if num1 > num2:
            print(f"A diferença entre os dois números é de: {num1 - num2}")
        else:
            print(f"A diferença entre os dois números é de: {num2 - num1}")
        break

print("EX8")

menor = None
contagem = 0

while contagem < 10:
    numero = int(input("Digite um número: "))
    if menor is None or numero < menor:
        menor = numero
    contagem += 1

print(f"O menor número digitado foi: {menor}")

print("EX9")

par = 0
impar = 0
soma_par = 0
soma_impar = 0
contagem = 0

n = int(input("Digite a quantidade de números: "))
print(f"Digite {n} números inteiros")
while contagem < n:
    num = int(input("Escreva aqui: "))
    contagem = contagem + 1
    if num % 2 == 0:
        par = par + 1
        soma_par += num
    elif num % 2 != 0:
        impar = impar + 1
        soma_impar += num

if par > 0:
    media_par = soma_par / par
    print(f"Média dos pares: {media_par}")
else:
    print("Não há números pares para calcular a média.")

if impar > 0:
    media_impar = soma_impar / impar
    print(f"Média dos ímpares: {media_impar}")
else:
    print("Não há números ímpares para calcular a média.")

print("EX10")

chico = 1.50
crescimento_chico = 0.02
juca = 1.10
crescimento_juca = 0.05
anos = 0
fchico = "1.50 + 0.02x"
fjuca = "1.10 + 0.05x"

print(f"A função que calcula a quantidade de anos que seriam necessários")
print(f"para Juca ser mais alto do que Chico é: {fchico} = {fjuca}")

while juca <= chico:
    chico += crescimento_chico
    juca += crescimento_juca
    anos += 1
print(f"Anos necessários: {anos}")

print("EX11")

s = 0
i = 1
n = int(input("Digite um número: "))
while i <= n:
    s = s + 1 / i
    i = i + 1
print(f"O valor da soma S = 1/1 + 1/2 + 1/3 ... 1/n equivale a: {s}")

print("EX12")

fatorial = 1
i = 1
num = int(input("Digite um número para calcular o fatorial dele: "))
while i <= num:
    fatorial *= i
    i += 1
print(f"O fatorial de {num} é {fatorial}")