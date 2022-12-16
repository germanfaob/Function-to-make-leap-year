# Un año es bisiesto si cumple dos condiciones:
# 1. Es divisible por 4 pero NO por 100
# 2. Es divisible por 4, por 100 y por 400
# La función contiene las dos condiciones anteriores dentro del "if"
# * % 4 == 0: comprueba que el resto sea 0 al dividir entre 4

def bisiesto(year):
    if year % 4 == 0 and year % 100 !=0:
        return True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

print(bisiesto(2023))