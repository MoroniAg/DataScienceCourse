## 🔹 ¿Qué es Machine Learning?

Una **definición directa**:

> Es el campo que entrena algoritmos para que aprendan patrones a partir de datos y tomen decisiones sin ser programados explícitamente para cada caso.


## 🧭 Mapa mental: Ramas vs Modelos

| **Rama de ML** | **¿Tiene etiquetas?** | **Objetivo** | **Modelos comunes** |
| --- | --- | --- | --- |
| 🟢 **Supervisado**  | ✅ Sí | Predecir una salida conocida | Regresión lineal / logística, Árboles de decisión / Random Forest, SVM, KNN, Redes neuronales, Gradient Boosting (XGBoost, LightGBM, etc.) 
| 🔵 **No Supervisado** | ❌ No | Encontrar patrones o estructura oculta | K-Means, DBSCAN, PCA, Autoencoders, Clustering jerárquico |
| 🟠 **Aprendizaje por refuerzo** | ✅/❌ (Recompensa, no etiqueta directa) | Tomar decisiones secuenciales | Q-Learning, Deep Q-Networks (DQN), Policy Gradient, Proximal Policy Optimization (PPO) |

### 👇 ¿Cómo interpretarlo?

- Si tus datos tienen **entradas y salidas claras** (por ejemplo, precio de una casa), estás en **supervisado** → usás regresión, árboles, etc.
- Si **solo tenés entradas** y querés descubrir **estructura o grupos**, estás en **no supervisado** → usás clustering, reducción de dimensionalidad, etc.
- Si tenés un **agente que toma decisiones** y aprende con **recompensas**, es **aprendizaje por refuerzo**.

## 🔧 ¿Qué se hace en un flujo de ML?

1. Obtener y entender los datos
2. Preprocesar y limpiar
3. Elegir un modelo
4. Entrenar con datos
5. Evaluar con métricas (accuracy, F1, etc.)
6. Ajustar hiperparámetros
7. ¡Poner en producción!