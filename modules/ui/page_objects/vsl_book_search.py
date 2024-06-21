from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VslBookSearch(BasePage):
    URL = "https://starylev.com.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(VslBookSearch.URL)

    def enter_search_query(self, search_item):
        search_field = self.driver.find_element(By.XPATH, '//*[@id="__next"]/section/header/div[1]/div/div[2]/div[1]/input')
        search_field.click()
        search_query = self.driver.find_element(By.XPATH, '//*[@id="__next"]/section/header/div[1]/div/div[2]/div[1]/input')
        search_query.send_keys(search_item)
        search_btn = self.driver.find_element(By.XPATH, '//*[@id="__next"]/section/header/div[1]/div/div[2]/div[1]/button[1]')
        search_btn.click()

    def list_search_result(self):
        search_list = self.driver.find_element(By.XPATH, '//*[@id="__next"]/section/main/div/div[4]/div[1]/h5[1]/span')
        return search_list.get_attribute("value")
    
    def check_title(self, expected_title):
        return self.driver.title == expected_title