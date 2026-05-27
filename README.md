# GoBus Selenium Test Automation

This repository contains Selenium-based automated test scripts for the **GoBus - Web-Based Bus E-Ticket Management System**.

## Prerequisites

Before running the test scripts, you must first set up the main GoBus project.

### Step 1: Download and Configure the Main Project

Download the main project repository:

https://github.com/MerinTaj/GoBus-Web-Based-Bus-E-Ticket-Management-System

Follow all setup instructions provided in that repository's README file to properly configure the project.

---

## Step 2: Start XAMPP Services

1. Open **XAMPP Control Panel**.
2. Start the following services:
   - Apache
   - MySQL

Make sure both services are running successfully before executing any Selenium test cases.

---

## Step 3: Install Required Python Packages

Open Terminal / Command Prompt in the Selenium testing project directory and install the required dependencies:

```bash
pip install selenium
```

If additional packages are required:

```bash
pip install -r requirements.txt
```

---

## Step 4: Run Test Cases

Navigate to the project directory:

```bash
cd SeleniumTests/BusticketTests
```

Run individual test scripts using:

```bash
python .\signup.py
```

Example:

```bash
python .\test_login.py
```

Other available test scripts:

```bash
python .\signup.py
python .\search.py
python .\ticket.py
python .\addpromo.py
python .\adminaddbus.py
python .\changepass.py
python .\logout.py
python .\test.py
python .\test_login.py
```

---

## Test Coverage

The automated test suite covers major functionalities of the GoBus system, including:

- User Registration
- User Login
- Bus Search
- Ticket Booking
- Admin Bus Management
- Promo Code Management
- Password Change
- Logout Functionality

---

## Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- XAMPP
- Apache
- MySQL

---

---

## Author

**Merin Taj**

American International University-Bangladesh (AIUB)

BSc in Computer Science and Engineering
