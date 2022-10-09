# Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

import math
import os


def getCircleAreaValue(radius):
    return math.pi * radius ** 2


def getCircleRadiusValue(diameter):
    return diameter / 2


def getCircleDiameterValue(radius):
    return 2 * radius


def getCircleCircumferenceValue(radius):
    return 2 * math.pi * radius


def getCircleArea():
    r = float(input("Informe o raio: "))
    c = getCircleAreaValue(r)
    return c


def getCircleRadius():
    a = float(input("Informe o diâmetro: "))
    r = getCircleRadiusValue(a)
    return r


def getCircleCircumference():
    r = float(input("Informe o raio: "))
    c = getCircleCircumferenceValue(r)
    return c


def getCircleDiameter():
    r = float(input("informe o raio: "))
    d = getCircleDiameterValue(r)
    return d


def clearConsole():
    os.system("clear") or None


def menu():
    option = -1
    a = 0
    r = 0
    while not option == 0:
        # Função clearConsole() funcional apenas via terminal
        clearConsole()
        print(" ====================================================== ")
        print("| 1 - Calcular área           |  3 - Calcular raio     |")
        print("| 2 - Calcular circunferência |  4 - Calcular diâmetro |")
        print("|======================================================|")
        print("| 0 - Sair                                             |")
        print(" ====================================================== ")
        option = int(input("Opção: "))

        if option == 1:
            a = getCircleArea()
            print("Área: ", a)
        elif option == 2:
            c = getCircleCircumference()
            print("Circunferência: ", c)
        elif option == 3:
            r = getCircleRadius()
            print("Raio: ", r)
        elif option == 4:
            d = getCircleDiameter()
            print("Diâmetro: ", d)
        elif option == 0:
            break
        else:
            print("Opção inválida")
        input("\n\nPressione qualquer tecla para prosseguir...")


if __name__ == "__main__":
    menu()


