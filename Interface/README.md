# Interface为一个基本自动化接口测试的框架

## base

封装了发送post和get请求

## config

封装了获取数据的一些方式，和数据依赖处理的封装

## datas

数据集，比如接口测试的用例和一些登录的信息、邮箱的信息等

运行程序前需要在email_count.py中填写邮件信息

## main

函数的入口

## report

保存测试报告的路径

## util

封装了对excel操作、json数据操作、发送邮件操作、数据库操作等

## 其他

使用Unittest的使用demo和使用HTMLTestRunner生成测试报告的demo