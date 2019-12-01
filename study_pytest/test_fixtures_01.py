"""
fixture 通常用来对测试方法,测试函数,测试类和整个测试文件进行初始化或还原测试环境.
setup_moudle/teardown-module:在当前文件中,所有测试用例执行前和之后执行

setup_function/teardown_function:在每个测试函数之前与之后执行

setup/teardown:在每个测试函数之前与之后执行.这两个方法同样可以作用域类方法
"""


# 功能函数

def multiply(a, b):
    return a * b


# ===============Fixture====================

def setup_module(module):
    print('setup_module===================>')


def teardown_module(module):
    print('teardown_module===================>')


def setup_function(function):
    print('setup_function---------------->')


def teardown_function(functon):
    print('teardown_function--------------------->')


def setup():
    print('setup++++++++>>')


def teardown():
    print("teardown+++++++++++>>")


# 测试用例
def test_multiply_3_4():
    print('test_numbers_3_4')
    assert multiply(3, 4) == 12


def test_multiplt_a_3():
    print('test_strings_a_3')
    assert multiply('a', 3) == 'aaa'
