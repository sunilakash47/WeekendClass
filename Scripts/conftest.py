import pytest
from selenium.webdriver import Chrome

@pytest.fixture
def setup():
    driver = Chrome()
    driver.get('https://secure.imvu.com/welcome/ftux/')
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.close()

"""Line	Purpose
import pytest	- Why: You need to import the pytest module because you're creating a fixture (a reusable setup function) for tests.
What it does: Provides the @pytest.fixture decorator and other testing tools.

from selenium.webdriver import Chrome	- Import Chrome driver

@pytest.fixture	- Why: Tells pytest that the following function is a fixture. Fixtures are used to set up and tear down things (like browser instances) before and after each test.
What it does: Allows setup() to be automatically injected into your tests as a parameter.

def setup(): - Why: Defines a fixture function named setup, which prepares the test environment.
What it does: The function sets up and returns a Selenium WebDriver instance.

driver = Chrome()	- Launch Chrome browser

driver.get(...)	- Navigate to Amazon

driver.maximize_window() -	Maximize browser window

driver.implicitly_wait(10)	- Why: Gives the browser time to load elements before throwing an error.
What it does: Sets an implicit wait of 10 seconds. Selenium will wait up to 10 seconds for elements to appear before failing (good for dynamic web pages).

yield driver	- Why: Temporarily hands control back to the test while keeping the browser open.
What it does: Provides the driver to the test function. After the test is done, the code after yield runs (i.e., the cleanup code).

driver.close()	Close current browser and clean up"""