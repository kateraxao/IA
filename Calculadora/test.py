from calculadora import sumar, restar, multiplicar, dividir


print("=== TEST CALCULADORA ===")

# ---- SUMA ----
try:
    assert sumar(2, 3) == 5
    print("SUMAR: OK")
except:
    print("SUMAR: FALLA")

# ---- RESTA ----
try:
    assert restar(5, 3) == 2
    print("RESTAR: OK")
except:
    print("RESTAR: FALLA")

# ---- MULTIPLICAR ----
try:
    assert multiplicar(3, 4) == 12
    print("MULTIPLICAR: OK")
except:
    print("MULTIPLICAR: FALLA")

# ---- DIVIDIR ----
try:
    assert dividir(10, 2) == 5
    print("DIVIDIR: OK")
except:
    print("DIVIDIR: FALLA")

# ---- DIVIDIR POR CERO ----
try:
    dividir(10, 0)
    print("DIVIDIR POR CERO: FALLA")
except ValueError:
    print("DIVIDIR POR CERO: OK")

print("========================")
