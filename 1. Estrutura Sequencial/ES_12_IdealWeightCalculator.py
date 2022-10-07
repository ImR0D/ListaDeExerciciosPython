# 12) Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: 	· (72.7 * altura) - 58


def ideal_weight(height):
    return float(72.7 * height) - 58


if __name__ == "__main__":
    
    print(":::: Ideal Weight ::::")
    getHeight = float(input("Enter your height: "))
    iw = ideal_weight(getHeight)
    print(f"You must got {iw:.2f}kg or {iw*2.20462:.2f}lb to get ideal weight")


