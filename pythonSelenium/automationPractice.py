from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

buttons = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(buttons))

for button in buttons:
    if button.get_attribute("value") == "option2":
        button.click()
        assert button.is_selected()
        break

radioButtons = driver.find_elements_by_name("radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()

#handling Java/Javascripts allerts
message = "Option3"
driver.find_element_by_css_selector("#name").send_keys(message)
driver.find_element_by_id("alertbtn").click()
#si mai jos o sa ne ocupam de alerte, de la driver trecem la alert, care ne va ajuta sa ne ocupam de pop up
alert = driver.switch_to.alert
alertText = alert.text
#print(alert.text) #afiseaza alerta
assert message in alertText
alert.accept() #acceptam alerta, de obicei apare o fereastra care trebuie apasat pe ok
#alert.dismiss() #daca vrem sa dam cancel la alerta

#mouse hover - adiuca sa te duci cu mouseul undeva si sa iti arate ce ai pe casuta aia fara sa dai click
#de asemenea sunt si altele precum right clisk etc
# pt asta avem nevoie de importarea ActionChains pt a putea face diverse interactiuni cu casutele

action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover") #este casuta
action.move_to_element(menu).perform()  #adica se duce cursorul pe aceea casuta #neaparat sa aiba perfom la sf ca sa se execute
top = driver.find_element_by_link_text("Top")
action.move_to_element(top).click().perform() #neaparat perform la sf

#action.context_click(driver.find_element_by_id("dropdown-class-example")).perform() #va face right click
#action.double_click(driver.find_element_by_id("dropdown-class-example")).perform() #metoda double click mereu face 2 clickuri

print(driver.find_element_by_id("displayed-text").is_displayed()) #ne va spune daca ceva este afosat - True
assert driver.find_element_by_id("displayed-text").is_displayed() #pt ca aici vreau true
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
print(driver.find_element_by_id("displayed-text").is_displayed()) #false
driver.find_element_by_id("show-textbox").click()
print(driver.find_element_by_id("displayed-text").is_displayed())
assert driver.find_element_by_id("displayed-text").is_displayed()

