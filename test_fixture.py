import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None
@pytest.fixture
def setup():    
    print("Start Browser")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield
    driver.quit()
    print("Close Browser")
    
def test_test_1(setup):    
    driver.get('https://itera-qa.azurewebsites.net/home/automation')
    print("Test_1 is executed")
    
def test_test_2(setup):
    driver.get('https://google.com/')
    print("Test_2 is executed")
    
def test_test_3(setup):
    driver.get('https://gmail.com/')
    print("Test_3 is executed")


