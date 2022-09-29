# Faça um programa que peça a temperatura em graus Celsius
# transforme e mostre em graus Fahrenheit
# 32 + (F * (9 / 5)


def conv(v_cels):
    return 32 + (v_cels * (9 / 5))


if __name__ == "__main__":
    cels = float(input("informe o valor em ºC para conversão: "))
    convertion = float(conv(cels))

    print(f">> {cels:.2f} ºC --> {convertion:.2f} ºF.")
