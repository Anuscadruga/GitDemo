from selenium import webdriver
from selenium.webdriver.support.select import Select
#chrome options - sunt utilizate pt chrome si se utilizeaza cand se invoca browserul
chrome_options = webdriver.ChromeOptions()
#in chrome options add argument adaugam diferite optiuni care se gasesc pe net
#https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("headless") #adica nu apare deloc browserul cand rulam
#chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chrome_options)
#se mai adauga si asta, sa se ruleze options

driver.get("https://www.rahulshettyacademy.com/angularpractice/")

#javascrip executer
#https://www.w3schools.com/js/js_htmldom_document.asp
#inainte sa fie invetat HTML, toate informatiile de pe o pagina puteam fi citite utilizand JavaScript HTML DOM documnet:
#The HTML DOM document object is the owner of all other objects in your web page.
#prin java scrips DOM putem accesa toate obictele din pagina la fel cum face si selenium, insa poate sa faca mult mai multe
#selenium are o metoda sa execute codul javascript  prin el

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text) #printeaza blank #deci nu printaza nimic in consola pt ca nu putem sa avem accees la ce am introdus
#daca introduce ceva intr-o casuta prin selenium si apoi incercam sa afisam ce am introdus, nu afiseaza
print(driver.find_element_by_name("name").get_attribute("value")) #va afisam Hello
#chiar daca in HTML nu avem nimic definit cu value, prin metodat getatrribute ne va returna ce am introdus noi in consola
#get attribute is inheriutate from DOM
print(driver.execute_script('return document.getElementsByName("name")[0].value')) #aici scriem java scrips comands
#'return document.getElementsByName("name")[0].value' - asta e pur si simplu comanda de javascrip ca sa retunreze ce am pus in casuta
#document.getElementsByName("name")[0].value daca se ruleaza in consola de la pagina, va returna hello
#selenium nu are nicio legaturta de acesta data, nu est folosit

#click folosind JS
#cu java script putem sa facem in selenium lucruri pe care selenium nu le poate face
#folosind diver.execute_script() si folosind scripturi in JS putem sa facem diverse

shopbutton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopbutton) #comanbda asta inlocuieste click normal din selenium
#unde este shopbutton putem sa punem mao multe butoane si arguments[0] se duce la shopbutton1 si arguments[1] se duce la shopbutton2
#https://www.w3schools.com/jsref/met_win_scrollto.asp - detaliile se pot gasi usor la o cautare pe net
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
#cu selenium nu se poate face scroll.
#folosim doar java script
