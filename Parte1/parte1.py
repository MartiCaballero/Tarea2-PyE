# Importar la librería pandas para manipular datos en forma de tablas
import pandas as pd

# Lectura del archivo CSV que contiene los datos de cancelaciones por día
df = pd.read_csv('cancelaciones.csv') 

# Cálculo de la frecuencia absoluta
# Se cuenta cuántas veces aparece cada valor de cancelaciones
frec_absoluta = df['cancelaciones'].value_counts().sort_index()

# Cálculo de la probabilidad empírica
# Se obtiene dividiendo cada frecuencia absoluta entre el total de días
# Esto estima la probabilidad de que ocurran ciertas cantidades de cancelaciones
total_dias = len(df)
prob_empirica = frec_absoluta / total_dias

# Cálculo de la distribución acumulada empírica
# Se va sumando la probabilidad empírica hasta cada valor x (función de distribución acumulada)
dist_acumulada = prob_empirica.cumsum()

# Se construye una tabla resumen con todos los resultados anteriores
tabla = pd.DataFrame({
    'Cancelaciones por día': frec_absoluta.index,           # xᵢ
    'Frecuencia Absoluta': frec_absoluta.values,            # fᵢ
    'Probabilidad Empírica': prob_empirica.values,          # pᵢ = fᵢ / N
    'Distribución Acumulada': dist_acumulada.values         # F(x) acumulada
})

# Mostrar la tabla por consola (en texto)
print(tabla)

# ------------------------------------------
# Mostrar la tabla como imagen con matplotlib
# ------------------------------------------
import matplotlib.pyplot as plt

# Crear figura y eje de dibujo
fig, ax = plt.subplots()

# Ocultar los ejes (ya que no se va a dibujar una gráfica, sino solo una tabla)
ax.axis('tight')
ax.axis('off')

# Crear una tabla visual dentro del gráfico usando los valores del DataFrame
tabla_matplotlib = ax.table(
    cellText=tabla.round(4).values,   # Se redondean los valores a 4 decimales para visualización clara
    colLabels=tabla.columns,          # Etiquetas de las columnas
    loc='center'                      # Posicionar la tabla en el centro
)

# Ajustar tamaño de fuente manualmente
tabla_matplotlib.auto_set_font_size(False)
tabla_matplotlib.set_fontsize(8)

# Escalar la tabla para que no se vea muy comprimida
tabla_matplotlib.scale(1.2, 1.2)

# Título de la tabla
plt.title("Tabla de Frecuencias y Distribuciones", pad=20)

# Mostrar la tabla como imagen
plt.show()

# ------------------------------------------
# 2. Cálculo de esperanza y varianza empíricas
# ------------------------------------------

# Obtener los valores posibles de cancelaciones (xᵢ)
valores_x = frec_absoluta.index

# Calcular la esperanza empírica (media)
# Se multiplica cada valor de cancelación xᵢ por su probabilidad pᵢ y se suman todos
# Esto representa el promedio ponderado de cancelaciones por día
esperanza = sum(valores_x * prob_empirica)

# Calcular la varianza empírica
# Se calcula la suma de pᵢ * (xᵢ - E[X])² para todos los valores
# Esto mide cuánto se desvían los datos respecto a la media
varianza = sum(prob_empirica * (valores_x - esperanza) ** 2)

# Mostrar los resultados finales por consola
print(f"Esperanza empírica (media): {esperanza:.4f}")
print(f"Varianza empírica: {varianza:.4f}")

# ------------------------------------------
# 3. Cálculo de mediana y el rango intercuartílico para la cantidad de cancelaciones diarias
# ------------------------------------------

# Extraer la serie de cancelaciones diarias
cancelaciones = df['cancelaciones']

# Calcular mediana
mediana = cancelaciones.median()

# Calcular primer cuartil (Q1) y tercer cuartil (Q3)
q1 = cancelaciones.quantile(0.25)
q3 = cancelaciones.quantile(0.75)

# Calcular rango intercuartílico (RIC = Q3 - Q1)
ric = q3 - q1

# Mostrar resultados
print(f"Mediana: {mediana}")
print(f"Primer cuartil (Q1): {q1}")
print(f"Tercer cuartil (Q3): {q3}")
print(f"Rango intercuartílico (RIC): {ric}")

# Crear diagrama de cajas (boxplot)
plt.figure(figsize=(6, 4))
plt.boxplot(cancelaciones, vert=False, patch_artist=True,
            boxprops=dict(facecolor="lightblue", color="blue"),
            medianprops=dict(color="red", linewidth=2))

plt.title("Diagrama de cajas - Cancelaciones diarias")
plt.xlabel("Cantidad de cancelaciones")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# ------------------------------------------
# 4. Histograma para la cantidad de cancelaciones diarias.
# ------------------------------------------

# Crear el histograma
plt.figure(figsize=(8,5))  # Tamaño de la figura (ancho x alto) en pulgadas

# plt.hist() crea el histograma:
# - cancelaciones: los datos que vamos a graficar
# - bins=10: número de "cubetas" o intervalos para agrupar los datos
# - color: color de las barras
# - edgecolor: color del borde de las barras para mejorar visualización
plt.hist(cancelaciones, bins=10, color='skyblue', edgecolor='black')

# Título del gráfico
plt.title('Histograma de Cancelaciones Diarias')

# Etiqueta eje X
plt.xlabel('Cantidad de cancelaciones')

# Etiqueta eje Y
plt.ylabel('Frecuencia (días)')

# Mostrar cuadrícula para facilitar lectura
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.show()