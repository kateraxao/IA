# 🧮 Calculadora Básica en Python

Proyecto sencillo de calculadora en Python que permite realizar operaciones básicas desde consola:

* ➕ Suma
* ➖ Resta
* ✖️ Multiplicación
* ➗ División

Incluye validación de números enteros y control de división por cero.

---

## 📂 Archivo principal

```
calculadora.py
```

---

## ▶️ Cómo ejecutar el programa

Desde la carpeta donde está el archivo:

```bash
python calculadora.py
```

El programa mostrará un menú con opciones y pedirá los números por teclado.

---

## 🧠 Funcionalidades

### Validación de entrada

La función `pedir_entero()` asegura que el usuario solo pueda introducir números enteros (positivos o negativos).

### Operaciones disponibles

* `sumar(a, b)` → devuelve la suma
* `restar(a, b)` → devuelve la resta
* `multiplicar(a, b)` → devuelve el producto
* `dividir(a, b)` → devuelve la división

  * Si `b` es 0, lanza un error `ValueError`

---

## ⚠️ Control de errores

La división por cero está controlada:

```python
raise ValueError("No se puede dividir entre cero")
```

---

## 🧪 Tests (opcional)

Puedes crear un archivo `test.py` con pruebas simples usando `assert` para verificar que las funciones funcionan correctamente.

---

## 🎯 Objetivo del proyecto

Proyecto educativo para practicar:

* funciones en Python
* entrada por teclado
* validación de datos
* control de errores
* estructura básica de programa

---

## 👩‍💻 Autor

Proyecto de práctica en Python.
