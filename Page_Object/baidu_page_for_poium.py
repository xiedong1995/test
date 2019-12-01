from poium import Page,PageElement
"""
baidu_page用poium重新实现版

"""
class Baidu(Page):
    """百度Page层,百度页面封装操作到的元素"""
    search_input = PageElement(id_ = "kw")
    search_button = PageElement(id_ = "su")



"""更多用法"""
# poium支持八种定位
class SomePage(Page):
    elem_id = PageElement(id_='id',timeout=5) # 设置元素超时时间
    elem_name = PageElement(name = 'name')
    elem_class = PageElement(class_name = 'class')
    elem_tag = PageElement(tag = 'input')
    elem_link_text = PageElement(link_text =  'this_is_link')
    elem_partial_link_text = PageElement(partial_link_text = 'is_link')
    elem_xpath = PageElement(xpath='//*[@id="kk"]')
    elem_css = PageElement(css='#id')