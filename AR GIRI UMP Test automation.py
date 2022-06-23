from selenium import webdriver
from selenium.webdriver.common.by import By

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
    
login()
