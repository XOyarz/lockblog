from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from unittest import skip

class FirstTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    @skip
    def test_check_home_page(self):
        self.browser.get(self.live_server_url)

# Check the login procedure! It won't work though because the username/pass is not
# registered in the test database.
    def test_login_button(self):
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_class_name('top-menu')
        link.click()
        time.sleep(3)

        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('xavier')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('nopassword')
        time.sleep(3)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)




