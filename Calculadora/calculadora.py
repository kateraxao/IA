# Función para validar que el número sea entero
def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.lstrip("-").isdigit():  # Permite números negativos
            return int(entrada)
        else:
            print("Error: Debes ingresar un número entero válido.")

# Funciones de operaciones
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

# Función principal
def calculadora():
    print("=== Calculadora Básica ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Elige una opción (1/2/3/4): ")
    
    if opcion in ["1", "2", "3", "4"]:
        num1 = pedir_entero("Ingresa el primer número entero: ")
        num2 = pedir_entero("Ingresa el segundo número entero: ")
        
        if opcion == "1":
            print("Resultado:", sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida")

# Ejecutar programa
if __name__ == "__main__":
  calculadora()
