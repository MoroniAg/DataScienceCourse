# **Long Short-Term Memory (LSTM)** – mejora de RNNs.

## 😵‍💫 EL PROBLEMA REAL DE LAS RNN:

### 👉 **¡Se les olvida todo a largo plazo!**

Si le das una frase muy larga como:

> “Hace 20 años, en un pequeño pueblo donde la vida era tranquila, nació un niño llamado Efraín, que un día…”
> 

Cuando llegás al final, la RNN ya se **olvidó de lo del principio**, porque la “memoria” se va diluyendo. Eso se llama:

### 🔻 *Desvanecimiento del gradiente*

---

## 🧠 ¿Qué es una LSTM entonces?

**LSTM = Long Short-Term Memory**

→ Es una evolución de la RNN que tiene **una memoria más inteligente**

→ Decide **qué recordar**, **qué olvidar** y **cuándo usar lo que recuerda**

Sí, es como una RNN, pero con **agenda, criterio y sentido común.**

---

## 🧭 ANALOGÍA PRÁCTICA

Imaginá que sos un estudiante y tenés que leer un libro de 300 páginas para un examen.

- Una **RNN** lee todo pero no anota nada. Va olvidando lo anterior mientras avanza.
- Una **LSTM**, en cambio, **tiene un cuaderno**:
    - ✍️ Apunta lo importante
    - ❌ Borra lo irrelevante
    - ✅ Usa sus apuntes cuando los necesita

---

## 🔧 MECANISMO INTERNO DE LA LSTM

Una LSTM tiene **"puertas"**. Y no, no es Hogwarts, aunque lo parece:

### 🚪1. *Forget Gate* (puerta de olvido)

Decide **qué parte de la memoria anterior descartar**

→ "Esto ya no es relevante, bórralo."

### 🚪2. *Input Gate* (puerta de entrada)

Decide **qué nueva información guardar**

→ "Esto es importante, anótalo."

### 🚪3. *Output Gate* (puerta de salida)

Decide **qué parte de la memoria usar ahora mismo**

→ "Necesito recordar esto para la salida actual."

---

## 🔁 FUNCIONAMIENTO EN PASOS

En cada timestep (paso en la secuencia):

1. Mira la entrada actual
2. Mira lo que tiene en su memoria
3. Usa las puertas para:
    - Limpiar lo inútil
    - Guardar lo útil
    - Decidir qué mostrar como salida

Resultado: **memoria más estable, más precisa y más duradera**

---

## 📚 ¿Cuándo usar una LSTM?

- Texto largo con dependencias distantes (novelas, artículos)
- Series de tiempo financieras
- Predicción meteorológica
- Audio y música con estructuras complejas
- Generación de texto (como lo hace GPT pero a nivel simple)

---

## 🤯 Miniresumen

| Característica | RNN | LSTM |
| --- | --- | --- |
| Memoria | Corto plazo | Largo y corto plazo |
| ¿Olvida con el tiempo? | Sí | Mucho menos |
| Ideal para | Secuencias cortas | Secuencias largas y complejas |

## 🎯 PARTE 1: EJEMPLO COMPARATIVO RNN vs LSTM

Imaginá que querés predecir la **palabra final** de una frase larga.

Frase:

> “El niño que vivía en la casa azul, junto a su perro, su bicicleta, sus juguetes, su vecina, y su abuela favorita... siempre fue muy __________.”
> 

---

### 🧠 ¿Qué hace una RNN?

- Empieza bien, entendiendo “niño”, “casa”, “perro”...
- Pero a medida que avanza, empieza a **olvidar el sujeto original**.
- Cuando llega al final, ya no recuerda que hablábamos del niño.
- Resultado: puede decir “tranquila”, “ruidosa”, “solitaria” → palabras sin contexto correcto.

---

### 🧠 ¿Qué hace una LSTM?

- Usa su “cuaderno mental” (las **puertas**) para **recordar el sujeto: el niño**.
- Aunque aparezcan muchos detalles intermedios, **no lo pierde de vista**.
- Llega al final y dice: *“Fue muy feliz”*, *“fue muy curioso”* → respuestas que **tienen sentido con el principio**.

🧠 **LSTM = memoria selectiva + contexto largo**

---

## 🔐 PARTE 2: ¿CÓMO FUNCIONAN LAS PUERTAS DE UNA LSTM?

Vamos a visualizarlo como una **línea de producción en una fábrica de recuerdos**, con 3 controles de paso.

---

### 💡 Cada paso de la secuencia pasa por 3 “puertas”:

### 1. 🧽 **Forget Gate**

> “¿Hay algo de lo anterior que deba tirar?”
> 
- Si estás leyendo “Hoy comí arroz, luego fui al parque...”,
    
    al llegar al parque, capaz el arroz **ya no importa** → lo olvida.
    

### 2. ✍️ **Input Gate**

> “¿Esta nueva información vale la pena guardarla?”
> 
- Si leés “...y vi a mi mejor amigo después de años”,
    
    eso **sí se guarda**, es relevante.
    

### 3. 📤 **Output Gate**

> “¿Qué parte de lo que tengo en la memoria quiero usar ahora mismo?”
> 
- Quizá recordás que **te hizo reír mucho**, y eso **influye en tu respuesta emocional actual**.

---

### ⚙️ Diagrama mental simple:

```
           Entrada actual
                 ↓
     ┌────────────────────────┐
     │    Forget gate         │  ← borra lo innecesario
     └────────────────────────┘
                 ↓
     ┌────────────────────────┐
     │    Input gate          │  ← guarda lo útil
     └────────────────────────┘
                 ↓
     ┌────────────────────────┐
     │    Output gate         │  ← usa lo relevante ahora
     └────────────────────────┘
                 ↓
              Salida

```

🔁 Todo eso se repite en **cada paso de la secuencia**.

Y todo se entrena con backpropagation como en una red normal, pero cada puerta tiene **sus propios pesos y decisiones**.