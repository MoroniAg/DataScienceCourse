# **Transformers** – modelo dominante en NLP y otras áreas.

## 🚀 ¿Qué es un Transformer?

Es una arquitectura que reemplaza las RNN y LSTM para manejar secuencias, pero sin procesar paso a paso. En vez de eso, **procesa toda la secuencia de una vez**, usando un mecanismo llamado **Atención**.

---

## 🔍 ¿Por qué es tan poderoso?

- Puede capturar **relaciones a largo plazo** en la secuencia sin perder contexto.
- Es **paralelizable**, así que entrena mucho más rápido que RNN/LSTM.
- Es la base de modelos como GPT, BERT, y otros gigantes del lenguaje.

---

## ⚙️ Conceptos clave:

- **Self-Attention:** Cada palabra “presta atención” a todas las otras palabras de la secuencia para entender contexto.
- **Positional Encoding:** Como no procesa secuencia en orden, usa esta técnica para saber el orden de las palabras.
- **Capas y bloques:** Construidos con multi-head attention y feed-forward layers.

---

## 🎯 Analogía simple:

Imaginá que estás leyendo un párrafo y podés instantáneamente ver cómo cada palabra se relaciona con todas las demás, sin tener que leer en orden uno a uno.

### 🔍 Paso 1: ¿Qué es la atención (Attention)?

La atención es como un **radar inteligente** que, para cada palabra de la secuencia, decide a qué otras palabras debe “prestar atención” para entender mejor su significado.

---

### 🧠 Ejemplo simple:

Frase:

*“El banco cerró temprano porque estaba lloviendo.”*

La palabra “banco” puede significar “institución financiera” o “banco para sentarse”.

Para saber cuál es, la atención hace que “banco” mire palabras como “cerró” y “lloviendo” para entender el contexto.

---

### 🔧 Paso 2: ¿Cómo se calcula la atención?

Para cada palabra (o “token”) se crean tres vectores:

- **Query (Q):** La palabra que está buscando información.
- **Key (K):** Las palabras contra las que se compara.
- **Value (V):** La información que se recupera.

---

### 🔁 Paso 3: El proceso

1. Se calcula la similitud (un producto punto) entre el Query de la palabra actual y los Keys de todas las palabras.
2. Se normalizan esas similitudes con softmax para obtener pesos (qué tanto “atender” a cada palabra).
3. Se usa esos pesos para hacer una combinación ponderada de los Values.
4. Esa combinación es la **atención final** para la palabra actual.

---

### 🔥 ¿Por qué es poderoso?

- Porque cada palabra **puede considerar todo el contexto**, no solo las palabras cercanas.
- Esto soluciona problemas de largo alcance que las RNN/LSTM tenían.

---

### 📦 Bonus: Multi-head attention

El Transformer no hace esto una sola vez, sino varias veces en paralelo (con diferentes parámetros), para capturar distintos tipos de relaciones y patrones.