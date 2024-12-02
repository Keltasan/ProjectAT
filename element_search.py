from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

# Путь к исполняемому файлу chromedriver.exe
chrome_driver_path = 'chromedriver-win64/chromedriver.exe'
# Создание сервиса Chrome
chrome_service = ChromeService(executable_path=chrome_driver_path)
# Создание экземпляра браузера
driver = webdriver.Chrome(service=chrome_service)
#Ссылка на учебный веб-проект и номер варианта
URL = "https://qa-test-selectors.netlify.app/"
variant = 15
try:
 # Открытие веб-системы
 driver.get(URL)
 #Ожидание загрузки всех элементов страницы
 driver.implicitly_wait(10)
 #Нажатие кнопки варианта
 v_button = driver.find_elements(By.TAG_NAME, "button")[variant-1]
 v_button.click()
 #Поиск по тэгу
 elements_by_tag = driver.find_elements(By.TAG_NAME, "h1")
 print("With h1 tag:", len(elements_by_tag))
 #Поиск по имени
 elements_by_name = driver.find_elements(By.NAME, "almond-nut")
 print("With almond-nut name:", len(elements_by_name))
 #Поиск по классу
 elements_by_class = driver.find_elements(By.CLASS_NAME, "imageContainer")
 print("With imageContainer class:", len(elements_by_class))
 #Поиск по ID
 elements_by_ID = driver.find_elements(By.ID, "peanut")
 print("With peanut ID:", len(elements_by_ID))
 #Поиск по атрибуту
 elements_by_attribute = driver.find_elements(By.CSS_SELECTOR, '[data-type="nuts"]')
 print("With data-type nuts:", len(elements_by_attribute))
 # Ждем некоторое время (в данном случае, 5 секунд)
 time.sleep(5)
except Exception as e:
 print(f"Произошла ошибка: {e}")
finally:
 # Закрытие браузера
 driver.quit()