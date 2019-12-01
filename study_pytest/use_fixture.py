import pytest

# @pytest.fixture()
# def some_data():
#     return 42
#
# def test_some_data(some_data):
#     assert some_data==42
#
@pytest.fixture()
def page_title():
    title = "百度一下，你就知道！"
    return title

def test_page_title(page_title):
    baidu_title = "百度一下，你就知道！"
    assert baidu_title == page_title
