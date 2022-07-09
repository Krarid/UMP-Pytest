from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import DesiredCapabilities
import time
import os

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
    pattern = [ ["Empty", "Hola", "Adios", "QA"], ["Falsch", "Hola", "Adios", "QA"], ["Üres", "Hola", "Adios", "QA"], \
                ["Vacio", "Hola", "Adios", "QA"], ["Pusty", "Hola", "Adios", "QA"] ]
    arObject = "wrench_ios"
    industrialIcon = "Forbidden 01.png"

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-insecure-localhost') # differ on driver version. can ignore. 
        caps = options.to_capabilities()
        caps["acceptInsecureCerts"] = True
        global driver
        driver = webdriver.Chrome(desired_capabilities=caps)
    
    def openChromeBrowser(self):
        driver.get(self.url)
        driver.maximize_window()

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

        time.sleep(3)

        try:
            driver.find_element(By.XPATH, "//h3[contains(text(), 'User Management')]")
        except:
            return False

        return True

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

        time.sleep(1)

        try:
            driver.find_element(By.XPATH, "//h5[contains(text(), 'Error while creating the user')]")
        except:
            return True

        return False

    def searchAccount(self):

        # Locate search textfield
        searchTextField = driver.find_element(By.XPATH, "//input[@id='Search']")

        # Send email
        searchTextField.send_keys(self.email + Keys.ENTER)

        time.sleep(2)
        
        try:
            driver.find_element(By.XPATH, "//div[@index=0]/div/div[1]/p[text()='" + self.email + "']")
        except:
            return False

        return True

    def resetPassword(self):
        # Locate reset button
        resetPasswordButton = driver.find_element(By.XPATH, "//div[@index=0]/div/div[4]/button")

        # Click on reset button
        resetPasswordButton.click()

        # Locate cancel button on pop up
        try:
            cancelButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
            cancelButton.click()
        except:
            return False

        return True

    def deleteAccount(self):
        # Locate trash button
        trashButton = driver.find_element(By.XPATH, "//div[@index=0]/div/div[5]/button")

        # Click on trash button
        trashButton.click()

        time.sleep(1)

        try:
            self.searchAccount()
            driver.find_element(By.XPATH, "//div[@index=0]/div/div[1]/p[text()='" + self.email + "']")
        except:
            return True

        return False

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

        time.sleep(2)

        try:
            # Locate Ok button on pop up
            okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")
            okButton.click()
        except:
            return False

        return True

    def addWorkplaces(self):

        # Locate the last button to add 10 workplaces
        addWorkplaceButton = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add 10')]")

        last = len(addWorkplaceButton) - 1

        # Click on button to add 10 workplaces
        addWorkplaceButton[last].click()

        time.sleep(1)

        try:
            # Locate Ok button on pop up
            okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")
            okButton.click()
        except:
            return False

        return True

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

        time.sleep(3)
     
        lastOrganization = driver.find_elements(By.XPATH, "//div[3]/div[1]/div/div/div/div[1]/p")
        last = len(lastOrganization) - 1
            
        deleted = True if lastOrganization[last].text not in test.organization else False

        return deleted

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

        time.sleep(5)

        try:
            pattern = driver.find_element(By.XPATH, "//p[text()='" + self.pattern[0][0] + " - " + self.pattern[0][1] + " - " + self.pattern[0][2] + " - " + self.pattern[0][3] + "']")
        except:
            return False

        return True

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

        time.sleep(3)

        lastSymbol = driver.find_elements(By.XPATH, "//div/div[@class='col-3 text-break']")
        last = len(lastSymbol) - 1

        deleted = True if lastSymbol[last].text not in test.arObject else False

        return deleted

    def uploadARObject(self):

        # Find input file to upload the AR Object
        uploadARObject = driver.find_element(By.XPATH, "//input[@id='assetsFieldHandle']")

        # Locate the AR Object resource from absolute path
        uploadARObject.send_keys(os.getcwd() + '/' + self.arObject)

        time.sleep(1)

        uploaded = True

        try:
            driver.find_element(By.XPATH, "//h4[contains(text(), 'The files were uploaded successfully')]")
        except:
            uploaded = False

        # Clic on OK button to confirm the action
        okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")

        okButton.click()

        return uploaded

    def industrialIcons(self):
        # Find the industrial icons tab by text
        industrialIcons = driver.find_element(By.XPATH, "//a[contains(text(), 'Industrial Icons')]")

        # Redirect to industrialIcons
        industrialIcons.click()

    def uploadIndustrialIcon(self):
        # Find input file to upload the AR Object
        uploadIndustrialIcon = driver.find_element(By.XPATH, "//input[@id='assetsFieldHandle']")

        # Locate the AR Object resource from absolute path
        uploadIndustrialIcon.send_keys(os.getcwd() + '/' + self.industrialIcon)

        time.sleep(2)

        uploaded = True

        try:
            driver.find_element(By.XPATH, "//h4[contains(text(), 'The files were uploaded successfully')]")
        except:
            uploaded = False

        # Clic on OK button to confirm the action
        okButton = driver.find_element(By.XPATH, "//button[contains(text(), 'Ok')]")

        okButton.click()

        return uploaded

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

        time.sleep(3)

        lastIcon = driver.find_elements(By.XPATH, "//div[@class='col-3 text-break '][1]/p")
        last = len(lastIcon) - 1

        deleted = True if lastIcon[last].text not in test.industrialIcon else False

        return deleted
        
test = UMPAutomation()

def test_open_browser():
    test.openChromeBrowser()

    assert driver.title == "Giri User Management Dashboard"

def test_login():
    assert test.login()

def test_create_account():
    assert test.createAccount()

def test_search_account():
    assert test.searchAccount()

def test_reset_password():
    assert test.resetPassword()

def test_delete_account():
    assert test.deleteAccount()

def test_organization_management():
    test.organizationManagement()

def test_create_organization():
    assert test.createOrganization()

def test_add_workplaces():
    assert test.addWorkplaces()

def test_delete_oganization():
    assert test.deleteOrganization()

def test_customize_giriMobileApp():
    test.customizeGiriMobileApp()
    time.sleep(1)

def test_create_new_pattern():
    assert test.createNewPattern()

def test_ar_objects():
    test.ARObjects()

def test_upload_AR_Object():
    assert test.uploadARObject()

def test_delete_AR_Object():
    assert test.deleteARObject()

def test_enable_AR_Object():
    test.enableARObject()

def test_industrial_icons():
    test.industrialIcons()

def test_upload_industrial_icon():
    assert test.uploadIndustrialIcon()

def test_enable_industrial_icon():
    test.enableIndustrialIcon()

def test_delete_industrial_icon():
    assert test.deleteIndustrialIcon()
