#https://the-internet.herokuapp.com/
#site destinayt automation practice
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
#HOW TO HANDLE CHILD WINDOWS - WINDOWS THAT ARE OPENED FROM ANOTHER WINDODW
#driver.find_element_by_link_text("Click Here").click()
driver.find_element_by_xpath("//div[@class='example']/a").click()
#in ambele cazuri de mai jos afidseaza gresit pt ca nu stie ca s a decchis o noua fereastra si inca ruleaza in fereatra initial deschisa
#de aceea vom introduce switch to winfow
#print(driver.find_element_by_xpath("//div[@class='example']/h3").text) #afiseaza Opening a new window si nu e bine ca in pagina arata new window
#print(driver.find_element_by_tag_name("h3").text) #afiseaza Opening a new window si nu e bine ca in pagina arata new window
childwindow = driver.window_handles[1] #[1] - este child and [0]- este parent
parent = driver.window_handles[0]
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text) #New Window
driver.close() #inchide child
driver.switch_to.window(parent)
print(driver.find_element_by_tag_name("h3").text) #Opening a new window