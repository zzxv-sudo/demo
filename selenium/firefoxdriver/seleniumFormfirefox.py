import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import insta_pass

options = webdriver.FirefoxOptions()

options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0")

driver = webdriver.Firefox(
    executable_path='C:\\Users\\bass\\Desktop\\selenium\\firefoxdriver\\geckodriver.exe',
    options=options
)

try:
    driver.get("https://instagram.com/")
    time.sleep(5)

    username_input = driver.find_element_by_name('username')
    username_input.clear()
    username_input.send_keys("zzxvhcrat@gmail.com")
    time.sleep(4)

    pass_input = driver.find_element_by_name("password")
    pass_input.clear()
    pass_input.send_keys(insta_pass)
    time.sleep(2)

    pass_input.send_keys(Keys.ENTER)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()