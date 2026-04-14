# titulo = "Estrutura de Repetição While"
# print(f"{titulo:^30}")
#
# # Se fosse necessário calcular a tabuada do 3, teriamos que fazer a mesma operação 10 vezes.
#
numero = 3
print(f"{numero} X 1 = {numero}")
print(f"{numero} X 2 = {numero * 2}")
print(f"{numero} X 3 = {numero * 3}")
#
# #while -> enquanto
# # A repetição está estruturada enquanto a
# # comparação for verdadeira.
# # While é muito parecido com o If,
# # mas funciona somente do lado verdadeiro.
#
# # Para o cálculo da tabuada, precisa repetir a mesma operação 10X
# numero = int(input("Digite um número para a tabuada: "))

numero = int(input("Digite um número para a tabuada: "))

while True:
    i = 1

    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")

        # só pergunta se NÃO for a última linha
        if i < 10:
            desejo = input("Deseja continuar? (S/N): ").lower()

            if desejo == "n":
                print("Fim dos cálculos!")
                break
            elif desejo != "s":
                print("Opção inválida!")
                break

        i += 1

    # se saiu antes de terminar a tabuada
    if i <= 10:
        break

    prox = input("Deseja calcular a tabuada do próximo número? (S/N): ").lower()

    if prox == "s":
        numero += 1
    elif prox == "n":
        print("Fim dos cálculos!")
        break
    else:
        print("Opção inválida!")
        break
