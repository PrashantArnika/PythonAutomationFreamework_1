class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_xpath = "//li[@class='oxd-userdropdown']//i"
        self.logout_link_xpath = "//ul[@class='oxd-dropdown-menu']//li[4]/a"

    def click_welcome(self):
        self.driver.find_element("xpath", self.welcome_link_xpath).click()

    def click_logout(self):
        self.driver.find_element("xpath", self.logout_link_xpath).click()


