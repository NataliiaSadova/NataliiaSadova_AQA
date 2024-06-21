import pytest
from modules.ui.page_objects.w3s_try_python import W3sTryPython
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.mark.ui_w3s
def test_block_try_it_yourself():
    python_pract = W3sTryPython()
    python_pract.go_to()
    python_pract.try_practice("print('Try Python code for autotest')")


    assert python_pract.check_title("Python Tutorial")

    python_pract.close()

