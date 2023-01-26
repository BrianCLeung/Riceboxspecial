from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Opens chromedriver and opens Google maps on google chrome.
driver = webdriver.Chrome("chromedriver")
driver.get("https://www.google.com/maps")

# Find the search box by ID.
def search_place():
	place = driver.find_element("id","searchboxinput")
# Input destination in search box.	
	place.send_keys("narita international airport")
# Finds and clicks on the search button in the search box.
	submit = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
	submit.click()
# Finds and click the search result within the side column.
def tab1():
	time.sleep(5)
	direct = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[9]/div[5]/div[2]/div/div[1]/a")
	direct.click()
    
# Runs the provided functions.
search_place()	
tab1()

# Wait 5 seconds before switching back the first tab (Google Maps).
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
# Finds the search box, selects all text (Ctrl+A) then backspace/delete text.
def selectall():
	select = driver.find_element("id","searchboxinput")
	select.send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)

#runs the "Select all" function.
selectall()

def search_place2():
	place = driver.find_element("id","searchboxinput")
	place.send_keys("754 Tokiwacho, Shimogyo Ward, Kyoto, 600-8505, Japan")
	submit = driver.find_element("id", "searchbox-searchbutton")
	submit.click()

def tab2():
	time.sleep(5)
	direct = driver.find_element(By.XPATH, "/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[11]/div[6]/div[2]/div/div[1]/a")
	direct.click()    

search_place2()
tab2()


time.sleep(5)
driver.switch_to.window(driver.window_handles[0])