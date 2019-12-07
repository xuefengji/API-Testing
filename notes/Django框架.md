# Django框架

## 安装

pip install django（基于python3）

## 启动

新建一个django工程后，再该目录下输入python manerge.py runserver，后再浏览器中输入127.0.0.1:8000 后即可打开浏览器

## 新建app应用

python manage.py startapp web(app应用名称)

+ 新建app后，需要在setting中添加该应用

![添加app](E:\API-Testing\images\添加app.png)

+ 开发简单的post和get接口步骤：

  1、在web/views中添加接口内容

  ![view内容](E:\API-Testing\images\view内容.png)

  2、在url中添加路径

  ![url设置](E:\API-Testing\images\url设置.png)