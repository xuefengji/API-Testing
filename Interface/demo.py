import unittest

class Demo(unittest.TestCase):
    @classmethod    #表示类方法，只调用一次
    def setUpClass(cls):
        print('这是类开始的方法')
    @classmethod
    def tearDownClass(cls):
        print('这是类结束的方法')
    #每次方法前调用，在每个测试方法之前调用
    def setUp(self):
        print('每次方法前调用')
    #每次方法后调用，在每个测试方法之后调用
    def tearDown(self):
        print('每次方法后调用')

    def test_01(self):
        print('这是第一个方法')

    def test_03(self):
        print('这是第二个方法')


if __name__=='__main__':
    unittest.main()
