from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_incorrect_credentials():

    # EC2 Linux settings
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Selenium finds Chrome automatically inside Docker
    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 15)

    driver.get("http://103.139.122.250:4000/login")

    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("qasim@malik.com")
    driver.find_element(By.ID, "password").send_keys("abcdefg")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    error_element = wait.until(EC.presence_of_element_located((
        By.XPATH, "//div[contains(@class,'text-red') or contains(@class,'error') or contains(@class,'alert')]"
    )))

    error_text = error_element.text
    print("Error text found:", error_text)
    assert len(error_text) > 0

    driver.quit()