import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ------------------------------------------
# DATABASE CHECK (Verify Promo Code Added)
# ------------------------------------------
def promo_exists(promo_code):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='gobus'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM promo_codes WHERE promo_code=%s", (promo_code,))
        return cursor.fetchone() is not None
    except Exception as e:
        print("DB Error:", e)
        return False
    finally:
        try:
            conn.close()
        except:
            pass


# ------------------------------------------
# USER INPUT
# ------------------------------------------
print("Login Required to Add Promo Code")

admin_phone = input("Enter admin phone number: ")
admin_password = input("Enter admin password: ")

print("\nAdd New Promo Code")
promo_code = input("Enter promo code (e.g., GOBUS15): ")
discount_value = input("Enter discount value (e.g., 10/15/200): ")
discount_type = input("Enter discount type (percent/fixed): ")
expiry = input("Enter expiry date (YYYY-MM-DD): ")

# ------------------------------------------
# SELENIUM AUTOMATION
# ------------------------------------------
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/Busticket/screens/login.php")

wait = WebDriverWait(driver, 10)

# Select login type: Admin
radio_xpath = "//input[@name='login_type' and @value='admin']"
wait.until(EC.presence_of_element_located((By.XPATH, radio_xpath))).click()

# Enter Credentials
wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(admin_phone)
driver.find_element(By.NAME, "password").send_keys(admin_password)

# Login button
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(3)

# Check login error
try:
    driver.find_element(By.CLASS_NAME, "error-message")
    print("Login failed — wrong credentials.")
    driver.quit()
    exit()
except:
    print("Login successful!")

# Open Admin Dashboard
driver.get("http://localhost/Busticket/screens/admin_dashboard.php")
time.sleep(2)

# Open Promo Code Management
driver.find_element(By.XPATH, "//a[@data-section='promo_section']").click()
time.sleep(2)

# ------------------------------------------
# Fill Promo Code Form
# ------------------------------------------
wait.until(EC.presence_of_element_located((By.ID, "promo-code"))).send_keys(promo_code)
driver.find_element(By.ID, "discount-value").send_keys(discount_value)
driver.find_element(By.ID, "discount-type").send_keys(discount_type)
driver.find_element(By.ID, "expiry-date").send_keys(expiry)

# Submit Button
driver.find_element(By.XPATH, "//button[@name='add_promo']").click()

time.sleep(5)

if promo_exists(promo_code):
    print(f"Promo Code '{promo_code}' added successfully!")
else:
    print("Promo Code addition failed!")

driver.quit()
