#implicit wait - astea apartin de selenium
#explicit wait
#pause the test for few seconds using Time Class time.sleep(2) - asta apartine de python
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.implicitly_wait(5)
#asta spune asteapta 5 sec pana cand obiectul din drive este afisat
#este un global wait, asteapta de la 0 la 5 sec, se termina si mai repede, nu sta pana la 5 sec
#daca obiectul nu apare deloc, atunci testul asteapta 5 secunde
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
#acum dureaza ceva pana cand cauta
time.sleep(5)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
search = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for item in search:
    item.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
#driver.find_element_by_xpath("//div[@class='cart-preview active']/div[2]/button").click()
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
#aici va mai dura putin
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text) #Code applied ..!