from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Generic.screenshot import *

def verify_element(element, driver):
    wait = WebDriverWait(driver, 10)
    try:
        wait.until(EC.visibility_of_element_located(element))
    except:
        take_screenshot(driver)
        raise Exception ("Element Is Not Present in WebPage")