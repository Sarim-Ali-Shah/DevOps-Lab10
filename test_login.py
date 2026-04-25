from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_incorrect_credentials():

    # Tell Selenium where your ChromeDriver is
    service = Service("C:\\Users\\SARIM\\Downloads\\chromedriver-win64\\chromedriver.exe")

    # NO headless mode for now - Chrome will open visually so we can see what happens
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Start the Chrome browser
    driver = webdriver.Chrome(service=service, options=options)

    # Wait up to 15 seconds for elements to appear
    wait = WebDriverWait(driver, 15)

    # Go to the login page
    driver.get("http://103.139.122.250:4000/login")

    # Wait until the email field appears, then type the email
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("qasim@malik.com")

    # Type the password
    driver.find_element(By.ID, "password").send_keys("abcdefg")

    # Click the Sign In button
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Wait until the error message appears
    error_element = wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[contains(@class,'text-red') or contains(@class,'error') or contains(@class,'alert')]"
    )))

    # Read the error message
    error_text = error_element.text
    print("Error text found:", error_text)

    # Check that an error message appeared
    assert len(error_text) > 0

    # Close the browser
    driver.quit()