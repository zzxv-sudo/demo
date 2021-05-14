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
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys("+79615970613")
    time.sleep(5)

    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    password_input.send_keys(vk_pass)

    login_button = driver.find_element_by_id("index_login_button").click()
    time.sleep(4)

    news_link = driver.find_element_by_id("l_nwsf").click()
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()