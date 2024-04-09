import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Cookies:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(5)

    def get_cookies_before_login(self):
        print("cookies before login")
        for cookies in (self.driver.get_cookies()):
            print(cookies)

    def get_cookies_after_login(self):
        print(" cookies after login")
        for cookies in (self.driver.get_cookies()):
            print(cookies)

    def logout(self):
        self.driver.find_element(By.XPATH,"//button[@id='react-burger-menu-btn']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()
        time.sleep(5)
        print("Logout: Success")

if __name__ == "__main__":
    cookie=Cookies("https://www.saucedemo.com/")
    cookie.start()
    cookie.get_cookies_before_login()
    cookie.get_cookies_after_login()
    cookie.logout()






