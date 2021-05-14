import time
# from selenium import webdriver
from seleniumwire import webdriver
import random
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://vk.com"

user_agent_list = [
    "hello_world",
    "kekw",
    "wait a minet"
]

useragent = UserAgent()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=zzxv")
# options.add_argument(f'user-agent={random.choice(user_agent_list)}')
options.add_argument(f'user-agent={useragent.random}')

# set proxy
# options.add_argument("--proxy-server=айпи")
proxy_options = {
    "proxy": {
        "https": f"https://{login}:{password}@ipserver(132:32:.dad."
    }
}

# driver = webdriver.Chrome(
#     executable_path='C:\\Users\\bass\\Desktop\\selenium\\chromedriver\\chromedriver.exe',
#     options=options
# )
driver = webdriver.Chrome(
    executable_path='C:\\Users\\bass\\Desktop\\selenium\\chromedriver\\chromedriver.exe',
    seleniumwire_options=proxy_options
)
try:
    driver.get(url="https://2ip.ru/")
    time.sleep(3)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()