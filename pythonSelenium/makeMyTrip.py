from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.find_element_by_id("fromCity").send_keys("Del")
time.sleep(4)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
for city in cities:
    city.text == "Delhi, India"
    city.click()
    break
