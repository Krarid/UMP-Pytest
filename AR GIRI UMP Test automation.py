from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://ar-giri.rocks")

def login(username = "Demo", password = "0000"):

    # Locate username textfield
    usernameTextField = driver.find_element(By.XPATH, "//input[1]")

    # Send username
    usernameTextField.send_keys(username)

    # Locate password textfield
    passwordTextField = driver.find_element(By.XPATH, "//input[2]")

    # Send password
    passwordTextField.send_keys(password)

    # Locate login button
    loginButton = driver.find_element(By.XPATH, "//button")

    # Click on login button
    loginButton.click()

def createAccount(email = "javier.melendez@fyware.com"):

    # Locate email textfield
    emailTextField = driver.find_element(By.XPATH, "//input[@type='email']")

    # Send email
    emailTextField.send_keys(email)

    # Locate dropdowns: type of account and organization
    select = driver.find_elements(By.XPATH, "//select")

    # Select the type of account
    Select(select[0]).select_by_index(1)

    # Select the organization
    Select(select[1]).select_by_index(1)

    # Select Create button
    createButton = driver.find_element(By.XPATH, "//div/div/div[2]/div[5]/button")

    # Click on Create button
    createButton.click()

def searchAccount(email = "javier.melendez@fyware.com"):

    # Locate search textfield
    searchTextField = driver.find_element(By.XPATH, "//input[@id='Search']")

    # Send email
    searchTextField.send_keys(email + Keys.ENTER)

def resetPassword():
    # Locate trash button
    resetPasswordButton = driver.find_element(By.XPATH, "//div[@index=0]/div/div[4]/button")

    # Click on trash button
    resetPasswordButton.click()

    # Locate cancel button on pop up
    cancelButton = driver.find_element(By.XPATH, "//button[@data-dismiss='modal']")
    cancelButton.click()
    
login()
time.sleep(1)
createAccount()
time.sleep(1)
searchAccount()
time.sleep(2)
resetPassword()
