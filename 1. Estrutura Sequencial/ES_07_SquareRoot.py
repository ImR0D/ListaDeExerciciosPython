# Faça um programa que calcule a área de um quadrado, em seguida mostre
# o dobro dessa área para o usuário


# Objetivo do algoritmo é obter a raíz quadrada sem o uso da função sqrt da lib 'math'
def isSqrt(sqrt, match):
    m = match ** 2
    if m <= sqrt:
        return True
    else:
        return False


def getSquareRoot(n):
    x = n/2
    while (x > 0):
        x = x / 2.0
        if not isSqrt(n, x):
            getSquareRoot(x)
        else:
            return x



print("Teste 1 - sqrt -> 8:    ", getSquareRoot(8))
print("Teste 2 - sqrt -> 28:   ", getSquareRoot(28))
print("Teste 3 - sqrt -> 1024: ", getSquareRoot(1024))
print("Teste 4 - sqrt -> 9765: ", getSquareRoot(9765))
print("Teste 5 - sqrt -> 1000: ", getSquareRoot(1000))
