# **Autoencoders** – compresión y reconstrucción.

## 🧠 ¿Qué es un Autoencoder?

Es un tipo de red neuronal **no supervisada** que aprende a **comprimir datos y luego reconstruirlos**.

👉 ¿Te suena a zip-descomprimir? Exactamente.

---

### 📦 Estructura básica:

Un Autoencoder tiene 3 partes:

1. **Encoder (codificador)**
    - Toma el input y lo **comprime** en una versión más pequeña (llamada *código* o *embedding*).
2. **Latent Space (espacio latente)**
    - El “resumen” de los datos originales.
    - Es lo que la red cree que es **lo más importante** del input.
3. **Decoder (decodificador)**
    - Toma el código comprimido y trata de **reconstruir el input original** lo mejor posible.

---

## 🎨 Analogía visual

Imaginá que te dan una imagen de 256x256 píxeles y te dicen:

> “No la guardes entera. Dibujala tú mismo desde la memoria, pero solo podés usar 50 números.”
> 

El encoder sería tu capacidad de **resumir** lo esencial.

El decoder sería tu capacidad de **recrear la imagen con lo poco que te acordás**.

---

### 🧩 ¿Para qué sirven los Autoencoders?

1. **Reducción de dimensionalidad**
    
    (como alternativa a PCA pero no lineal)
    
2. **Detección de anomalías**
    
    Si la red no puede reconstruir bien un dato → probablemente sea un dato raro.
    
3. **Eliminación de ruido (Denoising Autoencoders)**
    
    Entrenás a la red con inputs ruidosos y salidas limpias.
    
4. **Preentrenamiento de redes profundas**
    
    Puedes usar el encoder como base para otras tareas.
    
5. **Generación de datos**
    
    Como paso previo a modelos generativos más complejos (VAE, GANs).
    

---

### 📌 ¿Con qué se entrenan?

Con una **pérdida de reconstrucción**, por ejemplo:

> ¿Qué tan diferente es la salida comparada con el input original?
> 

🔁 Se entrena para que esa diferencia sea mínima.