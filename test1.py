from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.discount-zone-tech.com/foot-massager/special-offer/?affid=25")

while('true'):
    pass