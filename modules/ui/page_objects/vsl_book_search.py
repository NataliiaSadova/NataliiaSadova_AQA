from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

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
        search_list = self.driver.find_elements(By.XPATH, '//*[@id="__next"]/section/main/div/div[5]/div[1]')
        return search_list()
    
    def empty_search_result(self, message):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,'lato-h2 semibold')))
        except TimeoutException:
            pass
        try:
            empty_search = self.driver.find_element(By.CLASS_NAME,"lato-h2 semibold")
            return empty_search.text == message
        except NoSuchElementException:
            pass