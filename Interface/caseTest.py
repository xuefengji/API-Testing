import unittest
from post import Run_Main

class TestMethod(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/login/'
        self.run = Run_Main()
    def test_01(self):
        data = {'username': 'sdsdsdsd', 'password': 1111111}
        res = self.run.run_main(self.url,data,'POST')
        #添加断言
        self.assertEqual(data['password'], 1111111, '测试失败')

        print(res)

    def test_02(self):
        data = {'username': 'wewewee', 'password': 2222222}
        res = self.run.run_main(self.url, data, 'GET')
        #添加断言，'测试失败'：不相等的时候的提示的msg
        self.assertEqual(data['password'], 1111111, '测试失败')
        print(res)


if __name__=='__main__':
    unittest.main()