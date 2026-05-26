from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#login part
print("Select login as:")
print("1 = user")
print("2 = buscompany")
print("3 = admin")
choice = input("Enter your choice (1/2/3): ")

phone = input("Enter phone number: ")
password = input("Enter password: ")

login_map = {
    "1": "user",
    "2": "company",
    "3": "admin"
}

login_type = login_map.get(choice)
if not login_type:
    print("Invalid choice! Exiting.")
    exit()

driver = webdriver.Chrome()
driver.get("http://localhost/Busticket/screens/login.php")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

radio_xpath = f"//input[@name='login_type' and @value='{login_type}']"
login_radio = wait.until(
    EC.presence_of_element_located((By.XPATH, radio_xpath))
)
login_radio.click()

wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(phone)
driver.find_element(By.NAME, "password").send_keys(password)

driver.find_element(By.CLASS_NAME, "login-btn").click()

time.sleep(2)

try:
    driver.find_element(By.CLASS_NAME, "error-message")
    print("Login failed: Incorrect phone or password.")
    driver.quit()
    exit()
except:
    print("")

#logout part code
print("Logging out start")
#calling directly
driver.get("http://localhost/Busticket/screens/logout.php")

time.sleep(2)

if "login.php" in driver.current_url:
    print("Logout successful!")
else:
    print("Logout may have failed. Check browser.")
time.sleep(2)
driver.quit()
