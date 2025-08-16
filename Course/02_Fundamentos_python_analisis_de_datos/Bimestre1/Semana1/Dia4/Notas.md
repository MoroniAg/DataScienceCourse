# Día 4: Bucles (`for`, `while`).

## 🔁 ¿Qué es un bucle?

Un bucle es una estructura que permite **repetir un bloque de instrucciones** sin tener que escribirlo muchas veces. Se repite hasta que la condición se deje de cumplir (en el caso del `while`) o hasta que se recorra una secuencia completa (en el caso del `for`).

---

### 1. **Bucle `for`**

* Se usa cuando **sabemos cuántas veces queremos repetir**.
* En Python suele usarse con `range()` o para recorrer elementos de una lista, cadena, etc.

Ejemplo:

```python
for i in range(5):  
    print(i)
```

👉 Esto imprime del **0 al 4** (porque `range(5)` llega hasta 5 pero no lo incluye).

Se puede personalizar con inicio, fin y paso:

```python
for i in range(1, 10, 2):
    print(i)
```

👉 Imprime: `1, 3, 5, 7, 9`.

También sirve para recorrer colecciones:

```python
for letra in "hola":
    print(letra)
```

👉 Imprime cada letra de la palabra.

---

### 2. **Bucle `while`**

* Se usa cuando **no sabemos cuántas veces se repetirá**.
* Repite mientras una **condición booleana sea True**.

Ejemplo:

```python
x = 1
while x <= 5:
    print(x)
    x += 1
```

👉 Imprime del **1 al 5**.
⚠️ Si no actualizas la condición, el bucle nunca termina (bucle infinito).

---

### 3. **Control de bucles**

A veces queremos **romper o saltar** dentro de un bucle:

* `break` → sale del bucle inmediatamente.
* `continue` → salta a la siguiente iteración.
* `else` (menos usado) → se ejecuta si el bucle termina sin romperse con `break`.

Ejemplo:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

👉 Imprime `0, 1, 2` y luego se detiene.

---

### 4. **Comparación rápida**

* `for` → ideal para **recorrer algo** (listas, rangos, strings…).
* `while` → ideal para **repetir hasta que pase algo** (ej: pedir contraseña correcta).

## Ejercicios

**Ejercicio 1 (con `for`):**
Pide al usuario un número y muestra la tabla de multiplicar de ese número del 1 al 10.

---

**Ejercicio 2 (con `while`):**
Haz un programa que pida contraseñas al usuario hasta que escriba la correcta. Cuando la escriba bien, muestra un mensaje de bienvenida y termina.

---

**Ejercicio 3 (con combinación):**
Escribe un programa que sume todos los números del 1 hasta un número que el usuario ingrese. Usa un `while` o un `for`, el que prefieras.

---

