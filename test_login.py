from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# as user input
print("Select login as :")
print("1 = user")
print("2 = buscompany")
print("3 = admin")
choice = input("Enter your choice (1/2/3): ")

phone = input("Enter phone number: ")
password = input("Enter password: ")
#user selection
login_map = {
    "1": "user",
    "2": "company",
    "3": "admin"
}

login_type = login_map.get(choice)
if not login_type:
    print("Invalid choice! Exiting.")
    exit()

# SELENIUM SETUP 
driver = webdriver.Chrome()
driver.get("http://localhost/Busticket/screens/login.php")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Select login type after selecect option
radio_xpath = f"//input[@name='login_type' and @value='{login_type}']"

login_radio = wait.until(
    EC.presence_of_element_located((By.XPATH, radio_xpath))
)
login_radio.click()

# Enter phonenum pass as input
wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(phone)
driver.find_element(By.NAME, "password").send_keys(password)

# Click login button auto
driver.find_element(By.CLASS_NAME, "login-btn").click()

time.sleep(2)#waiting time

#login failed or not msg
try:
    # Wait up to 5 sec
    driver.find_element(By.CLASS_NAME, "error-message")
    print("Login failed: Incorrect phone or password.")
except:
    print("Login successful!")

# Wait to see result
time.sleep(5)

driver.quit()
