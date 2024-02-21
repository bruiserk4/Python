import math

class Area_Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

class Calculadora:
    def somar(self, x, y):
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
        
    def area_triangulo(self,x,y):
        return (x * y) / 2

def main():
    calc = Calculadora()
    circulo = None
    while True:
        print("Bem-vindos! Escolha a operação...\n")
        opcao = int(input("""1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Calculo de Área 
6 - Finalizar\nEscolha uma opção: """))
        
        if opcao == 6:
            print("Programa finalizado.")
            break
        elif opcao == 5:
            opcao_area = int(input("1 - Triangulo \n 2 - Circulo \nEscolha uma opção: "))
            if opcao_area == 2:
                raio = float(input("Raio do Círculo: "))
                circulo = Area_Circulo(raio)
                print("Área do círculo:", circulo.calcular_area())
            else:
                 x = float(input("Primeiro Valor: "))
                 y = float(input("Segundo Valor: "))
                 print("Área do Triângulo:", calc.area_triangulo(x, y))

        else:
            x = float(input("Primeiro Valor: "))
            y = float(input("Segundo Valor: "))
            if opcao == 1:
                print("Resultado da soma:", calc.somar(x, y))
            elif opcao == 2:
                print("Resultado da subtração:", calc.subtrair(x, y))
            elif opcao == 3:
                print("Resultado da multiplicação:", calc.multiplicar(x, y))
            elif opcao == 4:
                print("Resultado da divisão:", calc.dividir(x, y))
            else:
                print("Opção inválida.\n")

main()