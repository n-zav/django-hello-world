from django.conf import settings
from selenium import webdriver
import unittest


class TestHomePageSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_homepage(self):
        self.driver.get(settings.SESSION_COOKIE_DOMAIN + ':8000')
        self.assertEqual('Nastya',
                         self.driver.find_element_by_id('name').text)
        self.assertEqual('nastya.zavalkina@gmail.com',
                         self.driver.find_element_by_id('email').text)
        self.assertEqual('nastya.zavalkina',
                         self.driver.find_element_by_id('skype').text)
        self.assertIn(settings.SESSION_COOKIE_DOMAIN + ':8000',
                      self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
