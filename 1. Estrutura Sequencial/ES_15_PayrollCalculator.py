# 15) Faça um programa que pergunte quanto você ganha por hora e
# o número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda; 8% para o INSS; e 5% para o sindicato,
# faça um programa que nos dê:
#	a) salário bruto.
#	b) quanto pagou ao INSS.
#	c) quanto pagou ao sindicato.
#	d) o salário líquido.
#	e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
#	   + Salário Bruto : R$
#	   - IR (11%) : R$
#	   - INSS (8%) : R$
#	   - Sindicato ( 5%) : R$
#	   = Salário Liquido : R$
#	
# Obs.: Salário Bruto - Descontos = Salário Líquido.


salary = 0.0
worked_hour = 0
month_worked = 0
IR_TAX = 0.11
INSS_TAX = 0.08
SYNDICATE_TAX = 0.05


def wageWorkedByHour(earningPerHour, hourWorkedByMonth):
    return earningPerHour * hourWorkedByMonth
    

def discount_IR(value):
    return value * IR_TAX


def discount_INSS(value):
    return value * INSS_TAX


def discount_syndicate(value):
    return value * SYNDICATE_TAX


def net_wage(value):
    return value - discount_IR(value) - discount_INSS(value) - discount_syndicate(value)


if __name__ == "__main__":
    ganhoHora = float(input("Informe o valor ganho por hora: "))
    horasTrabalhadasMes = int(input("Horas trabalhadas no mês: "))
    raw = wageWorkedByHour(ganhoHora, horasTrabalhadasMes)
    taxByIR = discount_IR(raw)
    taxByINSS = discount_INSS(raw)
    taxBySyndicate = discount_syndicate(raw)
    net = net_wage(raw)
    print( "= - = - = - = - = - = - = - = - = - = - = - = - =")
    print(f" Salário bruto..........: R$ {raw:.2f}")
    print( "=================================================")
    print( " Descontos: ")
    print(f" - Taxa IR..............: R$ {taxByIR:.2f}")
    print(f" - Taxa INSS............: R$ {taxByINSS:.2f}")
    print(f" - Taxa Sindicato.......: R$ {taxBySyndicate:.2f}")
    print( "=================================================")
    print(f" - Salário líquido......: R$ {net:.2f}")
    print( "= - = - = - = - = - = - = - = - = - = - = - = - =")



