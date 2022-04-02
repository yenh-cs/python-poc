import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Exercise1(unittest.TestCase):
    def setUp(self):
        self.target = "http://main.ctqatest.info/test.php"
        
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_text_unde_shadow_root(self):
        """Find and assert text under shadow-root"""
        try:
            self.driver.get(self.target)
            shadow_host = self.driver.find_element(By.CSS_SELECTOR, '#site-info')
            shadow_root = shadow_host.shadow_root
            shadow_content = shadow_root.find_element(By.CSS_SELECTOR, 'span')
            assert shadow_content.text == 'This is a demo website for testing purpose'
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    
    def test_login(self):
        """ 
            Use the website http://main.ctqatest.info/test.php  and perform the following tasks.
            Go to the login page and enter the username as test@test.com and password as ThisIs@T3st. Check if there is an error displayed.
        """ 
        return None


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Exercise1)
    unittest.TextTestRunner(verbosity=2).run(suite)
