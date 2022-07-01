from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
import time

#Bypass "Your connection is not private"
options = webdriver.ChromeOptions()
options.add_argument('--allow-insecure-localhost') # differ on driver version. can ignore. 
caps = options.to_capabilities()
caps["acceptInsecureCerts"] = True
driver = webdriver.Chrome(desired_capabilities=caps)

driver.get("https://35.219.183.240/")

def login(username = "iconsAdmin", password = "0000"):

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

def createAccount(email = "javier.melendez@fyware.com", typeAccount="manager"):

    # Locate email textfield
    emailTextField = driver.find_element(By.XPATH, "//input[@type='email']")

    # Send email
    emailTextField.send_keys(email)

    # Locate dropdowns: type of account and organization
    select = driver.find_elements(By.XPATH, "//select")

    # Select the type of account
    Select(select[0]).select_by_value("manager")

    time.sleep(1)

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
    # Locate reset button
    resetPasswordButton = driver.find_element(By.XPATH, "//div[@index=0]/div/div[4]/button")

    # Click on reset button
    resetPasswordButton.click()

    # Locate cancel button on pop up
    cancelButton = driver.find_element(By.XPATH, "//button[@data-dismiss='modal']")
    cancelButton.click()

def deleteAccount():
    # Locate trash button
    trashButton = driver.find_element(By.XPATH, "//div[@index=0]/div/div[5]/button")

    # Click on trash button
    trashButton.click()

def organizationManagement():
    # Locate Organization Management tab
    organizationManagement = driver.find_element(By.XPATH, "//a[contains(text(), 'Organization Management')]")

    # Click on organization management
    organizationManagement.click()

def createOrganization(organization = "Test", domain = "test.com"):
    # Locate organization textfield
    organizationTextField = driver.find_element(By.XPATH, "//input[@id='orgName']")

    # Send organization
    organizationTextField.send_keys(organization)

    # Locate domain textfield
    domainTextField = driver.find_element(By.XPATH, "//input[@id='orgDomain']")

    # Send domain
    domainTextField.send_keys(domain)

    # Locate button to create organization
    createOrganization = driver.find_element(By.XPATH, "//button[@id='CreateDomainBtn']")

    # Click on create organization
    createOrganization.click()

    time.sleep(1)
    
    # Locate Ok button on pop up
    okButton = driver.find_element(By.XPATH, "//button[@data-dismiss='modal']")
    okButton.click()

def addWorkplaces():

    # Locate button to add 10 workplaces
    addWorkplaceButton = driver.find_elements(By.XPATH, "//div/div[4]/div/button")

    last = len(addWorkplaceButton) - 1

    addWorkplaceButton[last].click()

    # Click on button to add 10 workplaces
    # addWorkplaceButton.click()

    time.sleep(1)

    # Locate Ok button on pop up
    okButton = driver.find_element(By.XPATH, "//button[@data-dismiss='modal']")
    okButton.click()

def deleteOrganization():
    # Locate trash button
    trashButton = driver.find_element(By.XPATH, "//div[@index='0']/div[7]/button")

    # Click on trash button
    trashButton.click()

    time.sleep(1)

    # Locate Remove button
    removeButton = driver.find_element(By.XPATH, "//button[@class='btn btn-danger']")

    # Click on remove button
    removeButton.click()

    # Locate search textfield
    searchTextField = driver.find_element(By.XPATH, "//input[@id='Search']")

    # Clear textfield
    time.sleep(1)

    searchTextField.clear()
    
    searchTextField.send_keys(" " + Keys.BACKSPACE)

def customizeGiriMobileApp():
    # Locate Organization Management tab
    customizeGiriMobileApp = driver.find_element(By.XPATH, "//div/div/div[2]/nav/div/ul/li[3]/a")

    # Click on organization management
    customizeGiriMobileApp.click()

login()
time.sleep(1)
createAccount()
time.sleep(1)
searchAccount()
time.sleep(2)
resetPassword()
time.sleep(1)
deleteAccount()
time.sleep(1)
organizationManagement()
time.sleep(1)
createOrganization()
time.sleep(1)
searchOrganization()
time.sleep(1)
addWorkplaces()
time.sleep(1)
deleteOrganization()
time.sleep(1)
customizeGiriMobileApp()
