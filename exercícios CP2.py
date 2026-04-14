# Arthur Caram Fiorese Herrada Rm 569578
# Gustavo Ferreira Silva RM 571675
# Felipi Bandeira de Godoy RM 573741

# EX1 - jeito 1

# numero = 1
# while numero <= 20:
#     print(numero)
#     numero = numero + 1

# EX1 - jeito 2
#
# numero = 20
# while numero >= 1:
#     print(numero)
#     numero = numero - 1


# EX2 - jeito 1

# contagem = 1
# while contagem <= 10:
#         num = int(input("Digite um número: "))
#         contagem = contagem + 1
#         dobro = num * 2
#         print(f"O dobro do número é {dobro}")

# EX2 - jeito 2

# contagem = 1
# while contagem <= 10:
#         num = int(input("Digite um número: "))
#         contagem = contagem + 1
#         divisao = num / 2
#         print(f"A divisão do número por 2 é {divisao:.2f}")


# EX3 - jeito 1

# menor = 0
# contagem = 1
# while contagem <= 15:
#         idade = int(input("Digite sua idade: "))
#         contagem = contagem + 1
#         if idade < 18:
#             menor = menor + 1
# print(f"Contagem de menores de idade: {menor}")

# EX3 - jeito 2

# menor = 0
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
# idade = int(input("Digite sua idade: "))
# if idade < 18:
#     menor += 1
#
#
# print(f"Contagem de menores de idade: {menor}")


# EX4 - jeito 1

# numero_entre = 0
# contagem = 1
# while contagem <= 10:
#     numero = int(input("Digite um número: "))
#     contagem = contagem + 1
#     if numero > 100 and numero < 200:
#         numero_entre = numero_entre + 1
# print(f"A quantidade de números que estão entre 100 e 200 é: {numero_entre}")

# EX4 - jeito 2

# numero_entre = 0
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# numero = int(input("Digite um número: "))
# if 100 <= numero <= 200:
#     numero_entre += 1
#
# print(f"A quantidade de números que estão entre 100 e 200 é: {numero_entre}")


# EX5

# impar = 0
# contagem = 1
# while contagem <= 15:
#     soma = int(input("Digite um número: "))
#     contagem = contagem + 1
#     if soma % 2 != 0:
#         impar = impar + soma
# print(f"A soma dos números ímpares equivale a: {impar}")

# EX6

# soma = 0
# while True:
#     num = int(input("Digite um número: "))
#     if num == 0:
#         break
#     else:
#         soma = soma + num
# print(f"A soma dos números digitados foi: {soma}")

# EX7
#
# while True:
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite um número: "))
#     if num1 == num2:
#         print("Escolha números diferentes.")
#     else:
#         if num1 > num2:
#             print(num1 - num2)
#         else:
#             print(num2 - num1)

# EX8
# menor = None
# contagem = 0
#
# while contagem < 10:
#     numero = int(input("Digite um número: "))
#
#     if menor is None or numero < menor:
#         menor = numero
#
#     contagem += 1
#
# print(f"O menor número digitado é: {menor}")
