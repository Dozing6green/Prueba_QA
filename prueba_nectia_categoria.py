#Se importan las librerias correspondientes necesarias para este caso.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


#Se crea el objeto webdriver indicando el nombre "driver" y se define de la siguiente manera indicando su ruta correspondiente.
#Cabe como nota descargar el driver correspondiente para la correcta ejecución. 
#Se solicita descargar el driver correspondiente a su navegador, revisar la versión correspondiente, lo pueden encontrar en https://chromedriver.chromium.org/home (chrome)
#https://github.com/mozilla/geckodriver/releases (Firefox)
#Para ejecutar webdriver en navegador Firefox insertar "NombreObjeto=webdriver.Firefox(executable_path='Ruta correspondiente donde se guardó el archivo webdriver dentro del ordenador')

driver=webdriver.Firefox(executable_path='C:\drivers\geckodriver.exe')  

#Se llama al objeto indicando la página correspondiente solicitada y se declaran variables referentes al tiempo de espera en el navegador.
driver.get("https://cms-qa.parauco.com/login")
driver.maximize_window 

t=2
t2=4
driver.implicitly_wait(t2)

#Se utiliza XPATH para llamar los selectores correspondientes transformados a relativos y extraídos del HTML de la página indicada.

bt_user_login=driver.find_element(By.XPATH,value="//input[contains(@id,'user')]")
bt_user_login.send_keys("prueba@parauco.com" + Keys.TAB + "Prueba.2022" + Keys.TAB + Keys.ENTER)

cb_pais=driver.find_element(By.XPATH,value="//div[@class='ant-select-selection__rendered']").click()
time.sleep(t)

lista_paises=driver.find_element(By.XPATH,value="//li[@role='option']")
time.sleep(t)
pais_seleccionar=driver.find_element(By.XPATH,value="//li[@role='option'][contains(.,'Colombia')]")
time.sleep(t)
pais_seleccionar.click()

#Se crea función para evitar errores mediante el proceso referente a la creación de categorías, ya que al crear una categoría con el mismo nombre no permite proceder por regla establecida.
 
def crear_categoria(nombre):
    modulo_mall=driver.find_element(By.XPATH,value="//a[@href='/cms/mall/154/categories/list']").click()
    time.sleep(t)

    bt_nueva_categoria=driver.find_element(By.XPATH,value="//button[contains(.,'Nuevo')]").click()
    time.sleep(t)
    nombre_categoria=driver.find_element(By.XPATH,value="//input[@placeholder='Nombre de Categoria']")
    nombre_categoria.send_keys(nombre + Keys.TAB + Keys.ENTER)
    time.sleep(t)
    
    #while para seleccionar un elemento opción categoría correctamente sin errores.
    while(True):
        k = random.choice([4,5,6,7,8])
        try:
            seleccionar_categoria=driver.find_element(By.XPATH,value=f"(//li[contains(@role,'option')])[{k}]").click()
            time.sleep(t)
            print(f'Se pudo para selector {k}')
            break
        except:
            print(f'No se pudo para selector {k}')
            continue

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(t)


    bt_guardar=driver.find_element(By.XPATH,value="//button[contains(.,'Guardar')]")
    bt_guardar.click()
    time.sleep(t)

#luego de ejecutar la función se pueden agregar nombres correspondientes para la creación de categorías sin errores*
#En este caso, como se solicita, se crea una sola categoría.

crear_categoria("Prueba Categoria 01")
time.sleep(t)

#Se guarda la categoría y se selecciona el botón usuario para el correcto cierre de sesión

bt_usuario=driver.find_element(By.XPATH,value="//span[@class='name___1Odvx']")
time.sleep(3)
bt_usuario.click()
time.sleep(t)

#Se solicita al driver tiempo de espera correspondiente dentro del objeto seleccionado, el cual está dentro del botón seleccionado anteriormente.
#El navegador espera el tiempo correspondiente, se cierra y finaliza su función correctamente.

WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH,"//span[contains(.,'logout')]"))
).click()

time.sleep(t2)
driver.close()