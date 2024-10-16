#DANIEL SEPULVEDA - U ANDES - 202022738
#ANÁLISIS DE DATOS


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos
file_path = 'productividad_limpia.csv'
data = pd.read_csv(file_path)

data = pd.get_dummies(data, columns=['quarter', 'department','day','team'], drop_first=True)

print(data.columns)

# Verificar el DataFrame actualizado
print(data.columns)

# Convertir la columna de fecha a formato datetime
data['date'] = pd.to_datetime(data['date'])
data['day_of_week'] = data['date'].dt.day_name()  # Agregar el día de la semana

# 1. Gráfico de barras para comparar productividad real vs objetivo por equipos
def plot_bar_productivity(data):
    data['team'] = data.filter(like='team_').idxmax(axis=1)
    team_prod = data.groupby('team').agg({'actual_productivity': 'mean', 'targeted_productivity': 'mean'})
    team_prod.plot(kind='bar', figsize=(10,6))
    plt.title('Productividad Real vs Objetivo por Equipo')
    plt.ylabel('Productividad')
    plt.show()

# 2. Boxplot para comparar la productividad real en diferentes equipos
def plot_boxplot_productivity(data):
    data['team'] = data.filter(like='team_').idxmax(axis=1)
    plt.figure(figsize=(10,6))
    sns.boxplot(x='team', y='actual_productivity', data=data)
    plt.title('Boxplot de Productividad Real por Equipo')
    plt.xticks(rotation=90)
    plt.show()

# 3. Gráficos de dispersión para relacionar variables con productividad real
def plot_scatter_variables(data):
    variables = ['over_time', 'incentive', 'idle_time', 'wip']
    for var in variables:
        plt.figure(figsize=(8,6))
        sns.scatterplot(x=var, y='actual_productivity', data=data)
        plt.title(f'Relación entre {var} y Productividad Real')
        plt.show()

# 4. Heatmap para mostrar correlaciones entre múltiples variables clave
def plot_extended_heatmap(data):
    plt.figure(figsize=(14,10))
    # Seleccionar solo las columnas numéricas
    numerical_cols = data.select_dtypes(include=[np.number])
    # Calcular la matriz de correlación
    corr_matrix = numerical_cols.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Mapa de Calor de Correlaciones entre Variables')
    plt.show()

# 5. Series de tiempo para analizar la productividad a lo largo del tiempo
def plot_time_series(data):
    data_time = data.groupby('date').agg({'actual_productivity': 'mean'}).reset_index()
    plt.figure(figsize=(10,6))
    sns.lineplot(x='date', y='actual_productivity', data=data_time)
    plt.title('Serie de Tiempo de la Productividad Real')
    plt.xticks(rotation=45)
    plt.show()

# 6. Gráfico de violín para ver la distribución de la productividad por equipo
def plot_violin_productivity(data):
    data['team'] = data.filter(like='team_').idxmax(axis=1)
    plt.figure(figsize=(10,6))
    sns.violinplot(x='team', y='actual_productivity', data=data)
    plt.title('Distribución de la Productividad Real por Equipo (Violin Plot)')
    plt.xticks(rotation=90)
    plt.show()

# 7. Boxplot comparando incentivos con la productividad real
def plot_boxplot_incentive_productivity(data):
    plt.figure(figsize=(10,6))
    sns.boxplot(x='incentive', y='actual_productivity', data=data)
    plt.title('Productividad Real por Nivel de Incentivos (Boxplot)')
    plt.show()

# 8. Boxplot comparando el número de trabajadores con la productividad real
def plot_boxplot_workers_productivity(data):
    plt.figure(figsize=(10,6))
    sns.boxplot(x='no_of_workers', y='actual_productivity', data=data)
    plt.title('Productividad Real por Número de Trabajadores (Boxplot)')
    plt.show()

# 9. Gráfico de barras para comparar productividad por día de la semana
def plot_bar_productivity_weekday(data):
    weekday_prod = data.groupby('day_of_week').agg({'actual_productivity': 'mean', 'targeted_productivity': 'mean'})
    weekday_prod.plot(kind='bar', figsize=(10,6))
    plt.title('Productividad Real vs Objetivo por Día de la Semana')
    plt.ylabel('Productividad')
    plt.show()

# Ejecutar las funciones
plot_bar_productivity(data)
plot_boxplot_productivity(data)
plot_scatter_variables(data)
plot_extended_heatmap(data)
plot_time_series(data)
plot_violin_productivity(data)
plot_boxplot_incentive_productivity(data)
plot_boxplot_workers_productivity(data)
plot_bar_productivity_weekday(data)
