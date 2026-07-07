from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Launch Browser
driver=webdriver.Chrome()
#Open Website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#Explicit wait until login button is clickable upto 10 secs
login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
#identify user name
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
#Identify password
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin")
#click login
login.click()
import time
time.sleep(3)

paragraphs = driver.find_elements(By.TAG_NAME, "p")

for p in paragraphs:
    print(p.text)
print(driver.title)
print(driver.current_url)
#Wait for error message
error_message= WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))
)
print(error_message.text)
#Assertion
assert error_message.text == "Invalid credentials"
#Close Browser
driver.quit()


