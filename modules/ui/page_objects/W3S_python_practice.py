from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class W3S_PYTHON(BasePage):
    URL = "https://www.w3schools.com/python/"

    def __init__(self)->None:
        super().__init__()

    def go_to(self):
        self.driver.get(W3S_PYTHON.URL)

    def try_practice(self):
    #Знаходимо кнопку "Try it yourself>>"
        btn_element = self.driver.find_element(By.XPATH, "//div[contains(text(), "Try it Yourself >>")]")
        #print(btn_element)
        btn_element.click()