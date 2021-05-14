import time
from selenium import webdriver
from auth_data import vk_pass

# options
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0")

driver = webdriver.Chrome(
    executable_path='C:\\Users\\bass\\Desktop\\selenium\\chromedriver\\chromedriver.exe',
    options=options
)

try:
    driver.get(url="https://music.yandex.ru/home")
    time.sleep(50)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()