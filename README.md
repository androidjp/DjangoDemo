## 安装Django
* 前提：已经装了Python
  ```
  $ python
  Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
  Type "help", "copyright", "credits" or "license" for more information.
  >>> exit()
  ```
* 安装方式一：执行命令
  ```
  /// 当前最新的稳定版本下载
  $ pip install Django==2.0.5
  ```
* 安装方式二：PyCharm IDE new Django Project 时自动安装
  ![](./img/first_demo_1.png)
* 安装方式三：【全手动】github clone并扔到Python安装目录下的`Lib`目录中
  ```
  $ git clone https://github.com/django/django.git
  ```
* 查看Django版本
  ```
  $ python -m django --version
  ```

## 创建Django项目
#### 创建方式
- 方式一：执行命令
  ```
  $ django-admin startproject mysite
  ```
- 方式二：IDE直接gen（看上图）

#### 初始项目结构
  ![](./img/first_demo_2.png)
* 根目录`DjangoDemo`文件夹名字你随便改无所谓，但是下一级的`DjangoDemo`文件夹则可能有内部资源被外界调用，所以就不能乱改了。
* `__init__.py`：空文件，就是告诉别人我是一个py包
* `settings.py`：Django 配置文件
* `urls.py`：Django项目的URL声明，相当于你的网站的“目录"
* `wsgi.py`：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口

## 启动项目
执行命令：
  ```
  $ python mange.py runserver [端口号，默认8000]
  ```
然后我们看到了log，然后我们去跑`http://localhost:8000/`，然后就有了Django首页界面

- **原理：** 这个命令，启动的是Django自带的DevServer，他是一个纯Python写的轻量级服务器。
- **特点：** 这个devServer它很厉害，在每次被请求的时候，都会去重新加载一遍Python代码【事件驱动的热部署】.

> Django项目特点：在 Django 中，每一个应用都是一个 Python 包，并且遵循着相同的约定。Django 自带一个工具，可以帮你生成应用的基础目录结构，这样你就能专心写代码，而不是创建目录了。

## 数据库配置
在你项目目录的`settings.py`中，配置者整个Django项目的设置，其中包括Database

配置步骤：
1. 安装合适的database bindings（或者直接使用默认的sqlite3）
2. 更改`DATABASES'default'`中的键值：
  * `ENGINE`
    * `django.db.backends.sqlite3`
    * `django.db.backends.postgresql`
    * `django.db.backends.mysql`
    * `django.db.backends.oracle`
  * `NAME`
    * 数据库名称，`默认值 os.path.join(BASE_DIR, 'db.sqlite3')` 将会把数据库文件储存在项目的根目录
  * `USER`,`PASSWORD`,`HOST`等可选的配置







## 请求和页面跳转

## 多数据库连接
* 配置MongoDB环境[这个后来验证了不靠谱]
  1. 安装Django-nonrel
    `pip install git+https://github.com/django-nonrel/django@nonrel-1.5`
  2. 安装djangotoolbox
    `pip install git+https://github.com/django-nonrel/djangotoolbox`
  3. 安装 Django MongoDB Engine
    `pip install git+https://github.com/django-nonrel/mongodb-engine`
  4. 配置settings.py文件
    ```
    DATABASES = {
    'default' : {
      'ENGINE' : 'django_mongodb_engine',
       'NAME' : 'my_database'
      }
    }
    ```

## 采坑集
* 在跑`python manage.py test`时遇到这种和migrate有关的找不到db的问题
  ![](./img/issue_1.png)
  步骤：
  1. 先run `manage.py makemigrations`
  2. 后run `python manage.py migrate`
  3. 最后run `python manage.py test` 就OK了
* 在POST请求时，出现403 拒绝访问的情况
  ![](./img/issue_2.png)
  步骤：
  1. 导入：`from django.views.decorators.csrf import csrf_exempt`
  2. 在对应的服务端方法头上加上注解：`@csrf_exempt`



## 参考文章
* [Django官方文档](https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/)
* [如何进行多数据库环境配置](https://blog.csdn.net/songfreeman/article/details/70229839)
* [django-mongo-engine插件安装(配合上面的步骤，发现不支持Python3)](http://django-mongodb-engine.readthedocs.io/en/latest/topics/setup.html)
* [django 单元测试](https://www.jianshu.com/p/34267dd79ad6)
* [Python json与Object转换](https://blog.csdn.net/tterminator/article/details/63289400)
* [Python 单例模式写法](https://www.cnblogs.com/huchong/p/8244279.html)
