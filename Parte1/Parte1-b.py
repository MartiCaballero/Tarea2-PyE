# Volvemos a cargar el archivo CSV para realizar los ejercicios 5 y 6 con lujo de detalles
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import poisson

# Cargar los datos
df = pd.read_csv("Parte1\cancelaciones.csv")

# Obtener media empírica
lambda_poisson = df['cancelaciones'].mean()

# Construir el histograma empírico
valores = df['cancelaciones'].value_counts().sort_index()
x_vals = np.arange(valores.index.min(), valores.index.max() + 1)

# PMF de la Poisson escalada al tamaño de la muestra
poisson_pmf = poisson.pmf(x_vals, mu=lambda_poisson) * len(df)

# Gráfico del histograma con superposición de Poisson
plt.figure(figsize=(10, 6))
sns.histplot(df['cancelaciones'], bins=range(df['cancelaciones'].min(), df['cancelaciones'].max() + 2), 
             stat="count", discrete=True, label='Datos empíricos', color='skyblue', edgecolor='black')
plt.plot(x_vals, poisson_pmf, 'o-', color='red', label=f'Poisson(λ={lambda_poisson:.2f})', linewidth=2)
plt.title("Ejercicio 5: Histograma con superposición de Poisson")
plt.xlabel("Cancelaciones diarias")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Ejercicio 6: Probabilidades con el modelo Poisson
p_menos_5 = poisson.cdf(4, mu=lambda_poisson)     # P(X < 5)
p_mas_15 = 1 - poisson.cdf(15, mu=lambda_poisson) # P(X > 15)

print(f"📊 Media empírica (λ): {lambda_poisson:.2f}")
print(f"🔽 Probabilidad de menos de 5 cancelaciones (P(X < 5)): {p_menos_5:.4f}")
print(f"🔼 Probabilidad de más de 15 cancelaciones (P(X > 15)): {p_mas_15:.4f}")

# Devolver los resultados

lambda_poisson, p_menos_5, p_mas_15
