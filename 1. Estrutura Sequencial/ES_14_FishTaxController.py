# 14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. 
#
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. 
#
# *** Imprima os dados do programa com as mensagens adequadas ***

PAYTAX = 4.0
WEIGHT_LIMIT = 50.0
excesso = 0.0
over_tax = 0.0


peso = float(input("Informe o Peso: "))

if (peso > WEIGHT_LIMIT):
    excesso += peso - WEIGHT_LIMIT
    over_tax += (excesso / WEIGHT_LIMIT) * PAYTAX


print( "###################################################")
print(f" · Peso:\t\t\t{peso:.2f}kg")
if excesso > 0:
    print(f" · Excesso:\t\t\t{excesso:.2f}kg")
if over_tax > 0:
    print(f" · Taxa excedente a pagar:\tR$ {over_tax:.2f}")
else:
    print(" · Não há taxa excedente a pagar\t")  
print( "###################################################")



