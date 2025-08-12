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


### 5. Formateo básico con f-strings

1. **Números decimales con cierto número de decimales**

```python
pi = 3.1415926535

print(f"Pi con 2 decimales: {pi:.2f}")  # 3.14
print(f"Pi con 4 decimales: {pi:.4f}")  # 3.1416
```

`.2f` o `.4f` significa “mostrar 2 o 4 decimales después del punto”.

---

2. **Números enteros con relleno o alineación**

```python
num = 42

print(f"Número con 5 espacios, alineado a la derecha: {num:5d}")   # '   42'
print(f"Número con 5 espacios, alineado a la izquierda: {num:<5d}") # '42   '
```

`5d` significa: entero con ancho mínimo 5, rellenando con espacios.

---

3. **Texto alineado en un espacio fijo**

```python
nombre = "Moroni"

print(f"Nombre alineado a la derecha en 10 espacios: {nombre:>10}")
print(f"Nombre alineado a la izquierda en 10 espacios: {nombre:<10}")
print(f"Nombre centrado en 10 espacios: {nombre:^10}")
```

---

4. **Mostrar porcentaje**

```python
ratio = 0.8532

print(f"Porcentaje: {ratio:.2%}")  # Muestra '85.32%'
```

El formato `.2%` multiplica por 100 y agrega el símbolo `%` con 2 decimales.

---

### Recapitulando:

* Lo que pongas después de `:` dentro de `{}` en un f-string es para controlar **solo la forma en que se muestra** el dato.
* No cambia el valor original, solo el texto que se imprime.
* Puedes combinar formatos para que los reportes se vean limpios y profesionales.

---

¿Quieres que te arme un mini reto para practicar estos formatos con números y texto? Así lo afianzamos.
