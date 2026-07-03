import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

print("1.- Demostración de carga y lectura de datos")

dataset = pd.read_csv("automovil_dataset.csv") # Dataset de los automóviles

print(dataset.head()) # Primeras 5 filas del dataset

print(dataset.info()) # Información de las columnas y su tipo de dato respectivo

print("Filas y columnas: ", dataset.shape) # Cantidad de filas y columnas

# Regresión lineal múltiple (ya que esta cosa tiene muchas variables independientes, y solo el 
# precio depende de los demás)
print("2.- Regresión lineal múltiple")

variables_independientes = ["horsepower", "age", "mileage", "engine_size"]

variable_dependiente = "price"

x = dataset[variables_independientes]
y = dataset[variable_dependiente]

x_entr, x_prueba, y_entr, y_prueba = train_test_split(x, y, test_size=0.2, random_state=42)

modelo = LinearRegression() # Se construye el objeto de regresión lineal
modelo.fit(x_entr, y_entr)

y_predicho = modelo.predict(x_prueba)

# --Métricas de confianza del modelo--
print("R² =", r2_score(y_prueba, y_predicho)) # Si el R² es cercano a cero, entonces el
# modelo utilizado no me sirve para predecir un nuevo precio
print("MAE =", mean_absolute_error(y_prueba, y_predicho)) # Error absoluto medio
print("MSE =", mean_squared_error(y_prueba, y_predicho)) # Error cuadrático medio
print("RMSE =", np.sqrt(mean_squared_error(y_prueba, y_predicho))) # Raíz del ECM

# -------- Gráfico --------
plt.figure(figsize=(8, 6))

sns.scatterplot(x=y_prueba, y=y_predicho, alpha=0.7, color="green", label="Predicho")# Me gusta el verde

maximo_valor = max(max(y_prueba), max(y_predicho))
minimo_valor = min(min(y_prueba), min(y_predicho))
plt.plot([minimo_valor, maximo_valor], [minimo_valor, maximo_valor], color="red", linestyle="--", 
         linewidth=2, label="Línea de referencia")

plt.title("Gráfico de Regresión Lineal Múltiple", fontsize=14)
plt.xlabel("Valores reales", fontsize=14)
plt.ylabel("Valores predichos", fontsize=14)
plt.legend()
plt.grid(True, linestyle=":", alpha=0.6)

plt.show()

# Predicción de nuevo valor (no será representativo porque R2 es muy bajo))
print("3.- Predicción de un nuevo valor para un auto nuevo")

nuevo_auto = np.array([[165, 4, 58000, 2.0]])
resultado = modelo.predict(nuevo_auto)

print("El precio estimado del nuevo auto, basado en este modelo, es de $" + str(resultado))