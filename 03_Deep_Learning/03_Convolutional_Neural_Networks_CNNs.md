# **Convolutional Neural Networks (CNNs)** – procesamiento de imágenes.

### ¿Qué es una CNN (Convolutional Neural Network)?

**Idea principal:**

Una CNN es como un **ojo artificial**. Está diseñada para mirar una imagen **por partes**, detectar **patrones locales** (como bordes, formas, texturas), y luego combinar esa información para **reconocer objetos más grandes**.

Pero vamos con la analogía:

### Analogía visual: El detective con lupa 🔍

Imaginá que sos un detective que inspecciona una imagen para ver si hay un gato.

1. No mirás la imagen toda de golpe.
2. Usás una **lupa** (filtro) y la vas pasando por secciones.
3. Cada vez que ves “pelaje con rayas” o “una oreja puntiaguda”, **anotás una pista**.
4. Luego decís:
    
    > “Vi rayas, bigotes, y una cola. ¡Seguro que es un gato!”

Esa es la idea de una CNN:

- Cada **filtro detecta una característica**
- Cada **capa detecta cosas más complejas**
- Al final, **una MLP toma la decisión final**

### 🧱 Estructura de una CNN paso a paso:

1. **Entrada (Input Layer):**
    - Es la imagen en sí.
    - Puede ser de 28×28, 64×64, RGB o escala de grises.
2. **Capa de convolución (Convolutional Layer):**
    - Se aplican **filtros** para detectar patrones locales.
    - Resultado: un **mapa de activación** por cada filtro.
3. **Función de activación (ReLU):**
    - Rompe la linealidad y acelera el aprendizaje.
    - Convierte los valores negativos en ceros (normalmente).
4. **Capa de pooling (Max Pooling o Average Pooling):**
    - **Reduce** la dimensión de cada mapa.
    - Ejemplo: convierte una imagen de 24×24 a 12×12.
    - Conserva la información **más importante**.
5. **(Opcional) Más bloques de conv + ReLU + pooling:**
    - A medida que aumentás capas, detectás patrones **más complejos**: primero bordes, luego partes de objetos, luego objetos enteros.
6. **Flatten:**
    - Aplana todos los mapas de activación en un **vector** para que pueda entrar en una capa densa.
    - Es como “desenrollar” toda la imagen procesada.
7. **Capa densa (Fully Connected Layer / MLP):**
    - Toma todo lo aprendido por las capas anteriores y **toma decisiones**.
    - Acá es donde vive el clasificador como tal.
8. **Salida (Output Layer):**
    - Una neurona por clase (por ejemplo, una para “gato” y otra para “perro”).
    - Se aplica una **softmax** para decidir cuál es la más probable.

---

### 🎯 Ejemplo práctico: Imagen de un perro

- Convolución: detecta orejas, ojos, pelaje.
- Pooling: se queda con las partes más significativas.
- Más convoluciones: detecta la cara completa del perro.
- Flatten + capa densa: combina todo.
- Salida: 85% perro, 15% gato → **¡Es un perro!**