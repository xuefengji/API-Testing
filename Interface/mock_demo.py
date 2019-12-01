import unittest
from mock_test import mockTest
import HTMLTestRunner
from post import Run_Main
from demo import Demo


class TestMethod(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/login/'
        self.run = Run_Main()
        self.mock_test = mockTest()
    def test_01(self):
        data = {'username': 'sdsdsdsd', 'password': 1111111}
        #模拟返回的数据
        # self.run.run_main = mock.Mock(return_value=data)
        # res = self.run.run_main(self.url,data,'POST')
        res = self.mock_test.test_mock(self.run.run_main,self.url,data,'POST',data)
        print(res)
        #添加断言
        self.assertEqual(data['password'], 1111111, '测试失败')



        #设置跳过
    @unittest.skip
    def test_02(self):
        data = {'username': 'wewewee', 'password': 2222222}
        res = self.run.run_main(self.url, data, 'GET')
        #添加断言，'测试失败'：不相等的时候的提示的msg
        self.assertEqual(data['password'], 2222222, '测试失败')
        print(res)


if __name__=='__main__':
    #使用unittest中的main函数执行case:
    # unittest.main()
    #使用unittest的TestSuite执行case：
    # filepath = './report/htmlreport.html'
    # fp = open(filepath,'wb')
    suite = unittest.TestSuite()
    # suite.addTest(TestMethod("test_01"))
    suite.addTests([TestMethod("test_01"),TestMethod("test_02"),Demo("test_03")])
    unittest.TextTestRunner().run(suite)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='接口测试报告')
    # runner.run(suite)