# **Variational Autoencoders (VAE)**.

## 🤓 ¿Qué es un VAE?

Es una variante de autoencoder con un giro probabilístico:

En vez de codificar la entrada en un punto fijo en el espacio latente, codifica una **distribución probabilística** (media y desviación estándar).

Esto permite:

- Generar datos nuevos **muestreando** de esa distribución
- Tener un espacio latente **suave y continuo**, ideal para interpolar y crear variaciones.

---

## 🎨 Analogía rápida:

Si el autoencoder tradicional es como memorizar una foto exacta, el VAE es como aprender el “estilo” general para luego crear nuevas fotos similares, pero no idénticas.

---

## 📚 ¿Para qué sirven?

- Generar imágenes nuevas
- Reconstrucción con variabilidad
- Tareas donde el espacio latente debe ser ordenado y estructurado
- Base para muchos modelos generativos modernos