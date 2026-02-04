# Python笔记

<font face="楷体" color="orange" size=4>以下内容是基于优质书籍《 Python编程：从入门到实践（第3版）》进行补充编撰。</font>

## 目录
- [一、什么是Python](#什么是Python)
   - 1. 如何安装Python（Windows版）
   - 2. 应用领域

- [二、基础语法](#基础语法)
   - 1. 字面量
   - 2. 注释
   - 3. 变量
   - 4. 查看数据类型
   - 5. 运算符
   - 6. 转义符
   - 7. 占位符及有效数字保留
   - 8. 表达式
   - 9. 布尔数
   - 10. None值

- [二、数据容器](#数据容器)
   - 1. 数据容器概述
   - 2. 列表
   - 3. 元组
   - 4. 字符串
   - 5. 集合
   - 6. 字典

- [三、input输入和print()输出](#input输出)
   - 1. input()输入
   - 2. print()输出

- [四、for遍历和while循环](#循环)

- [五、函数](#函数)
   - 1. 定义
   - 2. 定义函数
   - 3. 函数的说明
   - 4. 变量作用域
   - 5. 多返回值
   - 6. 多种参数传递形式
   - 7. 函数作为参数传入
   - 8. 注意事项

- [六、模块](#模块)
   - 1. 定义
   - 2. 导入模块
   - 3. 安装第三方包

- [九、类](#类)
   - 1. 类的定义和使用
   - 2. 类内置方法（魔术方法）
   - 3. 封装
   - 4. 继承
   - 5. 多态
   - 6. 组合
   - 7. 类型注解

- [十、文件](#文件)
   - 1. 绝对路径与相对路径
   - 2. 基本操作
   - 3. 读取
   - 4. 写入
   - 5. 追加
   - 6. 存储及共享数据

- [十一、异常](#异常)
   - 1. 捕获常规异常
   - 2. 捕获指定异常
   - 3. 捕获多个异常
   - 4. 捕获全部异常
   - 5. else语句
   - 6. finally语句
   - 7. 传递异常

- [十二、静默](#静默)

- [十三、测试代码](#测试代码)
   - 1. 测试函数
   - 2. 测试类
   - 3. 夹具和装饰器

## 一、什么是Python<a id="什么是Python"></a>
Python 是一种高级、通用、解释型的编程语言，以其简洁易读的语法和强大的功能而广受欢迎。
是基于C/C++语言的一种功能强大的语言
### 1. 如何安装Python（Windows版）<a id="如何安装Python（Windows版）">
   这里是笔者所安装的版本 python-3.13
   对于后面更新的新版本我们可以去[python官网](https://www.python.org/)进行安装和下载
   至于配置环境和一些具体的操作详情可见[Python安装视频](https://www.bilibili.com/video/BV1qW4y1a7fU?spm_id_from=333.788.videopod.episodes&vd_source=0c8b5a93700047500e2347aa87475939&p=4)
   如果你用的是VScode，那么恭喜你，你只需要在VScode中找到Python的扩展安装即可
   （包括Python,Python Environment和Python Debugger）
### 2. 应用领域 <a id="应用领域"></a>
   - Web开发
   - 数据科学与机器学习
   - 自动化与脚本
   - 科学计算
   - AI
   - 教育与科研
**更多详情请自行参考蟒蛇书上的第一章教程**

## 二、基础语法<a id="基础语法"></a>
### 1.字面量<a id="字面量"></a>
在代码中被写在代码中的固定的值，包括整数，浮点数，字符串等
### 2.注释<a id="注释"></a>
单行注释：\#注释内容
多行注释："""注释内容"""
- 注释内容不会被执行
- 注意：在windows系统中我们可以使用快捷键来进行高效注释(Ctrl + /)
### 3.变量<a id="变量"></a>
#### 1.定义
变量是在程序运行时，能存储运算结果或能表示值的抽象概念（<font face="宋体" color="red" size=4>个人感觉可以先按照“就是给一个东西取了一个名字”这么理解</font>）
#### 2.定义变量
变量=值
#### 3.变量特点
可修改
- 这里的”可修改“，准确来说应该是“重新赋值”，就是在定义变量以后，我们可以在后面赋给他一个新的值，这里牵扯到**值的绑定**的问题，权且按下不表
### 4.查看数据类型<a id="查看数据类型"></a>
type(数据)
- 这里的type()是一个函数，会返回()内变量的类型
### 5.运算符<a id="运算符"></a>
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
### 6.转义符<a id="转义符"></a>
“ \ ” 后面的符号不会被解析
下面是一个例子：
```python
#现在我们要打印“Hello,world”（带上“”）
如果直接写：
print("I said,"Hello,world"") #这里会报错
但是我们可以用转义字符来进行转义，从而让python忽略掉我们的""
print("I said,\"Hello,world\"") #这里就会的带我们想要的输出I said,"Hello,world"
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
### 7.占位符及有效数字保留<a id="占位符及有效数字保留"></a>
- 将数据变为整数放入占位的位置：%d
- 将数据变为浮点数放入占位的位置：%f
- 将数据变为字符串放入占位的位置：%s 
- 精度控制：%m.nd(f/s)
m：控制宽度（很少使用），设置的宽度小于数字自身，不生效，用空格补全宽度
n：控制小数点精度，要求是数字，会进行小数的四舍五入

下面是详细解释：
#### 1.基本语法格式：
```python
   "格式化字符串" % 值
   "格式化字符串" % (值1, 值2, ...)  # 多个值用元组(这个后面会讲到)
```
#### 2.各个占位符详解
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

<a id="C语言占位符补充"></a>
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
#### 3.宽度控制 `%m`
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
#### 4.精度控制 `%.n`
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

#### 5.f-string用法（推荐）
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

### 8.表达式<a id="表达式"></a>
一条明确有执行结果的代码语句
### 9.布尔数<a id="布尔数"></a>
用于表示结果真假的数据类型
True表示真
False表示假
- 可通过比较运算得到布尔值
### 10.None值<a id="None值"></a>
#### 1.含义
None作为一个特殊的字面量，用于表示：空、无意义
#### 2.应用
- None可用于声明无内容的变量上
- 在if判断上，None等同于False

___
- [返回目录](#目录)
___

## 二、数据容器<a id="数据容器"></a>
### 1.数据容器概述<a id="数据容器概述"></a>
#### 1.定义
数据容器是可以储存多个元素的数据类型
#### 2.分类
列表(list)、元组(tuple)、字符串(str)、集合(set)、字典(dict)
#### 3.序列
序列是内容连续有序，可使用下标索引的一类数据容器
列表、元组、字符串 均可视为序列
#### 4.切片
==序列 [起始索引:结束索引:步长]==
- 起始索引留空表示从头开始
- 结束索引留空表示取到结尾
- 步长为负数表示反向取（起始和结束索引也要反向取）
#### 5.统计元素的数量
**len(数据容器)** 这个是统计总元素的数量
**数据容器.count(特定元素)** 这个是统计特定元素的数量
#### 6.求最大元素和最小元素
最**大**元素：==max()==
最**小**元素：==min()==
- **字典保留键去除值**
#### 7.排序
- 排序：
  - ==sorted(数据容器)==   **这里是临时排序（不改变原容器的顺序）**
  - ==数据容器.sort()==   **这里是排序（改变了原容器的顺序）**
- 反向排序：
  - 数据容器.sort(reverse=True) 
  - sorted(reverse=True)
  - 数据容器.reverse()
###### 下面是一些例子：
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

### 2.列表<a id="列表"></a>
#### 1.定义
列表=[元素,元素,元素...]
列表=list()
#### 2.索引
从前向后，编号从0递增
从后向前，编号从-1递减
#### 3.使用元素
列表[索引]
列表[外层索引][内层索引]（这里牵扯到了列表的嵌套）
#### 4.查找元素索引
列表.index(元素)
#### 5.修改元素
列表[索引]=新元素（这里相当于是重新赋值，重新绑定了一个值）
#### 6.添加元素
追加单个元素：**列表.append(元素)**
追加另一个数据容器的所有元素：**列表.extend(数据容器)**
插入单个元素：**列表.insert(索引,元素)**
###### 这里注意一下：对于要添加另一个容器的部分内容，我们可以使用extend()+切片的方法
```python
list1 = list(range(0, 10))
list2 = list(range(10, 20))
#现在让list2中的前五个元素添加到list1中
list1.extend(list2[:5])
print(list1)     #这里的结果是[0, 1, ..., 14]
```
#### 7.删除元素
**del 列表[索引]**
**列表.pop(索引)** （可用变量对删除元素进行接收）
**列表.remove(元素)** （列表中的第一个该元素）
#### 8.清空列表
**列表.clear()**
#### 9.统计元素的数量
某个元素在列表中的数量：**列表.count(元素)**
全部元素总数：**len(列表)**
#### 10.遍历列表
for遍历：
```
for 临时变量 in 数据容器:
   对临时变量进行处理
```
###### 例：
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
###### 例：
```python
list1 = [0, 1, 5, 5.0, 6.114514, 350234, 'Doro', 'cheems', 'PopCat']
index = 0
while index < len(list1):
   print(list1[index])
   index += 1
#这里就会依次打印上方的元素
```
#### 11.列表特点
1. 可以容纳多个元素(2^63^ - 1=9223372036854775807个)
2. 可容纳不同类型的元素
3. 数据有序存储
4. 允许重复数据
5. 可修改

### 3.元组<a id="元组"></a>
#### 1.定义
变量=(元素，元素，元素...)
变量=tuple()
- 定义一个元素的元组：变量=(元素，) （必须带有逗号）
#### 2.使用元素
元组[索引]
元组[外层索引][内层索引]
#### 3.查找元素索引
元组.index(元素)
#### 4.统计元素的数量
某个元素在元组中的数量：元组.count(元素)
全部元素总数：len(元组)
#### 5.遍历元组
for遍历：
```
for 临时变量 in 数据容器:
   对临时变量进行处理
```
###### 例：
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
###### 例：
```python
tuple = (1, 2, 3, 'Hakimi', 'HYW', 3.14)
index = 0
while index < len(tuple):
   print(tuple[index])
   index += 1
#依旧是打印上方的所有元素
```
#### 6.元组的特点
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
### 4.字符串<a id="字符串"></a>
#### 1.字符串嵌套
1. 交替使用单双引号
2. 使用转义符转义内层引号 ==(更为推荐)==
#### 2.字符串格式化
1. 使用加号连接字符串变量和字面量
2. 使用占位符%：
   "字符串1%s(%d/%f)字符串2" % 填入内容
   (多个变量占位，变量要用括号括起来，并按照顺序填入)
3. f"字符串1{变量}字符串2"
###### 下面是对应的例子：
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
#### 3.使用元素
字符串[索引]
#### 4.查找元素索引
字符串.index(元素)
#### 5.字符串替换
新字符串=字符串.replace(字符串1,字符串2)
```python
str1 = "Hello, world."
str2 = "China"
str3 = str1.replace("world", str2)
print(str3)    #Hello, China.
```
#### 6.字符串分割
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
#### 7.字符串规整
去除前后空格 字符串.strip()
删除右侧空白 字符串.rstrip() 
删除左侧空白 字符串.lstrip() 
去除前后指定内容 字符串.strip(字符串)
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
#### 8.统计元素的数量
某个元素在字符串中的数量：**字符串.count(元素)**
全部元素总数：**len(集合)**
#### 9.遍历字符串
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
###### 此处省略例子，跟上面的差不多
#### 10.字符串大小比较
1. 按位比较
2. 以ASCII码值确定大小
![ASCII码表](https://img.doc.xuehai.net/pic/44530094d89ba069c31ed8d9/1-966-jpg_6_0_______-628-0-0-628.jpg)
#### 11.字符串的特点
1. 只可存储字符串
2. 长度任意
3. 数据有序存储
4. 允许重复数据
5. 不可修改
### 5.集合<a id="集合"></a>
#### 1.定义（集合是唯一元素的无序集合）
集合={元素,元素,元素...}
集合=set()  （这里是设置了一个空集合）
#### 2.添加元素
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
#### 3.删除元素
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

# pop() - 随机删除并返回一个元素
item = s.pop()  # 随机删除一个元素
print(f"删除了: {item}")

# clear() - 清空集合
s.clear()       # set()
```
==注意，为了防止我们删除的时候我们一般使用discard(),这样我们删除元素的时候即使没有，我们也不会抛出异常==
#### 4.集合运算
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
#### 5.集合元素的访问
集合中元素是无序的，所以我们每次访问都会有不一样的结果
#### 6.遍历集合
```
for 临时变量 in 数据容器
   对临时变量进行处理
```
###### 值得注意的是，这里的结果是没有固定输出的，这是由于我们集合元素具有无序性的特点
#### 7.集合的特点
1. 可以容纳多个元素
2. 可容纳不同类型的元素
3. 数据无序存储（不支持索引）
4. 不允许重复数据
5. 可修改
#### 8.集合的一个非常重要的用途：去重
```python
# 最常见的用途
numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = list(set(numbers))  # 去重并转回列表
print(unique_numbers)  # [1, 2, 3, 4, 5]（顺序可能改变）
```
### 6.字典<a id="字典"></a>
#### 1.定义
**变量={键:值,键:值,键:值...}**
**变量=dict()**
#### 2.基于键获得值
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
#### 3.嵌套字典
字典={
   字典1:{ }
   字典2:{ }
   字典3:{ }
   ...
}
#### 4.添加及修改元素
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
#### 5.删除元素
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
#### 6.获取全部的元素
获取全部的键：字典.keys()
获取全部的值：字典.values()
获取全部的键值对：字典.items() **这里的items()方法要用两个变量接受**
- **返回值均为列表**
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
#### 7.遍历字典
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
#### 8.字典的特点
1. 可以容纳多个元素，每个元素为键值对
2. 可容纳不同类型的元素（键不能为字典）
3. 不支持索引
4. 不允许重复数据（重复会覆盖）
5. 可修改
## 三、input输入和print()输出<a id="input输出"></a>
1. input()输入<a id="input输入"></a>：
    1. 简单用法：
    ```python
    name = input("What is your name?")
    print(name)  #你所输入的信息

    inform = input()
    print(inform)  #终端中没有输出，但你再输入完后也会输出你所输入的内容
    ```
    2. 返回值
  **input()函数始终返回字符串类型**，因此就会涉及到类型转换的问题 <a id="类型转换问题"></a>
    ```python
    data = input("Please input a number.")   #这里即使你输入的是data（一个数据），但是在变量data中存储的类型还是字符串，而不是你所想的int/float型
    sum = int(data) + 1
    print(sum)    #这里的sum中含有int()函数进行了类型转换，未经转换直接使用会traceback：TypeError
    ```
  ###### 下面是一些类型转化实例
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
2. print()输出：<a id="print输出"></a>
    1. 简单用法：
      ```python
      print("要输出的内容")
      ```
    2. 详解:
      ```python
      print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
      ``` 
   ###### 参数说明：
   | 参数 | 说明 | 默认值 |
   | :--- | :--- | :--- |
   | `objects` | 要打印的对象，可以有多个 | 无 |
   | `sep` | 对象之间的分隔符 | space`' '` | 
   | `end` | 打印结束后的字符 | 换行符`'\n'` |
   | `file` | 输出流，可以是文件对象 | `sys.stdout` |
   | `flush` | 是否立即刷新缓冲区 | `Flase` |
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
## 四、for遍历和while循环：<a id="循环"></a>
for遍历和while循环都是一个计算机自动检索元素的过程
语法如下：
```python
for 临时变量 in 容器:
   操作
   ···

while 循环条件:
   操作
   ···
```
###### 要点注意：
- 这两个语句对于缩进有很高的要求
- while和for的使用功能虽然差的不是很多，但是具体情境要用哪个还要自行分析
## 五、函数<a id="函数"></a>
### 1.定义
函数是组织好的，可重复使用的，用来实现特定功能的代码段
### 2.定义函数
有名称的函数（多次使用）：
```
def 函数名(传入参数):
   函数体
   return 返回值 (可有可无)
```
###### 例：
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
###### 详解：
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
### 3.函数的说明
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
### 4.变量作用域
- 定义函数中的变量作用范围在函数内部，函数外部无法使用，为局部变量
- 函数内外部均可以使用的变量为全局变量
- ==局部变量转化为全局变量：global 变量==
### 5.多返回值
```
def 函数名(传入参数):
   函数体
   return 返回值1,返回值2,返回值3...
```
### 6.多种参数传递形式
#### 1.位置参数
传递参数和定义的参数的顺序和个数必须一致
#### 2.关键字参数
键=值
- 关键字参数可以不按照固定顺序
- 可以和位置参数混用，但位置参数必须在前，且匹配参数顺序
#### 3.缺省参数
- 在定义函数时为参数提供默认值，调用时不传入该参数的值，则该参数取该默认值，如果传入该参数的值，则取传入值
- 可将默认值设为空字符串或None配合if语句，从而将该值变为可选的
- 设置默认值**必须**在最后面
###### 例：
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
#### 4.可变参数（不定长参数）
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
### 7.函数作为参数传入
```
def 函数1(函数2):
   变量=函数2(传入参数)
def 函数2(传入参数):
   函数体
   return 返回值
```
### 8.注意事项
1. 描述性名称
2. 添加说明注释
3. ==指定默认值和关键字实参时，等号两边不要有空格==
4. 使用多个函数，使用两个空行将相邻的函数分隔开
## 六、模块
### 1.定义
- 模块是一个Python文件，以.py结尾
- 模块能定义函数，类和变量，模块里也能包含可执行的代码
- 一个模块就是一个工具包，每一个工具包中都有不同的工具用于实现不同的功能
### 2.导入模块
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
###### 下面是一些具体的例子：
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
### 3.安装第三方包
- 为确保运行正常，请先更新pip
- 不同编辑器安装方式不同，以下只列出了VS Code的安装方法
1. 安装
在终端输入
python -m pip install --user 第三方包名称
2. 更新
在终端输入
python -m pip install --upgrade 第三方包名称
###### 下面是对pip的一些简介：
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
## 九、类
### 1.类的定义和使用
#### 1.定义类
```
class 类名称:
   类的属性
   类的行为
```
- 类的属性：定义在类中的变量（成员变量）
- 类的行为：定义在类中的函数（成员方法）
#### 2.创建成员方法
```
def 方法名(self,形参1,形参2,形参3...)
   方法体
```
- 在方法内部，想要访问类的成员变量，必须使用“self.成员变量”，外部传入的变量无需。
- 在传参的过程中可忽略self
###### 例：
```python
class Car:
   """这是一个模拟汽车的类"""
   def __init__(self, make, model, year):
      """
      初始化一个对象的函数
      self: 代指对象自己
      make: 谁制造了它
      model: 什么型号的
      year: 那年生产的
      """
      self.make = make.title()
      self.model = model.title()
      self.year = year
      self.odometer = 0
   
   def get_descriptive_name(self):
      """返回格式规范化的表述"""
      long_name = f"{self.make} {self.model} {self.year}"
      return long_name

   def read_odometer(self):
   """打印一条消息，指出汽车的行驶里程"""
   print(f"This car has {self.odometer_reading} miles on it.")

   def update_odometer(self, mileage):
      """
      将里程表读数设置为指定的值
      拒绝将里程表的数值回调
      """
      if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
      else:
         print("You can't rol back an odometer.")

   def increment_odometer(self, miles):
      """让里程表的读数增加指定的量"""
      self.odometer_reading += miles
```
#### 2.创建类对象并调用其属性与方法
```
对象=类名称()
对象.类属性=内容
对象.方法名(传入参数)
```
###### 例：
```python
class Car:
   #--snip--

car = Class('aodi', 'a4', 2024)
#现在就可以调用各种方法了
car.read_odometer()     # 0
car.update_odometer(3000)
car.read_odometer()     # 3000
car.increment_odometer(500)
car.read_odometer()     # 3500
car.get_decripitive_name()    # Aodi A4 2024
```
### 2.类内置方法（魔术方法）
#### 1.构造方法
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
#### 2.字符串方法
当类对象需要被转换成字符串时，会输出内存地址，可以通过__str__方法，控制类转化为字符串的行为。
```
class 类名称:
   def __str__(self):
      return 字符串内容
```
###### 例：
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
##### 一个进阶用法：__repr__(self):
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
#### 3.比较运算符的方法：
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
###### 一个简单记忆的方法：
小：`l`
大：`g`
等：`e`
不：`n`
### 3.封装
#### 1.定义私有成员
变量名/方法名以“__”开头
#### 2.私有成员特点
- 私有方法无法直接被类对象使用，私有变量无法赋值也无法获取值
- 类内部成员变量和方法能够访问私有成员变量和方法
###### 这里的部分与C++差不多，我们想研究得更深入一些得话我们应该移步到C++学习
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
### 4.继承
#### 1.单继承
```
class 父类:
   父类主体
class 子类(父类):
   子类新增主体
```
#### 2.多继承
```
class 父类:
   父类主体
class 子类(父类1,父类2,父类3...):
   子类新增主体
```
###### 例：
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
#### 3.\_\_init__()的继承
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
#### 4.复写
**在子类重新定义与父类同名的属性或方法，从而对父类进行修改**
###### 例：
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
###### 有意思的是，这里的复写与C++中的重写略有所不同，有兴趣的可以自己研究一下
#### 5.调用父类同名成员
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
###### 对于super()函数的一点补充
super()函数是继承中非常重要的一个函数，我们在使用的时候应注意一下几点
- 调用super()时**不用传self参数**
- super()的调用遵循MRO顺序（多继承的情况）
###### 例：
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
### 5.多态
多态其实就是同一个名称的事物在不同情况下有不同的实现情况
#### 1.基本形式
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
###### 例：
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
#### 2.抽象类（接口）
抽象类：含有抽象方法的类叫做抽象类
抽象方法：方法体是空实现（pass）称之为抽象方法
- 抽象方法：只有方法声明，没有具体实现（方法体为空）
- 抽象类：包含至少一个抽象方法的类
- 特点：抽象类不能实例化，子类必须实现所有抽象方法
###### 例：
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
### 6.组合
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
###### 实例：
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
### 7.类型注解
类型注解是Python 3.5+引入的功能，用于在代码中明确指定**变量、参数和返回值的类型**，提高代码可读性和可维护性。
#### 1.基础数据
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
#### 2.类对象
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
#### 3.数据容器
变量:类型=
变量:容器类型[元素类型1,元素类型2,元素类型3...]
（元组需要标记出每个元素的类型，字典需要标记键和值的类型）
##### 各种容器的写法
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
#### 4.函数和方法
```
def 函数或方法名(形参名1:类型1,形参名2:类型2，形参名3:类型3...) -> 返回值类型:
   函数体
```
###### 例：
```python
def greet_guest(first: str, last: str,) -> None:
   full_name = f"{first} {last}".title()
   print(full_name)
```
#### 5.使用注释进行注解
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
#### 6.Union类型
Union类型表示这个变量或者数据容器中的变量可以是`[]`中的任意一种类型
数据容器：
```
from typing import Union
变量:数据容器[Union[类型1,类型2,类型3...]]
```
###### 例：
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
###### 例：
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
**注意：这里的`isinstance()`方法是用来判断变量是不是指定类型的函数，返回True/False**
###### 以上的内容说白了，就是告诉计算机：“这个一定是···类型的” ,这样可以提高你的代码的可维护性
## 十、文件<a id="文件"></a>
### 1.绝对路径与相对路径<a id="绝对路径和相对路径"></a>
#### 1.绝对路径
**绝对路径是从根目录出发的路径**
1. 类Unix系统
以“/”开头，路径间的每个目录之间用“/”进行分隔，最后以目标文件或目标目录结尾
2. Windows系统
以“分区名+\”开头，路径间的每个目录之间用“\”进行分隔，最后以目标文件或目标目录结尾
- 分区名（磁盘）：
C:/D:/E:...
#### 2.相对路径
**从一个参照位置出发的路径**
1. 用“.”表示当前文件所在的目录，用“..”表示更上一层的父目录，如果继续往上，就用“.. + /或\ + ..”
2. 往下走用/或\进行分隔，同绝对路径
3. “./”可以省略
### 2.基本操作<a id="基本操作"></a>
#### 1.打开文件
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
#### 2.mode三种基础访问模式
r：只读模式（**默认**）
w：写入（**原有文件内容会被删除**，若文件不存在，则创建新文件）
a：追加（新内容会被写入到已有内容之后，**若文件不存在，则创建新文件**）
#### 3.关闭文件
`文件对象.close()`
- 若不关闭文件，文件会一直被占用
- 内置flush()的功能
#### 4.with open语句
```
with open(name,mode,encoding) as 文件对象:
   对文件的操作
```
**文件会自动关闭**
**推荐使用with open()，因为当我们退出代码块的时候会自动关闭文件**
### 3.读取<a id="读取"></a>
方式一：
```
from pathlib import Path
文件对象.read_text()
```
方式二：
1. `文件对象.read(num)`
num表示要从文件中读取数据的长度（单位是字节），如果没有传入num，那么就读取文件中的所有数据。
2. `文件对象.readline()`
读取一行数据
3. `文件对象.readlines()`
readlines可以按照行的方式把整个文件的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据是一个元素
- **多次读取会从上一个读取停止的地方继续读取**
### 4.写入<a id="写入"></a>
方式一：
```
from pathlib import Path
文件对象.write_text()
```
方式二：
1. 文件写入：
`文件对象.write(写入内容)`
1. 内容刷新：
`文件对象.flush()`
- 直接调用write，内容并未真正写入文件，而是会积攒在程序内存中，称为缓冲区
- 当调用flush的时候，内容会真正写入文件
- 这样做能避免频繁的操作硬盘，导致效率下降
### 5.追加<a id="追加"></a>
与写入的方式二中相同，但在打开文件时使用“a”方式
```python
with open(file_path, mode="a", encoding="UTF-8"):
   file_path.write(内容)
```
### 6.存储及共享数据<a id="存储"></a>
#### 1.存储<a id="存储"></a>
```
from pathlib import Path
import json
文件对象=Path("要存储到的文件.json")
变量=json.dumps(存储内容)
文件对象.write_text(变量)
```
###### 例：
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
#### 2.读取<a id="读取"></a>
```
from pathlib import Path
import json
文件对象=Path("要存储到的文件.json")
变量=文件对象.read_text()
读取内容=json.load(变量)
```
###### 例：
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

#### 3.json.dump()和json.dumps()和json.load()和json.loads()辨析<a id="json辨析">
##### 1.json.dumps()是将Python对象转化为json字符串的形式
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
##### 2.json.loads()是将json字符串转化为Python对象
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
##### 3.json.dump()是将python对象写入文件
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
##### 4.json.load()是从文件读取json
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
## 十一、异常<a id="异常"></a>
### 1.捕获常规异常
```
try:
   可能出现的异常
except:
   如果出现异常执行的代码
```
（捕获全部异常）
###### 具体的例子：
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
### 2.捕获指定异常
```
try:
   可能出现的异常
except 指定异常 as 别名:
   如果出现异常执行的代码
```
###### 具体的例子：
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
### 3.捕获多个异常
```
try:
   可能出现的异常
except(异常1,异常2):
   如果出现异常执行的代码
```
###### 具体的例子:
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
### 4.捕获全部异常
```
try:
   可能出现的异常
except Exception as 别名:
   如果出现异常执行的代码
```
###### 具体的例子：
```python
try:
    num = int(input("请输入一个数字: "))
    result = 10 / num
    print(f"结果是: {result}")
except Exception as e:  # 捕获其他所有异常
    print(f"发生了错误: {e}")
#这里也可以这么写
#except Exception:
#    print(f"发生了错误：{Exception}")  #这个时候就是弹出具体的错误
```
### 5.else语句
```
try:
   可能出现的异常
except:
   如果出现异常执行的代码
else:
   没有出现异常时执行的代码
```
###### 例：
```python
try:
   num1 = input("Please input dividend.")
   num2 = input("Please input divisior.")
   try:
      res = num1 / num2
   except ZeroDivisionError:
      print("You can't divide some numbers by zero.")
   else:
      print(res)
```
在这里你想正常显示res，只有让num2非零，否则就会进入except板块
### 6.finally语句
```
try:
   可能出现的异常
except:
   如果出现异常执行的代码
finally:
   无论是否出现异常都需要执行的代码
```
###### 例：
```python
try:
   num1 = input("Please input dividend.")
   num2 = input("Please input divisior.")
   try:
      res = num1 / num2
   except ZeroDivisionError:
      print("You can't divide some numbers by zero.")
   else:
      print(res)
   finally:
      print("Mission Completed.")
```
这里我们会发现，即使num2为0，我们也会看到最后的“Mission Completed.”
### 7.传递异常
当函数中的一个异常没有被捕获处理时，他可以被传递到另一个函数，并可以继续传递下去，直到被捕获，或者报错
###### 例：
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
## 十二、静默<a id="静默"></a>
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
## 十三、测试代码<a id="测试代码"></a>
- **需先安装pytest第三方包**
命令如下：
```bash
python -m pip install --user pytest
```
- 所用测试文件应该以“**test_**”开头
### 1.测试函数
```
from 测试函数所在的文件 import 测试函数
def text_测试工具函数的名称():
   变量=测试函数(参数1,参数2,参数3...)
   assert 预期结果
```
在终端输入pytest以运行测试
一个测试通过出现一个“.”，一个测试未通过出现一个“F”
### 2.测试类
方式一：
**对每个类方法创建一个对象重复测试函数的过程进行测试**
方式二：
**使用fixture装饰器**
###### 例：
```
import pytest
from 测试类所在的文件 import 测试类
@pytest.fixture
def 创建一个对象的函数()
   函数体（用于创建一个对象并返回）
def text_测试工具函数的名称1(创建的对象):
def text_测试工具函数的名称2(创建的对象):
...
```
###### 例：
```python
from function import func1, func2
def text_func1():
   assert func1() == "预期的结果"

def text_func2():
   res = func2()
   assert res == "预期的结果"
```
### 3.夹具和装饰器
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
###### 下面是简单的夹具的使用
```python
#survey.py
class AnonymousSurvey:
    """手机匿名调查问卷的答案"""

    def __init__(self, question):
        """存储一个问题, 并未存储答案做准备"""
        self.question = question
        self.response = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, new_response):
        """存储淡粉调查问卷"""
        self.response.append(new_response)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Surevy results:")
        for response in self.response:
            print(f"- {response}")

    def calculate_differ(self):
        """计算有多少不同的答案"""
        temp = []
        for item in self.response:
            temp.append(item)
        
        return len(set(temp))
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
**注意这个时候test__()开始有参数了，因为我们的夹具有返回值，相当于提前做好的创建对象的任务**