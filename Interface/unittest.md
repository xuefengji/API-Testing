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

