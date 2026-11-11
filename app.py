def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

if __name__ == "__main__":
    print("=== Calculadora - Calidad y Pruebas de Software T3 ===")
    print("10 + 5 =", sumar(10, 5))
    print("10 - 5 =", restar(10, 5))
    print("10 * 5 =", multiplicar(10, 5))
    print("10 / 5 =", dividir(10, 5))