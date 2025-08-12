## Día 1 – Sintaxis, variables y tipos de datos en Python

### 1. Sintaxis básica

* **Indentación**: Python usa sangrías para definir bloques de código (4 espacios recomendados).
* **Case sensitive**: `variable` y `Variable` son cosas distintas.
* **Comentarios**: Se escriben con `#`.

Ejemplo:

```python
# Hola mundo en Python
print("Hola, Data Science")
```

---

### 2. Variables

En Python no se declara el tipo, se asigna directamente:

```python
nombre = "Pepe"    # string
edad = 32          # int
altura = 1.78      # float
```

**Buenas prácticas:**

* Nombres descriptivos en minúsculas y con `_` si son compuestos: `tasa_interes`.
* Evitar palabras reservadas como `if`, `for`, `class`.

---

### 3. Tipos de datos básicos

**Numéricos**

```python
entero = 10       # int
decimal = 3.14    # float
complejo = 2 + 3j # complex
```

**Texto**

```python
texto = "Data Science"
```

**Booleanos**

```python
activo = True
inactivo = False
```

**None**

```python
valor = None  # Sin valor asignado
```

---

### 4. Mini ejercicio

Simular datos de un usuario y calcular un valor útil.

```python
# Datos de ejemplo
nombre = "Moroni"
edad = 32
peso = 72.5
altura = 1.78

# Cálculo de IMC
imc = peso / (altura ** 2)

print("Usuario:", nombre)
print("Edad:", edad)
print("IMC:", round(imc, 2))
```

---

