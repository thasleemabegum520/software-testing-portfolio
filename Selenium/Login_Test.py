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
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
#click login
login.click()
print(driver.title)
print(driver.current_url)
#Wait for dashboard
dashboard_heading = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h6"))
)
print(dashboard_heading.text)
#Assertion
assert dashboard_heading.text == "Dashboard"
#Close Browser
driver.quit()
