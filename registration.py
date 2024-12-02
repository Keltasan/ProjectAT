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
#Ссылка на учебный веб-проект
URL = "https://qa-course.netlify.app/registration-form-timer"
try:
 # Открытие веб-системы
 driver.get(URL)
 #Ввод имени
 name = driver.find_element(By.NAME,"firstName")
 name.send_keys("Artyom")
 #Ввод Фамилии
 last_name = driver.find_element(By.NAME, "lastName")
 last_name.send_keys("Podberyozskij")
 #Ввод города
 city = driver.find_element(By.NAME, "city")
 city.send_keys("Saint-Petersburg")
 #Отправка данных
 button = driver.find_element(By.CSS_SELECTOR,'button[type="submit"]')
 button.click()
 # Ждем некоторое время (в данном случае, 5 секунд)
 time.sleep(5)
except Exception as e:
 print(f"Произошла ошибка: {e}")
finally:
 # Закрытие браузера
 driver.quit()