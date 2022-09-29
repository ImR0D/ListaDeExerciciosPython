# Faça um programa que peça a temperatura em graus Fahrenheit
# transforme e mostre a temperatura em graus Celsius.
# Conversão C = 5 * (F-32) / 9)

def conv(v_fahr):
    return float(5 * ((v_fahr-32) / 9))

if __name__ == "__main__":
    fahr = float(input("informe o valor em ºF para conversão: "))
    convertion = float(conv(fahr))

    print(f">> {fahr:.2f} ºF --> {convertion:.2f} ºC.")

