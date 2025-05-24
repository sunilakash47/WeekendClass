class Ftux:
    def __init__(self,driver):
        self.driver = driver
    def Ftux_login_button(self):
        self.driver.find_element("xpath",'(//button[.="Log In"])[1]').click()
    def Ftux_username(self,data):
        self.driver.find_element("xpath","//input[@name='avatarname']").send_keys(data)
    def Ftux_password(self,data):
        self.driver.find_element("xpath","//input[@name='password']").send_keys(data)
    def Ftux_signin_button(self):
        self.driver.find_element("xpath","(//button[.='Log In'])[3]").click()

