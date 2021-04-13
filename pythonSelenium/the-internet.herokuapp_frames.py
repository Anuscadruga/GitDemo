from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")
#acsetea de mai sus nu vor functiona, pt ca e vb de frames, nu e vb de frames si desi identifica, da eroare
#cand vedem tag like Frames, iframes, frameset clar este vorba de frames si nhu pot fi handle with selenium
#driver.find_element_by_id("tinymce").clear() #setrgem textul din casuta
#driver.find_element_by_id("tinymce").send_keys("ana a scris aici")

driver.switch_to.frame("mce_0_ifr") #se identifica prin frame ID, name, index value
#iframe id "mce_0_ifr" am l;uta id ul de la tagname cu frame, de la intregul frame
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("ana a fost aici.... hahahahaha")

#daca in continuare vrem sa afisam ceva din afara frame ului, va trebui sa iesim din frame si sa afisam din afara
#ne intoarcem la defalupt content dupa ce am facut mdoificarile in frame

driver.switch_to.default_content() #dupa switch to mereu vine punct si se modifica manual
print(driver.find_element_by_xpath("//div[@class='example']/h3").text) #An iFrame containing the TinyMCE WYSIWYG Editor
