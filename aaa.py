import requests,os
import time
from queue import Queue
from lxml import etree
import threading
class Douban(object):
    def __init__(self):
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.base_url = "https://movie.douban.com/top250?start="
        self.url_list = {}

        for page in range(0, 225 + 1, 25):
            self.url_list[page] = self.base_url+str(page)
        # 创建保存数据的队列

        self.data_queue = Queue()
        self.count = 0

    def send_request(self, url):
        print("[INFO]: 正在抓取" + url)
        html = requests.get(url, headers = self.headers).content
        # 每次请求间隔1秒

        time.sleep(1)

        self.parse_page(html)
    def parse_page(self, html):
        html_obj = etree.HTML(html)
        node_list = html_obj.xpath("//div[@class='info']")
        if os.path.exists("./douban") == False:
            os.makedirs("./douban")
        for page in self.url_list.keys():

            f = open("./douban/"+str(page) +".html","wb")
            f.write(html)
            f.flush()
            f.close()
        for node in node_list:
            # 电影标题
            title = node.xpath("./div[@class='hd']/a/span[1]/text()")[0]
            # 电影评分
            score = node.xpath(".//span[@class='rating_num']/text()")[0]
            with open("./douban/douban.txt","a",encoding="utf-8") as f:
                data = title + score
                f.write(data+"\n")

            self.count += 1
            self.data_queue.put(score + "\t" + title)
    def start_work(self):
        # 单线程：
        """
        for url in self.url_list:
            self.send_request(url)
        """
        thread_list = []
        for url in self.url_list.values():
            # 创建一个线程对象
            thread = threading.Thread(target = self.send_request, args = [url])
            # 启动线程，执行任务
            thread.start()
            # 将当前线程对象存到列表
            thread_list.append(thread)
        # 让主线程等待，所有子线程执行结束，再执行后面的代码
        for thread in thread_list:
            thread.join()
        while not self.data_queue.empty():
            print(self.data_queue.get())
        print(self.count)

if __name__ == "__main__":
    douban = Douban()
    douban.start_work()