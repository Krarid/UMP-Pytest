from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
import time
import os

options = webdriver.ChromeOptions()
options.add_argument('--allow-insecure-localhost') # differ on driver version. can ignore. 
caps = options.to_capabilities()
caps["acceptInsecureCerts"] = True
driver = webdriver.Chrome(desired_capabilities=caps)

class UMPAutomation:

    # Properties
    url = "https://35.219.183.240/"
    username = "iconsAdmin"
    password = "0000"
    email = "javier.melendez@fyware.com"
    typeAccount = "manager"
    organization = "Test"
    domain = "test.com"
    defaultLanguage = 0
    pattern = [ ["Empty", "Hola", "Adios", "QA"], ["Falsch", "Hola", "Adios", "QA"], ["Üres", "Hola", "Adios", "QA"], ["Vacio", "Hola", "Adios", "QA"], ["Pusty", "Hola", "Adios", "QA"] ]
    
    def openChromeBrowser(self):
        driver.get(self.url)

    def login(self):
        # Locate username textfield
        usernameTextField = driver.find_element(By.XPATH, "//input[1]")

        # Send username
        usernameTextField.send_keys(self.username)

        # Locate password textfield
        passwordTextField = driver.find_element(By.XPATH, "//input[2]")

        # Send password
        passwordTextField.send_keys(self.password)

        # Locate login button
        loginButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")

        # Click on login button
        loginButton.click()

    def createAccount(self):

        # Locate email textfield
        emailTextField = driver.find_element(By.XPATH, "//input[@type='email']")

        # Send email
        emailTextField.send_keys(self.email)

        # Locate dropdowns: type of account and organization
        select = driver.find_elements(By.XPATH, "//select")

        # Select the type of account
        Select(select[0]).select_by_value(self.typeAccount)

        time.sleep(1)

        # Select the organization
        Select(select[1]).select_by_index(1)

        # Select Create button
        createButton = driver.find_element(By.XPATH, "//button[text()='Create']")

        # Click on Create button
        createButton.click()

    def searchAccount(self):

        # Locate search textfield
        searchTextField = driver.find_element(By.XPATH, "//input[@id='Search']")

        # Send email
        searchTextField.send_keys(self.email + Keys.ENTER)

    def resetPassword(self):
        # Locate reset button
        resetPasswordButton = driver.find_element(By.XPATH, "//div[@index=0]/div/div[4]/button")

        # Click on reset button
        resetPasswordButton.click()

        # Locate cancel button on pop up
        cancelButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
        cancelButton.click()

    def deleteAccount(self):
        # Locate trash button
        trashButton = driver.find_element(By.XPATH, "//div[@index=0]/div/div[5]/button")

        # Click on trash button
        trashButton.click()

    def organizationManagement(self):
        # Locate Organization Management tab
        organizationManagement = driver.find_element(By.XPATH, "//a[contains(text(), 'Organization Management')]")

        # Click on organization management
        organizationManagement.click()

    def createOrganization(self):
        # Locate organization textfield
        organizationTextField = driver.find_element(By.XPATH, "//input[@id='orgName']")

        # Send organization
        organizationTextField.send_keys(self.organization)

        # Locate domain textfield
        domainTextField = driver.find_element(By.XPATH, "//input[@id='orgDomain']")

        # Send domain
        domainTextField.send_keys(self.domain)

        # Locate button to create organization
        createOrganization = driver.find_element(By.XPATH, "//button[@id='CreateDomainBtn']")

        # Click on create organization
        createOrganization.click()

        time.sleep(1)
        
        # Locate Ok button on pop up
        okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")
        okButton.click()

    def addWorkplaces(self):

        # Locate the last button to add 10 workplaces
        addWorkplaceButton = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add 10')]")

        last = len(addWorkplaceButton) - 1

        # Click on button to add 10 workplaces
        addWorkplaceButton[last].click()

        time.sleep(1)

        # Locate Ok button on pop up
        okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")
        okButton.click()

    def deleteOrganization(self):
        # Locate trash button
        trashButton = driver.find_elements(By.XPATH, "//div/div[6]/button")

        last = len(trashButton) - 1

        # Click on trash button
        trashButton[last].click()

        time.sleep(1)

        # Locate Remove button
        removeButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]")

        # Click on remove button
        removeButton.click()

    def customizeGiriMobileApp(self):
        # Locate Organization Management tab
        customizeGiriMobileApp = driver.find_element(By.XPATH, "//a[contains(text(), 'Customize Giri Mobile App')]")

        # Click on organization management
        customizeGiriMobileApp.click()

    def createNewPattern(self):
        # Locate the Create new Pattern button
        createPatternButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Create new Pattern')]")

        # Click on button
        createPatternButton.click()

        time.sleep(1)

        # Locate the radio button
        radio = driver.find_element(By.XPATH, "//input[@type='radio'][@value='" + str(self.defaultLanguage) + "']")

        # Click on radio button
        radio.click()

        # Locate Add mediatitle button
        mediatitleButton = driver.find_element(By.XPATH, "//button[contains(text(), '+ Add mediatitle')]")

        # Click on mediatitle Button
        for i in range( len(self.pattern[0]) - 1 ):
            time.sleep(1)
            mediatitleButton.click()

        # Fill the mediatitle text fields
        for j in range( len(self.pattern[0]) ):
            for i in range(1,6):
                mediatitleTextField = driver.find_element(By.XPATH,"//div[" + str(i) + "]/div[" + str(3 + j) + "]/input")
                mediatitleTextField.send_keys( self.pattern[i-1][j] )

        # Locate CONFIRM button
        confirmButton = driver.find_element(By.XPATH, "//button[contains(text(), 'CONFIRM')]")

        # Click on CONFIRM button
        confirmButton.click()

    def ARObjects(self):
        # Locate the ARObjects tab
        arObjects = driver.find_element(By.XPATH, "//a[contains(text(), 'AR Objects')]")

        # Click on AR Objects tab
        arObjects.click()

    def enableARObject(self):

        # Locate the toggle buton
        toggleButton = driver.find_elements(By.XPATH, "//div/div[3]/label/span")

        last = len(toggleButton) - 1

        # Click on toggle button
        toggleButton[last].click()

    def deleteARObject(self):

        # Locate the trash buton
        trashButtonList = driver.find_elements(By.XPATH, "//div/div[4]/img")

        last = len(trashButtonList) - 1
        
        # Click on the last trash button
        trashButtonList[last].click()

        time.sleep(1)

        # Locate the Delete anyway
        deleteButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete anyway')]")

        # Click on Delete button
        deleteButton.click()

    def uploadARObject(self):

        # Find input file to upload the AR Object
        uploadARObject = driver.find_element(By.XPATH, "//input[@id='assetsFieldHandle']")

        # Locate the AR Object resource from absolute path
        uploadARObject.send_keys(os.getcwd() + '/' + 'wrench_ios')

        time.sleep(1)

        # Clic on OK button to confirm the action
        okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")

        okButton.click()

    def industrialIcons(self):
        # Find the industrial icons tab by text
        industrialIcons = driver.find_element(By.XPATH, "//a[contains(text(), 'Industrial Icons')]")

        # Redirect to industrialIcons
        industrialIcons.click()

    def uploadIndustrialIcon(self):
        # Find input file to upload the AR Object
        uploadIndustrialIcon = driver.find_element(By.XPATH, "//input[@id='assetsFieldHandle']")

        # Locate the AR Object resource from absolute path
        uploadIndustrialIcon.send_keys(os.getcwd() + '/' + 'Forbidden 01.png')

        time.sleep(2)

        # Clic on OK button to confirm the action
        okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")

        okButton.click()

    def enableIndustrialIcon(self):

        # Locate the toggle buton
        toggleButtonList = driver.find_elements(By.XPATH, "//div/div[4]/label/span")

        last = len(toggleButtonList) - 1
        
        # Click on the last toggle button
        toggleButtonList[last].click()

    def deleteIndustrialIcon(self):
        # Locate the trash buton
        trashButtonList = driver.find_elements(By.XPATH, "//div/div[5]/img")

        last = len(trashButtonList) - 1
        
        # Click on the last trash button
        trashButtonList[last].click()

        # Locate the Delete anyway
        deleteButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Delete anyway')]")

        # Click on Delete button
        deleteButton.click()

test = UMPAutomation()

test.openChromeBrowser()

test.login()
time.sleep(3)

test.createAccount()
time.sleep(1)

test.searchAccount()
time.sleep(2)

test.resetPassword()
time.sleep(1)

test.deleteAccount()
time.sleep(1)

test.organizationManagement()
time.sleep(1)

test.createOrganization()
time.sleep(1)

test.addWorkplaces()
time.sleep(1)

test.deleteOrganization()
time.sleep(1)

test.customizeGiriMobileApp()
time.sleep(1)

test.createNewPattern()

test.ARObjects()
time.sleep(1)

test.uploadARObject()
time.sleep(1)

test.deleteARObject()
time.sleep(1)

test.enableARObject()
time.sleep(1)

test.industrialIcons()
time.sleep(1)

test.uploadIndustrialIcon()
time.sleep(1)

test.enableIndustrialIcon()
time.sleep(1)

test.deleteIndustrialIcon()
