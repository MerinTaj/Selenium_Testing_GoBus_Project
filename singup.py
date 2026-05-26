import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#my terminal output for user input
print("Registration: ")
username = input("Enter Username: ")
email = input("Enter Email: ")
phone = input("Enter Phone Number (11 digits): ")
nid = input("Enter NID (10 digits): ")
password = input("Enter Password: ")
confirm_password = input("Enter Confirm Password: ")

#connect to database for registration update
def check_user_in_db(username):
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='gobus'
        )
        cursor = connection.cursor()
        sql = "SELECT * FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print(f"Database Error: {e}")
        return False
    finally:
        try:
            connection.close()
        except:
            pass

#selenium pp
driver = webdriver.Chrome()
driver.get("http://localhost/Busticket/screens/signup.php")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

#user input
wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.NAME, "phone").send_keys(phone)
driver.find_element(By.NAME, "nid").send_keys(nid)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.NAME, "confirm_password").send_keys(confirm_password)

#auto singup press
driver.find_element(By.CLASS_NAME, "signup-btn").click()
time.sleep(3)

#database matching
print("\nChecking database...")
time.sleep(2)

if check_user_in_db(username):
    print(f" Registration Success! User '{username}' inserted into database.")
else:
    print("Registration Failed! Check the registrationn rules")

# View results before closing
input("\nPress Enter to close browser")
driver.quit()
