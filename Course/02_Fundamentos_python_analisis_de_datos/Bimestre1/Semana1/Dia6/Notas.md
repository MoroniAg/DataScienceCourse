# Día 6: Listas, tuplas, diccionarios.

## 🔹 Listas (`list`)

* Colecciones **ordenadas y mutables**.
* Puedes **modificar, añadir o eliminar** elementos.
* Se usan con corchetes `[]`.

Ejemplo:

```python
frutas = ["manzana", "pera", "uva"]
frutas.append("plátano")   # agregar
frutas[1] = "naranja"      # modificar
```

---

## 🔹 Tuplas (`tuple`)

* Colecciones **ordenadas pero inmutables** (no puedes cambiar sus valores).
* Se usan con paréntesis `()`.
* Útiles para **datos que no deben cambiar**.

Ejemplo:

```python
coordenada = (10, 20)
```

---

## 🔹 Diccionarios (`dict`)

* Colecciones **no ordenadas** (aunque en Python 3.7+ mantienen orden de inserción).
* Guardan pares **clave → valor**.
* Se usan con llaves `{}`.

Ejemplo:

```python
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Quito"
}
print(persona["nombre"])
```

---

📌 **Diferencias clave**:

* Lista → **mutable**, con índices numéricos.
* Tupla → **inmutable**, con índices numéricos.
* Diccionario → **mutable**, con índices de tipo clave.

=
