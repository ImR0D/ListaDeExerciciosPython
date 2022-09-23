# Faça um programa que peça dois números e imprima a soma

soma = 0
num = [0, 0]

for i in num:
    num[i] = int(input("Informe um valor: "))
    soma = soma + num[i]

print(f"A soma dos números é {soma}")


