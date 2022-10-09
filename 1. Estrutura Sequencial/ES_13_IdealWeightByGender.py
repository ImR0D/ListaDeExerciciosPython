#13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
#	· Para homens: (72.7*h) - 58
#	· Para mulheres: (62.1*h) - 44.7


def ideal_weight(height, gender):
    if gender.startswith("m"):
        return (72.7 * height) - 58
    elif gender.startswith("f"):
        return (62.1 * height) - 44.7

    return 0


if __name__ == "__main__":
    print(":::: Ideal Weight ::::")
    get_height = float(input("Enter your height: "))
    gender = str(input("Enter your gender (M - Male, F - Female): ")).lower()
    iw = ideal_weight(get_height, gender)
    print(f"You must got {iw:.2f}kg or {iw*2.20462:.2f}lb to get ideal weight")

