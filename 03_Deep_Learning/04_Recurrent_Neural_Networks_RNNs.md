# **Recurrent Neural Networks (RNNs)** – secuencias y datos temporales.

### 🧠 **¿Qué es una RNN?**

Imaginá que estás leyendo un libro, pero con una condición:

> Cada vez que lees una palabra nueva, puedes recordar lo que leíste antes para entender mejor lo que sigue.
> 

💬 Por ejemplo, si te digo:

- “El perro ladró porque estaba…”
- Vos ya intuís que la siguiente palabra podría ser *asustado*, *hambriento*, o *feliz*.
    
    Pero no podrías adivinarlo sin **recordar lo anterior**.
    

Eso es lo que hace una **RNN (Recurrent Neural Network)**:

🔁 *“lee” datos secuenciales paso a paso, y en cada paso guarda una pequeña memoria del pasado.*

---

### ⚙️ ¿Cómo se diferencia de una MLP?

| Situación | MLP | RNN |
| --- | --- | --- |
| Lee todo a la vez | ✅ Sí | 🚫 No, lee paso por paso |
| Recuerda pasos anteriores | 🚫 No | ✅ Sí |
| Ideal para texto/audio | 😒 No | 😍 Sí |

---

### 🧠 Metáfora rápida:

> Una MLP es como un turista con amnesia: solo ve lo que tiene enfrente.
> 
> 
> Una RNN es como un lector atento: recuerda lo que ya leyó.
> 

---

### 🛠️ ¿Para qué sirve una RNN?

- Traducción de idiomas
- Predicción de texto (*autocompletado*)
- Análisis de sentimiento
- Reconocimiento de voz
- Predicción de series de tiempo (ventas, clima, etc.)

## 🧠 PARTE 1 — ¿Cómo funciona internamente una RNN?

Vamos a meternos en el flujo de datos, **paso por paso**, con la siguiente idea base:

> Una RNN recibe una secuencia de datos y recuerda lo anterior para influir en lo que hace ahora.
> 

---

### 📦 Imaginá esta secuencia de palabras:

**“El clima está muy...”**

Y la red debe predecir la próxima palabra. Cada palabra se procesa **una a una**:

```
Timestep 1 → “El”
Timestep 2 → “clima”
Timestep 3 → “está”
Timestep 4 → “muy”
```

---

### 🔁 En cada paso ocurren **tres cosas clave**:

1. **Se recibe un dato de entrada**
    
    (por ejemplo, la palabra “clima” convertida en un vector numérico)
    
2. **Se recibe lo que la red “recuerda” del paso anterior**
    
    (esto se llama *estado oculto* o *hidden state*)
    
3. **Se genera una salida**
    
    (por ejemplo, una predicción o un nuevo estado que se pasa al siguiente paso)
    

---

### 📉 Diagrama simplificado:

```
Input_t + Hidden_{t-1} → Hidden_t → Output_t
```

> Es como una conversación:
> 
> - Lo que estás escuchando (input_t)
> - Lo que ya sabes (hidden_{t-1})
> - Y lo que concluyes (output_t)

Y luego ese “estado interno” se **pasa al siguiente paso**, para que lo que venga **tenga contexto**.

---

### 📚 Ejemplo concreto:

Supongamos que estás leyendo:

> “El niño estaba muy...”
> 

Y luego viene “triste”.

- Si la red sólo viera “triste”, no sabría de quién está hablando.
- Pero como **recordó que era ‘el niño’**, puede entender el contexto completo.

Eso es lo que permite la **estructura recursiva** de la RNN: **estado que fluye en el tiempo**.

---

### 🧠 ¿Qué significa el “estado oculto”?

- Es como una mini memoria interna.
- Guarda lo que la red aprendió hasta ahora.
- Y se actualiza **en cada paso**, dependiendo de lo que recibe.

---

### 🤯 ¿Qué lo diferencia realmente de un MLP?

En una **MLP**, si vos le das 10 palabras, ella las procesa **todas juntas, como si fueran independientes**.

En una **RNN**, esas 10 palabras **se procesan en orden**, y lo que la red hace con la palabra número 6 **depende de lo que pasó con la 1, 2, 3...**.

La RNN se convierte así en algo muy **cercano al pensamiento humano en lenguaje.**