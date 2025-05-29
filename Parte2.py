# Simulación de variable aleatoria uniforme continua en [0,1]
import time

a= 1664525
c = 1013904223
m = 2**32

semilla = int(time.time()*1000) % m

def generar_uniforme(): 
    global semilla
    semilla = (a * semilla + c) % m
    return semilla / m

# Generar una muestra de 100 variables uniformes
# Crear histograma y densidad

import matplotlib.pyplot as plt
import seaborn as sns

def muestra_uniforme():
    muestra = [generar_uniforme() for _ in range(100)]

    sns.histplot(muestra, bins=10, kde=True, stat='density', color='purple', edgecolor='black')
    plt.title('Uniforme [0,1]: Histograma y Densidad estimada')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()

    return muestra

#Demostración teórica de la transormada inversa
def transformada_inversa(): 
    """
    Si U ~ U[0,1] y F es estrictamente creciente, entonces: 
    X = F^(-1)(U) tiene distribución acumulada F

    Demostración: 
    P (X ≤ x) = P(F^(-1)(U) ≤ x) = P(U ≤ F(x)) 

    Por lo tanto, X ~ F
    """

    pass

#Algoritmo para generar variables con distribución Cauchy estándar
import math 
def generar_cauchy():
    u = generar_uniforme()
    return math.tan(math.pi * (u - 0.5))


# Generar muestra de Couchy + gráfico 
import numpy as np
from scipy.stats import cauchy

def muestra_cauchy():
    muestra = [generar_cauchy() for _ in range(100)]

    sns.histplot (muestra, kde= True, stat='density', color='orange', edgecolor='black', label= 'Densidad estimada')

    x_vals = np.linspace(-10, 10, 1000)
    plt.plt (x_vals, cauchy.pdf(x_vals), label="Densidad Cauchy Teórica"), color= "blue"

    plt.title("Cauchy estándar: Histograma, KDE y densidad teórica")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(True)
    plt.show()

    return muestra


#Para ejecutar: 
muestra_uniforme()
muestra_cauchy()
