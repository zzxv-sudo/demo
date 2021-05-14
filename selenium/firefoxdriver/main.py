import time
# from selenium import webdriver
from seleniumwire import webdriver
from fake_useragent import UserAgent
from proxy_auth_data import login, password

# url = "https://vk.com"

useragent = UserAgent()
# options
options = webdriver.FirefoxOptions()


# change useragent
options.set_preference("general.useragent.override", useragent.random)

# set proxy
# без логина и пароля
# proxy = "ip adress"
# firefox_capabilites = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilites["marionette"] = True
#
# firefox_capabilites["proxy"] = {
#     "proxyType": "MANUAL",
#     "httpProxy": "proxy",
#     "ftpProxy": "proxy",
#     "sslProxy": "proxy"
# }
proxy_options = {
    "proxy": {
        "https": f"https://{login}:{password}@ipserver(132:32:.dad."
    }
}

# driver = webdriver.Firefox(
#     executable_path='C:\\Users\\bass\\Desktop\\selenium\\firefoxdriver\\geckodriver.exe',
#     options=options, proxy=proxy
# )
driver = webdriver.Firefox(
    executable_path='C:\\Users\\bass\\Desktop\\selenium\\firefoxdriver\\geckodriver.exe',
    seleniumwire_options=proxy_options
)
try:
    # driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    # time.sleep(3)
    driver.get(url="https://2ip.ru/")
    time.sleep(4)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()