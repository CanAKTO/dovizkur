from selenium import webdriver
#import time
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()
driver.minimize_window()

website=driver.get("https://www.tcmb.gov.tr/wps/wcm/connect/tr/tcmb+tr/main+page+site+area/bugun")
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"sub-home-content2")))
doviz=driver.find_element(By.CLASS_NAME,"sub-home-content2")
doviz_list = doviz.text.splitlines()
with open("gunluk.txt", "w") as dosya:
    for i in doviz_list:
        dosya.write(i +"\n")
driver.close()


