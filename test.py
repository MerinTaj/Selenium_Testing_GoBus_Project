from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open browser
driver = webdriver.Chrome()
driver.get("http://localhost/Busticket/index.php")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Enter From city
wait.until(EC.presence_of_element_located((By.ID, "from_city"))).send_keys("Dhaka")

# Enter To city
wait.until(EC.presence_of_element_located((By.ID, "to_city"))).send_keys("Chittagong")

# Enter date
wait.until(EC.presence_of_element_located((By.NAME, "date"))).send_keys("2025-12-10")

# Click Search button
driver.find_element(By.CLASS_NAME, "search-btn").click()

# Wait to see result
time.sleep(3)

# Close browser
driver.quit()
driver.find_element(By.NAME,"phone").send_keys("01885540942")
driver.find_element(By.NAME,"PASSWORD").send_keys("1010101010")
driver.find_element(By.CLASS_NAME,"signup_btn").click()
wait.until(EC.presence_of_all_elements_located)