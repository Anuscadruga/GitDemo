from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://login.salesforce.com/")
#tagname#ID  - tagname optional
driver.find_element_by_css_selector("input#username").send_keys("ana-maria.radoi@finastra.com")
driver.find_element_by_css_selector("input.password").send_keys("password")
driver.find_element_by_css_selector("input.password").clear()
driver.find_element_by_css_selector(".password").send_keys("parola")
driver.find_element_by_link_text("Forgot Your Password?").click() #unde avem "a"- avem html cu linktext
#driver.find_element_by_partial_link_text("Forgot Your Passw").click()
#//tagname[text()=’xxx’]
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//div[@id='usernamegroup']/label").text)
print(driver.find_element_by_css_selector("div[id='usernamegroup'] label").text)
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_xpath("//div[@id='theloginform']/form/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(1)").text)
