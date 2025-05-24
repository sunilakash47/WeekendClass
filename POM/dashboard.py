
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class dashboard:
    def __init__(self,driver):
        self.driver=driver
    def profile_icon(self):
        self.driver.find_element("xpath","//a[@class='profile-icon-image loaded']").click()
    def signout(self):
        self.driver.find_element("xpath","//li[@data-action='signout']").click()
    def edit_profile(self):
        self.driver.find_element("xpath","//a[.='Edit Profile']").click()
    def edit_yourname(self,data):
        self.driver.find_element("xpath","//textarea[@placeholder='Yourname']").send_keys(data)
    def edit_bio(self,data):
        self.driver.find_element("xpath","//textarea[@placeholder='Briefly describe who you are.']").send_keys(data)
    def edit_hashtag(self):
        self.driver.find_element("xpath","//button[@class='uikit-button btn-tertiary size-s inline-item']").click()
    def hashtag_search_music(self,data):
        self.driver.find_element("xpath","//input[@placeholder='Search for more hashtags']").send_keys(data)
    def music(self):
        return self.driver.find_element("xpath","(//span[.='music'])[2]")
    def edit_hashtag_cancel(self):
        self.driver.find_element("xpath","(//a[@href='#'])[2]").click()
    def show_gender(self):
        self.driver.find_element("xpath","(//div[@class='track'])[1]").click()
