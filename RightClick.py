from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()


rc = driver.find_element(By.XPATH, "//span[text()='right click me']")

act = ActionChains(driver)
act.context_click(rc).perform()   # right click

 


