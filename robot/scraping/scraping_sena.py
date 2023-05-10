
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service


s = Service("C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=s)

url = 'https://sena.territorio.la/index.php?login=true'
driver.get(url)

user='1095910391'
passwd='1095910391'

time.sleep(2)
input_user=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/form/table/tbody/tr[5]/td/input')
input_user.send_keys(user)
input_passwd=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/form/table/tbody/tr[7]/td/label/input')
input_passwd.send_keys(passwd)

time.sleep(2)
boton = driver.find_element(By.XPATH,'//*[@id="ingresar"]')
boton.click()

time.sleep(3)
closed = driver.find_element(By.XPATH,'//*[@id="cierra"]')
closed.click()


time.sleep(8)
course = driver.find_element(By.XPATH,'/html/body/div[12]/div/div[2]/div[1]/div[3]/div[2]/ul/li[1]/div/div[2]/span[1]/div/a')
course.click()

time.sleep(2)
evidencia = driver.find_element(By.XPATH,'/html/body/div[15]/table[1]/tbody/tr/td[1]/div/ul/li/ul/li[7]/a')
evidencia.click()

time.sleep(10)
# Definir una lista de opciones
opciones = [7,8,9,10]  # Agregar más opciones si es necesario
resultados = {}
time.sleep(4)
# Iterar sobre las opciones
for opcion in opciones:
    time.sleep(4)
    # Seleccionar la opción
    select = driver.find_element(By.XPATH, f'//*[@id="idpondeMenu"]/option[{opcion}]')
    select.click()
    fase = select.text
    time.sleep(2)
    # Obtener el número de filas
    filas = driver.find_elements(By.XPATH, '/html/body/div[15]/table[1]/tbody/tr/td[2]/div[3]/div[3]/div[1]/div[4]/div/table/tbody/tr')
    time.sleep(3)
    # Iterar sobre las filas
    for i in range(1, len(filas) + 1):
        time.sleep(4)
        titulo = driver.find_element(By.XPATH, f'/html/body/div[15]/table[1]/tbody/tr/td[2]/div[3]/div[3]/div[1]/div[4]/div[{i}]/table/tbody/tr/td[1]/a').text
        time.sleep(2)
        calificacion = driver.find_element(By.XPATH, f'/html/body/div[15]/table[1]/tbody/tr/td[2]/div[3]/div[3]/div[1]/div[4]/div[{i}]/table/tbody/tr/td[4]').text
        time.sleep(2)
        entrega = driver.find_element(By.XPATH, f'/html/body/div[15]/table[1]/tbody/tr/td[2]/div[3]/div[3]/div[1]/div[4]/div[{i}]/table/tbody/tr/td[5]/strong').text
        time.sleep(2)
        resultados[titulo] = (calificacion, entrega, fase)

time.sleep(4)
driver.quit()

import pandas as pd

datos = pd.DataFrame.from_dict(resultados, orient='index', columns=['Calificacion', 'Entrega', 'Fase'])
datos.index.name = 'Titulo'
datos.reset_index(inplace=True)


df = datos
# Usamos la función str.replace para eliminar la subcadena antes de "Fase"
df['Fase'] = df['Fase'].str.replace(r'.*Fase', 'Fase')


# agregar columnas nuevas para el título corto y el código GA
df['Tarea'] = ''
df['Evidencia'] = ''

for i in range(len(df)):
    if pd.isna(df.loc[i, 'Titulo']):
        continue # saltar la iteración si el valor es NaN
    # verificar si el indicador "GA" está presente en el texto
    if 'GA' in df.loc[i, 'Titulo']:
        # separar el texto antes del indicador "GA"
        titulo_corto, codigo_ga = df.loc[i, 'Titulo'].split('GA')
        df.loc[i, 'Tarea'] = titulo_corto.strip()
        df.loc[i, 'Evidencia'] = 'GA' + codigo_ga.strip()
    else:
        # si el indicador "GA" no está presente, copiar todo el texto en "Titulo_corto"
        df.loc[i, 'Tarea'] = df.loc[i, 'Titulo']


evidencia = df.loc[:, ['Tarea', 'Evidencia', 'Calificacion','Entrega','Fase']]

import psycopg2

# Conectar a la base de datos
conn = psycopg2.connect(
    host="127.0.0.1",
    database="pcl",
    user="postgres",
    password="123456"
)

# Abrir un cursor
cur = conn.cursor()

# Ejecutar un TRUNCATE en la tabla para limpiarla
cur.execute("TRUNCATE adso.scraping_web")

# Iterar sobre las filas del dataframe y guardar los datos en la base de datos
for index, row in evidencia.iterrows():
    tarea = row['Tarea']
    evidencia = row['Evidencia']
    calificacion = row['Calificacion']
    entrega = row['Entrega']
    fase = row['Fase']
    query = f"INSERT INTO adso.scraping_web (Tarea, Evidencia, Calificacion, Entrega, Fase) VALUES ('{tarea}', '{evidencia}', '{calificacion}', '{entrega}', '{fase}')"
    cur.execute(query)

# Guardar los cambios y cerrar la conexión
conn.commit()
cur.close()
conn.close()
