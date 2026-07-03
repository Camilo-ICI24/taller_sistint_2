# Modelo de Regresión Lineal Múltiple para Predicción de Precio de Automóviles

Un modelo básico para predecir el valor de un nuevo vehículo basado en un dataset de autos.

## Tabla de contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Comentarios finales](#comentarios-finales)

## Descripción

Dado un dataset de automóviles vendidos, cuya información esencial contiene los caballos de fuerza, el kilometraje, la antigüedad, la cilindrada del motor y su precio de venta, se diseñó un modelo sencillo capaz de predecir el valor de un nuevo vehículo ingresando variables nuevas.

Para ellos, se tomó el dataset original (`automovil_dataset.csv`) para que el modelo pudiera leer la información dentro. Posteriormente, se hizo una división de los datos contenidos, formando una parte dedicada al entrenamiento del modelo, y otra destinada para pruebas, con el objetivo de desarrollar una herramienta confiable para la predicción de valores de vehículos nuevos.

Dado que lo que se buscaba predecir era el precio de un auto nuevo, se determinó que los demás datos (caballos de fuerza, kilometraje, cilindrada y antigüedad del vehículo) correspondían a las variables independientes, mientras que el parámetro a predecir se definió como el dependiente. A partir de esto, el modelo fue entrenado para construir una regresión lineal múltiple basado en la información histórica contenida en el dataset.

Adicionalmente, por transparencia, se calcularon métricas fundamentales para evaluar la confiabilidad del modelo utilizado. Sin embargo, una lectura fundamental como el R² arrojó un valor muy cercano a cero, por lo que se concluyó que el modelo utilizado y entrenado para predecir nuevos valores no es confiable para tal propósito.

## Instalación

Instrucciones para preparar el entorno y ejecutar el proyecto:

```bash
# Clonar el repositorio
git clone https://github.com/Camilo-ICI24/taller_sistint_2.git
cd taller_sistint_2

# Crear ambiente virtual. Se recomienda mantener el nombre original ya que es el mismo donde el modelo se desarrolló.
python -m venv taller2
source taller2/bin/activate

# Instalar dependencias
pip install -r requirements.txt

```

## Uso

Para ejecutar el modelo de regresión lineal múltiple:

```bash
python taller_sistint.py
```

En el segundo inciso, se abrirá una ventana emergente conteniendo el gráfico visual de regresión lineal múltiple y la ejecución en segundo plano se detendrá. Si se cierra la ventana con el gráfico, la consola imprimirá el resultado del último ejercicio antes de detenerse.

## Comentarios finales
Dentro de la estructura del proyecto se encontrará tanto el código fuente utilizado para el desarrollo de este taller, así como el dataset analizado y el PDF con las respuestas en base a los resultados obtenidos tras la ejecución del archivo Python.