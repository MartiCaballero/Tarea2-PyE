import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import cauchy


# Simulación de variable aleatoria uniforme continua en [0,1]
class UniformeGenerador:
    def __init__(self, semilla=123456789, a=1103515245, m=2**31):
        self.semilla = semilla
        self.a = a
        self.m = m
        self.estado = semilla

    def siguiente(self):
        self.estado = (self.a * self.estado) % self.m
        return self.estado / self.m
    

# Generar una muestra de 100 variables uniformes
# Crear histograma y densidad
def generar_muestra_uniforme(generador, n=100):
    return [generador.siguiente() for _ in range(n)]

def graficar_histograma_y_densidad_uniforme(muestra):
    plt.figure(figsize=(8, 5))
    sns.histplot(muestra, bins=10, kde=True, stat='density', color='skyblue')
    plt.title("Histograma + Densidad KDE de muestra U[0,1]")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.grid(True)
    plt.show()

#Teorema de la transformación inversa
#Se explica demostración teórica 


# Simulación de Cauchy estándar
# FX(t) = (1/pi) * arctan(t) + 1/2  => F^{-1}(u) = tan(pi(u - 0.5))

def inversa_cauchy(u):
    return np.tan(np.pi * (u - 0.5))


def generar_muestra_cauchy(muestra_uniforme):
    return [inversa_cauchy(u) for u in muestra_uniforme]



# Graficar muestra Cauchy
def graficar_histograma_y_densidad_cauchy(muestra):
    
    sns.histplot(muestra, bins=100, kde=True, stat="density", color="pink", edgecolor="black")
    
    x = np.linspace(-25, 25, 1000)
    y = cauchy.pdf(x)
    
    plt.plot(x, y, label="Densidad Cauchy estándar", color="blue")
    plt.title("Histograma y Densidad - Muestra Cauchy")
    plt.xlabel("Valor")
    plt.ylabel("Densidad")
    plt.xlim(-25, 25)
    plt.legend()
    plt.grid(True)
    plt.show()


#Ejecución del código

if __name__ == "__main__":
    # Parte 1: Inicializar generador
    generador = UniformeGenerador()

    # Parte 2: Muestra de 100 uniformes
    muestra_uniforme = generar_muestra_uniforme(generador, 100)
    graficar_histograma_y_densidad_uniforme(muestra_uniforme)

    # Parte 4-5: Simulación Cauchy
    muestra_cauchy = generar_muestra_cauchy(muestra_uniforme)
    graficar_histograma_y_densidad_cauchy(muestra_cauchy)