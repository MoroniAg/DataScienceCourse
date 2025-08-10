# **Regresión lineal**

## 📐 ¿Qué es la regresión lineal?

Es un modelo supervisado que sirve para **predecir un valor numérico continuo** a partir de uno o varios atributos (features).

> Idea básica: encontrar la línea recta (o plano, o hiperplano) que mejor se ajusta a los datos.
> 

---

## 🧠 Ejemplo intuitivo

Supongamos que quieres predecir el **precio de una casa** según su tamaño:

| Tamaño (m²) | Precio (USD) |
| --- | --- |
| 50 | 60.000 |
| 70 | 80.000 |
| 100 | 120.000 |

La regresión lineal dice:

> “Voy a encontrar la línea recta que mejor se ajusta a esos puntos.”
> 

Fórmula base:

```
y = w * x + b

```

- `x`: el input (tamaño de la casa)
- `w`: el peso (cuánto sube el precio por cada m²)
- `b`: el sesgo (precio base aunque el tamaño sea 0)
- `y`: la predicción (precio estimado)

---

### 🔢 ¿Qué hace durante el entrenamiento?

Ajusta `w` y `b` para que la línea:

- Pase lo más cerca posible de todos los puntos (mínimo error cuadrático)
- Use **mínimos cuadrados** para medir la diferencia entre predicción y realidad

---

## 🎯 ¿Cuándo usar regresión lineal?

✅ Cuando:

- Tenés una **relación aproximadamente lineal**
- Hay **pocos features**
- Querés algo **rápido y fácil de interpretar**

❌ No es buena si:

- Los datos tienen relaciones **no lineales**
- Hay **mucha multicolinealidad**
- Hay **outliers extremos** que distorsionan la línea

---

## 🧰 Variantes comunes:

- **Regresión lineal múltiple**: usa varios `x₁, x₂, x₃...`
- **Ridge / Lasso Regression**: agregan regularización para evitar sobreajuste