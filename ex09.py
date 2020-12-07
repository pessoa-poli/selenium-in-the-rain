from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
browser.get("https://www.w3schools.com/html/html_forms.asp")
fname = browser.find_element_by_id('fname')
fname.clear()
fname.send_keys('Shahriar')
lname = browser.find_element_by_id('lname')
lname.clear()
lname.send_keys('Shovon')
submitButton = browser.find_element_by_css_selector('input[type="submit"]')
submitButton.send_keys(Keys.ENTER)