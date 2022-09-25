from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def test_basic():
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("http://selenium.dev")

    driver.quit()
