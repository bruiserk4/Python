import math

class Area_Circulo:
    def __init__(self, raio):
        self.raio = raio

class Calculadora:
    def calcular_area(self):
        return math.pi * self.raio ** 2
    def somar(self,x,y):
        return x + y
    def subtrair(self, x, y):
        return x - y
    def multiplicar(self, x, y):
        return x * y
    def dividir(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Não é possível dividir por zero"
   

#x = float(input("Raio do Círculo: "))    
#circulo = Area_Circulo(x)2

def main(Calculadora, Area_Circulo):
    i = 0
    while(i == 6):
        print("Bem-vindos! Escolha a operação.../n")
        i = input("""1 - Soma
                2 - Subtração
                3 - Multiplicação
                4 - Divisão
                5 - Área de circulo
                6 - Finalizar""")
        x = float(input("Primeiro Valor: "))
        y = float(input("Segundo Valor: "))
        if i == 1:
            print(somar(x,y))

main(Calculadora,Area_Circulo)
        