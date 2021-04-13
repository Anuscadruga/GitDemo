from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Anusca Druga")
driver.find_element_by_css_selector("input[name='email']").send_keys("anuscadruga@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@id='exampleInputPassword1']").send_keys("Anaaremere")
#"//input[@name='email']"
#tagname[attribute=`value`]
driver.find_element_by_css_selector("input[value='Submit']").click()
print(driver.find_element_by_class_name("alert-success").text) #Success! The Form has been submitted successfully!.
print(driver.find_element_by_css_selector("[class*='alert-success']").text) #Success! The Form has been submitted successfully!.
print(driver.find_element_by_xpath("//div[contains(@class,'alert-success')]").text) #Success! The Form has been submitted successfully!.
#STATIC DROPDOWNS
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_index(0) #male=0 si female=1 daca avem 2 optiuni, selectam in functie de index care porneste de la 0
#dropdown.select_by_index(1)
#dropdown.select_by_value(aici punem ce este in campul value corespunzator lui Male sau Female)
#dropdown.select_by_visible_text("Male")
dropdown.select_by_visible_text("Female")

#assert 2==3 #daca este false, testul va pica - AssertionError
message = driver.find_element_by_class_name("alert-success").text
assert "Success" in message #daca apare, arata ok si o sa mearga mai departe testul si va functiona i  continuare
#assert "Success! The Form has been submitted successfully!" == message

