# 功能函数

def multiply(a,b):
    return a*b

class TestMultiply:
    #================Fixture=============

    @classmethod
    def setup_class(cls):
        print("setup_class=================>")

    @classmethod
    def teardown_class(cls):
        print("taerdown_class=====================>")

    def setup_method(self,method):
        print("setup_method")
