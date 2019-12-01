import csv
import codecs
import unittest
from time import sleep
from itertools import islice
from selenium import webdriver
from parameterized import parameterized


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"
        # cls.test_data = []
        # with codecs.open('baidu_data.csv','r','utf_8_sig') as f:
        #     data = csv.reader(f)
        #     for line in islice(data,1,None):
        #         cls.test_data.append(line)

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)

    # 通过parameterized实现参数化
    @parameterized.expand([
        ("case1", "selenium"),
        ("case2", "unittest"),
        ("case3", "parameterized"),
    ])
    def test_search(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")
        # name对应上面的case1，case2.。。

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
