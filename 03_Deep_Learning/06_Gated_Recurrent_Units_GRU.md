# **Gated Recurrent Units (GRU)** – otra variante de RNN.

## 🧠 ¿Qué es un GRU?

**GRU = Gated Recurrent Unit**

Es una versión más simple (y más rápida) de la LSTM, pero que aún **mantiene buena memoria** para secuencias.

---

### 📌 Comparación rápida:

| Característica | RNN | LSTM | GRU |
| --- | --- | --- | --- |
| ¿Tiene memoria? | Sí | Sí, con 3 puertas | Sí, con 2 puertas |
| ¿Es compleja? | Baja | Alta | Media |
| ¿Es precisa? | Media | Alta (en secuencias largas) | Casi igual a LSTM |
| ¿Es más rápida? | Sí | ❌ No | ✅ Sí |

---

## 🔍 ¿Qué hace un GRU diferente?

Mientras que la **LSTM tiene 3 puertas** (Forget, Input, Output), la **GRU combina y reduce**:

### 🔑 GRU solo tiene 2 puertas:

### 1. **Update Gate (puerta de actualización)**

> Decide cuánto de la memoria anterior se mantiene y cuánto se reemplaza.
> 

### 2. **Reset Gate (puerta de reinicio)**

> Decide cuánto olvidar del pasado para procesar la nueva entrada.
> 

---

### 🧠 Analogia sencilla:

Imaginá que estás tomando notas mientras alguien habla rápido.

- Si usás una **LSTM**, tenés 3 bolígrafos de colores para:
    - Subrayar lo importante
    - Tachar lo que no sirve
    - Escribir lo nuevo
        
        → Preciso, pero lento.
        
- Si usás una **GRU**, tenés solo 2 resaltadores:
    - Uno para lo que vale la pena mantener
    - Otro para decidir si ignorás lo anterior
        
        → Más rápido, menos sobrecargado.
        

---

### 📦 ¿Cuándo usar GRU?

✅ Cuando:

- Querés buena performance **con menos cómputo**
- Estás trabajando con secuencias **no tan largas**
- Necesitás entrenar **rápido** sin perder precisión

---

### ❗¿Pierde memoria como una RNN?

No.

Aunque es más simple que LSTM, el GRU sigue teniendo **una memoria sólida**, solo que con una estructura más compacta.