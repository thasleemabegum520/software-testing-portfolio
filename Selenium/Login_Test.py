from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.TAG_NAME, "button"))
)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
login.click()
curr_url=driver.current_url
print(driver.title)
print(curr_url)

Dashboard_heading = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.TAG_NAME, "h6"))
)
print(Dashboard_heading.text)
assert Dashboard_heading.text == "Dashboard"
driver.quit()
