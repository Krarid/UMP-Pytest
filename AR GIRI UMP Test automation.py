from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
import time
import os

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
    trashButton = driver.find_elements(By.XPATH, "//div/div[6]/button")

    last = len(trashButton) - 1

    # Click on trash button
    trashButton[last].click()

    time.sleep(1)

    # Locate Remove button
    removeButton = driver.find_element(By.XPATH, "//button[@class='btn btn-danger']")

    # Click on remove button
    removeButton.click()

def customizeGiriMobileApp():
    # Locate Organization Management tab
    customizeGiriMobileApp = driver.find_element(By.XPATH, "//a[contains(text(), 'Customize Giri Mobile App')]")

    # Click on organization management
    customizeGiriMobileApp.click()

def createNewPattern(defaultLanguage = 0, pattern = [ ["Empty"], ["Falsch"], ["Üres"], ["Vacio"], ["Pusty"] ] ):
    # Locate the Create new Pattern button
    createPatternButton = driver.find_element(By.XPATH, "//div/div/div[2]/div[4]/div/div[2]/div[2]/button")

    # Click on button
    createPatternButton.click()

    time.sleep(1)

    # Locate the radio button
    radio = driver.find_element(By.XPATH, "//input[@type='radio'][@value='" + str(defaultLanguage) + "']")

    # Click on radio button
    radio.click()

    # Locate Add mediatitle button
    mediatitleButton = driver.find_element(By.XPATH, "//button[text()=' + Add mediatitle ']")

    # Click on mediatitle Button
    for i in range( len(pattern[0]) - 1 ):
        time.sleep(1)
        mediatitleButton.click()

    # Fill the mediatitle text fields
    for j in range( len(pattern[0]) ):
        for i in range(1,6):
            mediatitleTextField = driver.find_element(By.XPATH,"//div[" + str(i) + "]/div[" + str(3 + j) + "]/input")
            mediatitleTextField.send_keys( pattern[i-1][j] )

    # Locate CONFIRM button
    confirmButton = driver.find_element(By.XPATH, "//button[text()=' CONFIRM ']")

    # Click on CONFIRM button
    confirmButton.click()

def ARObjects():
    # Locate the ARObjects tab
    arObjects = driver.find_element(By.XPATH, "//a[contains(text(), 'AR Objects')]")

    # Click on AR Objects tab
    arObjects.click()

def activeARObject():

    # Locate the toggle buton
    toggleButton = driver.find_element(By.XPATH, "//div[2]/div[3]/label/span")

    # Click on toggle button
    toggleButton.click()

def deleteARObject():

    # Locate trash button
    trashButton = driver.find_element(By.XPATH, "//div[2]/div[4]/img")

    trashButton.click()

    time.sleep(1)

    # Delete the icon
    # deleteAnyway = driver.find_element(By.XPATH, "//div[@class='modal-content']/div[2]/button[1]")
    # deleteAnyway.click()

    # Don't delete the icon
    dontDelete = driver.find_element(By.XPATH, "//div[@class='modal-content']/div[2]/button[2]")
    dontDelete.click()

def uploadARObject():

    # Find input file to upload the AR Object
    uploadIcon = driver.find_element(By.XPATH, "//input[@id='assetsFieldHandle']")

    # Locate the AR Object resource from absolute path
    uploadIcon.send_keys(os.getcwd() + '/' + 'wrench_ios')

    time.sleep(1)

    # Clic on OK button to confirm the action
    okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")

    okButton.click()
    
def industrialIcons():
    # Find the industrial icons tab by text
    industrialIcons = driver.find_element(By.XPATH, "//a[contains(text(), 'Industrial Icons')]")

    # Redirect to industrialIcons
    industrialIcons.click()
login()
time.sleep(3)
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
addWorkplaces()
time.sleep(1)
deleteOrganization()
time.sleep(1)
customizeGiriMobileApp()
time.sleep(1)
createNewPattern( 0, [ ["Empty", "Hola", "Adios", "QA"], ["Falsch", "Hola", "Adios", "QA"], ["Üres", "Hola", "Adios", "QA"], ["Vacio", "Hola", "Adios", "QA"], ["Pusty", "Hola", "Adios", "QA"] ] )
ARObjects()
time.sleep(1)
activeARObject()
time.sleep(1)
deleteARObject()
time.sleep(1)
uploadIndustrialIcon()
