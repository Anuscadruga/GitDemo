
#explicit wait il chemam doar unde vrem sa asteptam
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
wait = WebDriverWait(driver, 20)
# se importa WebDriverWait
#se speciaifxa ca argumente obiectul, driverul care trebuie sa astepte si cate secunde

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
#acum dureaza ceva pana cand cauta
time.sleep(5)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
search = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#acum suntem deja la nivelul butonului cu xpath ul de mai sus
#//div[@class='product-action']/button/parent::div/parent::div/h4
#item deja are in el asta //div[@class='product-action']/button si trebuie doar sa mai adaugam sf /parent::div/parent::div/h4
groceries = []
for item in search:
    print(item.find_element_by_xpath("parent::div/parent::div/h4").text) #aici imi va itera prin toate denumirile care mereu trebuie sa aiba text
    groceries.append(item.find_element_by_xpath("parent::div/parent::div/h4").text)
    print(groceries) #['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
    item.click() #aici face click pe button
#//div[@class='product-action']/button
#se poate traversa si de la copil la parinte si apoi la parintele parintelui ca mai apoi sa merge la un copil
#se poate merge in sus, si apoi duce in jos
# de ex suntem la un button si indicam un xpath pt acesta si de la acesta putem sa mergem in sus
#[//div[@class='product-action']/button] / [spunem ca vrem sa ne ducem la parinte cu parent, adica mai sus] :: tagname / parent::div/h4 ( cu h4 ma duc in jos)
#//div[@class='product-action']/button/parent::div/parent::div/h4
driver.find_element_by_css_selector("img[alt='Cart']").click()
#driver.find_element_by_xpath("//div[@class='cart-preview active']/div[2]/button").click()
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
#aici va mai dura putin
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@class='promoCode']")))
#se importa si expected_conditions
#se selecteaza presence_of_element_located daca vrem sa asteptam pana apare elementul nostru
#in paranteza By. se importa
#dupa By. putem importa dupa css, name etc
#specificam cum vrem si apoi ce anume asteptam
originalAmount = float(driver.find_element_by_css_selector(".discountAmt").text)
print(originalAmount)
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text) #Code applied ..!

cart = driver.find_elements_by_css_selector(".product-name")
cartList= []
for item in cart:
    print(item.text)
    cartList.append(item.text)
    print(cartList)

assert groceries == cartList

discountetAmount = float(driver.find_element_by_css_selector(".discountAmt").text)
print(discountetAmount)
assert discountetAmount < originalAmount

values = driver.find_elements_by_xpath("//tr/td[5]/p")
totalAmount = 0
for value in values:
    totalAmount = totalAmount+ int(value.text)

print(totalAmount)

assert originalAmount == totalAmount

#de incercat
#cautam altceva si verofocam daca elementele afisate match ce avem in cos
#verofocam daca face searcj corect si sa verificam cu lista noastra