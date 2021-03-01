
def get_absoluto(entero):
    return {True: entero, False: entero * -1} [entero >= 0]

def compara_signos(num1, num2):
    return {True: 1, False: -1} [(num1 >= 0 and num2 >= 0) or (num1 < 0 and num2 < 0)]

def es_positivo(entero):
    return entero >= 0

