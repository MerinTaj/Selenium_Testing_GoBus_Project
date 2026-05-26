import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# database connection to check if company exists
def company_exists(company_name, phone):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='gobus'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bus_companies WHERE company_name=%s OR phone=%s", (company_name, phone))
        return cursor.fetchone() is not None
    except Exception as e:
        print("DB Error:", e)
        return False
    finally:
        try:
            conn.close()
        except:
            pass

# user input for login first
print("To add bus company, login first")

phone = input("Enter admin phone number: ")
password = input("Enter admin password: ")

print("\nAdding New Bus Company")
company_name = input("Enter company name: ")
company_phone = input("Enter company phone (11 digits): ")
company_pass = input("Enter company password: ")
confirm_pass = input("Confirm company password: ")

# SELENIUM LOGIN
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/Busticket/screens/login.php")

wait = WebDriverWait(driver, 10)

# select admin login type automatically
radio_xpath = "//input[@name='login_type' and @value='admin']"
wait.until(EC.presence_of_element_located((By.XPATH, radio_xpath))).click()

# enter credentials
wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(phone)
driver.find_element(By.NAME, "password").send_keys(password)

# click login button
driver.find_element(By.CLASS_NAME, "login-btn").click()

time.sleep(5)

# login error check
try:
    driver.find_element(By.CLASS_NAME, "error-message")
    print("Login failed: Wrong phone or password.")
    driver.quit()
    exit()
except:
    print("Login successful!")

# go to admin dashboard
driver.get("http://localhost/Busticket/screens/admin_dashboard.php")
time.sleep(2)

# click bus companies section
driver.find_element(By.XPATH, "//a[@data-section='bus_companies']").click()
time.sleep(2)

# Fill company form
driver.find_element(By.ID, "company-name").send_keys(company_name)
driver.find_element(By.ID, "phone").send_keys(company_phone)
driver.find_element(By.ID, "password").send_keys(company_pass)
driver.find_element(By.ID, "confirm-password").send_keys(confirm_pass)

# Click add company button
driver.find_element(By.XPATH, "//button[@name='add_company']").click()

time.sleep(10)

# database check
if company_exists(company_name, company_phone):
    print(f"Company '{company_name}' added successfully!")
else:
    print("Company addition failed!")

driver.quit()