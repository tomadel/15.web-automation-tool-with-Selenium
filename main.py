from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class WebAutomation:
    def __init__(self):
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")

        download_path = os.getcwd()
        prefs = {'download.default_directory': download_path}
        chrome_options.add_experimental_option('prefs', prefs)

        # Create Service instance for ChromeDriver
        service = Service("chromedriver-win64/chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        # Open the login page

        self.driver.get("https://demoqa.com/login")

        # Wait for the login fields
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
        login_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))

        # Enter login details
        username_field.send_keys('username')
        password_field.send_keys('password')
        login_button.click()

    def fill_form(self, fullname, email, current_address, permanent_address):
        # Wait for and click the "Elements" section
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))
        )
        elements.click()

        # Click the "Text Box" option
        text_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
        text_box.click()

        # Locate the form fields and submit button
        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
        current_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'currentAddress')))
        permanent_address_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'permanentAddress')))

        submit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'submit')))

        # Fill the form areas
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute("arguments[0].click();", submit_button)

    def download(self):
        # Locate the  upload and download section, and download button
        upload_download = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "item-7")))
        upload_download.click()

        download_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'downloadButton')))
        driver.execute("arguments[0].click();", download_button)

    def close(self):
        # Close the browser session
        self.driver.quit()



if __name__ == "__main__"
    webautomation = WebAutomation()
    webautomation.login("xuser", "xpassword",)
    webautomation.fill_form("Guney Dogan", "guney@gmail.com", "Ruskonlahdenkatu", "Ruskonlahdenkatu")
    webautomation.download()
    webautomation.close()







