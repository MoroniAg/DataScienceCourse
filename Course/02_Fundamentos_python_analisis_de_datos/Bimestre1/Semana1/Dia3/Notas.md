# Día 3: Condicionales (if, elif, else).

## 🧩 Teoría clara

### 1. **`if`**

La palabra reservada `if` evalúa una condición.

* Si la condición es **verdadera**, se ejecuta el bloque de código.
* Si es **falsa**, se ignora y sigue.

```python
x = 10
if x > 5:
    print("x es mayor que 5")
```

---

### 2. **`else`**

Se ejecuta **cuando la condición del `if` no se cumple**.

```python
x = 3
if x > 5:
    print("x es mayor que 5")
else:
    print("x no es mayor que 5")
```

---

### 3. **`elif` (else if)**

Permite comprobar **múltiples condiciones** sin anidar muchos `if`.
El primero que sea verdadero, se ejecuta y los demás se ignoran.

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

---

### 4. **Condiciones múltiples**

Puedes combinar condiciones con:

* `and` → ambas deben cumplirse.
* `or` → basta con que una se cumpla.
* `not` → niega la condición.

```python
edad = 20
membresia = True

if edad >= 18 and membresia:
    print("Puede entrar al gimnasio")
```

---

### 5. **Anidamiento**

Un `if` puede ir dentro de otro, pero conviene usar `elif` para no hacer un lío.

```python
edad = 16
if edad >= 18:
    print("Es mayor de edad")
else:
    if edad >= 13:
        print("Es adolescente")
    else:
        print("Es niño")
```

---

## 🤓 Aplicaciones comunes en Data Science

* Verificar si un dato cumple un rango antes de procesarlo.
* Clasificar datos (ej: positivo, negativo, neutro).
* Validar entradas del usuario.
* Tomar decisiones en flujos de procesamiento.

## Ejercicios

### **Ejercicio 1 — Clasificador de edades**

Un programa debe clasificar a una persona según su edad:

* Si es menor de 12 → “Niño”
* Entre 12 y 17 → “Adolescente”
* Entre 18 y 59 → “Adulto”
* 60 o más → “Adulto mayor”

---

### **Ejercicio 2 — Control de notas**

Un estudiante presenta un examen con nota de 0 a 100.
El programa debe mostrar:

* 90 a 100 → “Sobresaliente”
* 70 a 89 → “Aprobado”
* Menos de 70 → “Reprobado”

---

### **Ejercicio 3 — Cajero automático**

El cajero entrega dinero si:

* La persona tiene **saldo suficiente** en su cuenta.
* El monto solicitado es múltiplo de 10 (ejemplo: 50, 120, 300).

El programa debe mostrar:

* “Transacción exitosa” si cumple las dos condiciones.
* “Fondos insuficientes” si el saldo es menor.
* “Monto inválido” si el valor no es múltiplo de 10.
