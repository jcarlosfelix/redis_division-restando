from pop_metodos import get_absoluto, compara_signos


class Division:
    dividendo = 0
    divisor = 0
    cociente = 0
    residuo = 0
    operacion = ''
    signo = 0


    def __init__(self, tupla):
        self.dividendo, self.divisor, self.cociente, self.residuo, self.operacion = tupla

    def get_signo(self):
        if (self.signo == 0): self.signo = compara_signos(self.dividendo, self.divisor)
        return self.signo


    def calcular(self):
        dividendo = get_absoluto(self.dividendo)
        divisor = get_absoluto(self.divisor)
        self.operacion = str(dividendo)

        while (dividendo >= divisor):
            dividendo = dividendo - divisor
            self.cociente += 1
            self.operacion += '-' + str(divisor)

        self.residuo = dividendo
        self.operacion += ' = ' + str(dividendo)

        if (self.cociente != 0): 
            self.cociente *= self.get_signo()
            self.residuo *= self.get_signo()


    def display(self):
        print('------------------------------')    
        print('Operacion: ' + str(self.dividendo) + ' / ' + str(self.divisor))
        print('Cociente:', self.cociente)        
        print('Residuo:', self.residuo)
        print('Equivale:', self.operacion)
