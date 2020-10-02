import time 

# importing webdriver from selenium 
from selenium import webdriver 
path = "C:\Program Files\chromedriver.exe"
# Here Chrome will be used 
driver = webdriver.Chrome(path) 

# URL of website 
url = "https://accounts.google.com/AddSession?hl=en&continue=https://www.google.com%3Fhl%3Den-US"

# Opening the website 
driver.get(url) 

# geeting the button by class name 
om = '//*[@id="identifierNext"]/div/button/div[2]'
button = driver.find_elements_by_xpath(om)

# clicking on the button 
button.click()
