from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

print("Select login as :")
print("1 = user")
print("2 = buscompany")
print("3 = admin")
choice = input("Enter your choice (1/2/3): ")

phone = input("Enter phone number: ")
password = input("Enter password: ")

login_map = {"1": "user", "2": "company", "3": "admin"}
login_type = login_map.get(choice)
if not login_type:
    print("Invalid choice! Exiting.")
    exit()

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 12)

driver.get("http://localhost/Busticket/screens/login.php")
radio_xpath = f"//input[@name='login_type' and @value='{login_type}']"
wait.until(EC.presence_of_element_located((By.XPATH, radio_xpath))).click()

wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys(phone)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(2)

try:
    driver.find_element(By.CLASS_NAME, "error-message")
    print("Login failed")
    driver.quit()
    exit()
except:
    print("Login successful!")

search_url = (
    "http://localhost/Busticket/screens/searchBus.php"
    "?from=Dhaka&to=Barisal&journey_date=2025-12-30"
    "&travel_type=One+Way&return_date="
)
driver.get(search_url)

try:
    view_seat_btn = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "view-seat-btn"))
    )
    view_seat_btn.click()
    print("'View Seat' clicked!")
except:
    print("Could not click 'View Seat'")
    driver.quit()
    exit()

print("seat layout")
print("A1  A2  A3  A4")
print("B1  B2  B3  B4")
print("C1  C2  C3  C4")
print("D1  D2  D3  D4")
print("E1  E2  E3  E4")
print("F1  F2  F3  F4")
print("G1  G2  G3  G4")
print("H1  H2  H3  H4")


seat_to_select = input("Enter the seat you want to select: ").strip().upper()

try:
    
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "seat-layout")))
    time.sleep(2)  
    
    seat_found = False
    
    try:
        seat_btn = driver.find_element(By.XPATH, f"//div[@class='seat-layout']//div[contains(@class, 'seat') and text()='{seat_to_select}']")
        driver.execute_script("arguments[0].scrollIntoView(true);", seat_btn)
        time.sleep(1)
        seat_btn.click()
        print(f"Seat {seat_to_select} selected!")
        seat_found = True
    except:
        pass
    
    if not seat_found:
        try:
            seat_btn = driver.find_element(By.XPATH, f"//div[@class='seat-layout']//*[contains(@id, 'seat-{seat_to_select}') or contains(@class, 'seat-{seat_to_select.lower()}')]")
            driver.execute_script("arguments[0].scrollIntoView(true);", seat_btn)
            time.sleep(1)
            seat_btn.click()
            print(f"Seat {seat_to_select} selected!")
            seat_found = True
        except:
            pass
    
    if not seat_found:
        try:
            seat_btn = driver.find_element(By.XPATH, f"//*[text()='{seat_to_select}']")
            driver.execute_script("arguments[0].scrollIntoView(true);", seat_btn)
            time.sleep(1)
            seat_btn.click()
            print(f"Seat {seat_to_select} selected!")
            seat_found = True
        except:
            pass
    
    if not seat_found:
        print(f"Seat {seat_to_select} not found.")
        driver.quit()
        exit()
        
except Exception as e:
    print(f"Error selecting seat: {e}")
    driver.quit()
    exit()
try:
    phone_input = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter phone number' or contains(@placeholder, 'phone') or @name='phone']")
    ))
    phone_input.clear()
    phone_input.send_keys(phone)
    
except Exception as e:
    print(f"Could not find phone input field.")
 
    try:
        phone_input = driver.find_element(By.NAME, "phone_number")
        phone_input.clear()
        phone_input.send_keys(phone)
        print(f"Phone number entered (alternative): {phone}")
    except:
        try:
            phone_input = driver.find_element(By.ID, "phone_number")
            phone_input.clear()
            phone_input.send_keys(phone)
            print(f"Phone number entered (by ID): {phone}")
        except:
            print("Could not locate phone number field")
        
            driver.save_screenshot("phone_field_error.png")
promo_choice = input("\nDo you want to enter a promo code? (y/n): ").strip().lower()
if promo_choice == 'y':
    promo_code = input("Enter promo code: ").strip()
    try:
        promo_input = driver.find_element(
            By.XPATH, "//input[@placeholder='Enter promo code' or contains(@placeholder, 'promo') or @name='promo_code']"
        )
        promo_input.clear()
        promo_input.send_keys(promo_code)
        print(f"Promo code entered: {promo_code}")
        
        time.sleep(2)  
        try:
            alert = driver.switch_to.alert
            print(f"Error: {alert.text}")
            alert.accept()  
            driver.quit()
            exit()
        except:
            print("Invalid promo")
    except:
        print("Could not find promo code field.")
        driver.quit()
        exit()

try:
    proceed_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'Proceed') or contains(text(), 'Payment') or @type='submit']")
    ))
    
    driver.execute_script("arguments[0].scrollIntoView(true);", proceed_btn)
    time.sleep(1)

    proceed_btn.click()
    
    time.sleep(10)
    
    if "payment" in driver.current_url.lower() or "checkout" in driver.current_url.lower():
        print("Successfully redirected to payment page!")
    else:
        print(f"Current URL: {driver.current_url}")
        print("Payment unsuccessful")
        
except Exception as e:
    print(f"Error clicking 'Proceed to Payment': {e}")
driver.quit()
