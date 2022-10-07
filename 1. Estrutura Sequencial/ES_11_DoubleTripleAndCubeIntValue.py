# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   - o produto do dobro do primeiro com metade do segundo
#   - a soma do triplo do primeiro com o terceiro
#   - o terceiro elevado ao cubo

def getProductDoubleWithinHalfOfSecond(first, second):
    return float((2 * first) + (second / 2))

def getSumOfTripleOfFirstWithinThird(first, third):
    return float((3 * first) + third)

def getThirdToCube(third):
    return float(third ** 3)

if __name__ == "__main__":
    print("Informe três números:")

    n1 = int(input("número 1: "))
    n2 = int(input("número 2: "))
    n3 = int(input("número 3: "))

    c1 = getProductDoubleWithinHalfOfSecond(n1, n2)
    c2 = getSumOfTripleOfFirstWithinThird(n1, n3)
    c3 = getThirdToCube(n3)

    print("\n")
    print("Núm 1:", str(n1), "| Núm 2:", str(n2), "| Núm 3:", str(n3))
    print("O produto do dobro do primeiro com metade do segundo:", c1)
    print("A soma do triplo do primeiro com o terceiro:", c2)
    print("O Terceiro elevado ao cubo:", c3)


