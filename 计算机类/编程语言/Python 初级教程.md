<a id="python-初级教程"></a>

<div align="center">

# Python 初级教程
</div>

---

笔记内容以 Eric Matthes 的《Python Crash Course》第三版为主线，并结合现有 Python 3 学习内容进行整理。目标是保留完整知识点，同时作为基础语法、常用操作和项目流程的快速查阅笔记。若发现问题，欢迎指正，邮箱：[2312786648@qq.com](https://mail.qq.com/)
<div align="right">编者：DoroKnight</div>

---

<a id="目录"></a>

## 目录

- [Python 初级教程](#python-初级教程)
  - [目录](#目录)
  - [一、什么是Python](#一什么是python)
    - [1. 如何安装Python（Windows版）](#1-如何安装pythonwindows版)
    - [2. 应用领域](#2-应用领域)
  - [二、基础语法](#二基础语法)
    - [1. 字面量](#1-字面量)
    - [2. 注释](#2-注释)
    - [3. 变量](#3-变量)
      - [1. 定义](#1-定义)
      - [2. 定义变量](#2-定义变量)
      - [3. 变量特点](#3-变量特点)
      - [4. 命名规则](#4-命名规则)
    - [4. 查看数据类型](#4-查看数据类型)
    - [5. 运算符](#5-运算符)
    - [6. 转义符](#6-转义符)
    - [7. 占位符及有效数字保留](#7-占位符及有效数字保留)
      - [1. 基本语法格式：](#1-基本语法格式)
      - [2. 各个占位符详解](#2-各个占位符详解)
      - [3. 宽度控制 `%m`](#3-宽度控制-m)
      - [4. 精度控制 `%.n`](#4-精度控制-n)
      - [5. f-string用法（推荐）](#5-f-string用法推荐)
    - [8. 表达式](#8-表达式)
    - [9. 布尔数](#9-布尔数)
    - [10. None值](#10-none值)
      - [1. 含义](#1-含义)
      - [2. 应用](#2-应用)
    - [11. 代码风格与 Python 哲学](#11-代码风格与-python-哲学)
  - [三、数据容器](#三数据容器)
    - [1. 数据容器概述](#1-数据容器概述)
      - [1. 定义](#1-定义-1)
      - [2. 分类](#2-分类)
      - [3. 序列](#3-序列)
      - [4. 切片](#4-切片)
      - [5. 统计元素的数量](#5-统计元素的数量)
      - [6. 求最大元素和最小元素](#6-求最大元素和最小元素)
      - [7. 排序](#7-排序)
    - [2. 列表](#2-列表)
      - [1. 定义](#1-定义-2)
      - [2. 索引](#2-索引)
      - [3. 使用元素](#3-使用元素)
      - [4. 查找元素索引](#4-查找元素索引)
      - [5. 修改元素](#5-修改元素)
      - [6. 添加元素](#6-添加元素)
      - [7. 删除元素](#7-删除元素)
      - [8. 清空列表](#8-清空列表)
      - [9. 统计元素的数量](#9-统计元素的数量)
      - [10. 遍历列表](#10-遍历列表)
      - [11. 列表特点](#11-列表特点)
      - [12. 排序、反转与长度](#12-排序反转与长度)
      - [13. 切片与复制](#13-切片与复制)
    - [3. 元组](#3-元组)
      - [1. 定义](#1-定义-3)
      - [2. 使用元素](#2-使用元素)
      - [3. 查找元素索引](#3-查找元素索引)
      - [4. 统计元素的数量](#4-统计元素的数量)
      - [5. 遍历元组](#5-遍历元组)
      - [6. 元组的特点](#6-元组的特点)
    - [4. 字符串](#4-字符串)
      - [1. 字符串嵌套](#1-字符串嵌套)
      - [2. 字符串格式化](#2-字符串格式化)
      - [3. 使用元素](#3-使用元素-1)
      - [4. 查找元素索引](#4-查找元素索引-1)
      - [5. 字符串替换](#5-字符串替换)
      - [6. 字符串分割](#6-字符串分割)
      - [7. 字符串规整](#7-字符串规整)
      - [8. 统计元素的数量](#8-统计元素的数量)
      - [9. 遍历字符串](#9-遍历字符串)
      - [10. 字符串大小比较](#10-字符串大小比较)
      - [11. 字符串的特点](#11-字符串的特点)
    - [5. 集合](#5-集合)
      - [1. 定义（集合是唯一元素的无序集合）](#1-定义集合是唯一元素的无序集合)
      - [2. 添加元素](#2-添加元素)
      - [3. 删除元素](#3-删除元素)
      - [4. 集合运算](#4-集合运算)
      - [5. 集合元素的访问](#5-集合元素的访问)
      - [6. 遍历集合](#6-遍历集合)
      - [7. 集合的特点](#7-集合的特点)
      - [8. 集合的一个非常重要的用途：去重](#8-集合的一个非常重要的用途去重)
    - [6. 字典](#6-字典)
      - [1. 定义](#1-定义-4)
      - [2. 基于键获得值](#2-基于键获得值)
      - [3. 嵌套字典](#3-嵌套字典)
      - [4. 添加及修改元素](#4-添加及修改元素)
      - [5. 删除元素](#5-删除元素)
      - [6. 获取全部的元素](#6-获取全部的元素)
      - [7. 遍历字典](#7-遍历字典)
      - [8. 字典的特点](#8-字典的特点)
      - [9. 安全访问与有序遍历](#9-安全访问与有序遍历)
      - [10. 嵌套](#10-嵌套)
  - [四、input输入和print()输出](#四input输入和print输出)
  - [五、条件判断与循环](#五条件判断与循环)
    - [1. 条件测试](#1-条件测试)
    - [2. `if` 语句](#2-if-语句)
    - [3. `for` 遍历](#3-for-遍历)
    - [4. `range()` 与数值序列](#4-range-与数值序列)
    - [5. 列表推导式](#5-列表推导式)
    - [6. `while` 循环](#6-while-循环)
    - [7. `break`、`continue` 与循环 `else`](#7-breakcontinue-与循环-else)
    - [8. 使用循环修改容器](#8-使用循环修改容器)
  - [六、函数](#六函数)
    - [1. 定义](#1-定义-5)
    - [2. 定义函数](#2-定义函数)
    - [3. 函数的说明](#3-函数的说明)
    - [4. 变量作用域](#4-变量作用域)
    - [5. 多返回值](#5-多返回值)
    - [6. 多种参数传递形式](#6-多种参数传递形式)
      - [1. 位置参数](#1-位置参数)
      - [2. 关键字参数](#2-关键字参数)
      - [3. 缺省参数](#3-缺省参数)
      - [4. 可变参数（不定长参数）](#4-可变参数不定长参数)
      - [5. 传递列表](#5-传递列表)
    - [6. 函数作为参数传入](#6-函数作为参数传入)
    - [7. 注意事项](#7-注意事项)
  - [七、模块](#七模块)
    - [1. 定义](#1-定义-6)
    - [2. 导入模块](#2-导入模块)
    - [3. 安装第三方包](#3-安装第三方包)
  - [八、类](#八类)
    - [1. 类的定义和使用](#1-类的定义和使用)
      - [1. 定义类](#1-定义类)
      - [2. 创建成员方法](#2-创建成员方法)
      - [2. 创建类对象并调用其属性与方法](#2-创建类对象并调用其属性与方法)
    - [2. 类内置方法（魔术方法）](#2-类内置方法魔术方法)
      - [1. 构造方法](#1-构造方法)
      - [2. 字符串方法](#2-字符串方法)
      - [3. 比较运算符的方法：](#3-比较运算符的方法)
    - [3. 封装](#3-封装)
      - [1. 定义私有成员](#1-定义私有成员)
      - [2. 私有成员特点](#2-私有成员特点)
    - [4. 继承](#4-继承)
      - [1. 单继承](#1-单继承)
      - [2. 多继承](#2-多继承)
      - [3. \_\_init__()的继承](#3-init-的继承)
      - [4. 复写](#4-复写)
      - [5. 调用父类同名成员](#5-调用父类同名成员)
    - [5. 多态](#5-多态)
      - [1. 基本形式](#1-基本形式)
      - [2. 抽象类（接口）](#2-抽象类接口)
    - [6. 组合](#6-组合)
    - [7. 类型注解](#7-类型注解)
      - [1. 基础数据](#1-基础数据)
      - [2. 类对象](#2-类对象)
      - [3. 数据容器](#3-数据容器)
      - [4. 函数和方法](#4-函数和方法)
      - [5. 使用注释进行注解](#5-使用注释进行注解)
      - [6. Union类型](#6-union类型)
    - [8. 导入类](#8-导入类)
  - [九、文件](#九文件)
    - [1. 绝对路径与相对路径](#1-绝对路径与相对路径)
      - [1. 绝对路径](#1-绝对路径)
      - [2. 相对路径](#2-相对路径)
    - [2. 基本操作](#2-基本操作)
      - [1. 打开文件](#1-打开文件)
      - [2. mode三种基础访问模式](#2-mode三种基础访问模式)
      - [3. 关闭文件](#3-关闭文件)
      - [4. with open语句](#4-with-open语句)
    - [3. 读取](#3-读取)
    - [4. 写入](#4-写入)
    - [5. 追加](#5-追加)
    - [6. 存储及共享数据](#6-存储及共享数据)
      - [1. 存储](#1-存储)
      - [2. 读取](#2-读取)
      - [3. json.dump()和json.dumps()和json.load()和json.loads()辨析](#3-jsondump和jsondumps和jsonload和jsonloads辨析)
        - [1. json.dumps()是将Python对象转化为json字符串的形式](#1-jsondumps是将python对象转化为json字符串的形式)
        - [2. json.loads()是将json字符串转化为Python对象](#2-jsonloads是将json字符串转化为python对象)
        - [3. json.dump()是将python对象写入文件](#3-jsondump是将python对象写入文件)
        - [4. json.load()是从文件读取json](#4-jsonload是从文件读取json)
  - [十、异常](#十异常)
    - [1. 捕获常规异常](#1-捕获常规异常)
    - [2. 捕获指定异常](#2-捕获指定异常)
    - [3. 捕获多个异常](#3-捕获多个异常)
    - [4. 捕获全部异常](#4-捕获全部异常)
    - [5. else语句](#5-else语句)
    - [6. finally语句](#6-finally语句)
    - [7. 文件异常与文本分析](#7-文件异常与文本分析)
    - [8. 传递异常](#8-传递异常)
  - [十一、静默](#十一静默)
  - [十二、测试代码](#十二测试代码)
    - [1. pytest 快速开始](#1-pytest-快速开始)
    - [2. pytest 测试函数](#2-pytest-测试函数)
    - [3. pytest 测试类](#3-pytest-测试类)
    - [4. 夹具和装饰器](#4-夹具和装饰器)
  - [十三、项目一：外星人入侵](#十三项目一外星人入侵)
    - [1. 项目结构](#1-项目结构)
    - [2. 创建窗口与游戏循环](#2-创建窗口与游戏循环)
    - [3. 集中管理设置](#3-集中管理设置)
    - [4. 飞船与连续移动](#4-飞船与连续移动)
    - [5. 事件处理与重构](#5-事件处理与重构)
    - [6. 子弹与精灵编组](#6-子弹与精灵编组)
    - [7. 外星人舰队](#7-外星人舰队)
    - [8. 碰撞、生命与关卡](#8-碰撞生命与关卡)
    - [9. Play 按钮与计分板](#9-play-按钮与计分板)
    - [10. 项目调试清单](#10-项目调试清单)
  - [十四、项目二：数据可视化](#十四项目二数据可视化)
    - [1. Matplotlib 折线图](#1-matplotlib-折线图)
    - [2. 散点图与颜色映射](#2-散点图与颜色映射)
    - [3. 随机漫步](#3-随机漫步)
    - [4. 掷骰子与频数统计](#4-掷骰子与频数统计)
    - [5. 读取 CSV 天气数据](#5-读取-csv-天气数据)
    - [6. GeoJSON 地震数据与全球地图](#6-geojson-地震数据与全球地图)
    - [7. Web API 基本流程](#7-web-api-基本流程)
    - [8. 可视化 API 数据](#8-可视化-api-数据)
  - [十五、项目三：Web 应用程序](#十五项目三web-应用程序)
    - [1. 虚拟环境与项目初始化](#1-虚拟环境与项目初始化)
    - [2. 创建应用](#2-创建应用)
    - [3. 定义模型](#3-定义模型)
    - [4. 管理网站与交互式 shell](#4-管理网站与交互式-shell)
    - [5. URL、视图与模板](#5-url视图与模板)
    - [6. 表单与重定向](#6-表单与重定向)
    - [7. 用户账户与权限](#7-用户账户与权限)
    - [8. 注册、登录与退出](#8-注册登录与退出)
    - [9. 样式与模板布局](#9-样式与模板布局)
    - [10. 部署检查清单](#10-部署检查清单)
  - [附录 A：安装、编辑器与求助](#附录-a安装编辑器与求助)
    - [1. 确认解释器](#1-确认解释器)
    - [2. 运行程序](#2-运行程序)
    - [3. 排错顺序](#3-排错顺序)
    - [4. 编辑器与 IDE](#4-编辑器与-ide)
  - [附录 B：Git 版本控制速查](#附录-bgit-版本控制速查)
  - [附录 C：教材版本说明](#附录-c教材版本说明)
    - [1. 标准库 `unittest` 补充](#1-标准库-unittest-补充)
  - [附录 D：部署故障排查](#附录-d部署故障排查)

<a id="一什么是python"></a>

## 一、什么是Python
Python 是一种高级、通用、解释型的编程语言，以简洁易读的语法和丰富的生态而广受欢迎。Python 是独立设计的语言；最常用的实现 CPython 主要使用 C 编写，但这不代表 Python 基于 C/C++ 语法。

<a id="1-如何安装pythonwindows版"></a>

### 1. 如何安装Python（Windows版）
   这里是笔者所安装的版本 python-3.13
   对于后面更新的新版本我们可以去[python官网](https://www.python.org/)进行安装和下载
   至于配置环境和一些具体的操作详情可见[Python安装视频](https://www.bilibili.com/video/BV1qW4y1a7fU?spm_id_from=333.788.videopod.episodes&vd_source=0c8b5a93700047500e2347aa87475939&p=4)
   如果你用的是VScode，那么恭喜你，你只需要在VScode中找到Python的扩展安装即可
   （包括Python,Python Environment和Python Debugger）

<a id="2-应用领域"></a>

### 2. 应用领域
   - Web开发
   - 数据科学与机器学习
   - 自动化与脚本
   - 科学计算
   - AI
   - 教育与科研
**更多详情请自行参考蟒蛇书上的第一章教程**

<a id="二基础语法"></a>

## 二、基础语法

<a id="1-字面量"></a>

### 1. 字面量
在代码中被写在代码中的固定的值，包括整数，浮点数，字符串等

<a id="2-注释"></a>

### 2. 注释
单行注释：`# 注释内容`

Python 没有专门的“多行注释”语法。连续的 `#` 才是多行注释；三引号字符串如果出现在模块、函数、类或方法开头，会成为文档字符串（docstring），其他位置只是未被使用的字符串字面量。

- 注释不会被执行，文档字符串则可以通过 `help()` 或 `__doc__` 读取。
- 注意：在windows系统中我们可以使用快捷键来进行高效注释(Ctrl + /)

<a id="3-变量"></a>

### 3. 变量

<a id="1-定义"></a>

#### 1. 定义
变量是在程序运行时，能存储运算结果或能表示值的抽象概念（<font face="宋体" color="red" size=4>个人感觉可以先按照“就是给一个东西取了一个名字”这么理解</font>）

<a id="2-定义变量"></a>

#### 2. 定义变量
变量=值

<a id="3-变量特点"></a>

#### 3. 变量特点
可修改
- 这里的”可修改“，准确来说应该是“重新赋值”，就是在定义变量以后，我们可以在后面赋给他一个新的值，这里牵扯到**值的绑定**的问题，权且按下不表

<a id="4-命名规则"></a>

#### 4. 命名规则

- 变量名只能包含字母、数字和下划线，不能以数字开头。
- 区分大小写，`name` 与 `Name` 是两个名称。
- 不能使用 `if`、`class` 等 Python 关键字。
- 使用能表达含义的 `snake_case` 名称，避免覆盖 `list`、`str`、`tuple` 等内置名称。
- 常量通常使用全大写名称表示约定上的“不可修改”：`MAX_SIZE = 100`。

赋值建立的是“名称到对象的绑定”，不是把值装入一个固定类型的盒子：

```python
message = "Hello"
message = 42  # 同一个名称可以重新绑定到不同类型的对象
```

<a id="4-查看数据类型"></a>

### 4. 查看数据类型
type(数据)
- 这里的type()是一个函数，会返回()内变量的类型

常见显式类型转换：

```python
int("42")       # 42
float("3.14")   # 3.14
str(23)          # "23"
list("abc")     # ["a", "b", "c"]
```

转换要求输入符合目标类型的格式，否则会引发 `ValueError`。

<a id="5-运算符"></a>

### 5. 运算符
数学运算符：
```
加： +
减： -
乘： *
除： /
乘方： **
取余数： %
整除： //
```
- 这里注意一下：这里的整除‘//’在数学上如同我们字面上的意思，使用高斯函数取整后的结果([]),但是在某些语言(如C/C++)，我们通常说的整除是省略掉小数部分的除法，这里就与数学上的整除就有所不同（负数不在是向下取整了，而是向零取整），在这个时候我们的“//”就等同于先“/”在用int()函数去掉小数后的部分

**注意：**Python 的 `//` 向负无穷取整，并不等价于 `int(a / b)`：

```python
-7 // 3       # -3
int(-7 / 3)   # -2，int() 向零截断
```

（复合）赋值运算符：
```
赋值 =
加法赋值 += （a += b等效于a = a + b）
减法赋值 -=
乘法赋值 *=
除法赋值 /=
乘方赋值 **=
取余赋值 %=
整除赋值 //=
```
下面是一个例子
```python
a = 10
a += 1
print(a) #这里就会输出11
```

比较运算符：
```
相等 ==
不相等 !=
大于 >
大于等于 >=
小于 <
小于等于 <=
```

整数可以进行任意精度运算，实际范围受可用内存限制；浮点数采用二进制近似表示，可能出现舍入误差：

```python
0.1 + 0.2                  # 0.30000000000000004
round(0.1 + 0.2, 2)        # 0.3
```

多个变量可以同时赋值，也可以直接交换：

```python
x, y, z = 1, 2, 3
x, y = y, x
```

较长的数字字面量可以使用下划线分组，提高可读性；下划线不影响数值：

```python
universe_age = 14_000_000_000
print(universe_age)  # 14000000000
```

<a id="6-转义符"></a>

### 6. 转义符
反斜杠 `\` 与后续字符组成转义序列，用来表示换行、制表符、引号、反斜杠等特殊字符；它不是简单地让后面的所有符号“都不解析”。
下面是一个例子：
```python
# 未转义的嵌套双引号会造成 SyntaxError
# print("I said,"Hello, world"")

print("I said, \"Hello, world\"")
# 输出：I said, "Hello, world"
```
- 补充：“/“
- 1. 转义特殊字符：让某些有特殊含义的字符能够正常显现出来
- 2. 原始字符串（取消转义）
  在字符串前加 r 或 R 可以创建原始字符串，\ 不会被转义：
  ```python
    print(r"Hello\nWorld")   # 输出: Hello\nWorld
    print(r"C:\Users\Name")  # 输出: C:\Users\Name
    print("C:\\Users\\Name") # 等价写法

    # 文件路径常用
    path = r"C:\Windows\System32"
  ```
- 3. 续行符
  在代码行末尾使用 \ 可以将一行代码分成多行写：
  ```python
   # 长表达式换行
   result = 1 + 2 + 3 + \
            4 + 5 + 6 + \
            7 + 8 + 9

   # 长字符串换行
   message = "This is a very long string " \
            "that continues on the next line " \
            "but is actually one string."

   print(result)   # 输出: 45
   print(message)  # 输出完整字符串
   ```
   这里其实想要满足PEP8的字符要求（个人认为）
- <font face="宋体" color="red" size=4>4.重点注意：
  - 在 f-string 中，\ 不能用于转义花括号：
  ```python
   # 错误！无法这样转义
   # print(f"{{value: {42}\}}")

   # 正确做法
   print(f"{{value: {42}}}")  # 输出: {value: 42}
   ```
  - 在三重引号字符串中，\ 仍然有效：
  ```python
   text = """第一行
   第二行\n第三行（这里有换行符）
   最后一行"""
   print(text)
  ```
  </font>

<a id="7-占位符及有效数字保留"></a>

### 7. 占位符及有效数字保留
- 将数据变为整数放入占位的位置：%d
- 将数据变为浮点数放入占位的位置：%f
- 将数据变为字符串放入占位的位置：%s
- 精度控制：%m.nd(f/s)
m：控制宽度（很少使用），设置的宽度小于数字自身，不生效，用空格补全宽度
n：控制小数点精度，要求是数字，会进行小数的四舍五入

下面是详细解释：

<a id="1-基本语法格式"></a>

#### 1. 基本语法格式：
```python
   "格式化字符串" % 值
   "格式化字符串" % (值1, 值2, ...)  # 多个值用元组(这个后面会讲到)
```

<a id="2-各个占位符详解"></a>

#### 2. 各个占位符详解
这些都是 Python 中传统的 **C 风格格式化字符串**方法（使用 % 运算符）。

"%d": 整数占位符
```python
   # 基本用法
   print("年龄: %d 岁" % 25)          # 年龄: 25 岁
   print("得分: %d 分" % 98.7)        # 得分: 98 分（浮点数转整数，小数部分被截断）

   # 多个整数
   print("%d + %d = %d" % (5, 3, 8))  # 5 + 3 = 8
```
"%f": 浮点数占位符
```python
   # 基本用法
   print("价格: %f 元" % 12.5)        # 价格: 12.500000 元（默认6位小数）
   print("温度: %f 度" % 36.6)        # 温度: 36.600000 度

   # 自动转换
   print("百分比: %f" % 75)           # 百分比: 75.000000（整数转浮点）
```
"%s": 字符串占位符
```python
   # 基本用法
   print("姓名: %s" % "张三")         # 姓名: 张三
   print("城市: %s" % "北京")         # 城市: 北京

   # 可以格式化任何类型（自动调用 str()）
   print("数字: %s" % 100)           # 数字: 100
   print("浮点数: %s" % 3.14)        # 浮点数: 3.14
   print("列表: %s" % [1, 2, 3])     # 列表: [1, 2, 3]
```

- 额外的补充：
  除了以上这些，还有`%g`和`%e`占位符,他们是是专门用于科学记数法或智能格式化的浮点数占位符。
  1. `%e`: 科学记数法（Exponential Notation）
      基本用法与上面的相同
      ```python
      # 将浮点数转换为科学记数法格式
      print("%e" % 12345.6789)      # 1.234568e+04
      print("%e" % 0.000012345)     # 1.234500e-05
      print("%e" % 3.14)            # 3.140000e+00

      # 不同精度控制
      print("%.2e" % 12345.6789)    # 1.23e+04（保留2位小数）
      print("%.5e" % 12345.6789)    # 1.23457e+04（保留5位小数）
      print("%.0e" % 12345.6789)    # 1e+04（无小数）
      ```
      **控制小数部分就使用“% + .nf”的形式**
      **默认精度为6位小数**
  2. `%g`：智能选择（General Format）
   `%g`会自动选择%f还是%e
      1. 默认规则：
         - 当指数 < -4 或指数 ≥ 精度时，使用 %e
         - 否则使用 %f
      2. 默认精度：6位有效数字（不是6位小数！）
      ```python
      num1 = 0.0000123456  # 很小
      num2 = 123456.789    # 很大
      num3 = 123.456       # 适中

      # 自动选择格式
      print("%g" % num1)   # 1.23456e-05（科学记数法）
      print("%g" % num2)   # 123457（普通格式，四舍五入）
      print("%g" % num3)   # 123.456（普通格式）

      # 对比其他格式
      print("%f" % num1)   # 0.000012（普通格式，不易读）
      print("%e" % num1)   # 1.234560e-05（科学记数法）
      ```

<a id="3-宽度控制-m"></a>

#### 3. 宽度控制 `%m`
1. 整数宽度控制:
   ```python
   # 宽度为5，右对齐（默认）
   print("数字: [%5d]" % 123)        # 数字: [  123]
   print("数字: [%5d]" % 12345)      # 数字: [12345]（宽度不够时按实际显示）

   # 宽度为3，数字更大
   print("数字: [%3d]" % 1234)       # 数字: [1234]（m < 数字宽度，不生效）
   ```
2. 浮点数宽度控制：
   ```python
   # 宽度10，默认6位小数
   print("[%10f]" % 3.14)            # [  3.140000]
   print("[%10f]" % 123.456)         # [123.456000]

   # 宽度不够的情况
   print("[%5f]" % 123.456)          # [123.456000]（宽度不够按实际显示）
   ```
3. 字符串宽度控制：
   ```python
   # 宽度为10，右对齐
   print("[%10s]" % "Hello")         # [     Hello]
   print("[%10s]" % "Python")        # [    Python]

   # 左对齐：在宽度前加负号
   print("[%-10s] 结束" % "Hello")   # [Hello     ] 结束
   ```

<a id="4-精度控制-n"></a>

#### 4. 精度控制 `%.n`
1. 浮点数精度控制:
   ```python
   # 控制小数位数
   print("π: %.2f" % 3.14159)        # π: 3.14（四舍五入）
   print("π: %.4f" % 3.14159)        # π: 3.1416（四舍五入）
   print("π: %.0f" % 3.14159)        # π: 3（四舍五入到整数）

   # 配合宽度使用
   print("[%10.2f]" % 3.14159)       # [      3.14]（宽度10，精度2）
   print("[%-10.2f]" % 3.14159)      # [3.14      ]（左对齐）
   ```
2. 字符串精度控制:
   ```python
   # 字符串精度 = 截取字符数
   print("%.3s" % "Python")          # Pyt（只取前3个字符）
   print("%.10s" % "Python")         # Python（超出长度按原样）
   print("[%10.3s]" % "Python")      # [       Pyt]（宽度10，只显示3字符）
   ```

<a id="5-f-string用法推荐"></a>

#### 5. f-string用法（推荐）
<font face="宋体" color="red" size=4>上面的内容是传统的C语言方式，较为麻烦，我们这里可以使用更为便捷的"f-string"格式.</font>

1. 基础语法
 ```python
   # 基本格式：f"字符串{表达式}"
   name = "张三"
   age = 25
   print(f"姓名：{name}，年龄：{age}")  # 姓名：张三，年龄：25

   # 直接计算表达式
   print(f"10 + 20 = {10 + 20}")       # 10 + 20 = 30
   print(f"平方：{5 ** 2}")            # 平方：25

   # 调用函数/方法
   text = "hello"
   print(f"大写：{text.upper()}")      # 大写：HELLO
   print(f"长度：{len(text)}")         # 长度：5
 ```
2. 格式规范语法：
   **完整的f-string格式
   f"{表达式:格式说明符}"

   下面是一个例子：
   ```python
   name = "Ge Changhao"
   age = 18
   salary = 1000.0
   print(f"My name is {name}.I'm {age} years old.My salaries are {salary}$")
   #结果：
   #My name is Ge Changhao.I'm 18 years old.My salaries are 1000.0$
   print(f"My name is {name}.I'm {age} years old.My salaries are {salary:.8f}$")
   #结果
   #My name is Ge Changhao.I'm 18 years old.My salaries are 1000.00000000$
   ```
3. 数字格式化
   整数：
   ```python
   num = 1234

   # 宽度和对齐
   print(f"[{num:10}]")      # [      1234] 宽度10，右对齐
   print(f"[{num:<10}]")     # [1234      ] 左对齐
   print(f"[{num:^10}]")     # [   1234   ] 居中对齐
   print(f"[{num:*>10}]")    # [******1234] 填充*

   # 符号显示
   print(f"{123:+}")         # +123
   print(f"{-123:+}")        # -123
   print(f"{123: }")         #  123（正数前有空格）
   print(f"{-123: }")        # -123

   # 进制转换
   print(f"二进制: {42:b}")   # 101010
   print(f"八进制: {42:o}")   # 52
   print(f"十六进制: {255:x}") # ff
   print(f"十六进制: {255:X}") # FF
   print(f"带前缀: {255:#x}")  # 0xff
   print(f"带前缀: {255:#X}")  # 0xFF
   ```
   浮点数：
   ```python
   pi = 3.1415926535

   # 固定小数位数
   print(f"π: {pi:.2f}")     # π: 3.14
   print(f"π: {pi:.4f}")     # π: 3.1416
   print(f"π: {pi:.0f}")     # π: 3

   # 宽度 + 精度
   print(f"[{pi:10.2f}]")    # [      3.14]
   print(f"[{pi:<10.4f}]")   # [3.1416    ]

   # 科学记数法
   num = 123456789
   print(f"{num:e}")         # 1.234568e+08
   print(f"{num:.2e}")       # 1.23e+08
   print(f"{num:E}")         # 1.234568E+08

   # 智能格式（%g 等效）
   print(f"{0.000123:g}")    # 0.000123
   print(f"{123456789:g}")   # 1.23457e+08
   print(f"{123.456:g}")     # 123.456

   # 百分比
   print(f"{0.75:%}")        # 75.000000%
   print(f"{0.75:.1%}")      # 75.0%
   print(f"{0.1234:.2%}")    # 12.34%
   ```

   字符串：
   ```python
   text = "Python"

   # 宽度和对齐
   print(f"[{text:10}]")      # [Python    ] 右对齐
   print(f"[{text:<10}]")     # [Python    ] 左对齐
   print(f"[{text:^10}]")     # [  Python  ] 居中对齐
   print(f"[{text:*^10}]")    # [**Python**] 填充居中

   # 截断
   print(f"{text:.3}")        # Pyt（前3个字符）
   print(f"[{text:10.3}]")    # [Pyt       ]（宽度10，显示3字符）

   # 填充特殊字符
   print(f"{text:═^20}")      # ═══════Python═══════
   print(f"{text:☆^20}")      # ☆☆☆☆☆☆☆Python☆☆☆☆☆☆☆
   ```

<a id="8-表达式"></a>

### 8. 表达式
一条明确有执行结果的代码语句

<a id="9-布尔数"></a>

### 9. 布尔数
用于表示结果真假的数据类型
True表示真
False表示假
- 可通过比较运算得到布尔值

<a id="10-none值"></a>

### 10. None值

<a id="1-含义"></a>

#### 1. 含义
None作为一个特殊的字面量，用于表示：空、无意义

<a id="2-应用"></a>

#### 2. 应用
- None可用于声明无内容的变量上
- 在if判断上，None等同于False

___
- [返回目录](#目录)
___

<a id="11-代码风格与-python-哲学"></a>

### 11. 代码风格与 Python 哲学

- 每级缩进使用 4 个空格，不混用制表符。
- 运算符两侧和逗号后通常留空格；函数调用的括号内侧不留空格。
- 函数之间通常空两行，类中的方法之间空一行。
- 行过长时优先使用圆括号进行隐式换行，不依赖反斜杠续行。
- 注释说明“为什么这样做”，不要重复代码已经清楚表达的内容。

在交互式解释器中运行下面的语句可以查看“Python 之禅”：

```python
import this
```

核心思想是优先选择简单、清晰、可读且容易维护的方案。能运行只是最低要求；代码还应让后来阅读的人快速理解。

<a id="三数据容器"></a>

## 三、数据容器

<a id="1-数据容器概述"></a>

### 1. 数据容器概述

<a id="1-定义-1"></a>

#### 1. 定义
数据容器是可以储存多个元素的数据类型

<a id="2-分类"></a>

#### 2. 分类
列表(list)、元组(tuple)、字符串(str)、集合(set)、字典(dict)

<a id="3-序列"></a>

#### 3. 序列
序列是内容连续有序，可使用下标索引的一类数据容器
列表、元组、字符串 均可视为序列

<a id="4-切片"></a>

#### 4. 切片
==序列 [起始索引:结束索引:步长]==
- 起始索引留空表示从头开始
- 结束索引留空表示取到结尾
- 步长为负数表示反向取（起始和结束索引也要反向取）

<a id="5-统计元素的数量"></a>

#### 5. 统计元素的数量
**len(数据容器)** 这个是统计总元素的数量
**数据容器.count(特定元素)** 这个是统计特定元素的数量

<a id="6-求最大元素和最小元素"></a>

#### 6. 求最大元素和最小元素
最**大**元素：==max()==
最**小**元素：==min()==
- **字典保留键去除值**

<a id="7-排序"></a>

#### 7. 排序
- 排序：
  - ==sorted(数据容器)==   **这里是临时排序（不改变原容器的顺序）**
  - ==数据容器.sort()==   **这里是排序（改变了原容器的顺序）**
- 反向排序：
  - 数据容器.sort(reverse=True)
  - sorted(reverse=True)
  - 数据容器.reverse()
**下面是一些例子：**
```python
numbers = [0, 2, 1, 5, 4, 6, 3, 8, 7, 9]
nums = numbers.copy()   #这里浅拷贝一下，避免影响原来的列表

print(sorted(nums))    #这里的结果是[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)    #这里的结果是[0, 2, 1, 5, 4, 6, 3, 8, 7, 9]

nums.sort()
print(nums)    #这里的结果就变成了[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]，进行完了排序

nums = numbers.copy()    #回复开始的样子
print(sorted(nums, reverse=True))    #结果：[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(nums)    #结果：[0, 2, 1, 5, 4, 6, 3, 8, 7, 9]
nums.reverse()
print(nums)    #结果：[9, 7, 8, 3, 6, 4, 5, 1, 2, 0]
nums.sort(reverse=True)
print(nums)    #结果：[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

<a id="2-列表"></a>

### 2. 列表

<a id="1-定义-2"></a>

#### 1. 定义
列表=[元素,元素,元素...]
列表=list()

<a id="2-索引"></a>

#### 2. 索引
从前向后，编号从0递增
从后向前，编号从-1递减

<a id="3-使用元素"></a>

#### 3. 使用元素
列表[索引]
列表[外层索引][内层索引]（这里牵扯到了列表的嵌套）

<a id="4-查找元素索引"></a>

#### 4. 查找元素索引
列表.index(元素)

<a id="5-修改元素"></a>

#### 5. 修改元素
列表[索引]=新元素（这里相当于是重新赋值，重新绑定了一个值）

<a id="6-添加元素"></a>

#### 6. 添加元素
追加单个元素：**列表.append(元素)**
追加另一个数据容器的所有元素：**列表.extend(数据容器)**
插入单个元素：**列表.insert(索引,元素)**
**这里注意一下：对于要添加另一个容器的部分内容，我们可以使用extend()+切片的方法：**
```python
list1 = list(range(0, 10))
list2 = list(range(10, 20))
#现在让list2中的前五个元素添加到list1中
list1.extend(list2[:5])
print(list1)     #这里的结果是[0, 1, ..., 14]
```

<a id="7-删除元素"></a>

#### 7. 删除元素
**del 列表[索引]**
**列表.pop(索引)** （可用变量对删除元素进行接收）
**列表.remove(元素)** （列表中的第一个该元素）

<a id="8-清空列表"></a>

#### 8. 清空列表
**列表.clear()**

<a id="9-统计元素的数量"></a>

#### 9. 统计元素的数量
某个元素在列表中的数量：**列表.count(元素)**
全部元素总数：**len(列表)**

<a id="10-遍历列表"></a>

#### 10. 遍历列表
for遍历：
```
for 临时变量 in 数据容器:
   对临时变量进行处理
```
**例：**
```python
list1 = [0, 1, 5, 5.0, 6.114514, 350234, 'Doro', 'cheems', 'PopCat']
for item in list1:
   print(item) #这里就会依次打印上方的元素
```
while循环：
```
index = 0
while index < len(列表):
   元素 = 列表[index]
   对元素进行处理
   index += 1
```
**例：**
```python
list1 = [0, 1, 5, 5.0, 6.114514, 350234, 'Doro', 'cheems', 'PopCat']
index = 0
while index < len(list1):
   print(list1[index])
   index += 1
#这里就会依次打印上方的元素
```

<a id="11-列表特点"></a>

#### 11. 列表特点
1. 可以容纳多个元素，实际容量受可用内存和解释器实现限制
2. 可容纳不同类型的元素
3. 数据有序存储
4. 允许重复数据
5. 可修改

<a id="12-排序反转与长度"></a>

#### 12. 排序、反转与长度

```python
cars = ["bmw", "audi", "toyota", "subaru"]

cars.sort()                    # 原地升序，返回 None
cars.sort(reverse=True)        # 原地降序
ordered = sorted(cars)         # 返回新列表，不修改 cars
cars.reverse()                 # 原地反转当前顺序，不等同于排序
count = len(cars)
```

**常见错误：**`cars = cars.sort()` 会让 `cars` 变成 `None`；原地修改方法一般不返回修改后的容器。

<a id="13-切片与复制"></a>

#### 13. 切片与复制

```python
players = ["charles", "martina", "michael", "florence", "eli"]

players[0:3]    # 索引 0、1、2
players[:4]     # 从开头到索引 4 之前
players[2:]     # 从索引 2 到末尾
players[-3:]    # 最后三项
players[::2]    # 步长为 2
players[::-1]   # 反向副本
```

完整切片可以创建浅复制：

```python
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
friend_foods.append("ice cream")
```

直接写 `friend_foods = my_foods` 只会让两个名称指向同一个列表。浅复制会复制外层列表，但嵌套的可变对象仍然共享。

<a id="3-元组"></a>

### 3. 元组

<a id="1-定义-3"></a>

#### 1. 定义
变量=(元素，元素，元素...)
变量=tuple()
- 定义一个元素的元组：变量=(元素，) （必须带有逗号）

<a id="2-使用元素"></a>

#### 2. 使用元素
元组[索引]
元组[外层索引][内层索引]

<a id="3-查找元素索引"></a>

#### 3. 查找元素索引
元组.index(元素)

<a id="4-统计元素的数量"></a>

#### 4. 统计元素的数量
某个元素在元组中的数量：元组.count(元素)
全部元素总数：len(元组)

<a id="5-遍历元组"></a>

#### 5. 遍历元组
for遍历：
```
for 临时变量 in 数据容器:
   对临时变量进行处理
```
**例：**
```python
tuple = (1, 2, 3, 'Hakimi', 'HYW', 3.14)
for item in tuple:
   print(item)    #这里就会依次打印上方的元素
```
while循环：
```
index = 0
while index < len(元组):
   元素 = 元组[index]
   对元素进行处理
   index += 1
```
**例：**
```python
tuple = (1, 2, 3, 'Hakimi', 'HYW', 3.14)
index = 0
while index < len(tuple):
   print(tuple[index])
   index += 1
#依旧是打印上方的所有元素
```

<a id="6-元组的特点"></a>

#### 6. 元组的特点
1. 可容纳多个数据
2. 可容纳不同类型的元素
3. 数据有序存储
4. 允许重复数据
5. 不可修改

**Tips：这里元组就是一个常量元素的集合，我们是不能通过正常手段来对其中的元素进行修改的，但是我们可以按照“先转成列表，再修改”的方式进行伪修改**
```python
t = (1, 2, 3, 'Hakimi', 'HYW', 3.14)
#我们现在假设要“修改”‘3‘这个元素
lst = list(t)
index = lst.index(3)
lst[index] = 4#你的目标
new_tuple = tuple(lst)
print(new_tuple) #”改好了“
```

<a id="4-字符串"></a>

### 4. 字符串

<a id="1-字符串嵌套"></a>

#### 1. 字符串嵌套
1. 交替使用单双引号
2. 使用转义符转义内层引号 ==(更为推荐)==

<a id="2-字符串格式化"></a>

#### 2. 字符串格式化
1. 使用加号连接字符串变量和字面量
2. 使用占位符%：
   "字符串1%s(%d/%f)字符串2" % 填入内容
   (多个变量占位，变量要用括号括起来，并按照顺序填入)
3. f"字符串1{变量}字符串2"
**下面是对应的例子：**
使用加号连接字符串变量和字面量
```python
name = "小明"
age = 20
score = 95.5

# 基本连接
result1 = "姓名：" + name + "，年龄：" + str(age)
print(result1)  # 姓名：小明，年龄：20

# 注意：数字需要转换为字符串
result2 = name + "的成绩是：" + str(score) + "分"
print(result2)  # 小明的成绩是：95.5分

# 与字面量直接连接
result3 = "Hello " + name + "!" + " 你好！"
print(result3)  # Hello 小明! 你好!
```
使用占位符%：
```python
name = "小红"
age = 22
price = 19.99
count = 3

# 单个占位符
result1 = "姓名：%s" % name
print(result1)  # 姓名：小红

# 多个占位符（必须用元组）
result2 = "%s今年%d岁，买了%.2f元的东西" % (name, age, price)
print(result2)  # 小红今年22岁，买了19.99元的东西

# 不同类型占位符
result3 = "商品：%s，单价：%.1f元，数量：%d个，总计：%.2f元" % (
    "苹果", price, count, price * count
)
print(result3)  # 商品：苹果，单价：19.99元，数量：3个，总计：59.97元

# 常用格式符：
# %s - 字符串
# %d - 十进制整数
# %f - 浮点数（%.2f表示保留2位小数）
# %x - 十六进制数
```
f"字符串1{变量}字符串2"
```python
name = "张三"
age = 25
height = 1.75
scores = [90, 85, 88]

# 基本使用
result1 = f"{name}今年{age}岁"
print(result1)  # 张三今年25岁

# 表达式计算
result2 = f"{name}的身高是{height}米，BMI指数为{65 / (height ** 2):.1f}"
print(result2)  # 张三的身高是1.75米，BMI指数为21.2

# 格式化数字
pi = 3.1415926
result3 = f"π的值是：{pi:.3f}"  # 保留3位小数
print(result3)  # π的值是：3.142

# 字典访问
person = {"name": "李四", "city": "北京"}
result4 = f"姓名：{person['name']}，城市：{person['city']}"
print(result4)  # 姓名：李四，城市：北京

# 函数调用
def get_greeting(name):
    return f"你好，{name}！"

result5 = f"{get_greeting('王五')}欢迎学习Python"
print(result5)  # 你好，王五！欢迎学习Python

# 对齐和填充
result6 = f"|{name:<10}|{age:^6}|{height:>8.2f}|"
print(result6)  # |张三        |  25  |    1.75|
# < 左对齐，^ 居中对齐，> 右对齐
```

<a id="3-使用元素-1"></a>

#### 3. 使用元素
字符串[索引]

<a id="4-查找元素索引-1"></a>

#### 4. 查找元素索引
字符串.index(元素)

<a id="5-字符串替换"></a>

#### 5. 字符串替换
新字符串=字符串.replace(字符串1,字符串2)
```python
str1 = "Hello, world."
str2 = "China"
str3 = str1.replace("world", str2)
print(str3)    #Hello, China.
```

<a id="6-字符串分割"></a>

#### 6. 字符串分割
**基础分割**
列表=字符串.split(字符串分割符)
```python
str1 = "To be or not to be,that's a question."
lst1 = str1.split() #默认是按照空格来分割
print(lst1)  #['To', 'be', 'or', 'not', 'to', "be,that's", 'a', 'question.']
```
**根据换行符分割**
列表=字符串.splitlines()
```python
str2 = "To be or not to be,that's a question.\n"\
       "Give every man thy ear, but few thy voice; take each man's censure, but reserve thy judgment.\n"\
       "When sorrows come, they come not single spies, - but in battalions.\n"\
       "There is nothing either good or bad, but thinking makes it so.\n"
lst2 = str2.splitlines()
print(lst2)
#下面是结果
["To be or not to be,that's a question.", "Give every man thy ear, but few thy voice; take each man's censure, but reserve thy judgment.", 'When sorrows come, they come not single spies, - but in battalions.', 'There is nothing either good or bad, but thinking makes it so.']
```

<a id="7-字符串规整"></a>

#### 7. 字符串规整
去除前后空格 字符串.strip()
删除右侧空白 字符串.rstrip()
删除左侧空白 字符串.lstrip()
去除前后指定内容 字符串.strip(字符串)

删除确定的前缀或后缀应使用 `removeprefix()` / `removesuffix()`；`strip(chars)` 删除的是两端属于字符集合 `chars` 的所有字符，不是完整子串：

```python
url = "https://nostarch.com"
url.removeprefix("https://")   # "nostarch.com"

filename = "python_notes.txt"
filename.removesuffix(".txt")  # "python_notes"
```
```python
text = "  ##666hhhxxx**     "
txt1 = text
txt2 = text
txt3 = text
txt4 = "##666hhhxxx**"
print(txt1.strip())
print(txt2.lstrip())
print(txt3.rstrip())
print(txt4.strip('#'))
#结果：
"""
##666hhhxxx**
##666hhhxxx**
  ##666hhhxxx**
666hhhxxx**
"""
```

<a id="8-统计元素的数量"></a>

#### 8. 统计元素的数量
某个元素在字符串中的数量：**字符串.count(元素)**
全部元素总数：**len(集合)**

<a id="9-遍历字符串"></a>

#### 9. 遍历字符串
for遍历：
```
for 临时变量 in 数据容器:
   对临时变量进行处理
```
while循环：
```
index = 0
while index < len(字符串):
   元素 = 字符串[index]
   对元素进行处理
   index += 1
```
**此处省略例子，跟上面的差不多：**

<a id="10-字符串大小比较"></a>

#### 10. 字符串大小比较
1. 按位比较
2. 以ASCII码值确定大小
![ASCII码表](https://img.doc.xuehai.net/pic/44530094d89ba069c31ed8d9/1-966-jpg_6_0_______-628-0-0-628.jpg)

<a id="11-字符串的特点"></a>

#### 11. 字符串的特点
1. 只可存储字符串
2. 长度任意
3. 数据有序存储
4. 允许重复数据
5. 不可修改

<a id="5-集合"></a>

### 5. 集合

<a id="1-定义集合是唯一元素的无序集合"></a>

#### 1. 定义（集合是唯一元素的无序集合）
集合={元素,元素,元素...}
集合=set()  （这里是设置了一个空集合）

<a id="2-添加元素"></a>

#### 2. 添加元素
**集合.add(元素)** ==这里是添加单个元素==
**集合.update(元素/容器)** ==这里可以添加多个元素==
```python
s = {1, 2, 3}

# add() - 添加单个元素
s.add(4)        # {1, 2, 3, 4}
s.add(2)        # {1, 2, 3, 4} - 重复元素不会添加

# update() - 添加多个元素
s.update([5, 6, 7])        # 从列表添加
s.update({8, 9})           # 从集合添加
s.update((10, 11))         # 从元组添加
s.update("ab")             # 从字符串添加 {'a', 'b'}
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'a', 'b'}
```

<a id="3-删除元素"></a>

#### 3. 删除元素
**集合.remove(元素)**
**集合.pop()** （可用变量对元素进行接收，且该元素不再在集合中）
**集合.clear()**
```python
s = {1, 2, 3, 4, 5}

# remove() - 删除指定元素（元素必须存在）
s.remove(3)     # {1, 2, 4, 5}
# s.remove(10)  # ❌ KeyError: 10（不存在）

# discard() - 删除指定元素（不存在也不报错）
s.discard(2)    # {1, 4, 5}
s.discard(10)   # {1, 4, 5} - 不会报错

# pop() - 删除并返回任意一个元素；不要依赖具体删除顺序
item = s.pop()
print(f"删除了: {item}")

# clear() - 清空集合
s.clear()       # set()
```
==注意，为了防止我们删除的时候我们一般使用discard(),这样我们删除元素的时候即使没有，我们也不会抛出异常==

<a id="4-集合运算"></a>

#### 4. 集合运算
```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# 并集( | )
print(A | B)        # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))   # 同上

# 交集( & )
print(A & B)        # {4, 5}
print(A.intersection(B))

# 差集（在A中但不在B中）( - )
print(A - B)        # {1, 2, 3}
print(A.difference(B))

# 对称差集（只在其中一个集合中） ( ^ )
print(A ^ B)        # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))
```

<a id="5-集合元素的访问"></a>

#### 5. 集合元素的访问
集合中元素是无序的，所以我们每次访问都会有不一样的结果

<a id="6-遍历集合"></a>

#### 6. 遍历集合
```
for 临时变量 in 数据容器
   对临时变量进行处理
```
**值得注意的是，这里的结果是没有固定输出的，这是由于我们集合元素具有无序性的特点：**

<a id="7-集合的特点"></a>

#### 7. 集合的特点
1. 可以容纳多个元素
2. 可容纳不同类型的元素
3. 数据无序存储（不支持索引）
4. 不允许重复数据
5. 可修改

<a id="8-集合的一个非常重要的用途去重"></a>

#### 8. 集合的一个非常重要的用途：去重
```python
# 最常见的用途
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = list(set(numbers))  # 去重并转回列表
print(unique_numbers)  # [1, 2, 3, 4, 5]（顺序可能改变）
```

<a id="6-字典"></a>

### 6. 字典

<a id="1-定义-4"></a>

#### 1. 定义
**变量={键:值,键:值,键:值...}**
**变量=dict()**

<a id="2-基于键获得值"></a>

#### 2. 基于键获得值
字典[键]
字典[外层键][内层键]（这里设计了一个字典的嵌套）
```python
dictionary = {
   'dict1' : {'key1' : 1, 'key2' : 2},
   'dict2' : {'key1' : 3, 'key2' : 4},
   'dict3' : {'key1' : 5, 'key2' : 6},
}
print(dictionary['dict2']['key1'])     #输出：3
```
字典.get(键，键不存在时的相应值)（若不输入第二个值，则当键不存在时，函数返回值为None）

<a id="3-嵌套字典"></a>

#### 3. 嵌套字典
字典={
   字典1:{ }
   字典2:{ }
   字典3:{ }
   ...
}

<a id="4-添加及修改元素"></a>

#### 4. 添加及修改元素
字典[键]=值
```python
my_dict = {}
#添加
my_dict['size'] = 'XXL'
my_dict['color'] = 'yellow'
print(my_dict)
#修改
my_dict['size'] = 'XL'
print(my_dict)
```

<a id="5-删除元素"></a>

#### 5. 删除元素
字典.pop(键)
del 字典[键]
```python
dictionary = {
   'size' : 'XXL',
   'color' : 'yellow',
   'board' : 'Anta',
}
del_inform = dictionary.pop('size')
print(dictionary)    #{'color': 'yellow', 'board': 'Anta'}
del dictionary['color']
print(dictionary)    #{'board': 'Anta'}
```

<a id="6-获取全部的元素"></a>

#### 6. 获取全部的元素
获取全部的键：字典.keys()
获取全部的值：字典.values()
获取全部的键值对：字典.items() **这里的items()方法要用两个变量接受**
- 三者返回的分别是动态视图 `dict_keys`、`dict_values` 和 `dict_items`，不是列表；需要列表时显式调用 `list()`。
```python
dictionary = {
   'size' : 'XXL',
   'color' : 'yellow',
   'board' : 'Anta',
}
#获取键:
for key in dictionary.keys():
   print(key)
#获取值：
for value in dictionary.values():
   print(value)
#获取键值对：
for key, value in dictionary.items():
   print(f"{key}: {value}")

```

<a id="7-遍历字典"></a>

#### 7. 遍历字典
遍历字典中的所有键
```
for 临时变量 in 字典.keys():
   后续处理
   (键=临时变量)
   (值=字典[临时变量])
或
for 临时变量 in 字典:
   后续处理
   (键=临时变量)
   (值=字典[临时变量])
```
遍历字典中的所有值
```
for 临时变量 in 字典.values():
   后续处理
   (值=临时变量)
```
遍历字典中的所有键值对
```
for 临时变量1,临时变量2 in 字典.items():
   后续处理
   (键=临时变量1)
   (值=临时变量2)
```

<a id="8-字典的特点"></a>

#### 8. 字典的特点
1. 可以容纳多个元素，每个元素为键值对
2. 值可为任意类型；键必须是可哈希对象，通常使用字符串、数字或只包含不可变对象的元组
3. 通过键访问，不支持按整数位置索引
4. 不允许重复数据（重复会覆盖）
5. 可修改

从 Python 3.7 起，普通字典保证保留插入顺序，但它的核心用途仍是建立“键到值”的映射。

<a id="9-安全访问与有序遍历"></a>

#### 9. 安全访问与有序遍历

```python
alien = {"color": "green", "points": 5}

alien["speed"]                 # KeyError
alien.get("speed")             # None
alien.get("speed", "unknown")  # 指定缺省值

for name in sorted(alien.keys()):
    print(name)

for value in set(alien.values()):
    print(value)                # 值去重后遍历
```

<a id="10-嵌套"></a>

#### 10. 嵌套

常见嵌套形式包括“字典列表”“列表存入字典”和“字典存入字典”：

```python
aliens = [
    {"color": "green", "points": 5},
    {"color": "yellow", "points": 10},
]

pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

users = {
    "aeinstein": {"first": "albert", "last": "einstein"},
    "mcurie": {"first": "marie", "last": "curie"},
}
```

嵌套层级过深会降低可读性；此时应考虑拆分数据或使用类。

<a id="四input输入和print输出"></a>

## 四、input输入和print()输出
1. input()输入：
   1. 简单用法：
    ```python
    name = input("What is your name?")
    print(name)  #你所输入的信息

    inform = input()
    print(inform)  #终端中没有输出，但你再输入完后也会输出你所输入的内容
    ```
    2. 返回值
   **input()函数始终返回字符串类型**，因此就会涉及到类型转换的问题
    ```python
    data = input("Please input a number.")   #这里即使你输入的是data（一个数据），但是在变量data中存储的类型还是字符串，而不是你所想的int/float型
    sum = int(data) + 1
    print(sum)    #这里的sum中含有int()函数进行了类型转换，未经转换直接使用会traceback：TypeError
    ```
**下面是一些类型转化实例：**
   ```python
   # 转换为整数
   num1 = int(input("请输入一个整数："))

   # 转换为浮点数
   num2 = float(input("请输入一个浮点数："))

   # 转换为布尔值（注意：非空字符串转换为True）
   flag = bool(input("输入任意内容（空表示False）："))

   # 转换为列表
   numbers = list(map(int, input("输入多个数字，用空格分隔：").split()))
   ```
   如果我们想用一个 `input()` 函数接受多个输入，可以使用 `map()` 函数和 `split()` 方法进行数据处理。
   ```python
   x, y, z = map(int, input().split())
   print(x + y + z)
   print(f"{(x + y + z) / 3:.2f}")
   ```
   2. map()函数python内置的高阶函数，其格式如下：
   `map(function, iterable)`
   第一个参数相当于我们要进行处理的方法，是一个函数，后面的是迭代器，可以理解为我们要处理的对象。
   值得注意的是，map()函数的返回值是一个一个数据（用function处理过的）。所以若果我们想要整个展出我们的数据，我们要用`list()`方法。
   ```python
   print(list(map(int, input("请输入文本：").split())))
   ```
   这样如果我们输入`1 2 3`，我们就会得到`[1, 2, 3]`这样的输出。
   当然，map()函数甚至可以处理多个列表：
   ```python
   list1 = [1, 2, 3]
   list2 = [10, 20, 30]

   # 让两个列表对应位置相加
   sums = list(map(lambda x, y: x + y, list1, list2))
   # 结果: [11, 22, 33]
   ```
   3. `split()` 是字符串方法，它可以将字符串拆分成列表；不传参数时会把连续空白视为一个分隔符，并忽略两端空白。
   **注意，这里的列表是字符串列表，不一定是我们需要的数据类型，要想进行转换可以使用map()函数**。
2. print()输出：
    1. 简单用法：
      ```python
      print("要输出的内容")
      ```
    2. 详解:
      ```python
      print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
      ```
**参数说明：**
   | 参数 | 说明 | 默认值 |
   | :--- | :--- | :--- |
   | `objects` | 要打印的对象，可以有多个 | 无 |
   | `sep` | 对象之间的分隔符 | space`' '` |
   | `end` | 打印结束后的字符 | 换行符`'\n'` |
   | `file` | 输出流，可以是文件对象 | `sys.stdout` |
   | `flush` | 是否立即刷新缓冲区 | `False` |
   由此我们可以得到一些进阶用法：
  - 打印多个对象：
    ```python
      # 字符串
      print("Hello, World!")

      # 数字
      print(123)
      print(3.14)

      # 变量
      name = "Alice"
      print(name)

      # 表达式
      print(10 + 20)
    ```
  - 修改分隔符：
    ```python
      # 使用逗号分隔
      print("苹果", "香蕉", "橙子", sep=", ")

      # 使用连字符分隔
      print("2024", "01", "15", sep="-")

      # 无分隔符
      print("a", "b", "c", sep="")

      # 使用特殊字符分隔
      print("项目1", "项目2", "项目3", sep=" | ")
      ```
  - 修改结束符
    ```python
      # 不换行
      print("Hello", end="")
      print("World")  # HelloWorld

      # 用空格结束
      print("Loading", end=" ")
      print("complete!")  # Loading complete!

      # 用逗号和空格结束
      print("First", end=", ")
      print("Second", end=", ")
      print("Third")  # First, Second, Third

      # 自定义结束符
      print("Processing", end="...")
      print("Done")  # Processing...Done
    ```

<a id="五条件判断与循环"></a>

## 五、条件判断与循环

<a id="1-条件测试"></a>

### 1. 条件测试

条件测试的结果只能是 `True` 或 `False`，常用于决定是否执行一段代码。

```python
age = 20
age == 20       # 相等
age != 18       # 不相等
age > 18        # 大于
age >= 20       # 大于等于
age < 30        # 小于
age <= 20       # 小于等于
```

字符串比较区分大小写；只想忽略大小写时，可以在比较时调用 `lower()`，而不修改原字符串：

```python
car = "Audi"
car.lower() == "audi"  # True
```

多个条件可以使用逻辑运算符连接：

| 运算符 | 含义 | 特点 |
| :---: | :--- | :--- |
| `and` | 所有条件都为真时结果为真 | 前一个条件为假时短路 |
| `or` | 至少一个条件为真时结果为真 | 前一个条件为真时短路 |
| `not` | 对条件结果取反 | `not in` 常用于成员判断 |

```python
age = 22
age >= 18 and age < 65
age < 18 or age >= 65

requested = ["mushrooms", "onions"]
"mushrooms" in requested
"pepperoni" not in requested
```

<a id="2-if-语句"></a>

### 2. `if` 语句

```python
if 条件:
    条件为真时执行的代码
elif 另一个条件:
    前面条件为假、此条件为真时执行的代码
else:
    所有条件都为假时执行的代码
```

- 只需要一次判断：使用 `if`。
- 二选一：使用 `if-else`。
- 多选一：使用 `if-elif-else`；Python 只执行第一个为真的分支。
- 多个条件可能同时成立：使用多个独立的 `if`，不要使用互斥的 `elif`。
- `else` 是兜底分支；如果最后一种情况也有明确条件，优先写成 `elif`，避免无效数据落入 `else`。

```python
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print(f"票价为 {price} 元。")
```

**判断容器是否为空：**空字符串、空列表、空元组、空集合和空字典在条件中都视为假。

```python
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")
```

<a id="3-for-遍历"></a>

### 3. `for` 遍历

`for` 依次取得可迭代对象中的元素，适合“对每个元素执行一次操作”的场景。

```python
for 临时变量 in 可迭代对象:
    循环体
```

```python
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

print("Thank you, everyone!")  # 缩进退出后，只执行一次
```

**常见错误：**忘记冒号、循环体未缩进、不应属于循环的语句多缩进，以及循环变量名称不能表达元素含义。

<a id="4-range-与数值序列"></a>

### 4. `range()` 与数值序列

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

`range()` 包含起点、不包含终点；返回惰性的 `range` 对象，需要列表时使用 `list()`。

```python
list(range(1, 6))        # [1, 2, 3, 4, 5]
list(range(2, 11, 2))   # [2, 4, 6, 8, 10]

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
```

数字列表常用统计函数：

```python
digits = list(range(1, 10))
min(digits)
max(digits)
sum(digits)
```

<a id="5-列表推导式"></a>

### 5. 列表推导式

列表推导式把“创建列表、遍历、计算并追加”压缩为一个表达式：

```python
squares = [value ** 2 for value in range(1, 11)]
even_squares = [value ** 2 for value in range(1, 11) if value % 2 == 0]
```

基本结构：

```python
[生成元素的表达式 for 临时变量 in 可迭代对象 if 可选条件]
```

表达式过于复杂时应改回普通循环，保证代码易读。

<a id="6-while-循环"></a>

### 6. `while` 循环

`while` 在条件为真时反复执行，适合“不确定重复次数，但知道停止条件”的场景。

```python
while 循环条件:
    循环体
```

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

可使用标志控制复杂循环：

```python
active = True

while active:
    message = input("输入 quit 结束：")
    if message == "quit":
        active = False
    else:
        print(message)
```

<a id="7-breakcontinue-与循环-else"></a>

### 7. `break`、`continue` 与循环 `else`

- `break`：立即结束当前最内层循环。
- `continue`：跳过本轮剩余代码，开始下一轮。
- 循环的 `else`：循环正常结束时执行；由 `break` 退出时不执行。

```python
while True:
    city = input("请输入城市（quit 结束）：")
    if city == "quit":
        break
    print(city)

for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number)
```

**常见错误：**`while` 条件一直为真且循环体没有修改相关状态，会形成无限循环；应检查计数器、标志或退出分支是否一定可能发生。

<a id="8-使用循环修改容器"></a>

### 8. 使用循环修改容器

遍历列表时直接删除其中的元素容易跳过数据。需要筛选时，优先创建新列表；需要逐项移动时，可以配合 `while`：

```python
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
```

删除列表中所有指定值：

```python
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
while "cat" in pets:
    pets.remove("cat")
```

使用字典记录用户输入：

```python
responses = {}
polling_active = True

while polling_active:
    name = input("Name: ")
    response = input("Mountain: ")
    responses[name] = response

    if input("Another response? (yes/no) ") == "no":
        polling_active = False
```

<a id="六函数"></a>

## 六、函数

<a id="1-定义-5"></a>

### 1. 定义
函数是组织好的，可重复使用的，用来实现特定功能的代码段

<a id="2-定义函数"></a>

### 2. 定义函数
有名称的函数（多次使用）：
```
def 函数名(传入参数):
   函数体
   return 返回值 (可有可无)
```
**例：**
```python
#无显式返回值
def greet_guest(name):
   print(f"Welcome! {name.title()}")
#有返回值
def format_name(first, last, middle=""):
   if middle == "":
      formatted_name = f"{first} {last}".title()
   else:
      formatted_name = f"{first} {middle} {last}".title()
   return formatted_name
```
无名称的函数（只能使用一次）：
```
lambda 传入参数: 函数体（一行代码）
```
**详解：**
1. 简单用法
```python
# 无参数
greet = lambda: "Hello, World!"
print(greet())  # Hello, World!

# 一个参数
square = lambda x: x ** 2
print(square(5))  # 25

# 多个参数
add = lambda a, b, c: a + b + c
print(add(1, 2, 3))  # 6

# 默认参数
power = lambda x, n=2: x ** n
print(power(3))     # 9
print(power(3, 3))  # 27python
```
2. 立即调用：
```python
# 立即调用lambda函数
result = (lambda x, y: x * y)(4, 5)
print(result)  # 20

# 带括号的立即调用
print((lambda s: s.upper())("hello"))  # HELLO
```
- 参数和返回值可省略
- 传入参数：形式参数，参数之间使用逗号分隔，数量不受限制
- 调用时输入的参数：实际参数，按照顺序，逗号分隔
- 返回值后的代码不会被执行，当不使用return时，返回值为None

<a id="3-函数的说明"></a>

### 3. 函数的说明
```
def func(x,y):
   """
   函数说明
   :param x:参数x的说明
   :param y:参数y的说明
   :return:返回值的说明
   """
   函数体
   return 返回值
```

<a id="4-变量作用域"></a>

### 4. 变量作用域
- 定义函数中的变量作用范围在函数内部，函数外部无法使用，为局部变量
- 函数内外部均可以使用的变量为全局变量
- ==局部变量转化为全局变量：global 变量==

<a id="5-多返回值"></a>

### 5. 多返回值
```
def 函数名(传入参数):
   函数体
   return 返回值1,返回值2,返回值3...
```

<a id="6-多种参数传递形式"></a>

### 6. 多种参数传递形式

<a id="1-位置参数"></a>

#### 1. 位置参数
传递参数和定义的参数的顺序和个数必须一致

<a id="2-关键字参数"></a>

#### 2. 关键字参数
键=值
- 关键字参数可以不按照固定顺序
- 可以和位置参数混用，但位置参数必须在前，且匹配参数顺序

<a id="3-缺省参数"></a>

#### 3. 缺省参数
- 在定义函数时为参数提供默认值，调用时不传入该参数的值，则该参数取该默认值，如果传入该参数的值，则取传入值
- 可将默认值设为空字符串或None配合if语句，从而将该值变为可选的
- 设置默认值**必须**在最后面
**例：**
```python
#位置参数(最一般的使用方式)
def func1(x, y):
   print(x, y, sep = ',') #输出：x,y

#关键字参数
def func2(x, y):
   return (x ** y)
res = func2(2, 3)   #x=2, y=3
print(res)  #结果：8
res = func2(y=2, x=3)   #x=3, y=2
print(res)   #结果：9

#缺省参数
def format_name(first, last, middle=""):
   if middle == "":
      formatted_name = f"{first} {last}"
   else:
      formatted_name = f"{first} {middle} {last}"
   return formatted_name
```

<a id="4-可变参数不定长参数"></a>

#### 4. 可变参数（不定长参数）
用于不确定调用函数时会传递多少个参数（不传参也可以）
- 位置传递：
```
def 函数名(*传入参数):
   函数体
函数名(参数1,参数2,参数3...)
（传入的所有参数合并成一个元组）
```
- 关键字传递：
```
def 函数名(**传入参数):
   函数体
函数名(键1=值1,键2=值2，键3=值3...)
（传入的所有参数合并成一个字典）
```

位置参数、任意数量的位置参数和任意数量的关键字参数可以组合：

```python
def build_profile(first, last, **user_info):
    profile = {"first_name": first, "last_name": last}
    profile.update(user_info)
    return profile

user = build_profile(
    "albert",
    "einstein",
    location="princeton",
    field="physics",
)
```

参数定义的一般顺序为：普通参数、带默认值的参数、`*args`、仅限关键字参数、`**kwargs`。

<a id="5-传递列表"></a>

#### 5. 传递列表

列表传入函数后，形参和实参指向同一个列表，因此函数内的原地修改会影响调用者：

```python
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

designs = ["phone case", "robot pendant"]
completed = []
print_models(designs, completed)
```

不希望修改原列表时可传入切片副本：

```python
print_models(designs[:], completed)
```

复制大型列表需要额外的时间和内存；允许函数修改列表时应直接传递原列表。

<a id="6-函数作为参数传入"></a>

### 6. 函数作为参数传入
```
def 函数1(函数2):
   变量=函数2(传入参数)
def 函数2(传入参数):
   函数体
   return 返回值
```

<a id="7-注意事项"></a>

### 7. 注意事项
1. 描述性名称
2. 添加说明注释
3. ==指定默认值和关键字实参时，等号两边不要有空格==
4. 使用多个函数，使用两个空行将相邻的函数分隔开
5. 每个函数只负责一个清晰任务；函数名和参数名使用描述性的 `snake_case`
6. 使用文档字符串说明函数的用途、参数、返回值和可能抛出的异常
7. 默认参数不要使用列表或字典等可变对象，避免多次调用共享同一个对象

```python
# 错误：多次调用共享同一个列表
def append_item(item, items=[]):
    items.append(item)
    return items

# 正确
def append_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

<a id="七模块"></a>

## 七、模块

<a id="1-定义-6"></a>

### 1. 定义
- 模块是一个Python文件，以.py结尾
- 模块能定义函数，类和变量，模块里也能包含可执行的代码
- 一个模块就是一个工具包，每一个工具包中都有不同的工具用于实现不同的功能

<a id="2-导入模块"></a>

### 2. 导入模块
```
[from 模块名] import [功能名/*] [as 别名]
```
- 其中括号表示可选内容
- 功能指模块、类、变量、方法、函数等
- 模块代码一般写在开头位置
1. 导入整个模块：`import 模块名` （调用：模块名.功能名()）
2. 导入模块中的特定功能：`from 模块名 import 功能名` （调用：功能名()）
3. 导入模块中的全部功能：`from 模块名 import *` （调用：功能名()）
4. 给模块指定别名：`import 模块名 as 别名` （调用：别名.功能名()）
5. 给功能指定别名：`from 模块名 import 功能名 as 别名` （调用：别名()）
**下面是一些具体的例子：**
```python
#guest.py
def format_name(first, last, middle=""):
   """
   格式化宾客的姓名，方便下文
   first: 名
   last: 姓
   middle(可选): 中间名
   返回值：一个格式化的姓名
   """
   if middle == "":
      formatted_name = f"{first} {last}"
   else:
      formatted_name = f"{first} {middle} {last}"
   return formatted_name.title()

def greet_guest(first, last, middle=""):
   """
   问候宾客
   first, last, middle传给format_name()来进行格式化
   无返回值
   """
   name = format_name(first, last, middle)
   print(f"Welcome to you,{name}!")

def farewell_guest():
   """
   欢送宾客
   无参数
   无返回值
   """
   print("This is truly a beautiful night!")
#patry.py
# import guest #这样我们就可以使用guest.py的所有函数了
# import guest as g #这样我们就可以将‘g’当作guest模块来使用了
# from guest import ···(具体的函数)
# from guest import formatt_name as f_n #我们使用f_n就相当于是使用了format_name()
```

<a id="3-安装第三方包"></a>

### 3. 安装第三方包
- 为确保运行正常，请先更新pip
- 不同编辑器安装方式不同，以下只列出了VS Code的安装方法
1. 安装
在终端输入
python -m pip install --user 第三方包名称
2. 更新
在终端输入
python -m pip install --upgrade 第三方包名称
**下面是对pip的一些简介：**
PIP（Package Installer for Python）是Python的官方包管理工具，用于安装和管理Python包/库。
- pip的升级
```bash
# 检查pip版本
pip --version
# 或
python -m pip --version

# Python 3中也可以使用
pip3 --version
```
- pip的安装
```bash
# 如果Python环境没有pip，可以这样安装

# Linux/Mac
python -m ensurepip --upgrade

# Windows（通过Python安装包时勾选pip选项）

# 通用方法：使用get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
- pip的升级
```bash
# 升级pip到最新版本
python -m pip install --upgrade pip

# 在Linux/Mac上可能需要sudo
sudo pip install --upgrade pip

# 针对Python 3
python3 -m pip install --upgrade pip
```

<a id="八类"></a>

## 八、类

<a id="1-类的定义和使用"></a>

### 1. 类的定义和使用

<a id="1-定义类"></a>

#### 1. 定义类
```
class 类名称:
   类的属性
   类的行为
```
- 类的属性：定义在类中的变量（成员变量）
- 类的行为：定义在类中的函数（成员方法）

<a id="2-创建成员方法"></a>

#### 2. 创建成员方法
```
def 方法名(self,形参1,形参2,形参3...)
   方法体
```
- 在方法内部，想要访问类的成员变量，必须使用“self.成员变量”，外部传入的变量无需。
- 在传参的过程中可忽略self
**例：**
```python
class Car:
    """模拟汽车。"""

    def __init__(self, make, model, year):
        self.make = make.title()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回格式规范化的描述。"""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """打印汽车的行驶里程。"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """设置里程，拒绝回调里程表。"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """让里程增加指定的量。"""
        if miles >= 0:
            self.odometer_reading += miles
```

<a id="2-创建类对象并调用其属性与方法"></a>

#### 2. 创建类对象并调用其属性与方法
```
对象=类名称()
对象.类属性=内容
对象.方法名(传入参数)
```
**例：**
```python
class Car:
   #--snip--

car = Car('audi', 'a4', 2024)
#现在就可以调用各种方法了
car.read_odometer()     # 0
car.update_odometer(3000)
car.read_odometer()     # 3000
car.increment_odometer(500)
car.read_odometer()     # 3500
car.get_descriptive_name()    # 2024 Audi A4
```

<a id="2-类内置方法魔术方法"></a>

### 2. 类内置方法（魔术方法）

<a id="1-构造方法"></a>

#### 1. 构造方法
语句：
```
class 类名称:
   def __init__(self,参数1,参数2,参数3...):
   self.属性1=参数1
   self.属性2=参数2
   self.属性3=参数3
   ...

对象=类名称(参数1,参数2,参数3...)
```
特点：
- 创建类对象时，会自动执行
- 创建类对象时，将传入参数自动传递给__init__方法使用

<a id="2-字符串方法"></a>

#### 2. 字符串方法
当类对象需要被转换成字符串时，会输出内存地址，可以通过__str__方法，控制类转化为字符串的行为。
```
class 类名称:
   def __str__(self):
      return 字符串内容
```
**例：**
```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"学生：{self.name}，年龄：{self.age}，分数：{self.score}"

# 使用示例
stu = Student("张三", 18, 95)
print(stu)  # 自动调用__str__：学生：张三，年龄：18，分数：95
print(str(stu))  # 显式调用：学生：张三，年龄：18，分数：95

# 对比：没有__str__方法时
class StudentNoStr:
    def __init__(self, name):
        self.name = name

stu2 = StudentNoStr("李四")
print(stu2)  # 输出：<__main__.StudentNoStr object at 0x7f8c3c0b2a90>
```
**一个进阶用法：__repr__(self)：**
```python
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"学生：{self.name}"

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, score={self.score})"

stu = Student("王五", 20, 88)
print(str(stu))   # 学生：王五
print(repr(stu))  # Student(name='王五', age=20, score=88)

# 在交互式环境中直接输入变量名会调用__repr__
# >>> stu
# Student(name='王五', age=20, score=88)
```

<a id="3-比较运算符的方法"></a>

#### 3. 比较运算符的方法：
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 小于 <
    def __lt__(self, other):
        return self.score < other.score

    # 小于等于 <=
    def __le__(self, other):
        return self.score <= other.score

    # 等于 ==
    def __eq__(self, other):
        return self.score == other.score

    # 不等于 !=
    def __ne__(self, other):
        return self.score != other.score

    # 大于 >
    def __gt__(self, other):
        return self.score > other.score

    # 大于等于 >=
    def __ge__(self, other):
        return self.score >= other.score

# 使用示例
alice = Student("Alice", 85)
bob = Student("Bob", 92)
charlie = Student("Charlie", 85)

print(alice < bob)     # True (85 < 92)
print(alice <= bob)    # True (85 <= 92)
print(alice == bob)    # False (85 == 92?)
print(alice != bob)    # True (85 != 92)
print(alice > bob)     # False (85 > 92?)
print(alice >= bob)    # False (85 >= 92?)

print(alice == charlie)  # True (85 == 85)
print(alice <= charlie)  # True (85 <= 85)
```
**一个简单记忆的方法：**
小：`l`
大：`g`
等：`e`
不：`n`

<a id="3-封装"></a>

### 3. 封装

<a id="1-定义私有成员"></a>

#### 1. 定义私有成员
变量名/方法名以“__”开头

<a id="2-私有成员特点"></a>

#### 2. 私有成员特点
- 私有方法无法直接被类对象使用，私有变量无法赋值也无法获取值
- 类内部成员变量和方法能够访问私有成员变量和方法
**这里的部分与C++差不多，我们想研究得更深入一些得话我们应该移步到C++学习：**
```python
# 一个使用示例
class Car:
   def __init__(self, make, model, year):
      self.make = make.title()
      self.model = model.title()
      self.year = year
      self.__odometer = 0

   def __get_maker(self):
      return self.make.title()

   def __get_model(self):
      return self.model.title()

   def __get_year(self):
      return self.year

   def get_odometer(self):
      return self.__odometer

car = Car('aodi', 'a4', 2025)
print(car.__get_maker())  #Error
print(car.__get_model())  #Error
print(car.__get_yaer())  #Error
print(car.make)  #Aodi
print(car.model)  #A4
print(car.year)  #2025
print(car.get_odometer())  # 0
print(car.__odometer)  #Error

```

<a id="4-继承"></a>

### 4. 继承

<a id="1-单继承"></a>

#### 1. 单继承
```
class 父类:
   父类主体
class 子类(父类):
   子类新增主体
```

<a id="2-多继承"></a>

#### 2. 多继承
```
class 父类:
   父类主体
class 子类(父类1,父类2,父类3...):
   子类新增主体
```
**例：**
```python
#先写两个父类
class Car:
   def __init__(self, make, model, year):
      self.make = make.title()
      self.model = model.title()
      self.year = year
      self.odometer = 0 # 表盘初始为0

   def update_odometer(self, data):
      if data <= self.odometer:
         return
      else:
         self.odometer = data

   def increase_odometer(self, data):
      self.odometer += data

   def get_discription(self):
      print(f"This car is made by {self.make} in {self.year},whose model is {self.model}.")

class Battery:
   def __init__(self, power=0):
      self.power = power

   def get_power(self):
      return self.power

   def charge(self, increase_power):
      if increase_power <= 0:
         return
      elif increase_power + self.power <= 100:
         self.power += increase_power
      else:
         self.power = 100

#现在开始继承
# 单继承
class GasCar(Car):
   def __init__(self, make, model, year, gas_model):
      super().__init__(make, model, year)  # 优先初始化父类
      self.gas_model = gas_model  #再初始化自己的特有成员
      self.gas_container = 0  # 油箱初始化为 0
   def get_gas_model(self):
      return self.gas_container
   def refuel(self, volume):
      if volume <= 0:
         return
      elif self.gas_container + volume <= 100:
         self.gas_container += volume
      else:
         self.gas_container = 100

# 多继承
class ElectricCar(Car, Battery):
   def __init__(self, make, model, year, init_power=0):
      super().__init__(make, model, year)
      super().__init__(init_power)

   def get_power(self):
      return Battery.get_power(self)

   def charge(self, increase_power=0):
      super().charge(increase_power)
```
**多个父类中具有同名成员变量或方法，先继承的优先级高于后继承的**

<a id="3-init-的继承"></a>

#### 3. \_\_init__()的继承
将父类用__init__()方法构造的属性全部继承，从而便于多态的复写修改
```
class 父类:
   def __init__(self,参数1,参数2,参数3...):
   self.属性1=参数1
   self.属性2=参数2
   self.属性3=参数3
   ...
class 子类(父类):
def __init__(self,参数1,参数2,参数3...):
   super().__init__(参数1,参数2,参数3...)
```

<a id="4-复写"></a>

#### 4. 复写
**在子类重新定义与父类同名的属性或方法，从而对父类进行修改**
**例：**
```python
class Animal:
    def speak(self):
        return "动物发出声音"

    def move(self):
        return "动物在移动"

class Dog(Animal):
    # 复写父类的speak方法
    def speak(self):
        return "汪汪！"

    # 添加新方法
    def wag_tail(self):
        return "摇尾巴"

class Cat(Animal):
    # 完全复写父类方法
    def speak(self):
        return "喵喵！"

    # 部分复写，调用父类方法并扩展
    def move(self):
        # 先执行父类的move
        parent_move = super().move()
        # 添加新的行为
        return f"{parent_move}，悄无声息地"

# 测试
animal = Animal()
dog = Dog()
cat = Cat()

print(animal.speak())  # 动物发出声音
print(dog.speak())     # 汪汪！  ← 复写了父类方法
print(cat.speak())     # 喵喵！  ← 复写了父类方法

print(animal.move())   # 动物在移动
print(dog.move())      # 动物在移动 ← 继承父类，未复写
print(cat.move())      # 动物在移动，悄无声息地 ← 扩展了父类方法
```
**有意思的是，这里的复写与C++中的重写略有所不同，有兴趣的可以自己研究一下：**

<a id="5-调用父类同名成员"></a>

#### 5. 调用父类同名成员
方式1：
**父类名.成员变量
父类名.成员方法(self)**
方法2：
**super().成员变量
super().成员方法()**
```python
# 方法一：
class Car:
   # --snip--
class Battery:
   # --snip--

class ElectricCar(Car, Battery):
   def charge(self, increase_power=0):
      Battery.charge(self, increase_power)
# 方法二：
class Car:
   # --snip--
class Battery:
   # --snip--

class ElectricCar(Car, Battery):
   def charge(self, increase_power=0):
      super().charge(increase_power)
```
**对于super()函数的一点补充：**
super()函数是继承中非常重要的一个函数，我们在使用的时候应注意一下几点
- 调用super()时**不用传self参数**
- super()的调用遵循MRO顺序（多继承的情况）
**例：**
```python
class A:
   def __init__(self, num):
      self.num1 = num
class B(A):
   def __init__(self, num, Num):
      super().__init__(num)
      self.num2 = Num
class C(A):
   def __init__(self, num, Num):
      super().__init__(num)
      self.num3 = Num
class D(B, C):
   def __init__(self, num, Num, n, N):
      B.super().__init__(num, Num)
      C.super().__init__(num, n)
      self.num4 = N
#查看D的继承顺序
print(D.__mro__)
# 输出: (<class '__main__.D'>, <class '__main__.B'>,
#        <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
d = D(1, 2, 3, 4)
print(d.num1) # 1
print(d.num2) # 2
print(d.num3) # 3
print(d.num4) # 4
```
这里涉及到多继承常出现的一个问题：**钻石继承问题**
```text
   A
  / \
 B   C
  \ /
   D
```
我们看上方的一处代码
```python
   def __init__(self, num, Num, n, N):
      B.super().__init__(num, Num)
      C.super().__init__(num, n)
      self.num4 = N
```
这里我们显式调用了B和C的初始化函数，我们的问题就出现在这，如果我们没有显式的指出，就会有下面的过程
```
D.__init__ 中的 super().__init__(num, Num)
    ↓
B.__init__(num, Num)  # 因为MRO中B在C前面
    ↓
B中的 super().__init__(num)  # 调用A.__init__(num)
    ↓
A.__init__(num)  # 设置 self.num1 = num
    ↓
回到B.__init__，设置 self.num2 = Num
    ↓
回到D.__init__，然后调用第二个 super().__init__(num, n)
    ↓
B.__init__(num, n)  # 再次调用B，覆盖之前的设置！
    ↓
...
```
所以这个时候就需要我们进行显式指出那个初始化`X.super()__init__(self, ···)`

<a id="5-多态"></a>

### 5. 多态
多态其实就是同一个名称的事物在不同情况下有不同的实现情况

<a id="1-基本形式"></a>

#### 1. 基本形式
```
class 父类:
   父类内容
class 子类1(父类):
   复写父类内容1
class 子类2(父类):
   复写父类内容2
class 子类3(父类):
   复写父类内容3
...
```
**例：**
```python
class Animal:
   def speak(self):
      print("发出声音")
class Dog(Animal):
   def speak(self):
      print("汪汪")
class Cat(Animal):
   def speak(self):
      print("喵喵")
class Duck(Animal):
   def speak(self):
      print("嘎嘎")

animal1 = Animal()
animal2 = Dog()
animal3 = Cat()
animal4 = Duck()
animals = [
   animal1,
   animal2,
   animal3,
   animal4,
]
for animal in animals:
   animal.speak()
# 发出声音
# 汪汪
# 喵喵
# 嘎嘎
```

<a id="2-抽象类接口"></a>

#### 2. 抽象类（接口）
抽象类：含有抽象方法的类叫做抽象类
抽象方法：方法体是空实现（pass）称之为抽象方法
- 抽象方法：只有方法声明，没有具体实现（方法体为空）
- 抽象类：包含至少一个抽象方法的类
- 特点：抽象类不能实例化，子类必须实现所有抽象方法
**例：**
```python
from abc import ABC, abstactmathod
from math import pi
class Shape(ABC):
   @abstractmethod   #抽象方法的修饰器
   def area(self):      #抽象方法
      """计算面积，子类必须实现"""
      pass #没有具体的实现方案
   @abstractmethod
   def perimeter(self):       #抽象方法
      """计算周长，子类必须实现"""
      pass

class Circle(Shape):
   def __init__(self, radius):
      self.radius = radius

   def area(self):      #子类的具体实现
      return pi * self.radius ** 2

   def perimeter(self):      #子类的具体实现
      return pi * self.radius * 2

class Rectangle(Shape):
   def __init__(self, length, width):
      self.length = length
      self.width = width

   def area(self):      #子类的具体实现
      return self.length * self.width

   def perimeter(self):       #子类的具体实现
      return 2 * (self.length + self.width)
```
**对于所有的抽象类，必须继承`ABC`，对于所有的抽象方法，要在定义添加一个修饰器`@abstactmethod`，而上方的两个都在模块`abc`中**

<a id="6-组合"></a>

### 6. 组合
组合：将类的一部分提取出来，作为一个独立的类，以简化原先大类的一种方式
实现方式：将对象作为属性
```
class 小类:
   类主体
class 大类:
   类属性=小类()
对象=大类()
对象.类属性.小类属性或方法
```
**实例：**
```python
# 定义小类（组件类）
class CPU:
    def __init__(self, brand, cores):
        self.brand = brand
        self.cores = cores

    def info(self):
        return f"{self.brand} CPU, {self.cores} cores"

# 定义大类（复合类）
class Computer:
    def __init__(self, cpu_brand, cpu_cores, ram_size):
        # 组合：将CPU对象作为Computer的属性
        self.cpu = CPU(cpu_brand, cpu_cores)
        self.ram = ram_size

    def show_specs(self):
        print(f"Computer specifications:")
        print(f"- CPU: {self.cpu.info()}")  # 访问CPU对象的方法
        print(f"- RAM: {self.ram}GB")

# 使用组合
my_pc = Computer("Intel", 8, 16)
my_pc.show_specs()
# 输出：
# Computer specifications:
# - CPU: Intel CPU, 8 cores
# - RAM: 16GB

# 也可以直接访问组合的对象
print(my_pc.cpu.brand)  # 输出：Intel
```
说白了，其实就是在一个类中我们使用了另一个类，官方说的关系一般是`has - a`的关系，而继承则是`is - a`的关系

<a id="7-类型注解"></a>

### 7. 类型注解
类型注解是Python 3.5+引入的功能，用于在代码中明确指定**变量、参数和返回值的类型**，提高代码可读性和可维护性。

<a id="1-基础数据"></a>

#### 1. 基础数据
变量:类型=
```python
# 基本类型注解
name: str = "Alice"
age: int = 25
height: float = 1.75
is_student: bool = True
score: float = 95.5

# None类型
result: None = None

# 任意类型,使用关键字any
data: any = "可以是任何类型"
data = 42  # 有效
data = [1, 2, 3]  # 有效

# 类型别名
Vector = list[float]
point: Vector = [1.0, 2.0, 3.0]
```

<a id="2-类对象"></a>

#### 2. 类对象
类对象:类=类()
```python
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> str:
        return f"Hello, I'm {self.name}"

class Company:
    def __init__(self, name: str):
        self.name = name
        self.employees: list[Person] = []  # 列表中的元素是Person对象

# 1. 类实例的类型注解
person: Person = Person("Alice", 30)  # person是Person类的实例
company: Company = Company("TechCorp")

# 2. 类属性的类型注解
company.employees.append(person)  # employees列表包含Person对象
#这里的注解是写在类里面的

# 3. Self类型注解（Python 3.11+）
from typing import Self

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Self] = None  # Self指代Node类本身

    def set_next(self, node: Self) -> Self:
        self.next = node
        return self

# 4. 类方法注解
class Calculator:
    @classmethod
    def add(cls, a: int, b: int) -> int:
        return a + b

    @staticmethod
    def multiply(x: float, y: float) -> float:
        return x * y

# 类引用作为类型
calculator_class: type[Calculator] = Calculator
```
**这里对Self类、类方法、和类引用(type[类型名])进行详细的解释**
1. 什么是Self类：
Self类是python在Python 3.11+添加的内置类型，一般用来解决“如何解决返回self时的注释问题”
```python
from typing import Self  # Python 3.11+ 内置

class Person:
    def set_name(self, name: str) -> Self:  # ✅ 用Self表示"返回自己"
        self.name = name
        return self
```
2. 为什么要返回self：
- 链式调用：
```python
class Person:
    def __init__(self, name: str):
        self.name = name
        self.age = 0
        self.city = ""

    def set_age(self, age: int) -> Self:  # 返回自己，方便链式调用
        self.age = age
        return self  # ⭐ 返回self本身

    def set_city(self, city: str) -> Self:
        self.city = city
        return self  # ⭐ 返回self本身

# 使用：链式调用，一行设置多个属性
person = Person("张三").set_age(25).set_city("北京")
# 等效于：
# person = Person("张三")
# person.set_age(25)
# person.set_city("北京")
```
- 在继承的时候非常有用
```python
class Animal:
    def set_species(self, species: str) -> Self:
        self.species = species
        return self

class Dog(Animal):  # Dog继承Animal
    def bark(self) -> str:
        return "汪汪！"

# 使用
dog = Dog().set_species("犬科")  # ✅ set_species返回的是Dog实例，不是Animal！
dog.bark()  # 可以调用Dog特有的方法
# 如果用 -> Animal，这里编辑器会以为返回Animal，不认.bark()方法
```
3. 什么是类方法
@classmethod，有cls参数，操作类本身
```python
class Calculator:
    # 普通方法：有self参数，操作实例
    def add(self, a: int, b: int) -> int:
        return a + b

    # 类方法：@classmethod，有cls参数，操作类本身
    @classmethod
    def add_class(cls, a: int, b: int) -> int:
        return a + b

    # 静态方法：@staticmethod，没有self/cls，就是普通函数
    @staticmethod
    def add_static(x: float, y: float) -> float:
        return x + y

# 用法辨析
# 创建实例
calc = Calculator()

# 普通方法：通过实例调用
result1 = calc.add(1, 2)          # ✅ 正确
# Calculator.add(1, 2)           # ❌ 错误：需要实例

# 类方法：可以通过类直接调用
result2 = Calculator.add_class(1, 2)  # ✅ 正确：不需要实例
result3 = calc.add_class(1, 2)        # ✅ 也正确：有实例也能用

# 静态方法：和类方法类似，但没有cls参数
result4 = Calculator.add_static(1.5, 2.5)  # ✅
result5 = calc.add_static(1.5, 2.5)        # ✅
```
4. 类引用

**类引用表示"类本身"，而不是"类的实例"**
```python
class Person:
    pass

# 两种不同的东西：
person_instance: Person = Person()  # Person的实例
person_class: type[Person] = Person  # Person类本身
```
**一般用于要传递类而不是传递类实例的情况**
```python
from typing import Type

class Animal:
    def speak(self) -> str:
        return "动物叫"

class Dog(Animal):
    def speak(self) -> str:
        return "汪汪！"

class Cat(Animal):
    def speak(self) -> str:
        return "喵喵！"

# 函数：接收一个类，创建实例并调用
def create_and_speak(animal_class: type[Animal]) -> str:
    """传入一个Animal类，创建实例并让它叫"""
    animal = animal_class()  # 创建类的实例
    return animal.speak()

# 使用
print(create_and_speak(Dog))  # 传入Dog类本身 ✅
print(create_and_speak(Cat))  # 传入Cat类本身 ✅
# print(create_and_speak(Dog()))  # ❌ 错误：传入的是实例，不是类
```

<a id="3-数据容器"></a>

#### 3. 数据容器
变量:类型=
变量:容器类型[元素类型1,元素类型2,元素类型3...]
（元组需要标记出每个元素的类型，字典需要标记键和值的类型）
**各种容器的写法：**
1. 列表：
直接用 `variable_name: list[typeame] = [···]` 就行
```python
# Python 3.8及之前
from typing import List
names: List[str] = ["张三", "李四", "王五"]

# Python 3.9+（推荐写法）
names: list[str] = ["张三", "李四", "王五"]

# 实际用法
students: list[str] = []
students.append("小明")    # ✅
students.append("小红")    # ✅
# students.append(123)    # ⚠️ 警告：应该是字符串！
```
2. 元组
元组有点意思，分两种情况：一个**固定长度但类型可变**，另一个**不固定长度但类型固定**
**格式：** `variable_name: tuple[str/int/float/···] = (······)`
```python
# Python 3.8及之前
from typing import Tuple

# 固定长度元组：要标注每个位置的类型
person1: Tuple[str, int, float] = ("张三", 25, 1.75)  # 三个位置类型都不同

# Python 3.9+
person2: tuple[str, int, float] = ("张三", 25, 1.75)

# 可变长度元组（长度不固定，但元素类型相同）
scores: tuple[int, ...] = (90, 85, 95, 88, 92)  # 任意多个整数
# 等价于：tuple[int, int, int, int, int, ...]     注意这里！！！！

# 错误示例
# person: tuple[str, int] = ("张三", 25, 1.75)  # ❌ 错误：多了一个元素
# person: tuple[str, int] = ("张三")           # ❌ 错误：少了一个元素
```
3. 字典
字典略有不同，他需要指定键的类型和值的类型
**格式：** `vatiable_name: dict[str/int/float, str/int/float] = {······}`
```python
# Python 3.8及之前
from typing import Dict
student_scores: Dict[str, int] = {"张三": 90, "李四": 85}

# Python 3.9+
student_scores: dict[str, int] = {"张三": 90, "李四": 85}

# 复杂字典
config: dict[str, any] = {  # value可以是任何类型
    "name": "app",
    "port": 8080,
    "debug": True
}

# 嵌套字典
class_info: dict[str, dict[str, int]] = {
    "一班": {"张三": 90, "李四": 85},
    "二班": {"王五": 88, "赵六": 92}
}
```

<a id="4-函数和方法"></a>

#### 4. 函数和方法
```
def 函数或方法名(形参名1:类型1,形参名2:类型2，形参名3:类型3...) -> 返回值类型:
   函数体
```
**例：**
```python
def greet_guest(first: str, last: str,) -> None:
   full_name = f"{first} {last}".title()
   print(full_name)
```

<a id="5-使用注释进行注解"></a>

#### 5. 使用注释进行注解
#type:类型
这个用法是在python 3.5以前用的，作用和上方的差不多
```python
# 变量: 类型 = 值
变量名 = 值  # type: 类型

# 示例
x = 5  # type: int
name = "张三"  # type: str

# 函数注释
def add(a, b):
    # type: (int, int) -> int
    return a + b

def greet(name):
    # type: (str) -> str
    return f"Hello, {name}!"
```

<a id="6-union类型"></a>

#### 6. Union类型
Union类型表示这个变量或者数据容器中的变量可以是`[]`中的任意一种类型
数据容器：
```
from typing import Union
变量:数据容器[Union[类型1,类型2,类型3...]]
```
**例：**
```python
from typing import Union, Optional

# 用户ID可以是整数或字符串
user_id: Union[int, str] = 1001
user_id = "admin001"  # 可以重新赋值为字符串

# 或者可以包含 None
result: Union[str, None] = "success"
result = None  # 也可以
# 等价于 Optional[str]
```
函数：
```
from typing import Union
def 函数或方法名(变量:Union[类型1,类型2,类型3...]) -> Union[类型1,类型2,类型3...]
   函数体
```
**例：**
```python
# 函数参数可以是不同类型
from typing import Union

def process_value(value: Union[int, str, list]) -> str:
    """处理不同类型的值"""
    if isinstance(value, int):
        return f"数字: {value}"
    elif isinstance(value, str):
        return f"字符串: {value}"
    elif isinstance(value, list):
        return f"列表长度: {len(value)}"

print(process_value(42))      # 数字: 42
print(process_value("hello"))  # 字符串: hello
print(process_value([1, 2, 3]))  # 列表长度: 3
# 函数返回值也可以是不同类型
from typing import Union

def find_item(items: list[str], target: str) -> Union[int, None]:
    """查找元素，找到返回索引，找不到返回None"""
    try:
        return items.index(target)
    except ValueError:
        return None

result = find_item(["apple", "banana", "orange"], "banana")
if result is not None:
    print(f"找到，索引是: {result}")
else:
    print("没找到")
```
**注意：这里的 `isinstance()` 用来判断对象是否是指定类型或其子类的实例，返回 `True` 或 `False`。**类型注解主要服务于阅读、编辑器和静态检查工具，Python 默认不会仅因注解不匹配而阻止程序运行。

<a id="8-导入类"></a>

### 8. 导入类

类也可以放入独立模块，使主程序更短、更清晰：

```python
# car.py
class Car:
    pass

class ElectricCar(Car):
    pass
```

```python
import car
my_car = car.Car()

from car import Car
my_car = Car()

from car import Car, ElectricCar
from car import ElectricCar as EC
```

- 一个模块可以保存多个相关类。
- 模块还可以导入另一个模块中的类，例如在 `electric_car.py` 中导入 `Car`。
- 避免 `from module import *`，否则名称来源不清晰，还可能发生覆盖。
- 可先导入标准库，再空一行导入自己的模块。

标准库也是模块集合，例如随机数工具：

```python
from random import choice, randint

randint(1, 6)                    # 闭区间 [1, 6]
choice(["rock", "paper", "scissors"])
```

<a id="九文件"></a>

## 九、文件

<a id="1-绝对路径与相对路径"></a>

### 1. 绝对路径与相对路径

<a id="1-绝对路径"></a>

#### 1. 绝对路径
**绝对路径是从根目录出发的路径**
1. 类Unix系统
以“/”开头，路径间的每个目录之间用“/”进行分隔，最后以目标文件或目标目录结尾
2. Windows系统
以“分区名+\”开头，路径间的每个目录之间用“\”进行分隔，最后以目标文件或目标目录结尾
- 分区名（磁盘）：
C:/D:/E:...

<a id="2-相对路径"></a>

#### 2. 相对路径
**从一个参照位置出发的路径**
1. 用“.”表示当前文件所在的目录，用“..”表示更上一层的父目录，如果继续往上，就用“.. + /或\ + ..”
2. 往下走用/或\进行分隔，同绝对路径
3. “./”可以省略

<a id="2-基本操作"></a>

### 2. 基本操作

<a id="1-打开文件"></a>

#### 1. 打开文件
方式一：
```
from pathlib import Path
文件对象=Path(文件路径)
```
方式二：
`文件对象 = open(name, mode, encoding)`
name：文件名（字符串）
mode：打开模式（只读，写入，追加）
encoding：编码格式（推荐使用UTF-8）

<a id="2-mode三种基础访问模式"></a>

#### 2. mode三种基础访问模式
r：只读模式（**默认**）
w：写入（**原有文件内容会被删除**，若文件不存在，则创建新文件）
a：追加（新内容会被写入到已有内容之后，**若文件不存在，则创建新文件**）

<a id="3-关闭文件"></a>

#### 3. 关闭文件
`文件对象.close()`
- 若不关闭文件，文件会一直被占用
- 内置flush()的功能

<a id="4-with-open语句"></a>

#### 4. with open语句
```
with open(name,mode,encoding) as 文件对象:
   对文件的操作
```
**文件会自动关闭**
**推荐使用with open()，因为当我们退出代码块的时候会自动关闭文件**

<a id="3-读取"></a>

### 3. 读取
方式一：
```
from pathlib import Path
内容 = 文件对象.read_text(encoding="utf-8")
```
方式二：
1. `文件对象.read(num)`
文本模式下 `num` 表示最多读取的字符数；未传入时读取当前位置到文件末尾的所有内容。
2. `文件对象.readline()`
读取一行数据
3. `文件对象.readlines()`
readlines可以按照行的方式把整个文件的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据是一个元素
- **多次读取会从上一个读取停止的地方继续读取**

逐行处理大文件时，不必一次加载全部内容：

```python
from pathlib import Path

path = Path("pi_digits.txt")
with path.open(encoding="utf-8") as file:
    for line in file:
        print(line.rstrip())
```

`read_text()`、`read()` 和逐行读取通常会保留文件中的换行符。仅删除行末空白可用 `rstrip()`；不要随意使用 `strip()`，否则行首有意义的空格也会消失。

<a id="4-写入"></a>

### 4. 写入
方式一：
```
from pathlib import Path
文件对象.write_text("要写入的内容", encoding="utf-8")
```
方式二：
1. 文件写入：
`文件对象.write(写入内容)`
1. 内容刷新：
`文件对象.flush()`
- `write()` 将内容交给缓冲区，返回写入的字符数；缓冲区会在适当时机、关闭文件或显式调用 `flush()` 时刷新。
- 写入文本时必须传入字符串，且 `write()` 不会自动添加换行符。
- 正常使用 `with` 时一般无需手动 `flush()` 或 `close()`。

<a id="5-追加"></a>

### 5. 追加
与写入的方式二中相同，但在打开文件时使用“a”方式
```python
with open(file_path, mode="a", encoding="utf-8") as file:
   file.write(内容)
```

<a id="6-存储及共享数据"></a>

### 6. 存储及共享数据

<a id="1-存储"></a>

#### 1. 存储
```
from pathlib import Path
import json
文件对象=Path("要存储到的文件.json")
变量=json.dumps(存储内容)
文件对象.write_text(变量)
```
**例：**
```python
from pathlib import Path
import json

path = Path("new_data.json")
numbers = []
while True:
   isGoing = input("Continue or Stop?(anything except 'q' to continue.)")
   if isGoing.lower() == 'q':
      break
   else:
      num = input("Please a number:")
      numbers.append(num)
      print("Now your number is stored in a container.")

contents = json.dumps(numbers)
path.write_text(contents)
```
**json.dumps()函数接受一个实参，转换为JSON格式的字符串**

<a id="2-读取"></a>

#### 2. 读取
```
from pathlib import Path
import json
文件对象=Path("要存储到的文件.json")
变量=文件对象.read_text()
读取内容=json.load(变量)
```
**例：**
```python
import json
from pathlib import Path
from typing import List

class Employee:
    def __init__(self, name: str, edu_background: str, age: int, init_salary: float = 5000):
        self.name = name.title()
        self.edu_background = edu_background.title()
        self.age = age
        self.salary = init_salary

    def change_salary(self, new_salary: float) -> None:
        self.salary = new_salary

    def increase_salary(self, increment: float) -> None:
        if increment <= 0:
            return
        else:
            self.salary += increment

    def to_dict(self) -> dict:
        """将Employee对象转换为字典，用于JSON序列化"""
        return {
            'name': self.name,
            'edu_background': self.edu_background,
            'age': self.age,
            'salary': self.salary
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """从字典创建Employee对象，用于JSON反序列化"""
        return cls(
            name=data['name'],
            edu_background=data['edu_background'],
            age=data['age'],
            init_salary=data['salary']
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.edu_background}, {self.age}岁, 薪资: ￥{self.salary:.2f}"

# 创建员工列表
company: List[Employee] = [
    Employee('Mike', 'Doctor', 30, 30000),
    Employee('John', 'master', 25, 5000)
]

# 显示原始数据
print("原始员工数据:")
for emp in company:
    print(emp)
print()

# 1. 保存到文件
path = Path("companys_info.json")  # 添加.json扩展名更好

# 转换为字典列表
company_dicts = [emp.to_dict() for emp in company]

# 写入JSON
try:
    # 方法1：使用Path.write_text
    contents = json.dumps(company_dicts, indent=2, ensure_ascii=False)
    path.write_text(contents, encoding='utf-8')
    print(f"数据已保存到: {path}")

    # 方法2：使用with open（更传统）
    # with open(path, 'w', encoding='utf-8') as f:
    #     json.dump(company_dicts, f, indent=2, ensure_ascii=False)

except Exception as e:
    print(f"保存失败: {e}")
    exit(1)

print()

# 2. 从文件读取
try:
    # 方法1：使用Path.read_text
    contents = path.read_text(encoding='utf-8')
    loaded_dicts = json.loads(contents)  # json.loads() 用于字符串

    # 方法2：使用with open
    # with open(path, 'r', encoding='utf-8') as f:
    #     loaded_dicts = json.load(f)  # json.load() 用于文件对象

    # 将字典转换回Employee对象
    loaded_company = [Employee.from_dict(emp_dict) for emp_dict in loaded_dicts]

    print("从文件读取的员工数据:")
    for employee in loaded_company:
        print(f"  姓名: {employee.name}")
        print(f"  学历: {employee.edu_background}")
        print(f"  年龄: {employee.age}")
        print(f"  薪资: ￥{employee.salary:.2f}")
        print()

except FileNotFoundError:
    print(f"错误: 文件 {path} 不存在")
except json.JSONDecodeError as e:
    print(f"错误: JSON解析失败 - {e}")
except Exception as e:
    print(f"错误: {e}")
```
**json.load()函数将一个JSON格式的字符串作为参数，并返回一个Python对象**

<a id="3-jsondump和jsondumps和jsonload和jsonloads辨析"></a>

#### 3. json.dump()和json.dumps()和json.load()和json.loads()辨析

<a id="1-jsondumps是将python对象转化为json字符串的形式"></a>

##### 1. json.dumps()是将Python对象转化为json字符串的形式
```python
import json

# Python字典
data = {
    "name": "张三",
    "age": 25,
    "is_student": False,
    "courses": ["数学", "英语", "编程"],
    "scores": {"数学": 90, "英语": 85}
}

# 转换为JSON字符串
json_string = json.dumps(data)
print(json_string)
# 输出：{"name": "\u5f20\u4e09", "age": 25, "is_student": false, "courses": ["\u6570\u5b66", "\u82f1\u8bed", "\u7f16\u7a0b"], "scores": {"\u6570\u5b66": 90, "\u82f1\u8bed": 85}}

# 美化输出（indent参数）
pretty_json = json.dumps(data, indent=2, ensure_ascii=False)
print(pretty_json)
# 输出：
# {
#   "name": "张三",
#   "age": 25,
#   "is_student": false,
#   "courses": [
#     "数学",
#     "英语",
#     "编程"
#   ],
#   "scores": {
#     "数学": 90,
#     "英语": 85
#   }
# }
```
**常用参数详解**
```python
import json
from datetime import datetime

data = {
    "name": "张三",
    "birthday": datetime.now(),  # 日期时间对象
    "score": 95.5
}

# 1. indent: 缩进美化
print("1. 缩进美化:")
print(json.dumps(data, indent=4))

# 2. ensure_ascii: 是否转义非ASCII字符（中文显示）
print("\n2. 中文显示:")
print(json.dumps({"name": "张三"}, ensure_ascii=False))  # {"name": "张三"}
print(json.dumps({"name": "张三"}, ensure_ascii=True))   # {"name": "\u5f20\u4e09"}

# 3. sort_keys: 按键排序
print("\n3. 按键排序:")
print(json.dumps({"b": 2, "a": 1, "c": 3}, sort_keys=True))  # {"a": 1, "b": 2, "c": 3}

# 4. separators: 自定义分隔符（默认: (', ', ': ')）
print("\n4. 紧凑格式:")
print(json.dumps(data, separators=(',', ':')))  # 更紧凑，无空格

# 5. default: 处理无法序列化的对象
def datetime_handler(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    raise TypeError(f"Type {type(obj)} not serializable")

print("\n5. 处理自定义对象:")
try:
    json.dumps(data)  # 会报错，datetime无法序列化
except TypeError as e:
    print(f"错误: {e}")

# 使用default参数
safe_json = json.dumps(data, default=datetime_handler, ensure_ascii=False)
print(f"安全序列化: {safe_json}")
```

<a id="2-jsonloads是将json字符串转化为python对象"></a>

##### 2. json.loads()是将json字符串转化为Python对象
```python
import json

# JSON字符串
json_string = '''
{
    "name": "李四",
    "age": 30,
    "married": true,
    "hobbies": ["读书", "游泳", "编程"],
    "address": {
        "city": "北京",
        "street": "中关村"
    }
}
'''

# 解析JSON字符串
data = json.loads(json_string)

print("解析后的数据类型:", type(data))  # <class 'dict'>
print("姓名:", data["name"])           # 李四
print("年龄:", data["age"])            # 30
print("已婚:", data["married"])        # True (注意：JSON的true转为Python的True)
print("爱好:", data["hobbies"])        # ['读书', '游泳', '编程']
print("城市:", data["address"]["city"]) # 北京

# 类型转换对照
print("\nJSON到Python类型转换:")
print("JSON null → Python", type(json.loads('null')))      # NoneType
print("JSON true → Python", type(json.loads('true')))      # bool
print("JSON false → Python", type(json.loads('false')))    # bool
print("JSON number → Python", type(json.loads('123')))     # int
print("JSON number → Python", type(json.loads('12.3')))    # float
print("JSON string → Python", type(json.loads('"hello"'))) # str
print("JSON array → Python", type(json.loads('[1,2,3]')))  # list
print("JSON object → Python", type(json.loads('{"a":1}'))) # dict
```

<a id="3-jsondump是将python对象写入文件"></a>

##### 3. json.dump()是将python对象写入文件
```python
import json

# 数据
data = {
    "students": [
        {"name": "张三", "score": 90},
        {"name": "李四", "score": 85},
        {"name": "王五", "score": 92}
    ],
    "class": "三年二班",
    "teacher": "王老师"
}

# 写入文件
with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("数据已写入 students.json")

# 验证写入
with open('students.json', 'r', encoding='utf-8') as f:
    content = f.read()
    print("\n文件内容:")
    print(content)
```

<a id="4-jsonload是从文件读取json"></a>

##### 4. json.load()是从文件读取json
```python
import json

# 先创建一个JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump({
        "name": "王五",
        "age": 28,
        "skills": ["Python", "Java", "SQL"]
    }, f, ensure_ascii=False, indent=2)

# 使用json.load()从文件读取
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # 注意：是load()不是loads()

print("从文件加载的数据:")
print(f"姓名: {data['name']}")
print(f"年龄: {data['age']}")
print(f"技能: {', '.join(data['skills'])}")
```

<a id="十异常"></a>

## 十、异常

<a id="1-捕获常规异常"></a>

### 1. 捕获常规异常
```
try:
   可能出现的异常
except:
   如果出现异常执行的代码
```
（捕获全部异常）
**具体的例子：**
```python
try:
    # 可能出错的代码
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print(f"结果是: {result}")
except:
    # 发生任何异常都会执行这里
    print("出错了！")
```

<a id="2-捕获指定异常"></a>

### 2. 捕获指定异常
```
try:
   可能出现的异常
except 指定异常 as 别名:
   如果出现异常执行的代码
```
**具体的例子：**
```python
try:
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print(f"结果是: {result}")

except ValueError:
    print("错误：输入的不是有效数字！")
except ZeroDivisionError:
    print("错误：不能除以零！")
except Exception as e:  # 捕获其他所有异常
    print(f"发生了未知错误: {e}")
```

<a id="3-捕获多个异常"></a>

### 3. 捕获多个异常
```
try:
   可能出现的异常
except(异常1,异常2):
   如果出现异常执行的代码
```
**具体的例子：**
```python
try:
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print(f"结果是: {result}")

except (ValueError, ZeroDivisionError):
    print("错误：输入的数字有问题！")
except Exception as e:  # 捕获其他所有异常
    print(f"发生了未知错误: {e}")
```

<a id="4-捕获全部异常"></a>

### 4. 捕获全部异常
```
try:
   可能出现的异常
except Exception as 别名:
   如果出现异常执行的代码
```
**具体的例子：**
```python
try:
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print(f"结果是: {result}")
except Exception as e:  # 捕获其他所有异常
    print(f"发生了错误: {e}")
```

应尽可能捕获具体异常。裸 `except:` 还会捕获 `KeyboardInterrupt`、`SystemExit` 等通常不应吞掉的异常；`except Exception as e` 虽然范围稍窄，也不应替代明确的异常类型。

<a id="5-else语句"></a>

### 5. else语句
```
try:
   可能出现的异常
except:
   如果出现异常执行的代码
else:
   没有出现异常时执行的代码
```
**例：**
```python
try:
    num1 = float(input("Please input dividend: "))
    num2 = float(input("Please input divisor: "))
    result = num1 / num2
except (ValueError, ZeroDivisionError) as error:
    print(f"Calculation failed: {error}")
else:
    print(result)
```
只把可能出错的代码放入 `try`；依赖成功结果的代码放入 `else`，避免意外捕获 `else` 中产生的异常。

<a id="6-finally语句"></a>

### 6. finally语句
```
try:
   可能出现的异常
except:
   如果出现异常执行的代码
finally:
   无论是否出现异常都需要执行的代码
```
**例：**
```python
try:
    num1 = float(input("Please input dividend: "))
    num2 = float(input("Please input divisor: "))
    result = num1 / num2
except (ValueError, ZeroDivisionError) as error:
    print(f"Calculation failed: {error}")
else:
    print(result)
finally:
    print("Mission completed.")
```
这里我们会发现，即使num2为0，我们也会看到最后的“Mission Completed.”

`finally` 适合释放必须清理的资源；文件通常直接使用 `with` 管理，无需手写 `finally` 关闭。

<a id="7-文件异常与文本分析"></a>

### 7. 文件异常与文本分析

```python
from pathlib import Path

path = Path("alice.txt")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.split()
    print(f"The file has about {len(words)} words.")
```

处理一组文件时，可以把读取和统计封装为函数。某个文件不存在时，选择提示用户或使用 `pass` 静默跳过，取决于它是否影响程序的正确性。

<a id="8-传递异常"></a>

### 8. 传递异常
当函数中的一个异常没有被捕获处理时，他可以被传递到另一个函数，并可以继续传递下去，直到被捕获，或者报错
**例：**
```python
def func1():
    print("func1开始")
    result = 1 / 0  # 这里会发生除零错误
    print("func1结束")

def func2():
    print("func2开始")
    func1()  # 调用func1
    print("func2结束")

def func3():
    print("func3开始")
    func2()  # 调用func2
    print("func3结束")

# 调用
try:
    func3()
except ZeroDivisionError as e:
    print(f"捕获到异常: {e}")

# 输出:
# func3开始
# func2开始
# func1开始
# 捕获到异常: division by zero
```
以下是其可视化过程
```text
程序开始
  ↓
func3()被调用
  ↓
func3调用func2()
  ↓
func2调用func1()
  ↓
func1中发生 ZeroDivisionError
  ↓
异常从func1向上传递到func2
  ↓
func2没有捕获，继续向上传递到func3
  ↓
func3没有捕获，继续向上
  ↓
在主程序的try-except中被捕获
```

<a id="十一静默"></a>

## 十一、静默
静默指使用pass语句，让系统什么都不要做，也叫做空实现
这里我们在之前的抽象类和抽象方法也提到过
- **静默失败**
```python
from pathlib import Path

path = Path("NotExistText.txt")
try:
   contents = path.read_text(encoding="utf-8")
except:
   pass
else:
   print("Successfully open.")
#这里什么也不会输出
```
- **抽象类的占位符**
```python
from abc import ABC, abstractmethod
class Shape:
   @abstractmethod
   def area(self):
      pass

   @abstractmethod
   def perimeter(self):
      pass

from math import pi

class Circle:
   def __init__(self, radius):
      self.radius = radius

   def area(self):
      return pi * radius ** 2

   def perimeter(self):
      return pi * radius * 2
```
___
- [返回目录](#目录)
___

<a id="十二测试代码"></a>

## 十二、测试代码
第三版教材统一使用 pytest。pytest 以普通函数、原生 `assert` 和夹具构建测试；标准库 `unittest` 作为补充保留，便于阅读旧项目。

<a id="1-pytest-快速开始"></a>

### 1. pytest 快速开始

```bash
python -m pip install --upgrade pip
python -m pip install --user pytest
python -m pytest
```

- 测试文件通常命名为 `test_*.py`，测试函数以 `test_` 开头。
- `pytest` 会自动发现测试；命令不可用时使用 `python -m pytest`。
- 只运行一个文件：`python -m pytest test_survey.py`。
- 测试通过显示 `.`，失败显示 `F`；失败报告会列出实际值、期望值和调用位置。
- 测试失败时优先修复被测试代码；只有需求确实改变时才修改测试。

<a id="2-pytest-测试函数"></a>

### 2. pytest 测试函数

- **需先安装 pytest 第三方包**
命令如下：
```bash
python -m pip install --user pytest
```
- 测试文件和测试函数通常都以 `test_` 开头
```
from 测试函数所在的文件 import 测试函数
def test_测试工具函数的名称():
   变量=测试函数(参数1,参数2,参数3...)
   assert 预期结果
```
在终端输入pytest以运行测试
一个测试通过出现一个“.”，一个测试未通过出现一个“F”

pytest 直接使用 Python 的 `assert` 表达式：

```python
def test_first_last_name():
    formatted = get_formatted_name("janis", "joplin")
    assert formatted == "Janis Joplin"

def test_value_is_rejected():
    with pytest.raises(ValueError):
        int("not-a-number")
```

常见检查包括相等、不相等、成员关系、真假值和预期异常；断言只描述必须成立的结果，不在测试中复制被测试函数的实现。

<a id="3-pytest-测试类"></a>

### 3. pytest 测试类
方式一：
**对每个类方法创建一个对象重复测试函数的过程进行测试**
方式二：
**使用fixture装饰器**
**例：**
```
import pytest
from 测试类所在的文件 import 测试类
@pytest.fixture
def 创建一个对象的函数()
   函数体（用于创建一个对象并返回）
def test_测试工具函数的名称1(创建的对象):
def test_测试工具函数的名称2(创建的对象):
...
```
**例：**
```python
from function import func1, func2
def test_func1():
   assert func1() == "预期的结果"

def test_func2():
   res = func2()
   assert res == "预期的结果"
```

<a id="4-夹具和装饰器"></a>

### 4. 夹具和装饰器
**夹具**（fixture）可帮助我们搭建测试环境。这通常意味着创建供多个测试使用的资源。在 pytest 中，要创建夹具，可编写一个使用装饰器 @pytest.fixture 装饰的函数。**装饰器**（decorator）是放在函数定义前面的指令。在运行函数前，Python将该指令应用于函数，以修改函数代码的行为。
1. **装饰器**：
简单来说装饰器是一个**接受函数作为参数的一个高阶函数**，它可以对我们的新定义的函数进行修饰
```python
# 1. 定义一个装饰器
def my_decorator(func):
    """一个简单的装饰器"""
    def wrapper():
        print("函数执行前 - 做一些准备工作")
        result = func()  # 执行原函数
        print("函数执行后 - 做一些清理工作")
        return result
    return wrapper

# 2. 使用装饰器
@my_decorator
def say_hello():
    print("Hello, World!")
    return "完成"

# 3. 调用被装饰的函数
result = say_hello()
print(f"返回值: {result}")

# 输出:
# 函数执行前 - 做一些准备工作
# Hello, World!
# 函数执行后 - 做一些清理工作
# 返回值: 完成
```
对于装饰器的定义，下面是他的结构：
```python
def decorator(func):
   """装饰器"""
   def new_func():
      # 一些新操作1
      result = func()
      # 一些新操作2
      return result
   return new_func
#运行顺序：按照new_func()的顺序进行
```
2. 夹具
夹具是pytest框架的核心特性，用于测试准备和清理工作。
**下面是简单的夹具的使用：**
```python
#survey.py
class AnonymousSurvey:
    """手机匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题, 并未存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储淡粉调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Surevy results:")
        for response in self.responses:
            print(f"- {response}")

    def calculate_differ(self):
        """计算有多少不同的答案"""
        return len(set(self.responses))
#test.py
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
   """
   一个可供所有测试函数使用的AnonymousSurvey实例
   """
   question = "What language did you first learn to speak?"
   language_survey = AnonymousSurvey(question)
   return language_survey
def test_store_single_response(language_survey):
   """测试单个答案会被妥善地存储"""
   language_survey.store_response('English')
   assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
   """测试三个答案会被妥善地存储"""
   responses = ['English', 'Spanish', 'Mandarin']
   for response in responses:
      language_survey.store_response(response)
   for response in responses:
         assert response in language_survey.responses
```

测试函数的参数名与夹具函数名一致时，pytest 会自动调用夹具，并把返回值注入测试。默认情况下，函数作用域夹具会为每个测试重新创建对象，避免测试之间共享状态。

<a id="十三项目一外星人入侵"></a>

## 十三、项目一：外星人入侵

本项目对应教材第 12～14 章，目标是使用 Pygame 构建一个具有飞船、子弹、外星人舰队、碰撞、计分和难度递增机制的二维游戏。重点不是记住每一行代码，而是掌握**事件循环、对象职责、状态管理和逐步重构**。

<a id="1-项目结构"></a>

### 1. 项目结构

推荐按职责拆分文件：

```text
alien_invasion/
├── alien_invasion.py   # 程序入口和主循环
├── settings.py         # 全局配置与动态速度
├── game_stats.py       # 本局运行状态与最高分
├── ship.py             # 飞船
├── bullet.py           # 子弹
├── alien.py            # 外星人
├── button.py           # Play 按钮
├── scoreboard.py       # 得分、等级和剩余飞船
└── images/
    └── ship.bmp
```

安装与启动：

```bash
python -m pip install pygame
python alien_invasion.py
```

<a id="2-创建窗口与游戏循环"></a>

### 2. 创建窗口与游戏循环

```python
import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """管理游戏资源和行为的主类。"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
```

主循环每一帧都遵循以下顺序：

1. 读取并处理键盘、鼠标和关闭窗口事件。
2. 根据当前输入更新飞船、子弹、外星人和碰撞状态。
3. 绘制背景、游戏对象、分数和按钮。
4. 使用 `pygame.display.flip()` 显示新画面。
5. 使用 `Clock.tick(60)` 将循环限制为每秒最多 60 帧，使不同硬件上的运行速度更一致。

第三版把整个游戏组织为 `AlienInvasion` 类，以下划线开头的方法表示仅供类内部使用。不要把耗时阻塞操作放入主循环，否则窗口会失去响应。

需要全屏时可以让 Pygame 使用当前显示器尺寸，并把实际尺寸同步到设置对象：

```python
self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
self.settings.screen_width = self.screen.get_rect().width
self.settings.screen_height = self.screen.get_rect().height
```

<a id="3-集中管理设置"></a>

### 3. 集中管理设置

```python
class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
```

固定设置在初始化时确定；随等级变化的设置放入 `initialize_dynamic_settings()`，新游戏时可以统一重置。

<a id="4-飞船与连续移动"></a>

### 4. 飞船与连续移动

Pygame 使用 `Rect` 保存对象的位置和尺寸。图像的 `get_rect()` 返回矩形，窗口的 `get_rect()` 返回屏幕矩形。

```python
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
```

使用浮点数 `center` 累积位置，最后同步给只保存整数坐标的 `rect`，才能保留小于一个像素的速度。按键按下时设置移动标志，松开时清除标志，可实现连续移动。

<a id="5-事件处理与重构"></a>

### 5. 事件处理与重构

第三版把事件处理拆成主类的私有方法：

```python
def _check_keydown_events(self, event):
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()
    elif event.key == pygame.K_q:
        sys.exit()


def _check_keyup_events(self, event):
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
```

`_check_events()` 负责分派事件，`_check_keydown_events()` 与 `_check_keyup_events()` 分别维护按键状态。`Q` 可直接退出；后续还可以让 `P` 键调用与 Play 按钮相同的启动逻辑。

<a id="6-子弹与精灵编组"></a>

### 6. 子弹与精灵编组

子弹继承 `pygame.sprite.Sprite`，多个子弹放入 `pygame.sprite.Group` 统一更新和绘制：

```python
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
        self.color = self.settings.bullet_color

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
```

```python
def _fire_bullet(self):
    if len(self.bullets) < self.settings.bullets_allowed:
        self.bullets.add(Bullet(self))


bullets = pygame.sprite.Group()
bullets.update()
for bullet in bullets.copy():
    if bullet.rect.bottom <= 0:
        bullets.remove(bullet)
```

删除集合元素时遍历 `copy()`，避免一边遍历一边修改原编组。

<a id="7-外星人舰队"></a>

### 7. 外星人舰队

单个外星人与飞船类似，也继承 `Sprite`。舰队按外星人的宽度和高度计算可容纳的行列数：

```python
available_space_x = settings.screen_width - 2 * alien_width
number_aliens_x = int(available_space_x / (2 * alien_width))

available_space_y = settings.screen_height - 3 * alien_height - ship_height
number_rows = int(available_space_y / (2 * alien_height))
```

创建舰队时使用嵌套循环；每个外星人的坐标由列号、行号和对象尺寸计算。舰队移动规则：

1. 所有外星人沿 `fleet_direction` 水平移动。
2. 任一外星人碰到左右边缘时，全体向下移动 `fleet_drop_speed`。
3. 将 `fleet_direction` 乘以 `-1`，改变水平移动方向。

```python
def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break
```

<a id="8-碰撞生命与关卡"></a>

### 8. 碰撞、生命与关卡

常用碰撞函数：

```python
collisions = pygame.sprite.groupcollide(
    bullets, aliens, True, True
)

if pygame.sprite.spritecollideany(ship, aliens):
    ship_hit(...)
```

- `groupcollide()` 的两个布尔参数决定碰撞后是否删除对应组中的对象。
- 外星人组清空后，删除剩余子弹、创建新舰队、提升等级并加速。
- 外星人撞到飞船或到达屏幕底部时减少一条生命，清空舰队与子弹，重新居中飞船。
- 生命用尽后将 `game_active` 设为 `False`，而不是直接退出进程。

```python
class GameStats:
    def __init__(self, settings):
        self.settings = settings
        self.high_score = 0
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
```

<a id="9-play-按钮与计分板"></a>

### 9. Play 按钮与计分板

按钮需要保存文字渲染结果和矩形区域。鼠标点击时用 `button.rect.collidepoint(mouse_x, mouse_y)` 判断是否点中。

开始新游戏的操作顺序：

1. 重置统计信息和动态设置。
2. 清空外星人与子弹编组。
3. 创建新舰队并居中飞船。
4. 重新准备分数、最高分、等级和剩余飞船图像。
5. 隐藏鼠标并把 `game_active` 设为 `True`。

第三版还让 `P` 键复用开始游戏逻辑。应把“重置并开始”的步骤封装为一个方法，同时检查游戏当前是否处于非活动状态，避免在游戏进行中误重置。

得分由碰撞结果计算：

```python
for aliens_hit in collisions.values():
    stats.score += settings.alien_points * len(aliens_hit)
```

每次分数、等级或生命变化后，都要重新渲染相应图像。最高分不随单局重置；只在当前分数更高时更新。

<a id="10-项目调试清单"></a>

### 10. 项目调试清单

- 确认事件循环每帧都运行，`QUIT` 事件能够退出。
- 更新对象后再绘制；绘制完所有对象后再 `flip()`。
- 图像路径以程序工作目录为参照，路径错误会触发加载异常。
- 碰撞不生效时检查对象是否都在精灵组中、`rect` 是否同步更新。
- 确认 `pygame.time.Clock` 在初始化时创建，并在每帧末尾调用 `tick(60)`；第三版仍按“每帧位移”更新，因此稳定帧率直接影响移动速度的一致性。
- 新游戏必须同时重置统计信息、动态速度和对象编组。

<a id="十四项目二数据可视化"></a>

## 十四、项目二：数据可视化

本项目对应第三版第 15～17 章，涵盖 Matplotlib、Plotly、CSV、GeoJSON 和 Web API。主线是“获取数据 → 检查结构 → 清洗转换 → 可视化 → 验证结果”。

<a id="1-matplotlib-折线图"></a>

### 1. Matplotlib 折线图

```python
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)
plt.show()
```

未提供横坐标时，Matplotlib 默认从索引 0 开始，可能造成数据含义错位，因此应显式传入 `input_values`。

<a id="2-散点图与颜色映射"></a>

### 2. 散点图与颜色映射

```python
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(
    x_values,
    y_values,
    c=y_values,
    cmap=plt.cm.Blues,
    edgecolors="none",
    s=20,
)
ax.axis([0, 1100, 0, 1_100_000])
plt.savefig("squares_plot.png", bbox_inches="tight")
```

- `c` 和 `cmap` 按数值映射颜色。
- `s` 控制点大小。
- `edgecolors="none"` 去掉点边缘。
- `savefig()` 应在 `show()` 前调用，`bbox_inches="tight"` 可裁掉多余空白。

<a id="3-随机漫步"></a>

### 3. 随机漫步

随机漫步保存横、纵坐标列表，每一步随机选择方向和距离，并拒绝原地踏步：

```python
from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self._get_step()
            y_step = self._get_step()
            if x_step == 0 and y_step == 0:
                continue
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

    @staticmethod
    def _get_step():
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance
```

绘制时可用点的序号作为颜色序列，突出时间顺序；单独标记起点和终点，并隐藏坐标轴：

```python
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors="none", s=15)
plt.scatter(0, 0, c="green", edgecolors="none", s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
plt.axis("off")
```

<a id="4-掷骰子与频数统计"></a>

### 4. 掷骰子与频数统计

```python
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
```

```python
die_1 = Die()
die_2 = Die()
results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result + 1)]
```

两个骰子的最小和是 2，最大和是两者面数之和。横坐标标签和频数列表必须使用相同的取值范围。大量数据用重复的 `count()` 效率较低时可改用 `collections.Counter`。

第三版使用 Plotly Express 生成交互式柱状图：

```python
import plotly.express as px

possible_results = range(2, max_result + 1)
title = "Results of Rolling Two D6 Dice 50,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}

fig = px.bar(
    x=possible_results,
    y=frequencies,
    title=title,
    labels=labels,
)
fig.update_layout(xaxis_dtick=1)
fig.show()

# 保存为可交互 HTML
fig.write_html("dice_visual.html")
```

`possible_results` 与 `frequencies` 必须一一对应。Plotly 支持悬停信息、缩放和交互；`xaxis_dtick=1` 确保每个可能点数都有刻度。静态图片导出通常还需要 Kaleido，交互结果可直接保存为 HTML。[^1]

<a id="5-读取-csv-天气数据"></a>

### 5. 读取 CSV 天气数据

```python
import csv
from datetime import datetime

dates, highs, lows = [], [], []
with open("sitka_weather_2014.csv", encoding="utf-8", newline="") as file:
    reader = csv.reader(file)
    header_row = next(reader)
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            continue
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
```

先用 `enumerate(header_row)` 确认列索引，不要假定所有数据集列顺序相同。绘制高低温并填充区间：

```python
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
fig.autofmt_xdate()
```

缺失或损坏的数据应在单行转换处捕获 `ValueError`，跳过该行并继续处理其他记录。

<a id="6-geojson-地震数据与全球地图"></a>

### 6. GeoJSON 地震数据与全球地图

GeoJSON 使用 JSON 表示地理要素。第三版使用美国地质调查局的地震数据；顶层通常包含 `metadata` 和 `features`，每个要素包含属性与几何坐标。

```python
import json
from pathlib import Path

path = Path("eq_data/eq_data_30_day_m1.geojson")
all_eq_data = json.loads(path.read_text(encoding="utf-8"))
all_eq_dicts = all_eq_data["features"]

magnitudes, longitudes, latitudes, titles = [], [], [], []
for eq_dict in all_eq_dicts:
    magnitudes.append(eq_dict["properties"]["mag"])
    longitudes.append(eq_dict["geometry"]["coordinates"][0])
    latitudes.append(eq_dict["geometry"]["coordinates"][1])
    titles.append(eq_dict["properties"]["title"])
```

GeoJSON 坐标顺序是 `(longitude, latitude)`，即经度在前、纬度在后。不能按常见的“纬度、经度”顺序读取。

```python
import plotly.express as px

title = all_eq_data["metadata"]["title"]
fig = px.scatter_geo(
    lat=latitudes,
    lon=longitudes,
    size=magnitudes,
    color=magnitudes,
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    title=title,
    hover_name=titles,
)
fig.show()
```

- `size` 用震级控制标记大小，`color` 用震级控制颜色。
- `hover_name` 显示地震位置说明。
- `metadata.title` 可自动生成与数据时间范围一致的标题。
- 数据源字段可能缺失或为 `null`，批量处理前应检查结构和异常值。
- 同样的流程可以用于世界火灾等其他包含经纬度的全球数据集。

<a id="7-web-api-基本流程"></a>

### 7. Web API 基本流程

API 请求的一般步骤：

1. 根据文档构造 URL、查询参数和请求头。
2. 发送请求并设置超时。
3. 检查状态码或调用 `raise_for_status()`。
4. 解析 JSON。
5. 检查关键字段和分页信息。
6. 清洗、排序并可视化结果。

```python
import requests

url = "https://api.github.com/search/repositories"
params = {"q": "language:python", "sort": "stars"}
headers = {"Accept": "application/vnd.github+json"}

response = requests.get(url, params=params, headers=headers, timeout=10)
response.raise_for_status()
response_dict = response.json()
repositories = response_dict["items"]
```

需要检查：

- `status_code == 200` 表示请求成功，但仍需验证响应结构。
- `total_count` 是匹配总量，当前响应中的 `items` 通常只是第一页。
- API 可能限制未认证请求频率；令牌不能写入源码仓库。
- 网络错误、超时、限流、字段缺失都应有明确处理。

<a id="8-可视化-api-数据"></a>

### 8. 可视化 API 数据

可按星标数排序仓库，展示名称、星标、描述和链接。图表工具只负责表现，数据准备应独立完成：

```python
names = [repo["name"] for repo in repositories]
stars = [repo["stargazers_count"] for repo in repositories]
descriptions = [repo.get("description") or "No description" for repo in repositories]
```

Plotly 的横轴标签可以直接使用 HTML 链接，悬停文本可组合仓库所有者和描述：

```python
import plotly.express as px

repo_links, stars, hover_texts = [], [], []
for repo in repositories:
    name = repo["name"]
    url = repo["html_url"]
    repo_links.append(f"<a href='{url}'>{name}</a>")
    stars.append(repo["stargazers_count"])
    owner = repo["owner"]["login"]
    description = repo.get("description") or "No description"
    hover_texts.append(f"{owner}<br />{description}")

fig = px.bar(
    x=repo_links,
    y=stars,
    title="Most-Starred Python Projects on GitHub",
    labels={"x": "Repository", "y": "GitHub Stars"},
    hover_name=hover_texts,
)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
                  yaxis_title_font_size=20)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
fig.show()
```

GitHub 在响应头中提供速率限制信息，也可请求 `https://api.github.com/rate_limit`。程序不应假设配额无限；遇到 `403`、`429` 或网络错误时应报告原因并停止或退避重试。

教材还以 Hacker News API 为例：先取得热门条目 ID，再逐个获取详情，最后按评论数排序。批量请求时要考虑失败重试、速率限制和请求总耗时。

<a id="十五项目三web-应用程序"></a>

## 十五、项目三：Web 应用程序

本项目对应第三版第 18～20 章，使用 Django 构建“学习笔记”网站，主线包括模型、URL、视图、模板、表单、认证、数据所有权、Bootstrap 样式和 Platform.sh 部署。第三方服务和部署命令具有版本时效性，实际部署前仍应核对当前文档。[^2]

<a id="1-虚拟环境与项目初始化"></a>

### 1. 虚拟环境与项目初始化

```bash
python -m venv .venv
```

Windows PowerShell 激活：

```powershell
.\.venv\Scripts\Activate.ps1
```

安装并创建项目：

```bash
python -m pip install django
django-admin startproject learning_log .
python manage.py migrate
python manage.py runserver
```

主要文件：

```text
learning_log/
├── manage.py
└── learning_log/
    ├── settings.py   # 应用、数据库、模板、时区等配置
    ├── urls.py       # 项目级 URL 路由
    ├── asgi.py       # ASGI 入口
    └── wsgi.py       # WSGI 入口
```

`runserver` 只用于开发环境，不应作为生产服务器。

<a id="2-创建应用"></a>

### 2. 创建应用

```bash
python manage.py startapp learning_logs
```

将应用加入 `INSTALLED_APPS`。一个 Django 项目可以包含多个应用；项目负责整体配置，应用负责一组具体功能。

<a id="3-定义模型"></a>

### 3. 定义模型

```python
from django.db import models


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.text[:50]}..."
```

- `ForeignKey` 建立多对一关系：一个主题可以有多条条目。
- `on_delete=models.CASCADE` 表示删除主题时同时删除其条目。
- 修改模型后执行：

```bash
python manage.py makemigrations learning_logs
python manage.py migrate
```

迁移文件应纳入版本控制，不能只修改数据库而不保存迁移。

<a id="4-管理网站与交互式-shell"></a>

### 4. 管理网站与交互式 shell

```bash
python manage.py createsuperuser
python manage.py shell
```

注册模型：

```python
from django.contrib import admin
from .models import Entry, Topic

admin.site.register(Topic)
admin.site.register(Entry)
```

常见 ORM 查询：

```python
Topic.objects.all()
Topic.objects.get(id=1)
topic.entry_set.all()
Topic.objects.order_by("date_added")
```

<a id="5-url视图与模板"></a>

### 5. URL、视图与模板

请求流：

```text
浏览器请求 → 项目 urls.py → 应用 urls.py → 视图 → 模板/数据 → HTTP 响应
```

应用路由：

```python
# learning_logs/urls.py
from django.urls import path
from . import views

app_name = "learning_logs"
urlpatterns = [
    path("", views.index, name="index"),
    path("topics/", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
```

视图负责查询和构造上下文：

```python
from django.shortcuts import get_object_or_404, render
from .models import Topic


def topic(request, topic_id):
    topic_obj = get_object_or_404(Topic, id=topic_id)
    entries = topic_obj.entry_set.order_by("-date_added")
    context = {"topic": topic_obj, "entries": entries}
    return render(request, "learning_logs/topic.html", context)
```

模板继承消除重复页面结构：

```django
{% extends "learning_logs/base.html" %}

{% block content %}
  <h2>{{ topic }}</h2>
  {% for entry in entries %}
    <p>{{ entry.date_added|date:"M d, Y H:i" }}</p>
    <p>{{ entry.text|linebreaks }}</p>
  {% empty %}
    <p>There are no entries for this topic yet.</p>
  {% endfor %}
{% endblock content %}
```

<a id="6-表单与重定向"></a>

### 6. 表单与重定向

```python
from django import forms
from .models import Entry, Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
```

处理 GET 与 POST：

```python
from django.shortcuts import redirect, render


def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")
    return render(request, "learning_logs/new_topic.html", {"form": form})
```

- GET 显示空表单，POST 验证并保存用户提交的数据。
- 模板中的 POST 表单必须包含 `{% csrf_token %}`。
- 保存成功后重定向，避免刷新页面导致重复提交。
- 编辑对象时给 `ModelForm` 传入 `instance=existing_object`。

<a id="7-用户账户与权限"></a>

### 7. 用户账户与权限

Django 自带认证系统，可提供登录、退出和用户模型。限制页面访问：

```python
from django.contrib.auth.decorators import login_required


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    return render(request, "learning_logs/topics.html", {"topics": topics})
```

为主题增加所有者：

```python
from django.contrib.auth.models import User

owner = models.ForeignKey(User, on_delete=models.CASCADE)
```

新增主题时不能让客户端选择任意所有者：

```python
new_topic = form.save(commit=False)
new_topic.owner = request.user
new_topic.save()
```

访问单个主题、创建条目和编辑条目前都必须验证所有权：

```python
topic = get_object_or_404(Topic, id=topic_id, owner=request.user)
```

仅隐藏页面链接不是权限控制；服务器端视图必须验证身份和对象归属。

<a id="8-注册登录与退出"></a>

### 8. 注册、登录与退出

- 登录使用 Django 提供的认证视图和登录模板。
- 注册通常使用 `UserCreationForm`，保存后可自动登录。
- 退出应使用框架提供的安全视图，并在界面中清晰显示当前用户。
- 设置 `LOGIN_URL` 或在装饰器中指定登录页，让未登录用户跳转后再返回原页面。

密码不应自行明文保存或手写哈希逻辑；使用 Django 的用户模型和认证 API。

<a id="9-样式与模板布局"></a>

### 9. 样式与模板布局

第三版通过 `django-bootstrap5` 集成 Bootstrap 5：

```bash
python -m pip install django-bootstrap5
```

在 `INSTALLED_APPS` 中加入：

```python
INSTALLED_APPS = [
    # Django 与项目应用...
    "django_bootstrap5",
]
```

基础模板加载 Bootstrap 标签：

```django
{% load django_bootstrap5 %}
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Learning Log</title>
    {% bootstrap_css %}
    {% bootstrap_javascript %}
  </head>
  <body>
    {% block content %}{% endblock content %}
  </body>
</html>
```

表单可使用 `{% bootstrap_form form %}` 和 `{% bootstrap_button %}` 渲染。无论使用哪一版 Bootstrap，都应遵循：

- 公共导航和页面骨架放在基础模板。
- 静态 CSS、JavaScript 和图片通过 Django static 系统管理。
- 表单错误必须显示给用户。
- 响应式布局在窄屏和宽屏上都要检查。
- 不要把业务查询写入模板；复杂逻辑留在视图或模型中。

<a id="10-部署检查清单"></a>

### 10. 部署检查清单

第三版以 Platform.sh 为例，基本流程如下：

1. 注册 Platform.sh，安装其 CLI，并在本地项目中登录。
2. 安装部署辅助包并冻结依赖：

   ```bash
   python -m pip install platformshconfig
   python -m pip freeze > requirements.txt
   ```

3. 为远程 PostgreSQL 和生产服务器准备额外依赖；第三版使用 `requirements_remote.txt` 单独列出 Gunicorn 和 PostgreSQL 驱动，避免要求本地开发环境也安装它们。
4. 创建 `.platform.app.yaml`、`.platform/routes.yaml` 和 `.platform/services.yaml`，分别描述应用构建、路由与数据库服务。
5. 在 `settings.py` 中使用 `platformshconfig.Config` 判断是否位于 Platform.sh，并仅在远程环境覆盖数据库、`SECRET_KEY`、`ALLOWED_HOSTS` 和 `DEBUG`。
6. 将项目纳入 Git，创建 Platform.sh 项目并推送代码。
7. 在远程环境运行迁移、创建管理员、检查静态文件和自定义错误页。

生产设置的核心原则：

```python
from platformshconfig import Config

config = Config()
if config.is_valid_platform():
    ALLOWED_HOSTS.append(".platformsh.site")
    DEBUG = False
    if config.projectEntropy:
        SECRET_KEY = config.projectEntropy

    if not config.in_build():
        db = config.credentials("database")
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": db["path"],
                "USER": db["username"],
                "PASSWORD": db["password"],
                "HOST": db["host"],
                "PORT": db["port"],
            }
        }
```

上面代码展示配置意图，具体属性名和数据库字典结构应以所安装的 `platformshconfig` 版本为准。通用部署检查仍包括：

1. 锁定依赖版本并选择受支持的 Python 版本。
2. 设置生产数据库并执行迁移。
3. 从环境变量读取 `SECRET_KEY`、数据库凭据和第三方令牌。
4. 设置 `DEBUG = False` 和正确的 `ALLOWED_HOSTS`。
5. 收集并托管静态文件。
6. 使用生产级 WSGI/ASGI 服务器。
7. 配置 HTTPS、日志、错误监控和备份。
8. 部署后检查注册、登录、权限、表单、静态资源和数据库持久化。

严禁把密钥、生产数据库文件或用户数据提交到 Git 仓库。Platform.sh 的套餐、CLI 和配置格式可能变化，因此第三版命令应视为部署案例，不是永久有效的服务手册。[^2]

<a id="附录-a安装编辑器与求助"></a>

## 附录 A：安装、编辑器与求助

<a id="1-确认解释器"></a>

### 1. 确认解释器

```bash
python --version
python -m pip --version
```

如果系统同时安装多个 Python，始终使用“运行程序的解释器”调用 pip，即 `python -m pip`，避免包被安装到另一个环境。

<a id="2-运行程序"></a>

### 2. 运行程序

```bash
python hello_world.py
```

终端当前目录必须能找到目标文件，或传入文件路径。交互式解释器适合试验短表达式，完整程序应保存为 `.py` 文件。

<a id="3-排错顺序"></a>

### 3. 排错顺序

1. 从 traceback 最后一行确认异常类型和消息。
2. 查看 traceback 指向的自己代码中的最后一处位置。
3. 检查拼写、缩进、括号、引号、类型和边界值。
4. 用更小的输入复现问题，打印关键变量或使用调试器。
5. 查阅当前版本的官方文档和库文档。
6. 搜索错误时去掉只属于本机的路径、用户名和敏感数据。

<a id="4-编辑器与-ide"></a>

### 4. 编辑器与 IDE

- VS Code：安装 Python 扩展，使用“选择解释器”确保编辑器、终端和调试器指向同一个虚拟环境。
- IDLE：随 Python 提供，适合运行短程序和交互式试验。
- PyCharm：集成项目、解释器、调试、测试和重构工具，适合较大的 Python 工程。
- Jupyter Notebook：适合交互式数据分析和可视化；代码按单元执行，运行顺序可能影响状态。
- Vim、Emacs、Sublime Text、Geany：需要自行配置解释器、语法检查和运行命令。

无论使用哪种工具，都应知道如何在终端中运行程序和测试，以便区分编辑器问题与 Python 本身的问题。

<a id="附录-bgit-版本控制速查"></a>

## 附录 B：Git 版本控制速查

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

git init
git status
git add .
git commit -m "Start project"
git log --oneline
```

项目开始时创建 `.gitignore`，常见内容：

```gitignore
__pycache__/
*.py[cod]
.venv/
.env
.pytest_cache/
*.sqlite3
```

- 每次提交只包含一个清晰目的，提交前先看 `git diff` 和 `git status`。
- 不要提交虚拟环境、缓存、密钥和本地数据库。
- 回退前先确认工作区是否存在未保存修改；不要把版本控制当作文件同步的替代品。

<a id="附录-c教材版本说明"></a>

## 附录 C：教材版本说明

本笔记当前以 2023 年《Python Crash Course》第三版为主线。第三版全面使用 Python 3，并更新了测试、可视化、Pygame 结构和 Django 部署示例。

- 测试框架由第一版的 `unittest` 主线更新为 pytest；`unittest` 仅作为标准库补充保留。
- 骰子和 API 可视化使用 Plotly，取代第一版的 Pygal。
- 全球数据案例由旧版世界人口地图更新为 GeoJSON 地震地图。
- Pygame 主程序使用 `AlienInvasion` 类，并通过 `pygame.time.Clock` 控制帧率。
- Web 项目使用 `django-bootstrap5`，第三版部署案例为 Platform.sh。
- Pygame、Matplotlib、Plotly、Django、Bootstrap、GitHub API 和部署平台的接口仍可能随版本变化。
- 遇到安装命令或第三方库代码无法运行时，应先核对当前库版本的官方文档，而不是强行照搬旧版代码。

<a id="1-标准库-unittest-补充"></a>

### 1. 标准库 `unittest` 补充

旧项目经常使用标准库 `unittest`。测试类继承 `unittest.TestCase`，测试方法以 `test_` 开头：

```python
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted, "Janis Joplin")


if __name__ == "__main__":
    unittest.main()
```

常用方法包括 `assertEqual()`、`assertTrue()`、`assertIn()` 和 `assertRaises()`；`setUp()` 在每个测试方法前运行，对应 pytest 中函数作用域夹具承担的准备工作。

<a id="附录-d部署故障排查"></a>

## 附录 D：部署故障排查

部署问题通常发生在不同阶段，应先判断失败位置：

1. **本地阶段**：测试、迁移或静态资源是否在本机正常。
2. **构建阶段**：Python 版本、依赖安装和配置文件是否正确。
3. **发布阶段**：数据库迁移、静态文件收集和服务启动是否成功。
4. **运行阶段**：域名、环境变量、数据库连接、权限和请求日志是否正常。

排查顺序：

- 先阅读平台给出的直接建议，再查看完整构建日志和运行日志。
- 找到第一条真正的错误；后续报错可能只是连锁结果。
- 对比本地与远程的 Python、Django 和依赖版本。
- 检查文件名大小写。Windows 通常不区分大小写，Linux 服务器通常区分。
- 检查未提交文件、`.gitignore`、环境变量、迁移和静态资源路径。
- 做一次最小改动后重新部署，避免同时修改多个可能原因。
- 不要为了隐藏错误而开启生产环境的 `DEBUG`；应通过日志定位问题。

若教材使用的平台已不再适合，可换用其他支持 Python WSGI/ASGI、环境变量、数据库和静态文件的托管方案；迁移时仍遵循相同的依赖、配置、迁移、安全和日志原则。

[^1]: 第一版使用 Pygal 生成骰子直方图；第三版已改用 Plotly Express。阅读旧代码时可能仍会遇到 `pygal.Bar()` 和 `render_to_file()`。

[^2]: 第三版出版时使用 Platform.sh、`platformshconfig` 和特定配置文件。托管平台的套餐、CLI、依赖版本与配置格式变化较快，实际部署必须核对当前服务文档。
