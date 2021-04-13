import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
#driver.implicitly_wait(10)
wait = WebDriverWait(driver, 20)

driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    print(product.find_element_by_xpath("div/h4").text)
    product_name = product.find_element_by_xpath("div/h4").text
    if product_name == "Blackberry":
        product.find_element_by_xpath("div[2]/button").click()

#driver.find_element_by_xpath("//li[@class='nav-item active']/a").click()
#driver.find_element_by_css_selector("a[class*='btn-primary']").click() - nu merge, posibil sa nu putem sa facem prin selenium
#comanda de mai sus nu mergea prin selenium, asa ca am facut prin java script

checkoutbutton = driver.find_element_by_css_selector("a[class*='btn-primary']")
driver.execute_script("arguments[0].click();", checkoutbutton)

#aici de exersat cum se verofica textul daca este acelasi din cart

cart_product = driver.find_element_by_xpath("//h4[@class='media-heading']/a").text
print(cart_product)

assert product_name == cart_product

driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
#aici punem un wait
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
agreebutton = driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']")
#assert agreebutton.is_selected() in acest caz nu merge pt ca nu este bine construit buttonul in html
driver.find_element_by_css_selector("input[type='submit']").click()

assert "Success" in driver.find_element_by_class_name("alert-success").text
driver.get_screenshot_as_file("screenshot.png") #se creaza un fisier aici cu screenshot si chiar face o poza cu contentul