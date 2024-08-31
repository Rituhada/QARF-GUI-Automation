import pytest
from selenium import webdriver
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    time.sleep(2)
