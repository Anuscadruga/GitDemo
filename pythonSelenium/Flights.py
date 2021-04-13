from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element_by_id("autosuggest").send_keys("ind")
#in timpul cautarii, poate dura mai mult si de aceea mai adaugam time.sleep
time.sleep(2)
#cand introducem ind vrem sa veroficam cate tari sunt in cautare si verofiocam lista pe care o vrem
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a") #aici returneaza nr de localitati iesite la cautare
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break #avem nevoie de break pt a inchide for atunci cand gasim ce avem nevoie

#selenium nu va putea sa citeasca ce este in casuta dupa ce completam cu india,
# #selenium citeste initial oinformatiile si apoi le mai citeste la refresh
#si cum dupa ce am pus india nu este niciun refresh, atunci nu putem sa citim din cazuta cu find element by class
#putem insa sa returnam valoarea
#print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"
#ce am scris acolo, va fi sub forma unui value