from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
