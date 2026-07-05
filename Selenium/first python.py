from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.demoblaze.com/")

links=driver.find_elements(By.CLASS_NAME,"hrefch")
print(len(links))
