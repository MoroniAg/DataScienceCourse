# Día 2: Operadores, entrada/salida, comentarios.

## 📌 1. Operadores en Python (a fondo)

### 🔹 Operadores aritméticos

| Operador | Descripción                      | Ejemplo  | Resultado |
| -------- | -------------------------------- | -------- | --------- |
| `+`      | Suma                             | `5 + 2`  | `7`       |
| `-`      | Resta                            | `5 - 2`  | `3`       |
| `*`      | Multiplicación                   | `5 * 2`  | `10`      |
| `/`      | División flotante                | `5 / 2`  | `2.5`     |
| `//`     | División entera (floor division) | `5 // 2` | `2`       |
| `%`      | Módulo (resto)                   | `5 % 2`  | `1`       |
| `**`     | Potencia                         | `5 ** 2` | `25`      |

---

### 🔹 Operadores de comparación

Devuelven siempre un **booleano** (`True` o `False`):

```python
5 == 5   # True
5 != 3   # True
5 > 2    # True
5 < 2    # False
5 >= 5   # True
5 <= 4   # False
```

---

### 🔹 Operadores lógicos

Trabajan con valores booleanos:

```python
# AND → True si ambas condiciones son True
(5 > 2) and (3 < 4)   # True

# OR → True si al menos una condición es True
(5 > 2) or (3 > 4)    # True

# NOT → Invierte el valor booleano
not(5 > 2)            # False
```

---

### 🔹 Operadores de asignación

Sirven para asignar o actualizar valores:

```python
x = 5     # Asignación
x += 3    # x = x + 3
x -= 2    # x = x - 2
x *= 4    # x = x * 4
x /= 2    # x = x / 2
x %= 3    # x = x % 3
x **= 2   # x = x ** 2
x //= 2   # x = x // 2
```

---

### 🔹 Operadores de pertenencia

Verifican si un elemento está dentro de una secuencia:

```python
"hola" in "hola mundo"   # True
"python" not in "java"   # True
```

---

### 🔹 Operadores de identidad

Comparan si dos variables apuntan al mismo objeto en memoria:

```python
a = [1, 2]
b = a
c = [1, 2]

a is b   # True  (misma referencia)
a is c   # False (mismo contenido, distinta referencia)
```

---

## 📌 2. Entrada y salida de datos

**Salida**:

```python
print("Hola mundo")
print(f"Hola {nombre}, tienes {edad} años")  # f-string
print("El resultado es:", resultado)         # varios argumentos
```

**Entrada**:

```python
nombre = input("Ingresa tu nombre: ")  # siempre str
edad = int(input("Ingresa tu edad: ")) # convierte a entero
altura = float(input("Ingresa tu altura: "))
```

💡 **Tip**: Conviene validar datos con `try/except` para evitar que el usuario meta letras donde debería ir un número.

---

## 📌 3. Comentarios

**Una sola línea**:

```python
# Esto es un comentario
```

**Varias líneas**:

```python
"""
Esto es un comentario
de varias líneas.
Python lo trata como string,
pero si no se asigna a nada, no se usa.
"""
```

