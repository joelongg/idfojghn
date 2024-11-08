from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time



browser = Options()
browser.add_argument("--headless")  # Включаем headless-режим
browser.add_argument("--disable-gpu")  # Отключаем использование GPU
browser.add_argument("--window-position=-10000,-10000")


driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="129.0.6668.89").install()), options=browser)