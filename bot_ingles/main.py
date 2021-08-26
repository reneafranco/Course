from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Instabot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver =webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(2)

Instabot('coding_python_tester', 'Rene2516')
