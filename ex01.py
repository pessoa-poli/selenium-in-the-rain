from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.firefox.options import Options

""" from shutil import which

FIREFOXPATH = which("firefox")
CHROMEPATH = which("chrome") """

firefox_options = Options()
firefox_options.add_argument('--headless')
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
#options.headless = True # also works

browser = webdriver.Firefox(executable_path="./drivers/geckodriver", options=firefox_options)

browser.get('https://git.camvoip.com.br/')
print(f'Browser windows title: {browser.title}')
dataElement = browser.find_element_by_id("post-4715.")
print(dataElement.text)
browser.quit()