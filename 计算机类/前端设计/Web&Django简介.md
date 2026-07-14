# Web 和 Django 

--- 
本笔记工科创项目："Python 项目开发实践 -- Web 网站的开发" 的学习笔记，内有介绍一些 Web 和 Django 框架的一些基本知识
<div align="right">作者：DoroKnight</div>

---
## 一、Web
### 简介
Web 是一种通过浏览器访问和运行的应用程序，存储在远程服务器上。Web 应用具有如下特点：
1. **易于访问**：Web应用可以从任何设备和浏览器访问，不占用本地存储空间。
2. **开发高效**：开发过程简单，适用于所有现代浏览器和设备，降低了开发成本。

这里需要区分一下 URL 和 Web 的区别：
1. **URL**：Uniform Resource Locator，统一资源定位符
   URL 是互联网上资源的地址，比如 [bilibili官网](https://www.bilibili.com/) 的地址 https://www.bilibili.com，就是一个 URL，它指向了 bilibili 的网页。同时，URL 不仅仅可以指向网页，它也可以指向**图片、视频或者文件**，有点像 C/C++ 中的指针，我们可以通过 URL 顺藤摸瓜找到我们的目标资源
2. **Web**：我们常说的**万维网**
   Web 是一种基于互联网的**信息系统**，它通过 http/https 协议来提供网页、图片等资源，
   他有四个组成部分：
   1. **网页**(HTML)
   2. **样式表**(CSS)
   3. **脚本**(JavaScript)
   4. **服务器端服务**(Web server)

Web 的组成个可以使用下面的图例来解释：
```
浏览器 (并不是 Web 的组成部分，但是是访问 Web 的客户端)
   │
   ▼
HTML + CSS + JavaScript
   │
   ▼
Web Server（服务器）
```

### Web 组成成分解释
#### 1. HTML -- 内容与结构
**HTML（HyperText Markup Language）负责描述网页的内容和结构。**
```html
<h1> 欢迎来到我的主页 </h1>
<p> 这是一个段落 </p>
<button> 点击我 </button>
```
上述的三个语句会被浏览器(Browser)理解为：
- 一个标题
- 一个段落
- 一个按钮

HTML 负责决定
- 页面有什么元素
- 元素之间怎么组织
- 内容是什么

**HTML 是网站的骨架，它的看着很像编程语言，但并不是**

#### 2. CSS -- 样式和外观
**CSS（Cascading Style Sheets）负责控制网页长什么样。**
```css
h1 {
    color: blue;
    font-size: 40px;
}
```
语句效果：
- 标题变蓝
- 字体变大

CSS 决定的是：
- 颜色
- 字体
- 间距
- 布局
- 动画

**CSS 是网站的"设计师"，同 HTML 一样，并不是一门编程语言**

#### 3. JavaScript -- 行为与交互
**JavaScript 负责让网页动起来**
```javascript
button.onclick = function() {
    alert("你好");
};
```
JavaScript 可以实现：
- 点击事件
- 表单验证
- 动态加载数据
- 聊天功能
- 游戏逻辑

#### 4. Web Server -- 提供资源
**Web Server 负责向客户端（浏览器[^1]）提供资源，而这些资源可能包括 HTML、CSS、JavaScript，以及图片、视频、API 数据等。**
下面是流程：
```
浏览器
   │ 请求
   ▼
服务器
   │ 返回HTML/CSS/JS
   ▼
浏览器显示网页
```

Web Server 负责：
- 存储网页文件（存储功能）
- 存储数据库数据
- 处理登录
- 处理支付
- 提供 API [^2]

Web Server 才是真正的核心，它负责**存储数据，处理请求，提供访问模式（API）**。

#### 5. 访问流程
当我们访问一个网址(URL)的流程如下：
```
① 浏览器访问URL
        │
        ▼
② Web服务器收到请求
        │
        ▼
③ 返回HTML
        │
        ▼
④ 浏览器发现需要CSS和JS
        │
        ▼
⑤ 再次请求CSS和JS文件
        │
        ▼
⑥ 浏览器执行JS、应用CSS
        │
        ▼
⑦ 页面显示并可交互
```

---
## 二、Django 框架
*Django* 框架是一个流行的开源 Web 应用框架，由 Python 语言编写。它实现了代码复用，便于 Web 应用（网站）的快捷开发。Django 的官方定位是：*The web framework for perfectionists with deadlines.*，即**帮你快速构建功能完整的网站。**
Django 强调：
- 快速开发
- 安全性
- 数据库操作
- 后台管理

Django 有以下的优势：
1. **易于项目管理**：Django 能够通过简单的命令对项目进行管理，例如创建项目、创建应用等操作。
2. **灵活的路由系统**：Django 能够非常便捷地定义各种形式的访问地址。
3. **便捷数据库功能**：Django 的数据库操作方法简单，易于数据存储和查询。

官方网址：[Django](https://www.djangoproject.com/)

### Django 在 Web 开发中对应的位置
网站的结构如下：
```
浏览器 (客户端)
   │
   ▼
Web Server (核心处理器)
   │
   ▼
后端程序 (运行逻辑)
   │
   ▼
数据库 (数据存储)
```
Django 在其中就属于**后端程序**，除了 Django 以外，还有下面的几个开源模板：
```
浏览器
   │
   ▼
Nginx
   │
   ▼
Django
   │
   ▼
PostgreSQL
```
其中：
- Nginx[^3]：接收 HTTP 请求
- Django：处理业务逻辑
- PostgreSQL[^4]：存储数据

### Django 的框架与项目文件文件
#### 1. Django 框架：
**Django的核心架构如下**：
```
URL
 │
 ▼
View
 │
 ▼
Model
 │
 ▼
Database
```
Django 不同于其他的框架采用 MVC[^5] 模式，它采用的是 MTV 架构：
```
Model
Template
View
```
1. Model(模型)
   Model 不是 AI 这种大模型，而是开发者自行定义的一系列操作与映射。Django 的 Model 是用来处理数据库交互的，这样我们就不用手写 SQL 了
2. View(视图)
   View 负责处理请求
3. Template(模板)
   Template 负责生成的是模板，先编写对应的 html 命令，然后处理命令后交给浏览器

除了以上这些功能外，还有 Django 最著名的功能：**ORM**（对象关系映射）
ORM 的出现解决了一个棘手的问题：**Python 操作的是对象（Object），数据库存储的是表（Relation/Table），两者的数据结构不一样。**

ORM 有以下优点：
1. **不需要大量的SQL**：很多操作像写 Python 代码一样轻松就能完成。
2. **跨数据库**：无论是 PostgreSQL、MySQL、SQLite 都能运行
3. **与 Python 对象统一**：直接使用对象即可，而不是使用复杂的 SQL 语言

#### 2. 项目文件
Django 的项目文件大致结构如下：
```
mysite/
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
```
应用结构如下：
```
blog/
├── models.py
├── views.py
├── admin.py
├── urls.py
├── tests.py
```

## 三、项目流程
**项目工具**：PyCharm
**运行终端**：Windows Powershell
**Python版本**：Python 3.14.4
**声明**：本项目使用命令均为 Powershell 命令，Linux 或 类Unix 系统(MacOS)可能有所差别

### 1. 新建 PyCharm 工程
![PyCharm工程建立](picture/image1.png)
效果图：
![PyCharm项目图](picture/image2.png)

### 2. 安装 Django 框架
注意 ：<由于 Python 的 PEP 668 协定，一下操作都必须在虚拟环境中进行

#### 配置虚拟环境
在进入新建的项目以后，PyCharm会自动为你建好虚拟环境，并直接进入虚拟环境，若要自己配置虚拟环境，使用下方命令：
```powershell
# Navigate to your project directory
cd PATH_OF_YOUR_PROJECT

# Create a virtual environment named ".venv"
python -m venv .venv

# Bypass execution policy for the current PowerShell session only 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Execute the PowerShell activatation script 
.\.venv\Script\Activate.ps1
```
配置完成后，终端中在你的用户名前会出现`(.venv)`的字样，如图所示
![环境配置成功](picture/image3.png)

#### 使用终端安装 Django
**声明**：本人 PyCharm 的版本可能老旧，不适合使用 PPT 中的方式，因此采用终端操作
在终端中输入下面命令：
```powershell
pip install django
```
等待下载即可，下面是效果图：
![效果图](picture/image4.png)

#### 新建 Django 项目
使用 Alt + F12 在 PyCharm 中叫出终端，在终端中输入下面的指令
```powershell
# Create a project 
django-admin startprojrct HomePage

# enter the project directory
cd HomePage

# Create a new application named "mine"
python manage.py startapp mine
```
运行完成后会有以下结构
![结构图](picture/image5.png)

---
### 3. 编写 Web 文件
#### 添加 APP 到项目
第一步： 进入 `setting.py` 文件中，找到 `INSTALLED_APPS`，在最后面加上 `'mine'`。注意，**最好是在 'mine' 的后面加上一个英文逗号**

#### 编写视图文件
这里是业务处理的核心，负责接受 Web 请求和返回 Web 对应的响应
完整代码见[附录View](#附录view)

#### 编写模型文件
模型文件 `model.py` 定义了用户类，是用来存储用户名(username)和密码(password)的，完整代码见[附录Model](#附录model)

#### 编写导航文件
导航文件 `urls.py` 定义了 URL 路径和视图函数之间的映射关系，使用**列表**的数据结构进行存储。完整代码见[附录URLs](#附录urls)

#### 将 `HomePage` 目录标记为源代码根目录
为什么要标记源代码目录：
- **构建模块解析路径**
- **启用代码自动补全与静态分析**
- **消解未解析的引用伪报错**
- **支持重构与自动化工具链**

#### 创建 HTML 文件和静态资源文件
在 `mine` 文件夹下面，我们要创建两个子目录：
- `static`：存放静态文件，下有 `images` 文件夹来存放照片
- `templates`：存放 html 文件，下有以下三个文件
  - `homepage.html`
  - `login.html`
  - `scores.html`

三个 html 文件的完整代码见[附录HTML](#附录html)

#### 创建数据库表
在终端中依次运行下面的命令：
```powershell
# Create a database
python manage.py makemigrations
python manage.py migrate
```
创建完成数据库表以后，效果图如下：
![效果图](picture/image6.png)

运行下面的命令，保存用户信息：
```powershell
python manage.py shell
```
运行完成后会进入类似 Python 交互环境的界面，如下图：
![Python交互环境图](picture/image7.png)

进入后载进行下面的命令：
```python
>>> from mine.models import User
>>> User.objects.create(username = YOUR_USERNAME, password = YOUR_PASSWORD)
```
完成后效果图如下：
![创建账户效果图](picture/image8.png)

当然，你也可以创建多个账户，这样下面的提示符后面的数字就会变成对应的账户数。如果想要输出所有的账户，运行下面的命令：
```python
>>> users = User.objects.all()
>>> for user in users:
...     print(f"ID: {user.id}, Username: {user.username}, Password: {user.password}")
... 
```
完成上述步骤后，效果图如下：
![输出账户效果图](picture/image9.png)

若想停止创建，可以输入 `quit()` 或 `exit()` 或 `Ctrl + Z` 来停止进程，值得注意的是 `Ctrl + C` 在这里是不好使的。

### 4. 运行 Web
以上所有步骤结束以后，在终端输入以下命令来运行程序：
```powershell
python manage.py runserver 8888
```
**注意**：这里的 `8888` 是端口号，端口号是计算机网络中用于表示特定服务的逻辑编号
运行完成会有下面的输出：
![运行效果图](picture/image10.png)

这个时候，点击终端中的网址，我们就可以跳转到我们创建的 Web 中了。
**注意**：直接点击会出现报错界面，属于正常现象，因为我们并没有进入真正的个人主页：
![错误信息图](picture/image11.png)

此时我们可以在 URL 后面添加 `/homepage` ，这样就会正常显示我们的主页了。
![登陆效果图](picture/image12.png)

登录我们的账号以后，会进入这样的界面：
![成绩展示图](picture/image13.png)


---
[^1]: 浏览器(Browser)
    - **作用**：用户的客户端，用来发起 HTTP 请求和显示响应内容。
    - **例子**：Chrome、Edge、Safari
    - **功能**
        - 发送请求（URL + 方法 + 参数）
        - 渲染返回的 HTML/CSS/JS
        - 处理用户交互（点击、输入、提交表单）

[^2]: 什么是 API：**API**（Application Programming Interface，应用程序编程接口），本质上是**一套规定好的方式，让一个程序向另一个程序请求服务或数据**，Web 的 API 和 AI 用的 API 其实就是一个东西，都是客户端发出的"请求"，整个过程可以用下面的流程图解释
    ```
    顾客（浏览器/App）
            │
            ▼
    API（菜单 + 点餐规则）
            │
            ▼
    Web Server（服务员/餐厅前台系统）
            │
            ▼
    后端程序（厨师）
            │
            ▼
    数据库（仓库/冰箱）
    ```

[^3]: Nginx:
    - **作用**：Web 服务器 / 反向代理
    - **功能**：
        1.  接收浏览器发来的 HTTP 请求。
        2.  决定请求由自己处理（静态资源如图片、CSS）还是转发给后端应用（如 Django）。
        3.  提供负载均衡（多台 Django 服务器之间分发请求）。
        4.  缓存静态资源，提高性能。
    - **使用原因**：
        - Django 自带开发服务器只适合测试，不适合生产环境。
        - Nginx 更擅长处理大量并发请求和静态资源。

[^4]: PostgreSQL:
    - **作用**：关系型数据库
    - **功能**：
        1. 存储结构化数据（如用户信息、文章、评论）。
        2. 提供 SQL 查询接口。
        3. 保障数据一致性和安全。

[^5]: MVC: 即 **Model + View + Controller** 的模式 

---
## 附录View
```python
from django.shortcuts import render, redirect

# Create your views here.
from mine.models import User
from functools import wraps

def check_login(f):
    @wraps(f)
    def inner(request, *arg, **kwargs):
        if request.session.get('is_login') == '1':
            return f(request, *arg, **kwargs)
        else:
            return redirect('/login/')
    return inner

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        print(user)
        if user:
            request.session['is_login'] = '1'
            request.session['username'] = username
            request.session['user_id'] = user[0].id
            return render(request, 'scores.html')
    return render(request, 'login.html')

def index(request):
    return render(request, 'login.html')

```
注意这里开头的 import 不是 Django 默认的，我们额外导入的 `redirect` 函数
### 附录Model
```python
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
```

### 附录URLs
```python
from django.contrib import admin
from django.urls import path
from mine import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('homepage/', views.index),
]
```

### 附录HTML
1. `homepage.html` 文件：
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        {% load static %}
        <img src = "static/images/photo.jpg" height = "100", width = "100">

        <p style = "font-size: 30px;" style = "font-family: SimHei;">李华</p>
        <p style = "front-size : 20px;">2000年生，就读于上海交通大学XX学院......</p>
    </body>
    </html>
    ```
2. `login.html` 文件
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>

    <h1>欢迎登录！</h1>
    <form action="/login/" method="post">
        {% csrf_token %}
        <p>
            用户名：
            <input type="text" name="username">
        </p>
        <p>
            密码：
            <input type="text" name="password">
        </p>
        <p>
            <input type="submit" value="登录">
        </p>
        <hr>
    </form>
    </body>
    </html>
    ```
3. `scores.html` 文件
   ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>成绩单</title>
        <p>语文： 88</p>
        <p>数学： 92</p>
        <p>英语： 95</p>
    </head>
    <body>

    </body>
    </html>
   ```
   