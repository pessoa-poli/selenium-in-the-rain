from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
browser.get("https://duckduckgo.com/")
searchInput = browser.find_element_by_id('search_form_input_homepage')
searchInput.send_keys('selenium hq' + Keys.ENTER)