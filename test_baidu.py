import unittest
from time import sleep
from selenium import webdriver


class TestBaidu(unittest.TestCase):
    """百度搜索测试"""
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.base_url = "https://www.baidu.com"
    #
    # def tearDown(self):
    #     self.driver.quit()
    #
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def test_search_key_selenium(self):
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(self.base_url)
    #     self.driver.find_element_by_id("kw").send_keys("selenium")
    #     self.driver.find_element_by_id("su").click()
    #     sleep(2)
    #     title = self.driver.title
    #     self.assertEqual(title,'selenium_百度搜索')
    #
    #
    # def test_search_key_unttest(self):
    #     self.driver.implicitly_wait(10)
    #     self.driver.get(self.base_url)
    #     self.driver.find_element_by_id("kw").send_keys("unittest")
    #     self.driver.find_element_by_id("su").click()
    #     sleep(2)
    #     title = self.driver.title
    #     self.assertEqual(title,'unittest_百度搜索')
    def baidu_search(self, search_key):

        self.driver.implicitly_wait(10)

        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(2)

    def test_search_key_selenium(self):
        """搜索关键字：selenium"""
        search_key = 'selenium'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    def test_search_key_unttest(self):
        """搜索关键字：unittest"""
        search_key = 'unittest'
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')


if __name__ == '__main__':
    unittest.main()
