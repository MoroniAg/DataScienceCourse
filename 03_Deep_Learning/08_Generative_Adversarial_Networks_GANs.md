# **Generative Adversarial Networks (GANs)** – generación de datos.

## ¿Qué es un GAN?

**GAN = Generative Adversarial Network**

Fue inventado por Ian Goodfellow (2014), y revolucionó la IA generativa.

Es una arquitectura con **dos redes neuronales enfrentadas entre sí**:

| Rol | Red | ¿Qué hace? |
| --- | --- | --- |
| 🧑‍🎨 Generador (G) | Red generativa | Intenta **crear datos falsos que parezcan reales** |
| 🕵️ Discriminador (D) | Red discriminativa | Intenta **detectar si los datos son reales o generados** |

Se entrenan **una contra la otra** como en una competencia.

---

### ⚔️ ¿Cómo funciona el entrenamiento?

1. El generador toma **ruido aleatorio** y lo convierte en algo que **parezca real** (por ejemplo, una imagen de un rostro).
2. El discriminador ve tanto datos reales como falsos y **aprende a distinguirlos**.
3. Ambos mejoran al mismo tiempo:
    - El generador mejora **engañando mejor**
    - El discriminador mejora **detectando mejor**

🔁 Se retroalimentan hasta que el generador **genera cosas que el discriminador ya no puede diferenciar** de los datos reales.

---

### 🧠 Analogía rápida:

Imaginá un falsificador y un policía forense:

- El falsificador (G) trata de hacer billetes falsos.
- El policía (D) examina billetes y dice cuáles son falsos.
- A medida que el falsificador mejora, el policía también se vuelve más exigente.
- Si el falsificador logra engañar al policía... ha ganado.

---

## 🖼️ ¿Para qué sirven los GAN?

- Generación de imágenes realistas (caras humanas, paisajes, arte)
- **Deepfakes** y animación de rostros
- Superresolución de imágenes (mejorar calidad)
- Estilo artístico (ej. convertir fotos en Van Gogh)
- Rellenar imágenes incompletas (inpainting)

---

## 📉 ¿Cómo se entrena un GAN?

No se usa una pérdida clásica.

Se usa una **función de pérdida adversarial**, que mide qué tan bien engaña el generador al discriminador.

🔁 El generador quiere **minimizar** la diferencia,

el discriminador quiere **maximizarla**.

---

## 🔥 GAN bien entrenado = generador que engaña sin que lo pillen.