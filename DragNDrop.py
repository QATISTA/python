import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.globalsqa.com/demo-site/draganddrop/#Propagation")
driver.maximize_window()
time.sleep(3)

iframe = driver.find_element(By.CSS_SELECTOR, "#post-2669 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > p > iframe")
driver.switch_to.frame(iframe)

source_ele1 = driver.find_element(By.XPATH, "//*[@id='draggable']")
#print(source_ele1)
time.sleep(3)

target_ele1 = driver.find_element(By.ID, "droppable")

act = ActionChains(driver)
act.drag_and_drop(source_ele1, target_ele1).perform()



