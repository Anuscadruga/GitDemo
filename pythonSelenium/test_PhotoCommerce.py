from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("[name='name']").send_keys("Anusca Druga")
driver.find_element_by_name("email").send_keys("anuscadruga@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("pass")
driver.find_element_by_id("exampleCheck1").click()
assert driver.find_element_by_id("exampleCheck1").is_selected()
sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
sel.select_by_visible_text("Female")
driver.find_element_by_xpath("//input[@value='Submit']").click()

alertText = driver.find_element_by_css_selector("[class*='alert-success']").text
assert "Success" in alertText