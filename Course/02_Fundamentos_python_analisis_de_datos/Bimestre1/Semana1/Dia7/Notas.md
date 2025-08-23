# Día 7: Comprensión de listas y manejo de errores (try/except).

## 🔹 1. Comprensión de listas (List comprehension)

### 🌱 ¿Qué es una comprensión de listas?

Es una forma **más corta y elegante** de crear listas en Python.
En lugar de usar un bucle `for` tradicional, puedes crear la lista directamente en **una sola línea**.

### 🧱 Sintaxis básica

```python
[expresión for elemento in iterable if condición]
```

* **expresión** → qué valor quieres guardar en la lista.
* **elemento** → el valor que vas tomando de la colección.
* **iterable** → la colección que recorres (ej: lista, rango, string).
* **if condición** *(opcional)* → filtra qué elementos entran en la lista.


Ejemplo normal:

```python
numeros = []
for i in range(5):
    numeros.append(i**2)
print(numeros)   # [0, 1, 4, 9, 16]
```

Con comprensión de listas:

```python
numeros = [i**2 for i in range(5)]
print(numeros)   # [0, 1, 4, 9, 16]
```

También puedes filtrar:

```python
pares = [i for i in range(10) if i % 2 == 0]
print(pares)   # [0, 2, 4, 6, 8]
```

---

### 📌 Ejemplos prácticos

1. **Lista de cuadrados**

```python
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]
```

> Equivalente a hacer un `for` y un `.append()`.

---

2. **Filtrar números pares**

```python
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

3. **Convertir texto a lista de caracteres**

```python
texto = "python"
lista_letras = [letra.upper() for letra in texto]
print(lista_letras)  # ['P', 'Y', 'T', 'H', 'O', 'N']
```

---

4. **Lista de tuplas**

```python
coordenadas = [(x, y) for x in range(2) for y in range(2)]
print(coordenadas)  # [(0, 0), (0, 1), (1, 0), (1, 1)]
```

---

5. **Condicional doble (`if/else`)**

```python
resultado = ["par" if x % 2 == 0 else "impar" for x in range(5)]
print(resultado)  # ['par', 'impar', 'par', 'impar', 'par']
```

---

## 🔹 2. Manejo de errores (try / except)

A veces tu código se rompe con errores (por ejemplo, dividir entre cero o acceder a una clave inexistente).
El bloque `try/except` permite **atrapar errores y manejar la situación sin que el programa muera**.

Ejemplo:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("No puedes dividir entre cero 🚫")
```

Otro ejemplo:

```python
try:
    edad = int(input("Ingresa tu edad: "))
    print("Tu edad es", edad)
except ValueError:
    print("Eso no es un número válido ❌")
```

Incluso puedes manejar múltiples errores:

```python
try:
    lista = [1, 2, 3]
    print(lista[5])   # índice fuera de rango
except IndexError:
    print("Ese índice no existe en la lista")
except Exception as e:   # atrapa cualquier otro error
    print("Error inesperado:", e)
```

---

👉 Resumen:

* **Comprensión de listas** = atajos para construir listas.
* **try/except** = tu escudo contra errores inesperados.


