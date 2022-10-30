# Faça um programa para uma loja de tinta. O programa deverá pedir o tamanho
# em metros quadrados da área a ser pintada. Considere que a cobertura da
# tinta é de 1 litro para cada 3 metros quadrados e que a tinha é vendida em
# latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas
# de tinta a serem compradas e o preço total.

import math


def pintarArea(tamanhoArea, coberturaPorLitro, tamanhoLata):
    return int(math.ceil((tamanhoArea / tamanhoLata) / 3))
    

if __name__ == "__main__":
    cobertura = 3
    tamanho_lata = 18
    preco_lata = 80.0
    mq_area = float(input(">> m² que serão pintados: "))
    latas = pintarArea(mq_area, cobertura, tamanho_lata)
    carrinho = float(latas * preco_lata)

    print(f"Cobertura de 1 litro pra cada 3 metros")
    print("Latas de tinta a comprar................: ", latas)
    print("Custo das latas.........................: ", carrinho)



