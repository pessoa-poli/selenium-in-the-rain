from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ErrorInResponseException
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')

browser = webdriver.Firefox(executable_path="./drivers/geckodriver", options=firefox_options)
browser.get("some-url")
username = browser.find_element_by_id('username')
username.send_keys("myuser")
passwd = browser.find_element_by_id("password")
passwd.send_keys("mypass")
loginbtn = browser.find_element_by_id("login-submit")
loginbtn.click()
/#configuracoesBtn = browser.find_element_by_link_text("Configurações")
try:
    advancedbtn = browser.find_element_by_id("advancedButton")
    advancedbtn.click()
    exceptionbtn = browser.find_element_by_id("exceptionDialogButton")
    exceptionbtn.click()
except:
    pass
table_rows = browser.find_elements_by_css_selector("td[aria-describedby='dispositivo-table_sigla_instituicao']")

for row in table_rows:    
    print(row.text)    
    #sigla_column = row.find_element_by_css_selector("td[aria-describedby='dispositivo-table_sigla_instituicao']")
    #sigla_column = browser.find_element_by_xpath
    #print(sigla_column.text)

"""
fname.clear() 
fname.send_keys('Shahriar')
lname = browser.find_element_by_id('lname')
lname.clear()
lname.send_keys('Shovon')
submitButton = browser.find_element_by_css_selector('input[type="submit"]')
submitButton.send_keys(Keys.ENTER) """
browser.close()