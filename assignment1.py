# 1) Open Web Browser
# 2) Open URL https://letcode.in/
# 3) Enter Username (test121@test.com)
# 4) Enter Password  (123456)
# 5) Click on Login.
# 6) Capture title of home page. (Actual Title)
# 7) Verify title of the page: LetCode with Koushik  (Expected)
# 8) Close browser


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:\TISTA\SELENIUM\YT\chromedriver\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://letcode.in/")
driver.find_element(By.XPATH, "//a[@href='/signin']").click()

driver.find_element(By.NAME, "email").send_keys("test121@test.com")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.XPATH, "//button[text()='LOGIN']").click()

a = driver.title
expected_title = "LetCode with Koushik"

if (a==expected_title) :
    print("PASS")
else :
    print("FAIL")

while("true"):
    pass