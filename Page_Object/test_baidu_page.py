import unittest
from time import sleep
from selenium import webdriver
from Page_Object.baidu_page import BaiduPage
from Page_Object.baidu_page_for_poium import Baidu

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_baidu_search_case(self):
        page = BaiduPage(self.driver)
        page.open()
        page.search_input("selenium")
        page.search_button()
        sleep(2)
        self.assertEqual(page.get_title(),"selenium_百度搜索")

    def test_baidu_search_for_poium_case(self):
        page = Baidu(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "selenium"
        page.search_button.click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
