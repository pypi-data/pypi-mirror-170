# 介绍

[Gitee](https://gitee.com/bluepang2021/qrunner_new)

![](Qrunner_logo.jpg)

[![PyPI version](https://badge.fury.io/py/qrunner.svg)](https://badge.fury.io/py/qrunner) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qrunner)
![visitors](https://visitor-badge.glitch.me/badge?page_id=qrunner_new.qrunner)

AppUI/WebUI/HTTP automation testing framework based on pytest.

> 基于pytest 的 App UI/Web UI/HTTP自动化测试框架。

## 特点

* 集成`facebook-wda`/`uiautomator2`/`selenium`/`requests`，支持安卓 UI/IOS UI/Web UI/HTTP测试。
* 集成`allure`, 支持HTML格式的测试报告。
* 提供脚手架，快速生成自动化测试项目。
* 提供强大的`数据驱动`。
* 提供丰富的断言。
* 支持生成随机测试数据。
* 支持设置用例依赖。


## 三方依赖

* Allure：https://github.com/allure-framework/allure2
* WebDriverAgent：https://github.com/appium/WebDriverAgent

## Install

```shell
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple qrunner
```

## 🤖 Quick Start

1、查看帮助：
```shell
usage: qrunner [-h] [-v] [-p PROJECT]

全平台自动化测试框架

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show version
  -p PROJECT, --project PROJECT
                        create demo project
```

2、创建项目：
```shell
> qrunner -p mypro
```
目录结构如下：
```shell
mypro/
├── test_dir/
│   ├── __init__.py
│   ├── test_android.py
│   ├── test_ios.py
│   ├── test_web.py
│   ├── test_api.py
├── test_data/
│   ├── data.json
└── run.py
```

3、运行项目：

* ✔️ 在`pyCharm`中右键执行。

* ✔️ 通过命令行工具执行。

```shell
> python run.py

2022-09-29 11:02:40,206 - root - INFO - 执行用例
2022-09-29 11:02:40,206 - root - INFO - 用例路径: test_adr.py
2022-09-29 11:02:40,206 - root - INFO - ['test_adr.py', '-sv', '--reruns', '0', '--alluredir', 'allure-results', '--clean-alluredir']
================================================================================================================================================= test session starts ==================================================================================================================================================
platform darwin -- Python 3.9.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/UI/PycharmProjects/qrunner_new_gitee/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/UI/PycharmProjects/qrunner_new_gitee
plugins: xdist-2.5.0, forked-1.4.0, allure-pytest-2.9.45, rerunfailures-10.2, dependency-0.5.1, ordering-0.6
collecting ... 2022-09-29 11:02:40,294 - root - INFO - [UJK0220521066836] Create android driver singleton
2022-09-29 11:02:40,303 - root - INFO - 启动 android driver for UJK0220521066836
2022-09-29 11:02:40,309 - urllib3.connectionpool - DEBUG - Starting new HTTP connection (1): ujk0220521066836:7912
2022-09-29 11:02:40,357 - urllib3.connectionpool - DEBUG - Starting new HTTP connection (1): 127.0.0.1:62522
2022-09-29 11:02:40,377 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /wlan/ip HTTP/1.1" 200 11
collected 1 item                                                                                                                                                                                                                                                                                                       

test_adr.py::TestLogin::test_login 2022-09-29 11:02:40,381 - root - DEBUG - [start_time]: 2022-09-29 11:02:40
2022-09-29 11:02:40,381 - root - INFO - 强制启动应用: com.qizhidao.clientapp
2022-09-29 11:02:40,496 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /shell HTTP/1.1" 200 39
2022-09-29 11:02:40,792 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /packages/com.qizhidao.clientapp/info HTTP/1.1" 200 221
2022-09-29 11:02:40,893 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /shell HTTP/1.1" 200 184
2022-09-29 11:02:40,895 - root - INFO - 存在才点击元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'},0
2022-09-29 11:02:40,895 - root - INFO - 判断元素是否存在: {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'},0
2022-09-29 11:02:40,895 - root - INFO - 查找元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'},0
2022-09-29 11:02:54,106 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 90
2022-09-29 11:02:54,179 - root - WARNING - 【exists:257】未找到元素 {'resourceId': 'com.qizhidao.clientapp:id/bottom_btn'}
2022-09-29 11:02:54,179 - root - INFO - 点击元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_view'},3
2022-09-29 11:02:54,179 - root - INFO - 查找元素: {'resourceId': 'com.qizhidao.clientapp:id/bottom_view'},3
2022-09-29 11:02:54,332 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 89
2022-09-29 11:02:54,685 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /screenshot/0 HTTP/1.1" 200 236334
2022-09-29 11:02:55,619 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 290
2022-09-29 11:02:55,822 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 89
2022-09-29 11:02:55,822 - root - DEBUG - 点击成功
2022-09-29 11:02:55,822 - root - INFO - 判断元素是否存在: {'text': '登录/注册'},0
2022-09-29 11:02:55,823 - root - INFO - 查找元素: {'text': '登录/注册'},0
2022-09-29 11:03:00,253 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /jsonrpc/0 HTTP/1.1" 200 90
2022-09-29 11:03:00,254 - root - WARNING - 【exists:257】未找到元素 {'text': '登录/注册'}
2022-09-29 11:03:00,254 - root - INFO - 已登录成功
2022-09-29 11:03:00,255 - root - DEBUG - 等待: 3s
PASSED2022-09-29 11:03:03,621 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "GET /screenshot/0 HTTP/1.1" 200 175495
2022-09-29 11:03:03,624 - root - INFO - 退出应用: com.qizhidao.clientapp
2022-09-29 11:03:03,782 - urllib3.connectionpool - DEBUG - http://127.0.0.1:62522 "POST /shell HTTP/1.1" 200 39
2022-09-29 11:03:03,783 - root - DEBUG - [end_time]: 2022-09-29 11:03:03
2022-09-29 11:03:03,783 - root - DEBUG - [run_time]: 23.40 s
```

4、查看报告

运行`allure server allure-results`浏览器会自动调起报告（需先安装配置allure）

![test report](./test_report.jpg)

## 🔬 Demo

[demo](/demo) 提供了丰富实例，帮你快速了解qrunner的用法。

### 安卓APP 测试

```shell
import qrunner
from qrunner import AndroidElement, story, title


class HomePage:
    ad_close_btn = AndroidElement(rid='id/bottom_btn', desc='首页广告关闭按钮')
    bottom_my = AndroidElement(rid='id/bottom_view', index=3, desc='首页底部我的入口')


@story('首页')
class TestClass(qrunner.AndroidTestCase):
    
    def start(self):
        self.hp = HomePage()
    
    @title('从首页进入我的页')
    def testcase(self):
        self.hp.ad_close_btn.click()
        self.hp.bottom_my.click()
        self.assertText('我的订单')


if __name__ == '__main__':
    qrunner.main(
        android_device_id='UJK0220521066836',
        android_pkg_name='com.qizhidao.clientapp'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.AndroidTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertText`、`assertElement` 等断言方法。
* 建议优先使用PageObject模式，方便后期代码维护
* 如需在自定义的Page类中使用driver则需要继承Page类，否则无需继承
    * 如继承Page类，实例化时需要传入driver参数

### IOS APP 测试

```shell
import qrunner
from qrunner import IosElement, story, title


class HomePage:
    ad_close_btn = IosElement(label='close white big', desc='首页广告关闭按钮')
    bottom_my = IosElement(label='我的', desc='首页底部我的入口')


@story('首页')
class TestClass(qrunner.IosTestCase):

    def start(self):
        self.hp = HomePage()

    @title('从首页进入我的页')
    def testcase(self):
        self.hp.ad_close_btn.click()
        self.hp.bottom_my.click()
        self.assertText('我的订单')


if __name__ == '__main__':
    qrunner.main(
        ios_device_id='00008101-000E646A3C29003A',
        ios_pkg_name='com.qizhidao.company'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.IosTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertText`、`assertElement` 等断言方法。
* 建议优先使用PageObject模式，方便后期代码维护
* 如需在自定义的Page类中使用driver则需要继承Page类，否则无需继承
    * 如继承Page类，实例化时需要传入driver参数

### Web 测试

```shell
import qrunner
from qrunner import WebElement, story, title, Page


class PatentPage(Page):
    search_input = WebElement(tid='driver-home-step1', desc='查专利首页输入框')
    search_submit = WebElement(tid='driver-home-step2', desc='查专利首页搜索确认按钮')

    def open(self):
        self.driver.open_url()


@story('专利检索')
class TestClass(qrunner.WebTestCase):
    
    def start(self):
        self.pp = PatentPage(self.driver)
    
    @title('专利简单检索')
    def testcase(self):
        self.pp.open()
        self.pp.search_input.set_text('无人机')
        self.pp.search_submit.click()
        self.assertTitle('无人机专利检索-企知道')


if __name__ == '__main__':
    qrunner.main(
        base_url='https://www-pre.qizhidao.com',
        executable_path='/Users/UI/Documents/chromedriver'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.WebTestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertTitle`、`assertUrl` 和 `assertText`等断言方法。
* 建议优先使用PageObject模式，方便后期代码维护
* 如需在自定义的Page类中使用driver则需要继承Page类，否则无需继承
    * 如继承Page类，实例化时需要传入driver参数

### HTTP 测试

```python
import qrunner
from qrunner import title, file_data, story


@story('PC站首页')
class TestClass(qrunner.TestCase):

    @title('查询PC站首页banner列表')
    @file_data('card_type', 'data.json')
    def test_getToolCardListForPc(self, card_type):
        path = '/api/qzd-bff-app/qzd/v1/home/getToolCardListForPc'
        payload = {"type": card_type}
        self.post(path, json=payload)
        self.assertEq('code', 0)


if __name__ == '__main__':
    qrunner.main(
        base_url='https://www-pre.qizhidao.com'
    )
```

__说明：__

* 创建测试类必须继承 `qrunner.TestCase`。
* 测试用例文件命名必须以 `test` 开头。
* qrunner的封装了`assertEq`、`assertLenEq` 和 `assertLenGt`等断言方法。

### Run the test

```python
import qrunner

qrunner.main()  # 默认运行当前测试文件，安卓和IOS第一次运行会报错，之后就可以了
qrunner.main(case_path="./")  # 当前目录下的所有测试文件
qrunner.main(case_path="./test_dir/")  # 指定目录下的所有测试文件
qrunner.main(case_path="./test_dir/test_api.py")  # 指定目录下的测试文件
```

### 感谢

感谢从以下项目中得到思路和帮助。

* [seldom](https://github.com/SeldomQA/seldom)

* [selenium](https://www.selenium.dev/)

* [uiautomator2](https://github.com/openatx/uiautomator2)
  
* [facebook-wda](https://github.com/openatx/facebook-wda)

* [requests](https://github.com/psf/requests)

# 开始

## 快速开始

### 基本规范

`qrunner`继承`pytest`单元测试框架，所以他的编写规范与[pytest](https://www.osgeo.cn/pytest/contents.html#full-pytest-documentation)
基本保持一致。

```shell
# test_sample.py
import qrunner

class TestYou(qrunner.TestCase):
    def test_case(self):
        """a simple test case """
        assert 1+1 == 2

if __name__ == '__main__':
    seldom.main()
```

基本规范：
1. 创建测试类`TestYou`并继承`qrunner.TestCase`类，必须以`Test`开头
2. 创建测试方法`test_case`, 必须以`test`开头。
3. `qrunner.mian()`是框架运行的入口方法，接下来详细介绍。

### `main()` 方法
`main()`方法是seldom运行测试的入口, 它提供了一些最基本也是最重要的配置。

```python
import qrunner
# ...
if __name__ == '__main__':
    qrunner.main(
      android_id=None,
      android_pkg=None,
      ios_id=None,
      ios_pkg=None,
      base_url=None,
      headers=None,
      headless=None,
      browser='chrome',
      executable_path=None,
      timeout=10,
      case_path=None,
      rerun=0,
      concurrent=False,
    )
```

__参数说明__

* android_id: 安卓设备id，通过adb devices命令获取
* android_pkg: 安卓应用包名，通过adb shell pm list packages命令获取
* ios_id: IOS设备id，通过tidevice list命令获取
* ios_pkg: IOS应用包名，通过tidevice applist命令获取
* browser: 浏览器类型，默认chrome，还支持firefox、edge、safari等
* case_path: 测试用例路径
* rerun: 失败重试次数
* concurrent: 是否并发执行用例
* base_url: 默认域名
* executable_path: 浏览器驱动程序路径
* headers: 默认请求头, {
    "login_headers": {},
    "visit_headers": {}
}
* timeout: 超时时间
* headless: 浏览器是否后台运行

### 运行测试

1. 运行当前文件中的用例

创建 `test_sample.py` 文件，在要文件中使用`main()`方法，如下：

```py
# test_sample.py
import qrunner

class TestYou(qrunner.TestCase):
    
    def test_case(self):
        """a simple test case """
        assert 1+1 == 2
        
if __name__ == '__main__':
    qrunner.main()  # 默认运行当前文件中的用例
```

`main()`方法默认运行当前文件中的所有用例。

```shell
> python test_sample.py      # 通过python命令运行
```

2. 指定运行目录、文件

可以通过`path`参数指定要运行的目录或文件。
   
```py
# run.py
import qrunner

qrunner.main(case_path="./")  # 指定当前文件所在目录下面的用例。
qrunner.main(case_path="./test_dir/")  # 指定当前目录下面的test_dir/ 目录下面的用例。
qrunner.main(case_path="./test_dir/test_sample.py")  # 指定测试文件中的用例。
qrunner.main(case_path="D:/seldom_sample/test_dir/test_sample.py")  # 指定文件的绝对路径。
```
* 运行文件
```shell
> python run.py
```

### 失败重跑

Seldom支持`错误`&`失败`重跑。

```python
# test_sample.py
import qrunner

class TestYou(qrunner.TestCase):
  
    def test_error(self):
        """error case"""
        assert a == 2
        
    def test_fail(self):
        """fail case """
        assert 1+1 == 3
        
if __name__ == '__main__':
    qrunner.main(rerun=3)
```

参数说明：

* rerun: 指定重跑的次数，默认为 `0`。

```shell
> python test_sample.py

/Users/UI/PycharmProjects/qrunner_new_gitee/venv/bin/python /Users/UI/PycharmProjects/qrunner_new_gitee/test_api.py
2022-10-08 11:59:24,673 - root - INFO - 执行用例
2022-10-08 11:59:24,738 - root - INFO - 用例路径: /Users/UI/PycharmProjects/qrunner_new_gitee/test_api.py
2022-10-08 11:59:24,738 - root - INFO - ['/Users/UI/PycharmProjects/qrunner_new_gitee/test_api.py', '-sv', '--reruns', '3', '--alluredir', 'allure-results', '--clean-alluredir']
============================= test session starts ==============================
platform darwin -- Python 3.9.10, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/UI/PycharmProjects/qrunner_new_gitee/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/UI/PycharmProjects/qrunner_new_gitee
plugins: xdist-2.5.0, forked-1.4.0, allure-pytest-2.9.45, rerunfailures-10.2, dependency-0.5.1, ordering-0.6
collecting ... collected 2 items

test_api.py::TestYou::test_error 2022-10-08 11:59:24,833 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,838 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,838 - root - DEBUG - [run_time]: 0.00 s
RERUN
test_api.py::TestYou::test_error 2022-10-08 11:59:24,839 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,841 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,841 - root - DEBUG - [run_time]: 0.00 s
RERUN
test_api.py::TestYou::test_error 2022-10-08 11:59:24,842 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,844 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,844 - root - DEBUG - [run_time]: 0.00 s
RERUN
test_api.py::TestYou::test_error 2022-10-08 11:59:24,845 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,846 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,846 - root - DEBUG - [run_time]: 0.00 s
FAILED
test_api.py::TestYou::test_fail 2022-10-08 11:59:24,848 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,849 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,850 - root - DEBUG - [run_time]: 0.00 s
RERUN
test_api.py::TestYou::test_fail 2022-10-08 11:59:24,851 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,853 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,853 - root - DEBUG - [run_time]: 0.00 s
RERUN
test_api.py::TestYou::test_fail 2022-10-08 11:59:24,855 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,856 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,856 - root - DEBUG - [run_time]: 0.00 s
RERUN
test_api.py::TestYou::test_fail 2022-10-08 11:59:24,858 - root - DEBUG - [start_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,860 - root - DEBUG - [end_time]: 2022-10-08 11:59:24
2022-10-08 11:59:24,860 - root - DEBUG - [run_time]: 0.00 s
FAILED

=========================== short test summary info ============================
FAILED test_api.py::TestYou::test_error - NameError: name 'a' is not defined
FAILED test_api.py::TestYou::test_fail - assert 2 == 3
========================== 2 failed, 6 rerun in 0.04s ==========================
```

### 测试报告

qrunner 默认在运行测试文件下自动创建`allure-results`目录，需要通过allure serve命令生成html报告

* 运行测试用例前
```shell
mypro/
└── test_sample.py
```
* 运行测试用例后
```shell
mypro/
├── allure-results/
│   ├── 0a1430a7-aafd-4d4a-984c-b2b435835fba-container.json
│   ├── 5c1bbb85-afd5-4f7a-a470-17ad4b0a2870-attachment.txt
└── test_sample.py
```
命令行执行allure serve allure-results，自动调起浏览器打开测试报告，查看测试结果。
![](./test_report.jpg)

## 高级用法

### 随机测试数据

测试数据是测试用例的重要部分，有时不能把测试数据写死在测试用例中，比如注册新用户，一旦执行过用例那么测试数据就已经存在了，所以每次执行注册新用户的数据不能是一样的，这就需要随机生成一些测试数据。

qrunner 提供了随机获取测试数据的方法。

```python
import qrunner
from qrunner import testdata


class TestYou(qrunner.TestCase):
    
    def test_case(self):
        """a simple test case """
        word = testdata.get_word()
        print(word)
        
if __name__ == '__main__':
    qrunner.main()
```

通过`get_word()` 随机获取一个单词，然后对这个单词进行搜索。

**更多的方法**

```python
from qrunner.testdata import *
# 随机一个名字
print("名字：", first_name())
print("名字(男)：", first_name(gender="male"))
print("名字(女)：", first_name(gender="female"))
print("名字(中文男)：", first_name(gender="male", language="zh"))
print("名字(中文女)：", first_name(gender="female", language="zh"))
# 随机一个姓
print("姓:", last_name())
print("姓(中文):", last_name(language="zh"))
# 随机一个姓名
print("姓名:", username())
print("姓名(中文):", username(language="zh"))
# 随机一个生日
print("生日:", get_birthday())
print("生日字符串:", get_birthday(as_str=True))
print("生日年龄范围:", get_birthday(start_age=20, stop_age=30))
# 日期
print("日期(当前):", get_date())
print("日期(昨天):", get_date(-1))
print("日期(明天):", get_date(1))
# 数字
print("数字(8位):", get_digits(8))
# 邮箱
print("邮箱:", get_email())
# 浮点数
print("浮点数:", get_float())
print("浮点数范围:", get_float(min_size=1.0, max_size=2.0))
# 随机时间
print("当前时间:", get_now_datetime())
print("当前时间(格式化字符串):", get_now_datetime(strftime=True))
print("未来时间:", get_future_datetime())
print("未来时间(格式化字符串):", get_future_datetime(strftime=True))
print("过去时间:", get_past_datetime())
print("过去时间(格式化字符串):", get_past_datetime(strftime=True))
# 随机数据
print("整型:", get_int())
print("整型32位:", get_int32())
print("整型64位:", get_int64())
print("MD5:", get_md5())
print("UUID:", get_uuid())
print("单词:", get_word())
print("单词组(3个):", get_words(3))
print("手机号:", get_phone())
print("手机号(移动):", get_phone(operator="mobile"))
print("手机号(联通):", get_phone(operator="unicom"))
print("手机号(电信):", get_phone(operator="telecom"))
```

* 运行结果

```shell
名字： Hayden
名字（男）： Brantley
名字（女）： Julia
名字（中文男）： 觅儿
名字（中文女）： 若星
姓: Lee
姓（中文）: 白
姓名: Genesis
姓名（中文）: 廉高义
生日: 2000-03-11
生日字符串: 1994-11-12
生日年龄范围: 1996-01-12
日期（当前）: 2022-09-17
日期（昨天）: 2022-09-16
日期（明天）: 2022-09-18
数字(8位): 48285099
邮箱: melanie@yahoo.com
浮点数: 1.5315717275531858e+308
浮点数范围: 1.6682402084146244
当前时间: 2022-09-17 23:33:22.736031
当前时间(格式化字符串): 2022-09-17 23:33:22
未来时间: 2054-05-02 11:33:47.736031
未来时间(格式化字符串): 2070-08-28 16:38:45
过去时间: 2004-09-03 12:56:23.737031
过去时间(格式化字符串): 2006-12-06 07:58:37
整型: 7831034423589443450
整型32位: 1119927937
整型64位: 3509365234787490389
MD5: d0f6c6abbfe1cfeea60ecfdd1ef2f4b9
UUID: 5fd50475-2723-4a36-a769-1d4c9784223a
单词: habitasse
单词组（3个）: уж pede. metus.
手机号: 13171039843
手机号(移动): 15165746029
手机号(联通): 16672812525
手机号(电信): 17345142737
```

### 用例的依赖

**depend**

`depend` 装饰器用来设置依赖的用例。

```python
import qrunner
from qrunner import depend


class TestDepend(qrunner.TestCase):
    
    @depend(name='test_001')
    def test_001(self):
        print("test_001")
        
    @depend("test_001", name='test_002')
    def test_002(self):
        print("test_002")
        
    @depend(["test_001", "test_002"])
    def test_003(self):
        print("test_003")
        
if __name__ == '__main__':
    qrunner.main()
```

* 被依赖的用例需要用name定义被依赖的名称，因为本装饰器是基于pytest.mark.dependency，它会出现识别不了被装饰的方法名的情况
  ，所以通过name强制指定最为准确
  ```@depend(name='test_001')```
* `test_002` 依赖于 `test_001` , `test_003`又依赖于`test_002`。当被依赖的用例，错误、失败、跳过，那么依赖的用例自动跳过。
* 如果依赖多个用例，传入一个list即可
```@depend(['test_001', 'test_002'])```
  
### 发送邮件

```python
import qrunner
from qrunner import Mail


if __name__ == '__main__':
    qrunner.main()
    mail = Mail(host='xx.com', user='xx@xx.com', password='xxx')
    mail.send_report(title='Demo项目测试报告', report_url='https://www.baidu.com', receiver_list=['xx@xx.com'])
```

- title：邮件标题
- report_url: 测试报告的url
- receiver_list: 接收报告的用户列表


### 发送钉钉

```python
import qrunner
from qrunner import DingTalk


if __name__ == '__main__':
    qrunner.main()
    dd = DingTalk(secret='xxx',
                  url='xxx')
    dd.send_report(msg_title='Demo测试消息', report_url='https://www.baidu.com')
```

- `secret`: 如果钉钉机器人安全设置了签名，则需要传入对应的密钥。
- `url`: 钉钉机器人的Webhook链接
- `msg_title`: 消息标题
- `report_url`: 测试报告url

## 数据驱动

数据驱动是测试框架非常重要的功能之一，它可以有效的节约大量重复的测试代码。qrunner针对该功能做强大的支持。

### @data()方法

当测试数据量比较少的情况下，可以通过`@data()`管理测试数据。


**参数化测试用例**

```python
import qrunner
from qrunner import data


class TestDataDriver(qrunner.TestCase):
    @data('name,keyword', [
        ("First case", "qrunner"),
        ("Second case", "selenium"),
        ("Third case", "unittest"),
    ])
    def test_tuple_data(self, name, keyword):
        """
        Used tuple test data
        :param name: case desc
        :param keyword: case data
        """
        print(f"test data: {name} + {keyword}")

    @data('name,keyword', [
        ["First case", "qrunner"],
        ["Second case", "selenium"],
        ["Third case", "unittest"],
    ])
    def test_list_data(self, name, keyword):
        """
        Used list test data
        """
        print(f"test data: {name} + {keyword}")

    @data('json', [
        {"scene": 'First case', 'keyword': 'qrunner'},
        {"scene": 'Second case', 'keyword': 'selenium'},
        {"scene": 'Third case', 'keyword': 'unittest'},
    ])
    def test_dict_data(self, json):
        """
        used dict test data
        """
        print(f"case desc: {json['scene']}")
        print(f"test data: {json['keyword']}")
    
    @data('param', [
            ("First case", "qrunner"),
            ("Second case", "selenium"),
            ("Third case", "unittest"),
        ])
    def test_tuple_single_param(self, param):
        """
        Used tuple test data
        :param name: case desc
        :param keyword: case data
        """
        print(f"test data: {param[0]} + {param[1]}")
    
    @data('param_a', [1, 2])
    @data('param_b', ['c', 'd'])
    def test_cartesian_product(self, param_a, param_b):
        """
        笛卡尔积
        :param param_a: case desc
        :param param_b: case data
        """
        print(f"test data: {param_a} + {param_b}")
```

通过`@data()` 装饰器来参数化测试用例。

### @file_data() 方法

当测试数据量比较大的情况下，可以通过`@file_data()`管理测试数据。

**JSON 文件参数化**

seldom 支持将`JSON`文件的参数化。

json 文件：

```json
{
  "login1": [
    [1, 2],
    [3, 4]
  ],
  "login2": [
    {"username":  1, "password":  2},
    {"username":  3, "password": 4}
  ]
}

```

> 注：`login1` 和 `login2` 的调用方法一样。 区别是前者更简洁，后者更易读。
```python
import qrunner
from qrunner import file_data


class TestYou(qrunner.TestCase):

    @file_data("login1")
    def test_default(self, login1):
        """文件名使用默认值
        file: 'data.json'
        """
        print(login1[0], login1[1])

    @file_data(key="login2", file='data.json')
    def test_full_param(self, login2):
        """参数都填上"""
        print(login2["username"], login2["password"])
```

- key: 指定字典的 key，默认不指定解析整个 JSON 文件。
- file : 指定 JSON 文件的路径。

# Web UI 测试

## 浏览器与驱动

### 下载浏览器驱动

> qrunner集成webdriver_manager管理浏览器驱动。
和Selenium一样，在使用qrunner运行自动化测试之前，需要先配置浏览器驱动，这一步非常重要。

seldom 集成 [webdriver_manager](https://github.com/SergeyPirogov/webdriver_manager) ，提供了`chrome/firefox/edge`浏览器驱动的自动下载。

__自动下载__

如果你不配置浏览器驱动也没关系，seldom会根据你使用的浏览器版本，自动化下载对应的驱动文件。

* 编写简单的用例

```python
import qrunner
from qrunner import WebElement, Page


class DemoPage(Page):
    url = 'https://www.bing.com'
    input = WebElement(id_='sb_form_q', desc='输入框')


class TestBing(qrunner.WebTestCase):

    def start(self):
        self.p = DemoPage(self.driver)

    def test_bing_search(self):
        """selenium api"""
        self.p.open()
        self.p.input.set_and_enter('seldom')
        self.sleep(2)
        self.assertTitle("seldom - 搜索")


if __name__ == '__main__':
    qrunner.main(browser="chrome")
```

qrunner 检测到的`Chrome`浏览器后，自动化下载对应版本的驱动，并保存到本地，以便于下次执行的时候就不需要下载了。
并且，非常贴心的将`chromedriver`的下载地址从 google 切换成了 taobao 的镜像地址。

__手动下载__

通过`qrunner`命令下载浏览器驱动。

```shell
敬请期待
```

指定浏览器驱动

```python
import qrunner


if __name__ == '__main__':
    qrunner.main(browser="chrome",
                 executable_path='/Users/UI/Documents/chromedriver')
```

### 指定不同的浏览器

我们运行的自动化测试不可能只在一个浏览器下运行，我们分别需要在chrome、firefox浏览器下运行。在qrunner中需要只需要修改一个配置即可。

```python
import qrunner
# ……
if __name__ == '__main__':
    qrunner.main(browser="chrome") # chrome浏览器,默认值
    qrunner.main(browser="gc")     # chrome简写
    qrunner.main(browser="firefox") # firefox浏览器
    qrunner.main(browser="ff")      # firefox简写
    qrunner.main(browser="edge")    # edge浏览器
    qrunner.main(browser="safari")  # safari浏览器
```
在`main()`方法中通过`browser`参数设置不同的浏览器，默认为`Chrome`浏览器。

## qrunner API

### 查找元素

* id_
* name
* class_name
* tag
* link_text
* partial_link_text
* css
* xpath

__使用方式__

```python
from qrunner import WebElement

WebElement(id_="kw", desc='xxx')
WebElement(name="wd", desc="xxx")
WebElement(class_name="s_ipt", desc="xxx")
WebElement(tag_name="input", desc="xxx")
WebElement(xpath="//input[@id='kw']", desc="xxx")
WebElement(css="#kw", desc="xxx")
WebElement(link_text="hao123", desc='xxx')
WebElement(partial_link_text="hao", desc='xxx')
```

__帮助信息__

* [CSS选择器](https://www.w3school.com.cn/cssref/css_selectors.asp)
* [xpath语法](https://www.w3school.com.cn/xpath/xpath_syntax.asp)

__使用下标__

有时候无法通过一种定位找到单个元素，那么可以通过`index`指定一组元素中的第几个。

```python
from qrunner import WebElement

WebElement(tag_name="input", index=7, desc="xxx")
```

通过`tag_name="input"`匹配出一组元素， `index=7` 指定这一组元素中的第8个，`index`默认下标为`0`。

### fixture

有时自动化测试用例的运行需要一些前置&后置步骤，seldom提供了相应的方法。

__start & end__

针对每条用例的fixture，可以放到`start()/end()`方法中。

```python
import qrunner
from qrunner import Page, WebElement


class DemoPage(Page):
    url = 'https://www.baidu.com'
    input = WebElement(id_='kw', desc='输入框')

class TestCase(qrunner.WebTestCase):
    def start(self):
        print("一条测试用例开始")
        self.dp = DemoPage(self.driver)
        
    def end(self):
        print("一条测试结果")
        
    def test_search(self):
        self.dp.open()
        self.dp.input.set_and_enter('qrunner')
```

__start_class & end_class__

针对每个测试类的fixture，可以放到`start_class()/end_class()`方法中。

```python
import qrunner
from qrunner import Page, WebElement


class DemoPage(Page):
    url = 'https://www.baidu.com'
    input = WebElement(id_='kw', desc='输入框')


class TestCase(qrunner.WebTestCase):
    
    @classmethod
    def start_class(cls):
        print("测试类开始执行")
        cls.dp = DemoPage(cls.driver)
        
    @classmethod
    def end_class(cls):
        print("测试类结束执行")
        
    def test_search(self):
        self.dp.open()
        self.dp.input.set_and_enter('qrunner')
```

> 警告：不要把用例的操作步骤写到fixture方法中! 因为它不属于某条用例的一部分，一旦里面的操作步骤运行失败，测试报告都不会生成。
### 断言

seldom 提供了一组针对Web页面的断言方法。

__使用方法__

```
# 断言标题是否等于"title"
self.assertTitle("title")

# 断言标题是否包含"title"
self.assertInTitle("title")

# 断言URL是否等于
self.assertUrl("url")

# 断言URL是否包含
self.assertInUrl("url")

# 断言页面包含“text”
self.assertText("text")

# 断言页面不包含“text”
self.assertNotText("text")

# 断言警告是否存在"text" 提示信息
self.assertAlertText("text")

# 断言元素是否存在
self.assertElement(css="#kw")

# 断言元素是否不存在
self.assertNotElement(css="#kwasdfasdfa")
```

### WebDriverAPI

qrunner简化了selenium中的API，使操作Web页面更加简单。

大部分API都由`WebDriver`类提供：

```python
import qrunner
from qrunner import WebElement


class TestCase(qrunner.WebTestCase):
    
    def test_case(self):
        self.driver.open_url("https://www.baidu.com") # 打开页面
        self.driver.back() # 返回上一页
        self.driver.screenshot("登录页") # 截屏
        self.driver.max_window() # 页面全屏
        self.driver.set_window(1920, 1080) # 设置页面宽高
        old = self.driver.get_windows() # 获取当前页面句柄列表
        self.driver.switch_window(old) # 切换当前页面句柄
        self.driver.window_scroll(1920, 1080) # 设置页面滚动范围
        self.driver.switch_to_frame('xxx_id') # 切换到iframe
        self.driver.switch_to_frame_out() # 从iframe退回顶层页面
        self.driver.execute_js('alert("hell")') # 执行js脚本
        self.driver.click(WebElement(id_='kw', desc='xxx')) # 强制点击一个元素，在元素本阻挡等情况下使用
        self.driver.quit() # 退出浏览器
        self.driver.close() # 关闭当前页签
        self.driver.add_cookies([{"name": "xxx", "value": "xxx"}]) # 添加cookie
        self.driver.get_cookies() # 获取当前cookie列表
        self.driver.get_cookie('cookie_name') # 获取指定的cookie
        self.driver.delete_all_cookies() # 清空所有cookie
        self.driver.delete_cookie('cookie_name') # 删除指定的cokkie
        self.driver.refresh() # 刷新页面
        print(self.driver.page_content) # 获取当前页面xml
        self.driver.get_title() # 获取页面标题
        self.driver.get_url() # 获取页面链接
        self.driver.get_alert_text() # 获取alert中的文本
        self.driver.accept_alert() # 同意
        self.driver.dismiss_alert() # 拒绝
```

### WebElement操作

qrunner把控件都封装成了WebElement对象，控件的操作封装成了WebElement对象的方法

```python
import qrunner
from qrunner import WebElement


class TestCase(qrunner.WebTestCase):

    def start(self):
        self.element = WebElement(id_='kw', desc='xxx')

    def test_case(self):
        self.element.get_elements()  # 获取定位到的控件列表
        self.element.get_element()  # 获取第一个定位到的控件
        self.element.exists()  # 判断控件是否存在
        self.element.click()  # 单击
        self.element.click_exists()  # 如果控件存在才单击
        self.element.slow_click()  # 慢慢移动到控件上，然后单击
        self.element.right_click()  # 右键单击
        self.element.move_to_elem()  # 鼠标移动到控件上
        self.element.click_and_hold()  # 长按
        self.element.drag_and_drop(100, 100)  # 拖动到
        self.element.double_click()  # 双击
        self.element.set_text('xxx')  # 单击控件并输入
        self.element.set_and_enter('xxx')  # 输入后点击enter
        self.element.clear_text()  # 清空输入框
        self.element.enter()  # 选中控件，点击enter
        self.element.select_all()  # 全选操作
        self.element.cut()  # 剪切
        self.element.copy()  # 复制
        self.element.paste()  # 粘贴
        self.element.backspace()  # 退格
        self.element.delete()  # 删除一个字符
        self.element.tab()  # 点一下tab
        self.element.space()  # 点击space建
        print(self.element.rect) # 返回控件左上角坐标和宽高
        print(self.element.get_attr('xxx')) # 控件的属性
        print(self.element.get_display()) # 控件的display属性
        print(self.element.text) # 控件的文本
        self.element.select_index(0) # 下拉列表选择
        self.element.select_text('xx') # 下拉列表选择
        self.element.submit() # 表单提交
```
