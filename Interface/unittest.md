# unittest

## 运行case

1、unittest.main()

运行类中的所有case

2、跳过某些测试的case

@unittest.skip，写在要跳过的case前

3、unittest.TestSuite：添加测试case

​    suite = unittest.TestSuite()
​    suite.addTest(TestMethod("test_01"))      添加单个case
​    suite.addTests([TestMethod("test_01"),TestMethod("test_02")])   添加多个case
​    unittest.TextTestRunner().run(suite)

# 注意

上述3中添加的case中有被@unittest.skip修饰时，该case不会被执行

# case关联

当执行case的时候，如果当前case的参数需要使用到上一个case的返回值，需要进行关联，可以将该返回值进行global声明



# case执行顺序

根据测试case的命令进行升序执行

# HTMLTestRunner

1、新建文件为HTMLTestRunner，从官网上下载内容将内容复制到此文件中

2、python3使用此文件时需要修改，如下：

+ 将94行的StringIO修改为io
+ 将539行的self.outputBuffer = StringIO.StringIO()修改为self.outputBuffer = io.StringIO()
+ 将631行print >>sys.stderr, '\nTime Elapsed: %s' % (self.stopTime-self.startTime)修改为print(sys.stderr, '\nTime Elapsed: %s' % (self.stopTime - self.startTime))
+ 将642行if not rmap.has_key(cls)改为 if not cls in rmap 
+ 将766行uo = o.decode('latin-1') 改为uo = e
+ 将772行ue = e.decode('latin-1')改为ue = e

3、执行测试

​    filepath = './report/htmlreport.html'     //测试结果记录
​    fp = open(filepath,'wb')
​    suite = unittest.TestSuite()
​    suite.addTests([TestMethod("test_01"),TestMethod("test_02"),Demo("test_03")])
​    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='接口测试报告')
​    runner.run(suite)