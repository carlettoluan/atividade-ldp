import math

def formaTriangulo(a, b, c):
    #Verifica se os valores a, b, c podem formar um triângulo.
    return a < b + c and b < a + c and c < a + b

def calcularAreaTriangulo(a, b, c):
    # Calcular a área de um triângulo
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Entrada dos valores
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# Verifica se formam um triângulo
if formaTriangulo(a, b, c):
    # Calcula a área
    area = calcularAreaTriangulo(a, b, c)
    print(f"Os valores formam um triângulo com área: {area:.2f}")
else:
    print(f"Os valores {a}, {b}, {c} não formam um triângulo.")
