# Día 5: Funciones y parámetros

## 🔹 ¿Qué es una función?

Una **función** es como una **máquina** que recibe algo, hace un proceso y devuelve un resultado.
Sirve para **organizar código**, **evitar repetirlo** y **hacerlo más legible**.

👉 Se define con `def`:

```python
def saludar():
    print("Hola")
```

---

## 🔹 Parámetros y argumentos

* **Parámetros** → son “espacios vacíos” que la función espera.
* **Argumentos** → son los valores concretos que le pasamos al llamar la función.

Ejemplo:

```python
def saludar(nombre):   # parámetro
    print("Hola", nombre)

saludar("Moroni")      # argumento
```

---

## 🔹 Return

Una función puede **devolver un valor** con `return`.
Eso la hace más útil porque no solo imprime, sino que **entrega resultados** que puedes guardar o usar en otra parte.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)   # guarda 8 en resultado
```

---

## 🔹 Tipos de parámetros

1. **Obligatorios** → debes darlos sí o sí.
2. **Opcionales (con valores por defecto)**:

   ```python
   def saludar(nombre="invitado"):
       print("Hola", nombre)
   ```
3. **Número variable de argumentos**:

   * `*args` → varios sin nombre.
   * `**kwargs` → varios con nombre.

---

✅ **En resumen:**

* Las **funciones** son bloques de código reutilizables.
* Los **parámetros** permiten darles flexibilidad.
* El `return` permite que devuelvan resultados.
* Hacen tu código más **limpio, modular y fácil de mantener**.


### 1. **Parámetros obligatorios**

Son los que tienes que dar sí o sí, porque la función no tiene un valor por defecto para ellos.
Ejemplo mental:

* Función `saludar(nombre)`
* Si no pasas `nombre`, Python se enoja (te lanza error).
  👉 Es como cuando te piden tu nombre en una entrevista: *no puedes decir "paso".*

---

### 2. **Parámetros opcionales (con valores por defecto)**

Aquí el programador le da un valor inicial al parámetro.

* Ejemplo:

  ```python
  def saludar(nombre="invitado"):
      print("Hola", nombre)
  ```
* Si no pasas nada, usa `"invitado"`.
* Si pasas algo, usa lo que diste.
  👉 Es como cuando en el restaurante te sirven arroz por defecto, pero si quieres puedes pedir papas.

---

### 3. **Número variable de argumentos**

Aquí es donde Python se pone más flexible:

* **`*args` → varios sin nombre.**
  Recoge todos los valores que le pases **sin nombre**, como una tupla.
  Ejemplo mental:

  ```python
  def sumar(*args):
      return sum(args)
  ```

  Si llamas `sumar(2, 3, 5)`, dentro la función `args = (2, 3, 5)`.
  👉 Es como decir: “tráeme varias frutas” y te llegan una manzana, una pera, un mango… todas en una misma canasta.

---

* **`**kwargs` → varios con nombre.**
  Recoge valores **con nombre** (clave=valor), como un diccionario.
  Ejemplo mental:

  ```python
  def describir_persona(**kwargs):
      print(kwargs)
  ```

  Si llamas `describir_persona(nombre="Ana", edad=25, ciudad="Quito")`, dentro `kwargs = {"nombre": "Ana", "edad": 25, "ciudad": "Quito"}`.
  👉 Es como un formulario donde pones casillas con su título: nombre, edad, ciudad. Cada dato viene con su etiqueta.

---

📌 Entonces, en resumen:

* **Obligatorios** → siempre tienes que darlos.
* **Opcionales** → tienen un valor de respaldo.
* **`*args`** → varios valores sin nombre.
* **`**kwargs`** → varios valores con nombre.

Ya, clarísimo 👌. Vamos paso a paso con ejemplos prácticos para que veas cómo se leen y cómo se usan.

---

## 1. `*args` → varios valores sin nombre

```python
def sumar_todo(*args):
    print("args recibido:", args)  # se ve como tupla
    return sum(args)

print(sumar_todo(1, 2, 3))       # 6
print(sumar_todo(5, 10, 15, 20)) # 50
```

👉 Aquí, `args` es una **tupla**.

* `sumar_todo(1,2,3)` recibe `(1,2,3)` dentro de `args`.
* Lo recorres como si fuera una lista.

---

## 2. `**kwargs` → varios valores con nombre

```python
def mostrar_info(**kwargs):
    print("kwargs recibido:", kwargs)  # se ve como diccionario
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

mostrar_info(nombre="Moroni", edad=32, ciudad="Quito")
```

👉 Aquí, `kwargs` es un **diccionario**.

* `kwargs = {"nombre": "Moroni", "edad": 32, "ciudad": "Quito"}`
* Lo recorres con `.items()` para leer clave-valor.

---

## 3. Combinando `*args` y `**kwargs`

```python
def fiesta(*args, **kwargs):
    print("Invitados sin etiqueta:", args)
    print("Invitados con etiqueta:", kwargs)

fiesta("Juan", "Pedro", "Lucía", VIP="Moroni", Cumpleañero="Efraín")
```

Salida:

```
Invitados sin etiqueta: ('Juan', 'Pedro', 'Lucía')
Invitados con etiqueta: {'VIP': 'Moroni', 'Cumpleañero': 'Efraín'}
```

👉 Los `args` guardan lo que llega **sin nombre**,
y los `kwargs` lo que llega **con nombre**.

---

## 4. Extra tip: *desempaquetar* listas/diccionarios al llamar

```python
numeros = [10, 20, 30]
opciones = {"sep": " - ", "end": " :) \n"}

print(*numeros)            # equivale a print(10, 20, 30)
print("Hola", "Mundo", **opciones)  
# equivale a print("Hola", "Mundo", sep=" - ", end=" :) \n")
```

Esto es muy usado porque te deja pasar listas o diccionarios directo como si fueran argumentos normales.


