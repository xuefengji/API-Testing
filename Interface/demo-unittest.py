import unittest

class demo(unittest.TestCase):
    #每次方法前调用
    def setUp(self):
        print('每次方法前调用')

    def tearDown(self):
        print('每次方法后调用')

    def test_01(self):
        print('这是第一个方法')

    def test_02(self):
        print('这是第二个方法')


if __name__=='__main__':
    unittest.main()
