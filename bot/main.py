from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
from webdriver_manager.chrome import ChromeDriverManager


#2 declara una funcion que te permita ir a la pagina de instagram para iniciar secion
def login(browser):
    browser.get("https://www.instagram.com/?hl=es")
    time.sleep(2)
    #declara variables para el usuario y contraseña
    username = browser.find_element_by_css_selector("[name ='username']")
    password = browser.find_element_by_css_selector("[name ='password']")
    login    = browser.find_element_by_css_selector("button")

    username.send_keys("coding_python_tester")
    password.send_keys("Rene2516")
    login.click()

    time.sleep()
#1declara funcion principal 
def main():
    browser =  webdriver.Chrome(ChromeDriverManager().install())
    login(browser)

#3 instasia la funcion 
main()