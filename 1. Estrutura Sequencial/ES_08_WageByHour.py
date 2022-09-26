# Faça um programa que pergunte quanto você recebe de salário por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês.


if __name__ == "__main__":
    employee_name = str(input("Nome do funcionário: "))
    hourly_salary = float(input("Salário recebido por hora: "))
    worked_hour = int(input("Horas trabalhadas: "))
    worked_days = int(input("Quantidade de dias trabalhados: "))

    monthly_wage = hourly_salary * worked_hour * worked_days
    
    print("\n                                           ")
    print("                 PAY STUB                    ")
    print(" =========================================== ")
    print(f" Employee Name:\t\t{employee_name}"            )
    print(f" Hourly received:\t$ {hourly_salary}"       )
    print(f" Worked hour:\t\t{worked_hour}h"            )
    print(f" Worked days:\t\t{worked_days}d"            )
    print(" =========================================== ")
    print(f" NET Amount:\t\t$ {monthly_wage}          ")
    print("\n                                           ")


