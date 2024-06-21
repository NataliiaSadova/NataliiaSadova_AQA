from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class W3sTryPython(BasePage):
    URL = "https://www.w3schools.com/python/"

    def __init__(self)->None:
        super().__init__()

    def go_to(self):
        self.driver.get(W3sTryPython.URL)

    def try_practice(self, value):
    #Find button "Try it yourself>>"
        btn_element = self.driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/a') 
        btn_element.click()
        text_elem = self.driver.find_element(By.ID, "textareacontainer")
        text_elem.send_keys(value)
        scnd_btn_elem = self.driver.find_element(By.ID, "runbtn")
        scnd_btn_elem.click()
    def check_title(self, expected_title):
        return self.driver.title == expected_title