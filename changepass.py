import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#database connection
def username_exists(new_username):
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='gobus'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (new_username,))
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
print("To change the password login first")

phone = input("Enter login phone number: ")
password = input("Enter login password: ")

print("\n Changing Details")
new_username = input("Enter new username (or press ENTER to skip): ")
current_pass = input("Enter current password: ")
new_pass = input("Enter new password: ")
confirm_pass = input("Confirm new password: ")

# SELENIUM LOGIN
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost/Busticket/screens/login.php")

wait = WebDriverWait(driver, 10)

# select user login type automatically
radio_xpath = "//input[@name='login_type' and @value='user']"
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

# change password option connect to user accounts
driver.get("http://localhost/Busticket/screens/userAccountSettings.php")
time.sleep(2)

# Username (only if user entered new)
if new_username.strip() != "":
    name_field = wait.until(EC.presence_of_element_located((By.NAME, "name")))
    name_field.clear()
    name_field.send_keys(new_username)

# Current Password
driver.find_element(By.NAME, "current_password").send_keys(current_pass)

# New Password
driver.find_element(By.NAME, "new_password").send_keys(new_pass)

# Confirm Password
driver.find_element(By.NAME, "confirm_password").send_keys(confirm_pass)

# Click Save
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(10)
#database check
if new_username.strip() != "":
    if username_exists(new_username):
        print(f"Account updated! Username changed to '{new_username}'.")
    else:
        print("Username update failed!")
else:
    print("Username unchanged.")

print("Failed,You have enter null value")

driver.quit()
