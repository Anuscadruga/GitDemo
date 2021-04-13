from selenium import webdriver
#selenium de obicei cheama un fisier executabil si noi il invocam
#invocand fisierul,exe punand path ul lui, se va deschide ulterior browserul
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/#/index")
print(driver.title) #arata titlul pagini care arata numele paginii
print(driver.current_url) #arata daca am deschis URL care trebuie
#driver.close() #inchide browserul, insa doar fereastra curenta care s a deschis
#driver.quit() #face la fel ca close() insa daca la executare se deschid 2 ferestre, se vor inchide ambele

driver.get("https://www.rahulshettyacademy.com/#/consulting")
driver.back() #ne duce inapoi, cum am apasa back la browser
driver.refresh()
driver.maximize_window()
driver.minimize_window()
