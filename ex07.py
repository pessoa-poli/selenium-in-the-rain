from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path="./drivers/geckodriver")

browser.get("http://random-name-generator.info/")

nameList = browser.find_elements_by_css_selector('ol.nameList li')

for name in nameList:
  print(name.text)

browser.quit()