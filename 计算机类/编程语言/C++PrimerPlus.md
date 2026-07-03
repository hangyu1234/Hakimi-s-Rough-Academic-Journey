# C++ Primer Plus 笔记

> 整理自《C++ Primer Plus》第六版，内容涵盖 C++ 基础到进阶知识

## 📑 目录

- **[一、基础知识](#一基础知识)**
  - [1.1 C++注释](#11-c注释)
  - [1.2 预处理指令 `#include`](#12-预处理指令-include)
  - [1.3 库和头文件 `<iostream>`](#13-库和头文件-iostream)
  - [1.4 关键字 `using`](#14-关键字-using)
  - [1.5 名称空间 `namespace`](#15-名称空间-namespace)
  - [1.6 语句](#16-语句)
  - [1.7 关键字](#17-关键字)
  - [1.8 函数和 cin/cout](#18-函数和-cincout)
- **[二、简单数据](#二简单数据)**
  - [2.1 变量简介](#21-变量简介)
  - [2.2 变量名](#22-变量名)
  - [2.3 整形变量](#23-整形变量)
  - [2.4 初始化](#24-初始化)
  - [2.5 char 类型](#25-char-类型)
  - [2.6 无符号类型](#26-无符号类型)
  - [2.7 bool 类型](#27-bool-类型)
  - [2.8 const 限定符](#28-const-限定符)
  - [2.9 浮点数](#29-浮点数)
  - [2.10 C++11 中的 auto 声明](#210-c11-中的-auto-声明)
  - [2.11 算数运算符](#211-算数运算符)
- **[三、复合类型](#三复合类型)**
  - [3.1 数组](#31-数组)
  - [3.2 数组初始化](#32-数组初始化)
  - [3.3 字符串](#33-字符串)
  - [3.4 string 类](#34-string-类)
  - [3.5 结构](#35-结构)
  - [3.6 共用体](#36-共用体)
  - [3.7 枚举](#37-枚举)
  - [3.8 指针](#38-指针)
  - [3.9 存储方式](#39-存储方式)
- **[四、循环和关系表达式](#四循环和关系表达式)**
  - [4.1 for 循环](#41-for-循环)
  - [4.3 表达式和语句](#43-表达式和语句)
  - [4.4 while 循环](#44-while-循环)
  - [4.5 do while 循环](#45-do-while-循环)
  - [4.6 基于范围的 for 循环](#46-基于范围的-for-循环)
  - [4.7 循环和文本输入](#47-循环和文本输入)
  - [4.8 嵌套循环和二维数组](#48-嵌套循环和二维数组)
- **[五、分支语句和逻辑运算符](#五分支语句和逻辑运算符)**
  - [5.1 if 语句](#51-if-语句)
  - [5.2 if else 语句](#52-if-else-语句)
  - [5.3 if-else if-else 结构](#53-if-else-if-else-结构)
  - [5.4 逻辑表达式](#54-逻辑表达式)
  - [5.5 字符串库 cctype](#55-字符串库-cctype)
  - [5.6 `? :` 运算符](#56-运算符)
  - [5.7 switch 语句](#57-switch-语句)
  - [5.8 break 和 continue 语句](#58-break-和-continue-语句)
  - [5.9 goto 语句](#59-goto-语句)
- **[六、函数](#六函数)**
  - [6.1 函数定义](#61-函数定义)
  - [6.2 函数原型和函数调用](#62-函数原型和函数调用)
  - [6.3 函数参数和按值传递](#63-函数参数和按值传递)
  - [6.4 函数和数组](#64-函数和数组)
  - [6.5 函数和C-风格字符串](#65-函数和c-风格字符串)
  - [6.6 函数与结构](#66-函数与结构)
  - [6.7 函数和string + array](#67-函数和string-array)
  - [6.8 函数指针](#68-函数指针)
  - [6.9 递归](#69-递归)
- **[七、函数进阶](#七函数进阶)**
  - [7.1 内联函数](#71-内联函数)
  - [7.2 引用变量](#72-引用变量)
  - [7.3 默认参数](#73-默认参数)
  - [7.4 函数重载](#74-函数重载)
  - [7.5 函数模板](#75-函数模板)
- **[八、内存模型和名称空间](#八内存模型和名称空间)**
  - [8.1 单独编译](#81-单独编译)
  - [8.2 头文件及管理](#82-头文件及管理)
  - [8.3 存储持续性、作用域和链接性](#83-存储持续性作用域和链接性)
  - [8.4 说明符和限定符](#84-说明符和限定符)
  - [8.5 函数和链接性](#85-函数和链接性)
  - [8.6 语言链接性](#86-语言链接性)
  - [8.7 动态内存分配](#87-动态内存分配)
  - [8.8 名称空间](#88-名称空间)

---


## 一、基础知识
```cpp
// first.cpp --print "Hello, world."
#include <iostream>
using namespace std;
int main(){
    cout << "Hello, world." << endl;
    return 0;
}
```
这是一个非常简短的一个程序，我第一个接触到的C++程序是这个（我在python语言也差不多都是从打印"Hello, world."开始）。这个程序有下面的要素：
- 注释：`//`
- 预处理指令：`#include`
- 头文件：`<iostream>`
- 关键字：`using`
- 名称空间：`namespace`
- 函数：`int main(){···}`
- cout(cin)；`cout`
- 语句：`cout << ···` 和 `return`

我们一个一个看：
### 1.1 C++注释

C++ 继承了 C 语言的注释方法，同时也有着自己的注释方式：
   - `//`：C++ 风格注释，适用于**单行注释**。
   - `/**/`：C 风格注释，适用于**多行注释**。
   - 两者可以混用，在 VS 和 VScode 中快捷键`Ctrl + /`将选中的部分进行注释。
### 1.2 预处理指令 `#include`

几乎所有的 C++ 文件都会有`#include`语句，这种语句叫做**预处理指令**，我们通过这个命令在程序运行之前进行一些操作（比如联编一些我们的文件和我们的库）。
   **只要是以`#`开头的都是预处理指令**。
### 1.3 库和头文件 `<iostream>`
`<iostream>` 是一种文件，他被包含在其他文件中，又称包含文件，也叫**头文件**。C 语言和 C++ 的头文件有所区别，C 语言中的头文件都是有扩展名 `.h` 的[^1]，但是 C++ 中的头文件是没有扩展名的，当然对于一些老式的 C 语言的头文件 C++ 保留了扩展名。
`<iostream>`包含在**C++标准库**中，头文件中包含[声明](#1声明语句)，而库是**实现**，库中包含了头文件中的声明的具体实现。也就是说：**头文件是接口[^2]，而库是实现**。
两者还是有区别的：头文件是**源码格式（文本格式）**，库是**经过编译的二进制文件**。库是一个庞大的集合，里边包含了头文件中所包含的声明的实现。
### 1.4 关键字 `using`
`using` 是一种起**引入**或着是**起别名**功能的关键字。
1. 引入名称空间，或者是指定的成员：
    ```cpp
    using namespace std;
    using std::cout;
    using Base::func;
    ```
    这三个语句都是合理的。第一个是引入名称空间`std`，第二个是引入一个成员`std::cout`。第三个与类有关：
    - 恢复被遮蔽的函数：
    如果子类重写了父类的一个函数，父类的同名重载函数会被“隐藏”。用 using 可以把它们找回来
    ```cpp
    class Base {
    public:
        void show(int i) { ... }
    };

    class Derived : public Base {
    public:
        using Base::show; // 告诉编译器，把父类的 show 也包含进来
        void show(string s) { ... } // 否则这里会把父类的 show(int) 遮蔽掉
    };
    ```
    - 继承构造函数 (C++11)
    ```cpp
    class Base {
    public:
        void show(int i) { ... }
    };

    class Derived : public Base {
    public:
        using Base::show; // 告诉编译器，把父类的 show 也包含进来
        void show(string s) { ... } // 否则这里会把父类的 show(int) 遮蔽掉
    };
    ```
2. 类型别名
    在C++11以后我们可以给一些类型起外号：
    ```cpp
    // 以前的方法 (C语言风格)
    typedef unsigned long ulong;

    // 现代 C++ 方法 (更清晰)
    using ulong = unsigned long;
    using vec_int = std::vector<int>;

    // 甚至可以给函数指针起别名
    using FuncPtr = void(*)(int, double);
    ```
### 1.5 名称空间 `namespace`
名称空间是用来限定类、函数、变量等C++组件的。由于命名的自由性，我们很容易就会发生命名重复（这个在C++中有其他的含义），就会导致很混乱。因此，我们需要引入名称空间来限定名称的适用范围。要使用名称空间的名称，我们要用`namespace::func_name`的格式来使用，其中`::`被称为**域名解析符**。

### 1.6 语句
在C++中，每条完整的指令都被称为**语句**，且所有的语句都以**分号**结束。
#### 1.声明语句
在C/C++中我们需要明确信息的存储位置和所需的内存空间，这个时候就需要我们的**声明语句**。声明语句的结构：`Typename + Variable-name`。这里的`typename`是类型名，可以是任何一种类型，`variable-name`是变量名/函数名，总之是一种标签。
###### 声明与定义：
程序中的声明语句叫做定义声明语句，简称**定义**。定义意味着他将命令编译器为变量分配内存空间。但是声明还有不分配空间的情况，称为**引用声明**。
声明和定义的关系：定义 = 声明 + 分配内存
| 关键词/特征 | 声明 (Declaration) | 定义 (Definition) |
| :--- | :---: | :---: |
| `extern` (无初始化) | ✅ | ⬜ |
| `extern` (有初始化) | ✅ | ✅ |
| `static` 全局变量 | ⬜ | ✅ |
| `struct` 标签 | ✅ | ✅ |
| 函数原型 (无 `{ }`) | ✅ | ⬜ |
| 函数体 (`{ ... }`) | ⬜ | ✅ |
| `typedef` / `using` | ✅ | ⬜ |
| `&` 引用 | ✅ | ✅ |
##### 2.赋值语句
符号 `=` 叫做赋值运算符，与数学中的`=`不同，他表示**将值绑定到该标签**。我们允许连续赋值，比如下面的例子
```cpp
int a, b, c;
a = b = c = 0;
```
这个时候的赋值顺序是`0->c->b->a`，即从右向左赋值。这种连续赋值在C中是不允许的，是C++的特性之一。
```cpp
int a = 10;
a = a - 1; // a = 9
```
由于赋值语句是将值绑定到标签上。所以`a = a - 1`实际上是计算了表达式`a - 1`后，将评估结果（值）绑定到了`a`上（尽管在数学上这看起来很奇怪）。
**赋值语句的值是最后左操作数的值**：
```cpp
cout << (a = 1) + 2;    // 输出 3 （1 + 2）
```

### 1.7 关键字
关键字是计算机语言中的词汇。比如 int、void、return和double。由于这些关键字都是C++专用的，因此不能用作他用。也就是说，不能将return用作变量名，也不能把double用作函数名。不过可以把它们用作名称的一部分，如painter（其中包含int）或return_aces。
另外，main不是关键字，由于它不是语言的组成部分。然而，它是一个必不可少的函数的名称。可以把main用作变量名。同样，其他函数名和对象名也都不能是关键字。然而，在程序中将同一个名称（比如cout）用作对象名和变量名会把编译器搞糊涂。也就是说，在不使用cout对象进行输出的函数中，可以将cout用作变量名，但不能在同一个函数中同时将cout用作对象名和变量名。

### 1.8 函数和 cin/cout

这两个在后面有单独的记录，此处先略过，也可以直接跳转：[函数](#18-函数和-cincout)，[cin/cout](#18-函数和-cincout)

## 二、简单数据
### 2.1 变量简介
在编程中，变量是程序为了存储数据而申请的一块内存空间。
为了把信息寻出在计算机中，程序必须记录3个基本属性：
- 信息将存储在哪里（内存位置）
- 要存储什么值（变量内容）
- 存储何种类型的信息（变量类型）

### 2.2 变量名
C++ 中的变量名既自由又有约束。C++变量名需要遵循以下规则：
- 在名称中只能使用字母字符、数字和下划线(_)
- 名称的第一个字符不能是数字
- 区分大小写
- 不能将C++关键字用作名称
- 以两个下划线或下划线和大写字母打头的名称被保留给实现（编译器及其使用的资源）使用。以一个下划线开头的名称被保留给实现，用作全局标识符。
- C++对名称的长度是没有限制的，名称中的所有字符都有意义。但有些平台有长度限制。

###### 对于上方的倒数第二点，C/C++规定：任何以`__`和`_大写字母`开头的名字，保留给**实现**使用。普通程序员不要定义这种名字，避免与编译器或者标准库冲突。[^3]
```cpp
int __myVar;  // ❌ 不要用，保留给编译器
int _Xyz;     // ❌ 不要用
```
下面是一些命名例子:
```cpp
int poodle;      // valid
int Poodle;      // valid and distinct from poodle
int POODLE;      // valid and even more distinct
Int terrier;     // invalid -- has to be int, not Int
int my_stars3;   // valid
int _Mystars3;   // valid but reserved -- starts with underscore
int 4ever;       // invalid because starts with a digit
int double;      // invalid -- double is a C++ keyword
int begin;       // valid -- begin is a Pascal keyword
int __fools;     // valid but reserved -- starts with two underscores
int the_very_best_variable_i_can_be_version_112;  // valid
int honky-tonk;  // invalid -- no hyphens allowed
```
C/C++中的命名方式是自由的，我们可以在不违反规定的情况下随意命名，但是一个好的命名习惯是必要的，这不仅是工程实践的经验，也是为了自己看着舒服。我们也可以在我们的变量名前加入一些前缀，这方便我们进行判读这些我们写的变量的用途（包会忘的）例如，可以将整型变量myWeight命名为nMyWeight，其中前缀n用来表示整数值，在阅读代码或变量定义不是十分清楚的情况下，前缀很有用。另外，这个变量也可以叫做intMyWeight，这将更精确，而且容易理解，不过它多了几个字母（对于很多程序员来说，这是非常讨厌的事）。常以这种方式使用的其他前缀有：str或sz（表示以空字符结束的字符串）、b（表示布尔值）、p（表示指针）和c（表示单个字符）。

### 2.3 整形变量
整型就是我们在数学上所说的整数（没有小数部分）有些语言只提供一种整型（一种类型满足所有要求！），而C++则提供好几种，这样便能够根据程序的具体要求选择最合适的整型。
不同C++整型使用不同的内存量来存储整数。使用的内存量越大，可以表示的整数值范围也越大。另外，有的类型（符号类型）可表示正值和负值，而有的类型（无符号类型）不能表示负值。术语宽度
（width）用于描述存储整数时使用的内存量。使用的内存越多，则越宽。
C++中的整型(按照宽度递增排列)分别是`char, short, int, long, long long(C++11新增)`，这些都有器有符号版本(signed)和无符号版本(unsigned)。其中的`char`最常用来表示字符。对于 char 我们放在后面单说，也可以直接[跳转](#25-char-类型)
#### 2.3.1 整型short、int、long和long long
计算机内存由一些叫做位（bit）的单元组成。C++的short、int、long和long long类型通过使用不同数目的位来存储值，最多能够表示4种不同的整数宽度。但是内存是有限的，即他们的上线是被锁死的，但是C++保证了他们的最小长度。如下所示：
- short >= 16bit
- int >= short
- long >= 32bit and long >= int
- long long >= 64bit and long long >= long

计算机内存的基本单元是位（bit）。可以将位看作电子开关，可以开，也可以关。关表示值0，开表示值1。字节（byte）通常指的是8位的内存单元。从这个意义上说，字节指的就是描述计算机内存量的度量单位，在C++中，字节也是最小的可寻址的内存单位。且其中的位因为是连续的，不会分散在内存里。C++ 中的字节是连续的位组成的存储单位，它必须至少有足够的不同取值来表示 C++ 的基本字符集。
当前的系统搜使用的是最小长度。笔者所使用的windows系统对应的他们的所占字节如下：
| 名称 | `short` | `int` | `long` | `long long` |
| :--: | :--: | :--: | :--: | :--: |
| 字节数 | 1 | 4 | 4 | 8 |
| 表示范围 | 一般用来表示字符 | $-2^{31}$ 到 $2^{31}-1$ | $-2^{31}$ 到 $2^{31}-1$ | $-2^{63}$ 到 $2^{63}-1$ |

这些类型都是C++中内置的类型，使用方法也和int一样。
```cpp
short score;             // creates a type short integer variable
int temperature;         // creates a type int integer variable
long position;           // creates a type long integer variable
```

实际上short是short int的简称，而long是long int的简称。

要知道系统中整数的最大长度，可以在程序中使用C++工具来检查类型的长度。首先，sizeof运算符返回类型或变量的长度，单位为字节。其次，头文件climits（在老式实现中为limits.h）中包含了关于整型限制的信息。具体地说，它定义了表示各种限制的符号名称。例如，`INT_MAX`为int的最大取值，`CHAR_BIT`为字节的位数。

#### 2.3.2 运算符sizeof和头文件climits
在C++文件中，我们可以使用`sizeof`运算符来获取简单类型对象的内存长度（对于数组等则是获取对应的元素个数）。**运算符**是内置的语言元素，对一个或多个数据进行运算，并生成一个值。`sizeof`可以计算类型的所占内存（单位：byte）。对于单纯的类型名，我们要将他放在`()`中，但是如果是变量名，我们可以省略掉`()`
```cpp
sizeof(int); // Windows中会输出 4
sizeof n_short; //显示n_short对应类型的内存大小
```
头文件climits定义了符号常量来表示类型的限制。下面是对应的符号常量和其对应的含义：
| 符号常量 | 表示 |
| :--- | :--- |
| CHAR_BIT | char的位数 |
| CHAR_MAX | char的最大值 |
| CHAR_MIN | char的最小值 |
| SCHAR_MAX | signed char的最大值 |
| SCHAR_MIN | signed char的最小值 |
| UCHAR_MAX | unsigned char的最大值 |
| SHRT_MAX | short的最大值 |
| SHRT_MIN | short的最小值 |
| USHRT_MAX | unsigned short的最大值 |
| INT_MAX | int的最大值 |
| INT_MIN | int的最小值 |
| UNIT_MAX | unsigned int的最大值 |
| LONG_MAX | long的最大值 |
| LONG_MIN | long的最小值 |
| ULONG_MAX | unsigned long的最大值 |
| LLONG_MAX | long long的最大值 |
| LLONG_MIN | long long的最小值 |
| ULLONG_MAX | unsigned long long的最大值 |

#### 2.3.3 整形类型的使用
C++提供了大量的整型，通常我们是使用`int`，对于其他的C++整型也有一些使用的原因。
1. long和long long的使用
如果知道变量可能表示的整数值大于16位整数的最大可能值，则使
用long。即使系统上int为32位，也应这样做。这样，将程序移植到16位
系统时，就不会突然无法正常工作（这里是因为在Windows系统中int为32位和long相同，但是Linux系统中int为16位。）如果要存储的值超过20亿，可使用long long。
2. short的使用
short比int小我们可以用short来节省内存（这是一个非常好的编程习惯！）通常，仅当有大型整型数组时，才有必要使用short来节省内存。
3. int的使用
遇事不决用int就行(doge)，具体原因如下：
   1. **CPU 的“原生”处理能力 (最核心原因)**
   现代 CPU（尤其是 32 位和 64 位架构）在处理`int`类型时是最快的。
   - 字对齐（Word Alignment）： CPU 读取内存通常是一次读取 32 位或 64 位。如果你定义一个 int，它正好适配 CPU 的总线宽度。
   - 大多数 CPU 的算术指令（加减乘除）是直接针对“寄存器大小”优化的。即便你定义一个 char（8 位）变量进行加法运算，CPU 往往也会先把它提升为 int，做完计算后再截断存回内存。这就使得我们用char反而还增加了运算的任务。
   1. **数值溢出的风险**
   char 的表示范围非常小（通常是 -128 到 127）。在实际编程中，稍微大一点的计数器或者循环变量，甚至是一次简单的加法，都很容易造成溢出（Overflow）。
   2. **代码的可读性和可维护性**
   当你在代码中看到 int 时，潜意识里会认为这是一个“正常的数字”。如果你看到 char，大脑会下意识地去想：“这里是不是要处理字符？是不是要处理 ASCII 码？还是这里有极端的内存限制？”使用 int 可以减少沟通成本，避免误解。

#### 2.3.4 整形字面值
字面值[^4]是指你在代码里直接写出来的值。之所以叫“字面值”，是因为你一眼就能从“字面上”看出它的值和类型，而不需要通过变量名去查找。
|进制(base)|10|8|16|
|:--:|:--:|:--:|:--:|
|格式|正常表示|第一位用0第二位为1到7|前两位为0x或0X|
|例子| 114514 | 042(等同于34) | 0xF(等同于15)、0XA5(等同于165) |
在默认情况下，cout使用十进制格式显示整数（方便我们的日常使用）[^5]。虽然我们眼中这些进制有所区别，但是对于计算机来说他们都一样，因为他们都要被以二进制存储。

#### 2.3.5 常量
**常量**是不允许修改的值，我们在进行初始化以后就不允许再次进行修改。
我们使用**声明**将整型变量的类型告诉了C++编译器，但是对于像114514这样的常量，除非有理由存储为其他类型（如使用了特殊的后缀来表示特定的类型，或者值太大，不能存储为int），否则C++将整型常量存储为int类型。
先来看看后缀。后缀是放在数字常量后面的字母，用于表示类型。
|后缀| u / U |l / L | ul(顺序任意，大小写任意) | ll / LL | ull等（同ul要求）|
|:--:|:--:|:--:|:--:|:--:|:--:|
|含义|unsinged int|long|unsigned long|long long|unsigned long long|
再来看看长度。在C++中，对十进制整数采用的规则，与十六进制和八进制稍微有些不同。对于不带后缀的十进制整数，将使用下面几种类型中能够存储该数的最小类型来表示：int、long或long long。对于不带后缀的十六进制或八进制整数，将使用下面几种类型中能够存储该数的最小类型来表示：int、unsigned int/long、unsigned long、long long或unsigned long long。这是因为十六进制常用来表示内存地址，而内存地址是没有符号的，因此，usigned int比long更适合用来表示16位的地址。

### 2.4 初始化
#### 2.4.1 传统初始化
初始化是将赋值和声明合并在一起。
`int x = 0;`
我们也可以用字面值常量来初始化，用另一个已经定义过的变量来初始化另一个变量。
```cpp
int x = 0;
int y = x;
cout << y;  //output: 0
```
当然我们也可以用表达式来这么做
```cpp
int x1 = 0;
int x2 = 1;
int x3 = x1 + x2;
cout << x3;  //output: 1
```
这种初始化应注意我们用来初始化的变量或者内容是先前定义好的。如果出现了未声明或定义的变量，编译器就会报错。
除此之外，我们还有另外的一种C++独有的初始化方式：
```cpp
int owls = 101;   //traditional C initialization, sets owls to 101.
int wrens(432);   //alternative C++ syntax, set wrens to 432.
```
###### 这里的`wren(432)`类似于我们定义类时用到的**构造函数**
如果我们知道变量的初始值应该是什么，对他进行初始化是一个非常好的变成习惯，可以避免忘记给变量赋值的情况发生。
#### 2.4.2 C++11 风格的初始化
除了上面的初始化方式，C++还有一种，这种方式用于数组和结构，但在C++98中我们还可以用于单值变量：
`int hamburgers = {24}; // set hamburgers to 24`
在C++11中我们使用这种情形就变多了，首先在这种方式下，我们既可以使用等号也可以不使用。
```cpp
int emus{7};    //set emus to 5
int rheas = {12};    //set rheas to 12
```
在这种情况下我们的大括号中可以包含数据可以为空，为空的时候我们就会将变量初始化为0
```cpp
int psychics = {};     //set psychics to 0
int rocs{}    //set rocs to 0
```
这样的初始化有一个好处：**更好的防范类型转换错误。**
###### 以前，C++使用不同的方式来初始化不同的类型：初始化类变量的方式不同于初始化常规结构的方式，而初始化常规结构的方式又不同于初始化简单变量的方式；通过使用C++新增的大括号初始化器，初始化常规变量的方式与初始化类变量的方式更像。C++11使得可将大括号初始化器用于任何类型（可以使用等号，也可以不使用），这是一种通用的初始化语法。

### 2.5 char 类型
char很特殊，**内存仅占有 1 byte**，他的**大小范围是-128到127**。虽然char经常用来处理字符，但是我们也可以用它来表示比short更小的整型。对于字符表示，我们有不同的表示方法。目前我们常接触到的ASCII是美国制定定的标准。但是这只是一个方言，并不能很好的实现国际化（例如IBM大型机使用的EBCDIC编码也是一种表示方法）。为了让全世界的文字都能在电脑里显示，人们发明了 Unicode（万国码）。它给世界上的每一个字符都分配了一个唯一的数字编号。但是Unicode需要表示的字符太多，传统的 char 类型（通常只占 1 个字节，即 8 位）装不下这么大的数字。所以，C++ 引入了 `wchar_t`（宽字符类型），它的内存空间更大（通常占 2 字节或更多），专门用来存储这些“国际化”的大数字。
在程序中，我们使用char来表示字符，但是在内存中，我们是以数字的形式进行保存的，比如‘M’，我们查看内存可知是77，但是在输出和输入的时候我们看到或使用的却是M，这是因为智能的cin和cout。输入时，cin将键盘输入的M转换为77；输出时，cout将值77转换为所显示的字符M。在程序中，我们书写字符是应使用单引号`''`而不是双引号`""`（双引号代表的是**字符串**，两者有很大区别）。
由于char是一个整数，我们也可以对其进行整数操作。
```cpp
char ch = 'A'
cout << ch + 1;   //输出66
```
这里的输出设计了[自动类型转换](#2114-类型转换)，在C++中，当char类型数据参与算术运算的时候，编译器会自动将char转换成int型。此时的cout检测到后面的表达式是`int`型，所以输出的是66。
#### 2.5.1 char字面值
在C++中，书写字符常量的方式有多种。对于常规字符（如字母、标点符号和数字），最简单的方法是将字符用单引号括起。这种表示法代表的是字符的数值编码。这种表示法更加清晰，且不需要知道编码方式，在不同的编译器中都能用。
但是总有一些例外，比如我们的`""`，他们不能简单的用这种表示，因为C++赋予了他们新的含义——用来表示字符串，如果强制用的话会使编译器报错。因此，C++使用了一种特殊的表示方法——**转义序列**。转义序列在很多编程语言中都有涉及，我们在使用的时候，需要在要转义的字符前加上`\`来表修饰。
#### 2.5.2 特殊字符
对于一些特殊的祖字符，他们在C++语言中是有含义的，但是我们依然想用这些字符，这时我们可以使用转义符`\`来进行表示，下面的表格是他们的对应含义：
| 字符名称 | ASCII 符号 | C++ 代码 | 十进制 ASCII 码 | 十六进制 ASCII 码 |
| :--- | :--- | :--- | :--- | :--- |
| 换行符 | NL (LF) | `\n` | 10 | 0xA |
| 水平制表符 | HT | `\t` | 9 | 0x9 |
| 垂直制表符 | VT | `\v` | 11 | 0xB |
| 退格 | BS | `\b` | 8 | 0x8 |
| 回车 | CR | `\r` | 13 | 0xD |
| 振铃 | BEL | `\a` | 7 | 0x7 |
| 反斜杠 | \ | `\\` | 92 | 0x5C |
| 问号 | ? | `\?` | 63 | 0x3F |
| 单引号 | ' | `\'` | 39 | 0x27 |
| 双引号 | " | `\"` | 34 | 0x22 |

虽然我们表示时需要转义的字符很多，但是我们在C++11以后需要转义的还剩5个：
- `\n`(换行符)：用于结束当前行
- `\\`(反斜杠)：表示文字路径和处理特殊字符是不可或缺
- `\'`(单引号)：在字符常量中必须使用
- `\"`(双引号)：在字符串中包含双引号时必须使用
- `\t`(水平制表符)：在控制台对齐输出时偶尔会用到。
剩下的进本已经放弃使用/极少使用。这里建议实在是要用或者是看到了一些很老的C++文件，我们直接问问AI吧。
换行符可以替代endl，但是还是要记得endl有`\n`所不具备的功能，清空缓冲区。显示数字时，使用endl比输入“\n”或‘\n’更容易些，但显示字符串时，在字符串末尾添加一个换行符所需的输入量要少些。
对于一些我们常用的、但是不能用简单字符表示的，我们可以用八进制或十六进制的方式表示。例如Ctr+Z的ASCII码为26，对应的八进制编码为032，十六进制编码为0x1a。可以用下面的转义序列来表示该字符：\032或\x1a。
- 八进制格式：`\ooo`，即`\`+八进制数字。
- 十六进制格式：`\x`+十六进制数字，需要注意，我们的十六进制表示要尽可能多的读取后面的十六进制字符。
相较于八进制，我们还是推荐十六进制，因为十六进制不易出错。
对于以上转义，我们在使用的时候为了避免歧义，在必要位置要进行分割，否则会出现一些奇怪的结果。
#### 2.5.3 通用字符名
C++标准允许实现提供扩展源字符集（在键盘上的符号集）和扩展执行字符集（在程序执行过程中能过显示到显示器上的字符）[^6]。C++有一种表示这种特殊字符的机制，它独立于任何特定的键盘，使用的是通用字符名（universal character name）。这个通用字符名的本意就是让部分地方语言也能够进行计算机编码（比如简体中文/日文/法文等等）。通用字符名可以用`\u`和`\U`打头。后面跟的分别是八进制和十六进制。

#### 2.5 4 wchar_t
对于一些我们无法用8位一字节的方式表达的文字系统，C++有两种处理方式：一种是编译厂商将char定义为16或着更长的字节，另一种就是我们来实现一个能同时支持一个小型基本字符集和一个较大的扩展字符集。wchar_t（宽字符类型）可以表示扩展字符集。
wchar_t并不是一个固定大小的类型，在不同的厂商所定义的wchar_t有所不同。Windows中将这个定义为了2字节，相当于是`unsigned short`，但是在Linux和Mac系统中就被定义为了4字节。相当于是`int`。
**建议**：现代 C++ 已经引入了更明确的类型（如 char16_t 和 char32_t），它们在所有平台上大小都是固定的。如果你在做跨平台开发，建议优先使用 char16_t 或 char32_t，而不是 wchar_t。

传统的cin/cout是将输入和输出看成char流，无法处理wchar_t，但是在iostream中的最新版本提供了wcin和wcout来处理wchat_t流。对于字符常量和字符串，我们还可以通过加上前缀`L`来指示
```cpp
wchar_t bob = L'P';        // a wide-character constant
wcout << L"tall" << endl;  // outputting a wide-character string
```
这个对于开发者来讲一般是不用涉及的，但是我们要有了解，尤其是在进行国际编程或使用Unicode或ISO 10646时。

#### 2.5.5 char16_t和char32_t
C++11新增了类型char16_t和char32_t，其中前者是无符号的，长16位，而后者也是无符号的，但长32位。C++11使用前缀`u`表示char16_t字符常量和字符串常量，并使用前缀`U`表示char32_t常量，前缀u和U分别指出字符字面值的类型为char16_t和char32_t。
**建议**：对于这两个类型，我们由3个实践来借鉴：
1. 存储和网络传输：一律用 char 存 UTF-8。它是目前互联网的事实标准，最省空间，兼容性最好。
2. Windows 界面开发： 必须习惯使用 wchar_t 或 char16_t，否则你的程序无法处理中文路径和复杂的用户名。
3. 算法处理： 如果需要频繁地按字符拆分、计数（比如写一个文本编辑器），转换成 char16_t 或 char32_t 处理会让你少掉很多头发。
如果你只写简单的控制台练习题，char 确实够了；但如果你要写一个正经的、给别人用的软件，Unicode 是你无法绕过的关卡，而 char16_t 就是你手中的武器之一。

### 2.6 无符号类型
C++ 中的没有像`unsigned`关键字的，都是有符号数。但是无符号数它的优点是表示的范围变大了2倍（因为没有符号位了）要创建他们，只需要用关键字`unsigned`
来修改声明即可。
```cpp
unsigned short change;         // unsigned short type
unsigned int rovert;           // unsigned int type
unsigned quarterback;          // also unsigned int
unsigned long gone;            // unsigned long type
unsigned long long lang_lang;  // unsigned long long type
// 注意，unsigned本身是unsigned int的缩写
```
##### 对于溢出的科普：我们在学C++的时候所讨论的溢出的根本原因在于我们的内存有限制正如前文所述，计算机虽然强大，但是我们不能无限制的存储非常大的数字，我们在这里的类型也是如此，当我们存储了超出该类所该存储的数据范围就会发生数据溢出，这将会导致我们的结果发生非常大的改变，甚至出现一些非常离谱的ERROR，如果真的想试试的话可以用下面的程序试试
```cpp
#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int overflow = pow(114, 514);     //这个数非常大，如果半天没反应可以用Ctrl+C强制结束进程。
    cout << overflow;
    return 0;
}
```
我在VScode上使用的时候是输出了-2147483648（很奇怪不是吗，正正得了负）。所以我们在进行编程的时候我们应非常注意溢出的问题（谁也不想我们的程序最后输出了一个奇奇怪怪的数字）。

### 2.7 bool 类型
在以前，C++和C一样是没有bool值的。C++将**非零值**解释为`true`，将**0**解释为`false`。现在我们可以用预定义的字面值`true`和`false`来表示真假了。
字面值`true`和`false`都可以提升转换成int型，true->1，false->0。另外任何数字或者指针值都可以进行隐式转换为bool值，任何非零值都被转换为true，而零被转换为false，任何非NULL或nullptr的都会转换成true，NULL和nulllptr会被转换成0。

### 2.8 const 限定符
如果程序在多个地方使用同一个常量，则需要修改该常量时，只需修改一个符号定义即可。C++有一种比`#define`更好的处理符号常量的方法，这种方法就是使用const关键字来修改变量声明和初始化。格式如下：
`const int Number = 600`
这样我们就规定了一个常量 Number ，当我们以后每次使用 Number 的时候我们都相当于使用其所对应的值。但是，**这样定义的变量以后是不允许重新赋值的,也就是说，我们必须进行初始化名进行赋值**[^1]。这里的关键字 const 称为限定符，它限定了声明的含义。
创建常量的通用格式如下：
`const type name = initial_value`
###### const 变量的命名格式和习惯
- 名称首字母大写
- 整体名称大写
- 以字母 k 打头

如果你之前学习过 C 语言，在 C 语言中我们常用`#define NAME VALUE`来定义常量（这其实是在定义**宏**）。但是 const 比 #define 要好，首先 const 是能够明确指出其类型，其次可以使用C++的作用域规则将定义限制在特定的函数或文件中，第三可以将const用于更复杂的类型（后面会有介绍）。
还有一个就是，在 C++ 中我们可以使用 const 值来声明数组长度。

### 2.9 浮点数
他是 C++ 的第二组基本类型，可以表示小数部分的数字，对于它在计算机中的存储原理，可以学习一下**数字电子技术(Digigtal Fundamental by Thomas L. Floyd)**[^7]
#### 2.9.1 浮点数书写
C++ 中有两种书写浮点数的形式，一种是我们日常的写法：
```cpp
12.34       // floating-point
939001.32   // floating-point
0.00023     // floating-point
8.0         // still floating-point
```
由上例可知，即使小数部分为零，小数点也将会确保数字以浮点数表示。
第二种表示的方法叫做**E 表示法**，像这样：`3.45E6`，这意为 3.45 * 10^6，这里的 6 为指数，3.45 为底数。E 就表示为 10 的……次方。
```cpp
2.52e+8                 // can use E or e, + is optional
8.33E-4                 // exponent can be negative
7E5                     // same as 7.0E+05
-18.32e13               // can have + or - sign in front
1.69e12                 // 2010 Brazilian public debt in reais
5.98E24                 // mass of earth in kilograms
9.11e-31                // mass of an electron in kilograms
```
E 表示法可以表示非常大的数，也可以表示非常小的数。E表示法确保数字以浮点格式存储，即使没有小数点。注意，既可以使用E也可以使用e，指数可以是正数也可以是负数。数字中不能有空格。
#### 2.9.2 浮点类型
C++ 中有三种浮点类型：float、double 和 long double。他们和整形一样是按照表示的最小范围来分类的。有效位（significant figure）是数字中有意义的位。有效位数不依赖于小数点的位置。
C++ 对于上方三种的要求是：float 至少 32 位，double 至少 48 位，且要大于 float，long double 是要大于等于 double。通常情况下，float 为 32 位，double 为 64 位，long double为 80、96或128 位。我们可以从头文件 cfloat 中找到系统的限制。
对于小数点精度的控制我们在 ostream 文件中有专门的方法，`setf()`方法，下方给出了使用的案例，其中的 `ios_base::fixed` 和 `ios_base::floatfield` 是用来固定小数点位的常量（由iostream文件提供）。
```cpp
// floatnum.cpp -- floating-point types
#include <iostream>
int main()
{
    using namespace std;
    cout.setf(ios_base::fixed, ios_base::floatfield); // fixed-point
    float tub = 10.0 / 3.0;      // good to about 6 places
    double mint = 10.0 / 3.0;    // good to about 15 places
    const float million = 1.0e6;

    cout << "tub = " << tub;
    cout << ", a million tubs = " << million * tub;
    cout << ",\nand ten million tubs = ";
    cout << 10 * million * tub << endl;

    cout << "mint = " << mint << " and a million mints = ";
    cout << million * mint << endl;
    return 0;
}
```
下面是输出
```
tub = 3.333333, a million tubs = 3333333.250000,
and ten million tubs = 33333332.000000
mint = 3.333333 and a million mints = 3333333.333333
```
通常cout会删除结尾的零。但是调用`cout.setf( )`将覆盖这种行为，至少在新的实现（就是在该语句之后的实现）中是这样的。由于 float 的精度问题，我们的第二个输出出现了数值上的小问题，这也体现了计算机对于 float 精度的控制。
对于精度的控制，我们在后面有更详尽的介绍。

##### 2.9.3 浮点常量
对于浮点常量，在默认情况下我们是储存为 double 类型。如果希望改变类型，float 对应在数字后面加上 `f` 或 `F`后缀。对于 long double 类型，可以使用 `l` 或 `L` 后缀（这里建议使用 `L` 后缀）。
```cpp
1.234f                  // a float constant
2.45E20F                // a float constant
2.345324E28             // a double constant
2.2L                    // a long double constant
```
##### 2.9.4 浮点数的优缺点
与整数相比，浮点数有两点好处，一是可以表述整数范围内的值，而是、由于有缩放因子，他们表示的范围要大得多。但是并不是没有缺点，浮点运算的速度是要比整数要慢的。
###### 以上介绍的整型和浮点型统称为算数类型。

### 2.10 C++11 中的 auto 声明
C++11中新增了可以让编译器根据初始值自行判断变量类型的类型——`auto`。如果使用关键字 auto，但是不指定变量的类型，编译器将会把变量的类型设置成于初始值相同。
```cpp
auto n = 100;         // n is int
auto x = 1.5;         // x is double
auto y = 1.3e12L;     // y is long double
```
显示声明类型的时候，将变量初始化为0不会导致问题，但是用关键字 auto 的时候就会导致问题（因为 0 本身是 int 型的）
对于更加复杂的含义，可以直接看[这里](#210-c11-中的-auto-声明)

auto 的使用有着严格的限制：
1. **必须立即初始化**，这是基本要求
2. **右侧表达式必须有明确的类型**
   ```cpp
   auto a = {1, 2, 3};      // 有歧义，不建议使用
   auto a = NULL;       // 建议使用 nullptr，有时 NULL 会被识别成 int 类型。
   ```
3. **不能用于非静态成员变量**
   在 C++11 中不能在类的定义中直接使用 auto 来定义成员变量。
   ```cpp
   class MyClass {
       auto x = 10;     // invalid
   }
   ```
   ###### 虽然现在的 C++ 允许这么做，但是还是建议类成员显式声明对应的类型
4. **不能直接用于函数参数**
   ```cpp
   void add(auto a, auto b) {
       ···
   }    // invalid
   ```
   这里可以使用[模板](#75-函数模板)，在 C++20 后虽然被允许，但是还是建议这样做。
5. **不能推导数组类型**
   使用 auto 声明数组，这个变量会退化成指针：
   ```cpp
   int arr[3] = {1, 2, 3};
   auto a = arr;    // 这里的 a 是指针，不是大小为 3 的数组
   ```
   
总结：
| 推荐使用 `auto` 的场景 | 建议避开 `auto` 的场景 |
| :--- | :--- |
| **复杂迭代器**：`auto it = vec.begin();` | **简单基本类型**：`auto i = 5;` (写 `int` 更直观) |
| **函数指针**：`auto p = func;` | **影响可读性时**：`auto x = some_complex_func();` (不知道返回了啥) |
| **模板编程**：处理未知类型的返回值 | **需要特定精度时**：比如必须用 `float` 而不是 `double` |

### 2.11 算数运算符
C++ 由 5 中基本的运算符：
- `+`：对操作数进行加法运算。
- `-`：等同于数学上的减法
- `*`：等同于数学上的乘法
- `/`：等同于数学上的除法（但是要注意类型）
- `%`：等同于数学上的取余（获得余数）

变量和常量都可以用作操作数。**注意`%`的操作数只能是整数**。
#### 2.11.1 运算符的优先级
C++ 的所有运算符都是有各自的优先级的，对于运算上的优先级，我们依然是按照数学上的优先级进行运算。当两个运算符的优先级相同时，C++将看操作数的结合性（associativity）是从左到右，还是从右到左。从左到右的结合性意味着如果两个优先级相同的运算符被同时用于同一个操作数，则首先应用左侧的运算符。从右到左的结合性则首先应用右侧的运算符。
```cpp
int num1 = 120 / 6 * 114514  // 正常从左向右运算
int num2 = 120 * 12 + 4 / 5  // 按照数学上的运算顺序即可
```
#### 2.11.2 除法分支
除法运算符`/`行为取决于两个操作数的类型（其实是涉及了隐式转换），整数和整数就是按整除进行运算，有至少一个浮点数就会转换成浮点数的结果。
实际上，对不同类型进行运算时，C++将把它们全部转换为同一类型。
###### 对于`/`的补充，我们在正常的编程语言中一般是一个运算符对应一种操作，但是这里的`/`其实是由三种运算构成的：int除法，float除法和double除法。这种使用相同符号进行多种操作的叫做运算符重载。像`/`这种是 C++ 内置的实例，我们还可以扩展运算符重载，以便能够用于用于自定义的类。这个我们在后面会有更详尽的介绍。

#### 2.11.3 求模运算
求模运算符返回整数除法的余数。它与整数除法相结合，尤其适用于解决要求将一个量分成不同的整数单元的问题。

#### 2.11.4 类型转换
C++ 有多种类型供用户选择，但也使得计算机的操作更加复杂。为了简化或者避免混合类型运算时的麻烦，C++ 会自动执行很多类型转换。
- 将一种算数运算符的值付给另一种算术类型的变量时，C++ 会进行转换
- 表达式中包含不同的类型时，C++ 会进行转换
- 将参数传递给函数的时候，C++ 会进行值的转换
  
下面是详细的转化解释：
1. 初始化和赋值进行的转换
C++ 允许将一种类型的值赋给另一种类型的变量。这样做时，值将被转换为接收变量的类型。我们将范围大的类型的值赋给范围小的类型的时候，由于精度的减少，C++强制将精度将为被赋值对象的精度，就会导致数据的丢失。但是将范围小的类型的值赋给范围大的值就不会有这种问题。
下面给出一些转换问题：

| 转 换 | 潜在的问题 |
| :--- | :--- |
| 将较大的浮点类型转换为较小的浮点类型，如将double转换为float | 精度（有效数位）降低，值可能超出目标类型的取值范围，在这种情况下，结果将是不确定的 |
| 将浮点类型转换为整型 | 小数部分丢失，原来的值可能超出目标类型的取值范围，在这种情况下，结果将是不确定的 |
| 将较大的整型转换为较小的整型，如将long转换为short | 原来的值可能超出目标类型的取值范围，通常只复制右边的字节 |

还有将 0 赋值给 bool 变量的时候转换为 false，非零值则转换为 true。
我这里给出一个例子：
`int debt = 7.2E12`
这里的 debt 本应该使用double来表示，但是我们的 debt 是 int 型，所以本应该要进行强制转换，但是，这里发生的是**未定义行为**。这里的输出很奇怪，是不可预测的，在不同的硬件处理器下，这里的输出是不同的（笔者编译的时候是输出 INT_MIN，即-2147483648）。因此，我们要避免出现这种情况。

2. 以{}方式初始化时进行的转换（C++11）
C++11 将使用大括号的初始化称为**列表初始化**。因为这种初始化常用于给复杂的数据类型（比如**数组**）提供值列表。 C++11 初始化中存在**窄化转换**规则，这对我们转化会进行强制的类型检查。
这种初始化对于类型转换要求十分严格。**列表初始化是不允许缩窄的，即变量的类型可能无法表示赋给它的值**。换句话说，这里没有所谓的大转小了（数值无法被目的类型有效的表示）。
  ```cpp
  const int code = 66;
  int x = 66;
  char c1 {31325};   // narrowing, not allowed
  char c2 = {66};    // allowed because char can hold 66
  char c3 {code};    // ditto(同上)
  char c4 = {x};     // not allowed, x is not constant
  x = 31325;
  char c5 = x;       // allowed by this form of initialization
  ```
这里的 x 不被允许初始化，是因为 x 是一个变量，编译器在初始化的时候是无法保证 x 一定是不发生窄化的值。**如果使用 {} 初始化，且源类型不是能被证明是安全的常量，则一律禁止隐式窄化。**

3. 表达式中的转换
当表达式中出现了；两种不同的类型的时候，C++ 会执行两种自动转换：首先，一些类型在出现的时候就会发生转换；其次，有些类型用到的时候才会被转换。
- 自动转换
  C++ 将 bool、char、unsigned char、signed char、和 short 值转换成int。这些转换称为**整型提升**。
  ```cpp
  short chickens = 20;        // line 1
  short ducks = 35;           // line 2
  short fowl = chickens + ducks; // line 3
  ```
  在这个程序中，我们将chickens和ducks转换成int，在计算完成后有转换成short型。
  但是对于unsigned short，我们通常会转换成 usnsigned int以避免数据的丢失。
  对于wchar_t的提升和char差不多，是提升成下列能够存储wchar_t取值范围的类型：int、unsigned int、long或 unsigned long。
- 算术表达式的转换
  不同类型进行算术运算的时候会进行一些转换，。当运算设计两种类型的时候，较小的类型会被转换成较大的类型。编译器通过校验表来确定在算术表达式中执行的转换。下面是C++11中的校验表。
  **如果操作数中包含浮点类型**：
  *   (1) 如果有一个操作数的类型是 `long double`，则将另一个操作数转换为 `long double`。
  *   (2) 否则，如果有一个操作数的类型是 `double`，则将另一个操作数转换为 `double`。
  *   (3) 否则，如果有一个操作数的类型是 `float`，则将另一个操作数转换为 `float`。
  **如果操作数均为整型**：
  *   (4) 否则，说明操作数都是整型，执行**整型提升**。
  *   (5) 如果两个操作数都是有符号或都是无符号的，且其中一个操作数的级别比另一个低，则**转换为级别高的类型**。
  *   (6) 如果一个操作数为有符号的，另一个为无符号的，且无符号操作数的级别比有符号操作数高，则将有符号操作数转换为**无符号操作数所属的类型**。
  *   (7) 否则，如果“有符号类型”可表示“无符号类型”的所有可能取值，则将无符号操作数转换为**有符号操作数所属的类型**。
  *   (8) 否则，将两个操作数都转换为**有符号类型的无符号版本**。
核心逻辑：C++ 的转换原则通常是**由小到大、有低精度到高精度**，目的就是为了在运算过程中不丢失信息。
对于上方介绍的类型，对应的级别可以按照需求的内存大小进行初步判断，值得一提：类型bool的级别最低。wchar_t、char16_t和char32_t的级别与其底层类型相同。

4. 传递参数时的转换（这里建议可以先看看[函数](#18-函数和-cincout)部分）
对于函数参数的类型转换，他们是由C++函数原型来控制的。当然，我们也可以取消对函数参数传递的控制，但是这么做并不推荐。另外，为保持与传统C语言中大量代码的兼容性，在将参数传递给取消原型对参数传递控制的函数时，**C++将float参数提升为double**。
###### 什么是“有原型”和“无原型”？所谓的“取消对函数参数传递的控制”，指的就是“不使用函数原型”，或着说是不使用不定长的参数列表，即`...`语法
- 有原型（现代C++的标准做法）：
  在调用函数之前知道函数的每一种参数类型。
  ```cpp
  void myFunc(int a, float b); // 明确的函数原型
  ```
- 无原型/取消控制（C语言的遗留做法）：
  在 C 语言中，你可以定义一个参数列表不确定的函数（例如标准库里的 printf）。
  ```cpp
  void myFunc(...); // 使用省略号，取消了对具体参数类型的控制
  ```

5. 强制类型转换
C++ 还运行要通过强制类型转换机制来显示的进行类型转换。强制类型转换的格式有两种。通用格式如下：
```cpp
(typeName) value    // converts value to typeName type
typeName (value)    // converts value to typeName type
```
第一种的格式来自于C语言，第二种格式是纯粹的C++。新格式的想法是，要让强制类型转换就像是函数调用。这样对内置类型的强制类型转换就像是为用户定义的类设计的类型转换。
C++还引进了4个人强制类型转换运算符，对他们的使用要求更加严格。咋这四个运算符中，`static_cast<>`可以用于将值从一种类型转换成另一种类型，例如：
`static_cast<long> (thorn)  // return a type long conversion of thorn`
下面是通用格式：
`static_cast<typeName> (value)  // converts value to typeName type`

## 三、复合类型

### 3.1 数组

数组（array）是一种数据格式，能够存储多个同类型的值。要创建数组，可使用声明语句。数组声明应指出以下三点：
- 存储在每个元素中的值
- 数组名
- 数组中的元素数

在 C++ 中我们可以按照下面的格式进行数组声明：
`typeName arrayName[arraySize]`

表达式中的arraySize指定元素数目，他必须是整形常数（如10）或者是 const 值，也可以是常量表达式（如8*sizeof(int)），即其中u送有的值在编译时都是已知的。换句话说，arraySize不能够是变量。
数组之所以被称为复合类型，是因为它是使用其他类型来创建的。不能仅仅将某种东西声明为数组，它必须是特定类型的数组。
数组的很多用途都是给予一个事实：可以单独访问数组元素。方法是使用下标或者是索引来对元素进行编号。C++ 数组是从0开始编号。使用带索引的方括号表示法来指定数组元素。**注意左后一个元素的索引比数组长度小1**。因此，数组声明能够使用一个声明创建大量的变量，然后用索引来表示和访问各个元素，
C++的编译器不会检查使用的下标是否有效，因此如果下标出现问题，我们的程序结果就会出现
问题。必须要确保程序只是用有效的下标值。

###### 关于sizeof和数组：sizeof运算符时返回类型或者是数据对象的长度（单位是字节）。但是将sizeof用于数组名，我们会得到整个数组的字节数。但是用在数组元素上就是对应类型的长度。
```cpp
int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
cout << sizeof(array); // 输出 4 * 10 = 40 
cout << sizeof(array[0])    //输出 4
```
###### 关于 `&` 和数组：当我们使用 & （取地址运算符）对数组名取地址时，返回的是整个数组的地址（其实依旧是数组首元素的地址）。

### 3.2 数组初始化
对于数组的初始化，这里更加推荐`typeName name[arraySize] = {element1, element2, ...};`格式。这种只需提供一个用逗号分隔的值列表（初始化列表），并将它们用花括号括起即可。列表中的空格是可选的。如果没有初始化函数中定义的数组，则其元素值将是不确定的。有的编译器可能会自动给你初始化为全是0（如VS code）。
C++11使用大括号的初始化（列表初始化）作为一种通用的初始化方式，可用于所有的类型。数组以前就可以使用列表初始化，但是C++11中的列表初始化新增了一些功能：
1. 初始化数组时，可省略等号（=）：
    `double earnings[4] {1.2e4, 1.6e4, 1.1e4, 1.7e4};  // ok with C++11`
2. 可不在大括号内包含任何东西，这将把所有元素都设置为零：
    ```cpp
    unsigned int counts[10] = {};   // all elements set to 0
    float balances[100] {};     // all elements set to 0
    ```
3. 列表初始化禁止缩窄转换（这是所有列表初始化的要求）：
    ```cpp
    long plifs[] = {25, 92, 3.0}    // not allowed
    short slifs[4] {'h', 'i', 1122011, '\0'};   // not allowed
    char tlifs[4] {'h', 'i', 112, '\0'};    // allowed
    ```
前两个犯了缩窄转换的问题：精度变小。第三个可以，没有超出类型的范围。
C++ 标准模板库（STL）提供了一种数组替代品——模板类vector，二C++新增了模板类array。这些替代品比内置的复合类型更加复杂、更灵活。

### 3.3 字符串
字符串是存储在内存的连续字节中的一系列字符。C++处理字符串
的方式有两种：一种来自传统的C语言，称为C风格字符串。另一种还有基于string类库的方法。
存储在连续字节中的一系列字符意味着可以将字符串存储在char数组中，其中每个字符都位于自己的数组元素中。C-风格字符串具有一种特殊的性质：以空字符（null character）结尾，空字符被写作\0，其ASCII码为0，用来标记字符串的结尾。
```cpp
char dog[8] = {'b', 'e', 'a', 'u', 'x', ' ', 'I', 'I'};        // 不是字符串！
char cat[8] = {'f', 'a', 't', 'e', 's', 's', 'a', '\0'};       // 是字符串！
```
这两个都是char数字，但是只有第二个数组是字符串。空字符对于C风格字符串至关重要。。对于C++中的很多函数，都是遇见`\0`结束的。字符数组和字符串是两个不一样的东西。
对于上方的cat字符串，这种初始化很麻烦，我们有另一种初始化的方法，**用引号引起字符串即可**，这种字符串成为**字符串常量**或**字符串字面值**。
```cpp
char bird[11] = "Mr. Cheeps";   // the \0 is understood
char fish[] = "Bubbles";    //let the compiler count
```
用引号括起的字符串隐式地包括结尾的空字符，因此不用显式地包括它。另外，各种C++输入工具通过键盘输入，将字符串读入到char数组中时，将自动加上结尾的空字符.
当然，要确保数组应该足够的大，能够储存字符串中的所有字符——包括空字符。让编译器计算元素数目更为安全。C++对字符串长度没有限制。
###### 在编写C语言字符串的时候，创建数组的时候不要忘了最后为`\0`流出空间。
**注意，字符串常量（使用双引号）不能与字符常量（使用单引号）互换。**两者有着明显的区别：
```cpp
char ch1 = 'A';  // ok
char ch2 = "A"; // not allowed
```
对于ch2，虽然在表面上我们内容与ch1是一样的，但是我们的ch2其实等价于`char ch2[2] = {'A', '\0'};`

#### 3.3.1 拼接字符串常量
C++允许拼接字符串字面值，即将两个用引号括起的字符串合并为一个。事实上，任何两个由空白（空格、制表符和换行符）分隔的字符串常量都将自动拼接成一个。下面的格式都是可以的。
```cpp
cout << "I'd give my right arm to be" " a great violinist.\n";
cout << "I'd give my right arm to be a great violinist.\n";
cout << "I'd give my right ar"
"m to be a great violinist.\n";
```
注意，拼接时不会在被连接的字符串之间添加空格，第二个字符串的第一个字符将紧跟在第一个字符串的最后一个字符（不考虑\0）后面。第一个字符串中的\0字符将被第二个字符串的第一个字符取代。

#### 3.3.2 在数组中使用字符串
要在数组中使用字符串，常用方法有两种：一是将数组初始化为字符串常量，二是将键盘或文件输入读入到数组中。直接看一个例子：
```cpp
// strings.cpp -- storing strings in an array
#include <iostream>
#include <cstring>  // for the strlen() function

int main()
{
    using namespace std;
    const int Size = 15;
    char name1[Size];                // empty array
    char name2[Size] = "C++owboy";  // initialized array
    // NOTE: some implementations may require the static keyword
    // to initialize the array name2

    cout << "Howdy! I'm " << name2;
    cout << "! What's your name?\n";
    cin >> name1;
    cout << "Well, " << name1 << ", your name has ";
    cout << strlen(name1) << " letters and is stored\n";
    cout << "in an array of " << sizeof(name1) << " bytes.\n";
    cout << "Your initial is " << name1[0] << ".\n";
    
    name2[3] = '\0';                // set to null character
    cout << "Here are the first 3 characters of my name: ";
    cout << name2 << endl;
    
    return 0;
}
```
下面是运行结果：
```
Howdy! I'm C++owboy! What's your name?
Basicman     // 这里是我们在键盘上的输入
Well, Basicman, your name has 8 letters and is stored
in an array of 15 bytes.
Your initial is B.
Here are the first 3 characters of my name: C++
```
注意：我们在这里的strlen()函数是C++头文件`<cstring>`中的函数，它接受一个字符串，返回其中的元素个数（不含有`\0`）。这里的sizeof运算符中的结果是15而不是8是因为我们`()`中的是数组名，sizeof(数组名)会返回数组所用的内存长度（char字节数为1），无论你有没有`\0`。至于为什么最后的输出是“C++”是因为cout在处理到\0后就不会继续输出该数组了，后面的内容直接忽略。

#### 3.3.3 字符串输入
```cpp
// instr1.cpp -- reading more than one string
#include <iostream>
int main()
{
    using namespace std;
    const int ArSize = 20;
    char name[ArSize];
    char dessert[ArSize];

    cout << "Enter your name:\n";
    cin >> name;
    cout << "Enter your favorite dessert:\n";
    cin >> dessert;
    cout << "I have some delicious " << dessert;
    cout << " for you, " << name << ".\n";
    return 0;
}
```
下面是我们的运行结果：
```
Enter your name:
Alistair Dreeb  (这里是输入)
Enter your favorite dessert:
I have some delicious Dreeb for you, Alistair.
```
注意到后面的输入出现了问题，我们命名没有输入但是却直接输出了最后的结果。这是因为cin存在着**空白截断**的问题。cin使用空白符来确定字符串的结束位置，因此上方的程序cin只读取了一个单词。读取该单词后，cin将该字符串放到数组中，并自动在结尾添加空字符。因此当我们在出现线面的提示信息之前，我们的数组就已经被处理好了。
上方是字符串中的**空白截断**问题，其实我们还存在着数组长度小于对应的字符串长度的问题。这就需要我们在创立数组的时候进行注意了。

#### 3.3.4 字符串读取（整行）
对于上方的问题，istream文件中的类（如cin）提供类一些面向行的类成员函数：getline()和get()。这两个函数都是读取行输入，值啊都换行符，但是getline()会丢弃最后的换行符，而get()会将换行符保留在输入序列中（即**缓冲区**）。
1. getline()
   getline()读取整行，使用回车键的输入的换行符来确定输入结尾。要调用，可以使用`cin.getline()`。该函数有两个参数。第一个是用来存储行的数组名称。第二个是要读取的字符数。**注意这里的字符数是要加上`\0`的，也就是说实际读取的内容应该改是“字符数-1”。getline( )成员函数在读取指定数目的字符或遇到换行符时停止读取。
   `cin.getline(name, 20)   // 读取19个字符到name中（有\0占位）`
   ###### 如果超出了规定的字符数，当我们输出的时候，也不会输出对应的后续内容，因为已经被自动补充的\0截断了。
   值得补充的是，其实cin.getline()并不是必须是以回车键结尾，我们是可以指定我们想要的结束符的。
   ```cpp
    #include <iostream>
    using namespace std;

    int main() {
        const int ArSize = 50;
        char buffer[ArSize];

        cout << "请输入内容（以分号 ';' 结束输入）：" << endl;
        
        // 这里传入了 ';' 作为第三个参数
        cin.getline(buffer, ArSize, ';'); 

        cout << "你输入的内容是: " << buffer << endl;
        return 0;
    }
   ```
   这个程序中，我们在第二次使用cin.getline()的时候我们是使用";"来作为我们的结束符的。换句话说cin.getline()的完全体应该是有三个参数的：数组名 + 长度 + 结束符。

2. get()
   get()函数有着多种变体。其中一种的工作方式于getline()类似，他们接受的参数相同，解释参数的方式也相同，并且都读到行尾。但是get并不丢弃换行符，而是将其留在输入队列中（缓冲区）。假设我们连续两次调用get()，由于第一次调用后，换行符将留在输入队列中，因此第二次调用时看到的第一个字符便是换行符。因此get()认为已到达行尾，而没有发现任何可读取的内容。如果不借助于帮助，get()将不能跨过该换行符。
   get()还有一种变体，使用不带任何参数的cin.get()可以读取下一个字符（即使是换行符），因此可以使用他来处理换行符。也就是说我们上方遇到的连续使用cin.get()会导致后面的cin.get()出现问题的解决方案就是在两次get()中间添加一个cin.get()来处理换行符。
   还有一种get()的使用方式是将两个类成员函数拼接起来（合并）：
   `cin.get(name, 20).get();    //concatenate member functions`。这样就不用担心下面的cin.get()会出现遇见换行符而停止输入的问题了。
    ###### 补充一下：C++允许函数有多个版本，条件是这些版本的参数列表不同。
    C++ 建议使用get()而不是getline()有两点原因：一是老式的实现是没有getline()的，二是get()可以让输入变得更加仔细。
    如何知道停止读取的原因是由于已经读取了整行，而不是由于数组已填满呢？查看下一个输入字符，如果是换行符，说明已读取了整行；否则，说明该行中还有其他输入。
3. 空行和其他问题：
   当getline()和get()读取空行的时候，C++将会设置**失效位**。这意味着接下来的输入将会被阻断。但是可以使用下面的命令恢复：
   `cin.claer();`
   这个语句的作用是**重置流的错误状态**。
   另一个潜在的问题是，输入字符串可能比分配的空间长。如果输入行包含的字符数比指定的多，则getline()和get()将把余下的字符留在输入队列中，而getline()还会设置失效位，并关闭后面的输入。

#### 3.3.5 混合输入字符串和数字
混合输入数字和面向行的字符串会导致问题。来看一个例子：
```cpp
// numstr.cpp -- following number input with line input
#include <iostream>
int main()
{
    using namespace std;
    cout << "What year was your house built?\n";
    int year;
    cin >> year;
    cout << "What is its street address?\n";
    char address[80];
    cin.getline(address, 80);
    cout << "Year built: " << year << endl;
    cout << "Address: " << address << endl;
    cout << "Done!\n";
    return 0;
}
```
结果如下：
```
What year was your house built?
1966
What is its street address?
Year built: 1966
Address: 
Done!
```
我们发现啊当我们输入1966给address后，后面的输入过程就直接没有了。问题在于，当cin读取年份，将回车键生成的换行符留在了输入队列中。后面的cin.getline( )看到换行符后，将认为是一个空行，并将一个空字符串赋给address数组。我们几种方法来解决这个问题：
1. 使用没有参数的cin.get()和有一个char参数的cin.get()，单独调用。
   ```cpp
   cin >> year;
   cin.get();   // or cin.get(ch);
   ```
2. 也可以使用表达式`cin>>year`返回cin对象，将调用拼接起来：
   ```cpp
   (cin >> year).get();     // or (cin >> year).get(ch);
   ```
这里的两种方法看起来很奇怪，这里的原理是**流提取运算符将内容赋给cin对象后返回的还是cin对象，这将允许我们继续使用cin的成员函数get()来清楚后面的换行操作。这里的更深的原理会在后面提到。

### 3.4 string 类
C++98 通过添加string类扩展了C++库，现在可以使用string类型的对象来存储字符串。
要使用string类，我们要在程序中包含头文件string。string类位于名称空间std中。所以要么用using编译指令，要么用`std::string`来引用他。string类隐藏了字符串的数组性质，因此我们可以像处理普通字符数组一样处理字符串。下面是一个例子
```cpp
// strtypel.cpp -- using the C++ string class
#include <iostream>
#include <string>       // make string class available

int main()
{
    using namespace std;
    char charr1[20];            // create an empty array
    char charr2[20] = "jaguar"; // create an initialized array
    string str1;                // create an empty string object
    string str2 = "panther";    // create an initialized string

    cout << "Enter a kind of feline: ";
    cin >> charr1;
    cout << "Enter another kind of feline: ";
    cin >> str1;        // use cin for input
    
    cout << "Here are some felines:\n";
    cout << charr1 << " " << charr2 << " "
         << str1 << " " << str2 // use cout for output
         << endl;

    cout << "The third letter in " << charr2 << " is "
         << charr2[2] << endl;
    cout << "The third letter in " << str2 << " is "
         << str2[2] << endl;   // use array notation

    return 0;
}
```
下面是运行情况：
```
Enter a kind of feline: ocelot
Enter another kind of feline: tiger
Here are some felines:
ocelot jaguar tiger panther
The third letter in jaguar is g
The third letter in panther is n
```
string对象使用方式和使用字符数组在很多方面相同：
* **初始化**：可以使用 C-风格字符串（即字符数组或字符串字面值）来初始化 `string` 对象。
* **输入**：可以使用 `cin` 将键盘输入直接存储到 `string` 对象中。
* **输出**：可以使用 `cout` 直接显示 `string` 对象。
* **访问**：可以使用数组表示法（即下标运算符 `[]`）来访问存储在 `string` 对象中的字符。
string类对象和字符数组之间的主要区别是：string对象可以声明为**简单变量**，而**不是数组**。string类的设计让程序能够自动处理string的大小。这使得与使用字符数组相比，使用string对象更加方便，也更加安全。

#### 3.4.1 string字符串初始化
string对象也可以使用列表初始化。
```cpp
string first_date = {"The Bread Bowl"}；
string second_date {"Hank's Fine Eats"};
```

#### 3.4.2 赋值、拼接string类字符串
使用string类时，string对象之间可以互相赋值，但是字符数组是不可以的。
```cpp
char charr1[20];               // create an empty array
char charr2[20] = "jaguar";    // create an initialized array
string str1;                   // create an empty string object
string str2 = "panther";       // create an initialized string
charr1 = charr2;               // INVALID, no array assignment
str1 = str2;                   // VALID, object assignment ok
```
对于字符串的拼接，string类简化了字符串的合并操作。可以使用运算符`+`将两个string对象合并起来，还可以使用运算符`+=`将字符串加到string对象的末尾。
```cpp
string str3;
str3 = str1 + str2;     // assign str3 the joined strings.
str1 += str2;   // add str2 to the end of str1
```

#### 3.4.3 string类的其他操作
在新增string类之前，我们也可以对字符串进行赋值操作。对于C-风格字符串，我们可以使用C语言库中的函数来玩长任务。头文件`<cstring>`提供了这些函数。比如我们可以使用strcpy()函数将字符串赋值到字符数组中。使用strcat()将字符数组附加到字符数组末尾。
```cpp
strcpy(charr1, charr2);  // copy charr2 to charr1
strcat(charr1, charr2);  // append contents of charr2 to charr1
```
下面的例子是综合应用：
```cpp
// strtype3.cpp -- more string class features
#include <iostream>
#include <string>              // make string class available
#include <cstring>             // C-style string library
int main()
{
    using namespace std;
    char charr1[20];
    char charr2[20] = "jaguar";
    string str1;
    string str2 = "panther";

    // assignment for string objects and character arrays
    str1 = str2;               // copy str2 to str1
    strcpy(charr1, charr2);    // copy charr2 to charr1

    // appending for string objects and character arrays
    str1 += " paste";          // add paste to end of str1
    strcat(charr1, " juice");  // add juice to end of charr1

    // finding the length of a string object and a C-style string
    int len1 = str1.size();    // obtain length of str1
    int len2 = strlen(charr1); // obtain length of charr1

    cout << "The string " << str1 << " contains "
         << len1 << " characters.\n";
    cout << "The string " << charr1 << " contains "
         << len2 << " characters.\n";

    return 0;
}
```
下面是输出：
```cpp
The string panther paste contains 13 characters.
The string jaguar juice contains 12 characters.
```

这里的`str1.size()`原型是`std::string.size()`，我们在C++中的string类中还有一种成员函数来获取字符长度：`std::string.length()`，一般来讲，这两种函数是等价的。第一种：遵循 STL 容器统一接口（如`vector.size()`、`list.size()`）更通用一些。第二种：源于 C 风格字符串的习惯（如`strlen()`），更语义化，适合处理文本。只要不混用，怎么用都行（是不建议混用）。

处理string对象的语法通常比C字符串函数简单：
```cpp
str3 = str1 + str2;
strcpy(str3, str1);
strcat(str3, str2);
```
第一句和后面的是等价的。

另外，使用字符数组时，总是存在目标数组过小，无法存储指定信息的危险，但是string类具有自动调整大小的功能，从而能够避免这种问题发生。C函数库确实提供了与strcat( )和strcpy( )类似的函—strncat( )和strncpy( )，它们接受指出目标数组最大允许长度的第三个参数，因此更为安全，但使用它们进一步增加了编写程序的复杂度。

#### 3.4.4 string类的I/O
我们可以使用cin和运算符`>>`来将输入存储到string对象中，使用cout和运算符`<<`来显示string对象。但是string对象每次读取的是一行而不是一个单词。我们来看一个例子：
```cpp
// strtype4.cpp -- line input
#include <iostream>
#include <string>              // make string class available
#include <cstring>             // C-style string library
int main()
{
    using namespace std;
    char charr[20];
    string str;

    cout << "Length of string in charr before input: "
         << strlen(charr) << endl;
    cout << "Length of string in str before input: "
         << str.size() << endl;
    cout << "Enter a line of text:\n";
    cin.getline(charr, 20);      // indicate maximum length
    cout << "You entered: " << charr << endl;
    cout << "Enter another line of text:\n";
    getline(cin, str);           // cin now an argument; no length specifier
    cout << "You entered: " << str << endl;
    cout << "Length of string in charr after input: "
         << strlen(charr) << endl;
    cout << "Length of string in str after input: "
         << str.size() << endl;

    return 0;
}
```
下面是运行结果：
```cpp
Length of string in charr before input: 27
Length of string in str before input: 0
Enter a line of text:
peanut butter
You entered: peanut butter
Enter another line of text:
blueberry jam
You entered: blueberry jam
Length of string in charr after input: 13
Length of string in str after input: 13
```
这里的结果有个问题：为什么`strlen(charr)`的结果要比正常的我们规定的数组长度大？首先，未初始化的数组中的内容是未定义的；其次，函数strlen()从数组中的第一个元素开始计算字节数，直到遇见空字符。但是由于我们的数组中的内容未被定义，所以这个`\0`的位置就是不确定的。在不同的编译器上这里的结果是不同的。
但是，string对象不一样，未被初始化的string对象的长度被自动设置为0。
下面来看两种读取字符串的方法：
```cpp
cin.getline(charr, 20);
getline(cin, str);
```
第一种正是我们前文介绍的cin中的getline()方法。第二种是我们`<string>`中的函数。第一种的句点表示法表明，函数getline()是istream类种的一个类方法。第二种没有句点表示法，这表示getline()不是一个类方法。它将cin作为参数，指出到哪里去查找输入。另外，也没有指出字符串长度的参数，因为string对象将根据字符串的长度自动调整自己的大小。

#### 3.4.5 其他形式的字符串字面值
这里的其他类型指的是wchar_t, char16_t, char32_t。对于这些类型的字符串字面值，C++分别使用前缀L、u和U表示，下面是一个如何使用这些前缀的例子：
```cpp
wchar_t title[] = L"Chief Astrogrator";   // w_char string
char16_t name[] = u"Felonia Ripova";    // char_16 string
char32_t car[] = U"Humber Super Snipe";    // char_32 string
```
C++11还支持Unicode字符编码UFT-8。C++使用前缀u8来表示这种类型的字符串字面值。
C++11新增的另一种类型式原始（raw）字符串。在原始字符串中，字符表示的就是自己，例如，序列\n不表示换行符，而表示两个常规字符——斜杠和n。

### 3.5 结构
结构是用户定义的类型，而结构声明定义了这种类型的数据属性。定义了类型后，便可以创建这种类型的变量。创建结构分为两步。首先先定义结构——描述并标记了能够存储到结构中的各种数据类型，然后再创建对应的对象。下面创建结构体的一个例子：
```cpp
struct inflatable{
    char name[20];
    float volume;
    double price;
};
```
程序中的`struct`是关键字，这些代码定义的是一个结构的布局。标识符inflatable是这种数据格式的名称，因此新类型的名称为inflatable。接下来的大括号中包含的是结构存储的数据类型的列表，其中每个列表项都是一条声明语句。列表中的每一项都被称为**结构成员**。
定义好后我们就可以创建这种类型的变量了。
如果你学过C语言就会发现C++与C语言有点不同：C++允许声明结构变量的时候省略`struct`。在C++中，结构标记的用法与基本类型相同，这种变化强调了**结构声明定义了一种新类型**。
由于结构体是一种新的类，因此我们可以使用**成员运算符**`.`来访问成员。并且我们可以像以往使用内置类型那样使用它们。
我们可以直接对结构进行初始化，只需要**依次**填入对应的值即可，不用必须使用多行。
结构的声明尽量是要在进行外部声明。**C++提倡使用外部结构声明，但是不建议使用外部变量**。

#### 3.5.1 结构初始化
C++11中的结构体也是支持使用**列表初始化**的。当初始化的`{}`中没有包含任何东西，所有的成员都将被设置为0。同样，**不允许缩窄转换**。
对于未被初始化的成员或指定初始值比成员少，剩下的成员会被置为 0。

#### 3.5.2 使用string类作为成员
C++是允许使用别的类充当一种类的成员类型的（只要你在使用之前声明过）。这种类型混用的形式我们在后面回说，叫做**组合**。

#### 3.5.3 结构属性
C++使用户定义的类型与内置类型尽可能相似。例如，可以将结构作为参数传递给函数，也可以让函数返回一个结构。另外，还可以使用赋值运算符`=`将结构赋给另一个同类型的结构，这样结构中每个员都将被设置为另一个结构中相应成员的值，即使成员是数组[^8]。这种赋值被称为**成员赋值**。

C++中的结构是支持在声明的同时进行对象创建和初始化的：
```cpp
struct perks
{
    int key_number;
    char car[12];
} mr_smith, ms_jones;    // two perks variables
```
在声明结构的同时创建了两个该结构的对象`mr_smith`和`ms_jones`。
```cpp
struct perks
{
    int key_number;
    char car[12];
} mr_glitz =
{
    7,              // value for mr_glitz.key_number member
    "Packard"       // value for mr_glitz.car member
};
```
声明结构体的同时创建了对象并进行了初始化。
虽然C++支持上述的做法，但是将结构定义和变量声明分开是个非常好的习惯。除了上述的两种做法，我们还可以创建一种没有名称的结构和对应对象，但是这种方法只能创建一个对象（因为没有名称，后续无法使用这种结构继续创建对象，也就是说是一次性的）。
除了上面说的这些，C++还允许结构中出现成员函数（在结构中定义的函数，可以当作该结构的成员来使用，这在C语言中是不被允许的）。这将在后面说**类**的时候进一步区分。

#### 3.5.4 结构数组
由于结构可以像内置类型一样使用，那么也是可以创建数组的。方法和创建基本类型数组完全相同。
`structName name[size]`
这个时候创建的是数组，不是结构对象，所以我们使用直接使用成员运算符是会报错的（但是我们对数组中的元素使用是不会有问题的，因为这个时候是该结构的对象）。
由于数组中的每个元素都是结构，所以我们可以使用结构初始化的方式来提供他的值，就像这样：
```cpp
inflatable guests[2] =          // initializing an array of structs
{
    {"Bambi", 0.5, 21.99},      // first structure in array
    {"Godzilla", 2000, 565.99}  // next structure in array
};
```

#### 3.5.5 结构中的位字段
所谓的**位字段**，就是允许使用以**位（bit）**为单位来指定成员所占用的内存空间，而不是使用传统的**字节（byte）**。字段的类型应为**整型或枚举**，接下来是冒号，冒号后面是一个数字，它指定了使用的位数。可以使用没有名称的字段来提供间距。每个成员都被称为位字段。下面是一个例子：
```cpp
struct torgle_register {
    unsigned int SN : 4;  // SN 占用 4 位（取值范围 0-15）
    unsigned int    : 4;  // 无名位字段，占用 4 位，用来做填充（间距）
    bool goodIn     : 1;  // 占用 1 位（0 或 1，即 false 或 true）
};
```

#### 3.5.6 使用new创建动态结构
在运行时创建数组优于在编译时创建数组，对于结构也是如此。需要在程序运行时为结构分配所需的空间，这也可以使用new运算符来完成。通过使用new，可以创建动态结构。当然这里介绍的也适用于类。
使用new创建动态结构分为两步：**创建结构和访问成员**。我们在定义好一个结构后，我们就可以像之前分配动态变量一样创建相应的结构：
```cpp
structName *ptr = new structName;   // 创建好了一个动态结构
```
但是访问成员有点复杂，不能将成员运算符句点用于结构名，因为这种结构没有名称，只是知道它的地址。C++专门为这种情况提供了一个运算符：箭头成员运算符`−>`。该运算符由连字符和大于号组成，可用于指向结构的指针，就像点运算符可用于结构名一样。
###### 如果结构标识符是结构名，则使用句点运算符；如果标识符是指向结构的指针，则使用箭头运算符。
另一种访问结构成员的方法是：使用`(*ptr).contributorName`，由于ptr是一个指针，我们可以解引用，然后再访问成员名。

### 3.6 共用体
**共用体**（union）是一种数据格式，它能够存储不同的数据类型，但只能同时存储其中的一种类型。也就是说，结构可以同时存储int、long和double，共用体只能存储int、long或double。共用体的句法与结构相似，但含义不同。我们看下面的例子：
```cpp
union one4all
{
    int int_val;
    long long_val;
    double double_val;
};

one4all pail;
pail.int_val = 15;            // 存储一个 int 类型的值
cout << pail.int_val;
pail.double_val = 1.38;       // 存储一个 double 类型的值，原先的 int 值将丢失
cout << pail.double_val;
```
共用体的是所有成员公用一块地址（也就是说，所有的对象住在一起，你来了我就必须走，即数据丢失）。每一次赋值都会覆盖掉上一次所用的内存。由于我们必须要有足够的空间来存储最大的成员，所以我们**共用体的最大长度为共用体最大成员的长度**。
共用体的用途之一是，当数据项使用两种或更多种格式（但不会同时使用）时，可节省空间。与结构一样，共用体也可以没有名称**匿名共用体**，这个时候他们的成员将成为位于相同地址的变量。
```cpp
struct widget
{
    char brand[20];
    int type;
    union                // anonymous union
    {
        long id_num;     // type 1 widgets
        char id_char[20]; // other widgets
    };
};
...
widget prize;
...
if (prize.type == 1)
    cin >> prize.id_num;
else
    cin >> prize.id_char;
```
由于共用体是匿名的，因此id_num和id_char被视为prize的两个成员，它们的地址相同，所以不需要中间标识符id_val。

### 3.7 枚举
C++中的enum工具提供了另一种创建符号常量的方式，则种方式可以替代 const。还允许新类型，但必须按严格的限制进行。看下面的语句：
```cpp
enum spectrum {red, orange, yellow, green, blue, violet, indigo, ultraviolet};
```
上面的语句完成两项工作：
- 让`sqectyum`成为新的类型名称：spectrum称为**枚举**。
- 将red, orange, yellow等作为符号常量，对应整数值0~7。这些量叫做**枚举量**。

在默认情况下，将整数值赋给枚举量，第一个枚举量值为0，第二个枚举量为1。
因为枚举名算是一种类型名，所以我们也可以用来声明变量：
`spectrum band;`
虽然枚举可以算是一种类型，但是在不进行强制类型转换的情况下，只能将枚举时使用的枚举量赋给这种枚举的变量。
```cpp
band = blue;    // vaild
band = 2000;    // invaild
```
对于枚举，只定义了赋值运算符。具体地说，没有为枚举定义算术运算。
枚举量时整型，可以转为int型，但是int型不能自动转换成枚举类型：
```cpp
int color = blue;   // valid
band = 3;   // incalid, ing not converted to spectrum
color = 3 + red;    // valid, red converted to int
```
枚举的规则相当严格。实际上，枚举更常被用来定义相关的符号常量，而不是新类型。
#### 3.7.1 设置枚举量的值
我们可以使用复数运算符来显式的设置枚举量的值：
`enum bits {one = 1, two = 2, four = 4, eight = 8};`
指定的值必须是整数（并不是必须是int型），也可以进行部分的赋值
`enum bigstep {first, second = 100, thrid};`
这里的first还是0，但是second以后就是从100开始进行依次排序了。
最后我们可以创建多个值相同的枚举量：
`xnum {zero, null = 0, one, numero_uno = 1};`
#### 3.7.2 枚举的取值范围
取值范围的定义如下。首先，要找出上限，需要知道枚举量的最大值。找到大于这个最大值的、最小的2的幂，将它减去1，得到的便是取值范围的上限。例如，前面定义的bigstep的最大值枚举值是101。在2的幂中，比这个数大的最小值为128，因此取值范围的上限为127。要计算下限，需要知道枚举量的最小值。如果它不小于0，则取值范围的下限为0；否则，采用与寻找上限方式相同的方式，但加上负号。例如，如果最小的枚举量为−6，而比它小的、最大的2的幂是−8（加上负号），因此下限为−7。

### 3.8 指针
指针[^9]是一个变量，其存储的是值的地址，而不是值本身。要找到常规变量的地址，我们可以使用地址运算符`&`，显示地址时，cout在不同的系统中使用的进制可能会有不同，但是大部分都是十六进制。

#### 3.8.1 声明和初始化指针
```cpp
int *p;
```
这个声明表明：`*p` 类型为 int，由于`*`被用于指针，因此，p变量本身必须是指针，可以说：**`p`本身是指针，但是`*p`不是指针，是int型的变量**。
对于`*`运算符两边的空格是可选的，实际上，在C语言中，我们使用`int *ptr`的格式，C++中我们也可以使用`int* ptr`，这两种的效果没有区别，因为C++允许这样做，但是**还是推荐前面的格式**。我们来看个例子：
```cpp
int *p1, *p2;   // 我们声明了两个指向int型的指针
int* p1, p2;    // 我们声明了一个int型的指针——p1，一个int型的变量p2.
```
对于每一个指针变量名，我们都要有一个`*`[^10]，对于其他类型的指针我们也可以这样声明。
虽然不同类型的指针所指对象不一样，但是他们本身的长度是一样的。地址的长度或值既不能指示关于变量的长度或类型的任何信息，也不能指示该地址上有什么内容。
我们可以在声明语句中初始化指针：
```cpp
int number = 666;
int *p_int = &number;
```
这样我们的`p_int`指针就指向了`number`这个int型的变量。

#### 3.8.2 指针的危险
在C++中创建指针的时候，计算机会分配用来存贮地址的内存，但不会分配用来存储指针所指向数据的内存。为数据提供空间是一个独立的步骤。[^11]
```cpp
int *p_int;       // 设置一个 int 型的指针 
*p_int = 114514;    // danger! 这里会出问题，这里的114514数据是没有内存地址的，因为他根本就没有被计算机分配内存。这就会导致指针所指向的地址是一个随机值。
```

#### 3.8.3 指针和数字
指针不是整形，但是计算机总是将地址当作整数处理。指针描述的是位置，将两个地址相乘是没有意义的（但是相加可能会有一点点意义吧——笔者并不是很了解）。因此，我们不能简单的将整数赋给指针。
```cpp
int *pt;
pt = 0xB800000000;  // 类型不符
```
这里的语句在C语言中是被允许的，但是在C++中，我们对类型的要求是更加严格的，所以我们要用到强制类型转化换：
```cpp
int *pt;
pt = (int *) 0xB80000000;   // 类型匹配
```

#### 3.8.4 使用new来分配新内存
变量是在编译时分配的有名称的内存，而指针只是为可以通过名称直接访问的内存提供了一个别名。指针真正的用武之地在于，在运行阶段分配未命名的内存以存储值。在这种情况下，只能通过指针来访问内存。在C语言中，我们可以使用`malloc()`库函数来分配内存，在C++中，我们可以使用运算符`new`。
下面是声明语句格式：
`typeName *pointer_name = new typeName(same to former);`
这个语句告诉程序：“我要一块 typeName 类型的内存”。运算符 new 会自动为你分配相应的内存。并返回其地址赋给对应的指针，这样，你的指针就指向了一块新的地址。
上方指针指向的内存没有名称，我们可以说这个指针指向了一个**数据对象**。这里的对象不是我们OOP中的对象，而是一种**东西**。
使用new运算符分配内存是在程序运行的时候进行的。对于指针，需要指出的另一点是，new分配的内存块通常与常规变量声明分配的内存块不同。变量nights和pd的值都存储在被称为**栈**（stack）的内存区域中，而new从被称为**堆**（heap）或自由存储区（freestore）的内存区域分配内存。这些我们在后面会说）。

#### 3.8.5 用delete释放内存
当我们使用完对应空间时，我们可以将这片空间归还给计算机。这个时候我们就可以使用运算符`delete`了。使用delete时[^12]，后面要加上指向内存块的指针（这些内存块最初是用new分配的）。
只能用delete来释放使用new分配的内存。然而，对空指针（NULL或者是nullptr）使用delete是安全的.
事实上`delete`运算符删除的并不是我们的指针，而是指针所指向的内存地址，所以：**当我们使用两个指针指向同一块节点的时候，不要轻易使用`delete`，因为有可能导致错误删除**。

#### 3.8.6 使用new来创建动态数组
如果我们使用简单的变量，`new`运算符的用处不是很大，但是，我们在使用大型数据的时候（如数组、字符串和结构），应使用new。如果通过声明来创建数组，则在程序被编译时将为它分配内存空间。不管程序最终是否使用数组，数组都在那里，它占用了内存。在编译时给数组分配内存被称为**静态联编**。但使用new时，如果在运行阶段需要数组，则创建它；如果不需要，则不创建。还可以在程序运行时选择数组的长度。这被称为**动态联编**。
1. 使用 new 来创建动态数组
   在C++中，我们创建动态数组很容易，我们只需要告诉 new 数组的元素类型和我们想要的数量即可。
   ```cpp
   int *ptr = new int [10]; // 创建一个10个int型数据的数组
   ```
   new 运算符会返回首元素的地址。这样我们就创建好了一个动态数组。当我们不用的时候我们就可以使用delete进行释放内存。
   ```cpp
   delete [] ptr;   // 释放内存
   ```
   如果使用new时带方括号，则使用delete时也应带方括号。
   总之，使用new和delete有一下的规则：
   - 不要使用delete释放不是new分配的内存
   - 不要使用delete释放同一个内存块两次
   - 如果使用new[]为数组分配内存，用delete[]释放
   - 使用new[]为实体（元素）分配内存，同delete释放。
   - 空指针( NULL 和 nullptr)对于delete是安全的
    
   还有就是对于new分配的内存，程序是不公用的，倒是我们不能使用sizeof运算符来确定动态分配的数组包含的字节数。
   下面是通用格式：
   ```cpp
   type_name *pointer_name = new type_name [num_elements];
   ```
2. 使用动态数组
   当我们想要访问数组的时候，我们可以将**指针名当数组名使用**。也就是说，我们在分配内存创建数组以后，这个指针不仅指向数组中的第一个元素，还可以代表着这个数组。数组和指针基本等价是C和C++的优点之一。但是这并不代表着两者就是一个东西。
   虽然我们可以使用指针名代表对应的数组，但是**指针和数组名有一些本质区别**：**指针是变量，但是数组名不是**，我们可以改变指针，但是不能修改数组名。

#### 3.8.7 指针、数组和指针算数
**指针和数组基本等价的原因在于指针算数**。将整数变量加1后，其值将增加1；但将指针变量加1后，增加的量等于它指向的类型的字节数。于此同时，数组名在C++中被解释为地址。
```cpp
int arr1[10] = {0};
double arr2[3] = {114.514, 0.01, 350.234};
int *arr_ptr1 = arr1;     // ok;
int *arr_ptr2 = &arr2[0];   // ok;
```
上面的操作中，效果都是一样的，我们将指针指向了第一个元素。且都是合法的。
我们来看看数组表达式`arr2[0]`，C++编译器将该表达式看作是`*(stacks + 1)`这意味着先计算数组第2个元素的地址，然后找到存储在那里的值。两者是等价的。即`arrayname[index] == *(arrayname + index)`。如果是指针我们也支持这样的操作：`pointername[index] == *(pointername + index)`。
我们再看看sizeof运算符，对着数组用，我们返回的是数组的长度，而对指针应用则是指针的长度，即使指针指向了一个数组。在使用sizeof时，C++不会讲数组名解释为地址。

#### 3.8.8 指针和字符串
数组和指针的特殊关系可以扩展到C-风格字符串。当我们创立一个C风格字符串后，使用cout进行输出时，我们传递的时首地址，无论是指针还是数组名。**这意味着对于数组中的字符串、用引号括起的字符串常量以及指针所描述的字符串，处理的方式是一样的，都将传递它们的地址。**这种传递地址的习惯，我们是比较提倡的，因为我们不用将所有的内弄进行传递，不仅减少了运行时间，我们还减少了消耗的内存。
对于字符串常量：有些编译器将字符串字面值视为只读常量，如果试图修改它们，将导致运行阶段错误。在C++中，字符串字面值都将被视为常量。有些编译器只使用字符串字面值的一个副本来表示程序中所有的该字面值
**C++不能保证字符串字面值被唯一地存储。**如果在程序中多次使用了字符串字面值“wren”，则编译器将可能存储该字符串的多个副本，也可能只存储一个副本。但是无论如何，由 const 声明的指向常量的指针是不被允许修改其中的内容的（因为本身我们就不可以修改常量的内容）。
我们来看一个非常重要的例子：
```cpp
char *ptr1;
char *ptr2 = new char [20];
// cin >> ptr1;    // error
cin >> ptr2;    // ok, 但是不要超过19个字符
cout << ptr1;   // 不建议，因为不同的编译器会导致不同的结果，可能会输出一段垃圾信息，也可能会导致崩溃。
cout << ptr2;   // 输出ptr2指向的字符串
int *ptr3;
char str = "pig";
cout << str << ' ' << (int *)str << endl;
cout << ptr << ' ' << (int *)ptr << ' ' << *ptr << endl;   
```
最后两个输出很有意思，第一段输出都是字符串内容，第二个是地址，第二行的第三个输出的是字符串的第一个字符。[^13]
这里直接输入ptr1是不可以的，因为他没有分配内存（是没分配指向的内存，cin和cout对于字符串的处理很相似，都是处理所指向的内容）。如果我们像ptr2输入，我们就可以正常输入。因为ptr2指向了分配好的内存。
对于指针代表的字符串之间的赋值，我们要用`<cstring>`库中`strcpy()`函数，他有两个参数：第一个是要复制的指针和数组名，第二个是样本。然后返回拷贝成功的首地址。如果分配的内存长度够用，但是我们不想用这么多，我们还可以使用`strncpy()`，与上方的函数差不多，但是有第三个参数来指定复制几个字符。

#### 3.8.9 多级指针
指针具有很高的灵活性，指针不仅可以指向一些我们自己创建的类或者是系统内置的类，还可以做到**指向另一个指针**。这种指向指针的指针就叫做**多级指针**。
```cpp
int **point_pointer;
```
这里我们声明了一个二级指针，它可以指向`int*`类型的指针。变量名前面的`*`有几个就代表了是几级指针：
```cpp
int ***pointer3;    // 三级指针
```
多级指针的重要用途就是[创建和使用多维数组](#482-动态二维数组)。
使用多级指针可以创建多维的数组，但是与之相应的，我们也需要使用多次delete来对内存进行释放（详情见[动态二维数组](#482-动态二维数组)）

#### 3.8.10 指针数组
由于指针本身也是一种类型，所以也会有对应的数组：
```cpp
typeName *ptrArray[Size];   // 创建了一个size大小的type类型的指针数组。
```
同普通指针一样，我们是也是将一堆指针放在了一片连续的空间中。冰洁都是相同类型。使用时像使用普通数组一样访问其成员即可。但是成员毕竟还是指针，对成员操作还是要像操作指针一样。
###### 这里其实就是多维指针的雏形。

#### 3.8.11 数组的替代品
1. 模板类vector：<a id="模板类vector"></a>
    模板类vector类似于string类，也是一种动态数组。您可以在运行阶段设置vector对象的长度，可在末尾附加新数据，还可在中间插入新数据。基本上，它是使用new创建动态数组的替代品。实际上，vector类确实使用new和delete来管理内存，但这种工作是自动完成的。
    首先，要使用vector对象，必须包含头文件vector。其次，vector包含在名称空间std中，因此我们可使用using编译指令、using声明或std::vector。第三，模板使用不同的语法来指出它存储的数据类型。第四，vector类使用不同的语法来指定元素数。
    ```cpp
    #include <iostream>
    #include <vector>
    using namespace std;
    ···
    vector<int> vi;     // 创建一个规模为0的数组
    int n;
    cin >> n;
    vector<double> vd(n);   // 创建一个n大小的数组
    ```
    其中，vi是一个vector<int>对象，vd是一个vector<double>对象。由于vector对象在我们插入或添加值时自动调整长度，因此可以将vi的初始长度设置为零。但要调整长度，需要使用vector包中的各种方法。
    下面是标准格式：
    ```cpp
    vector<typeName> vt(n_elem);    // 建一个n_elem大小的数组
    ```
2. 模板类array：
    vector虽然比数组强大且方便，但是效率较低。鉴于此，C++11新增了模板类array，也位于名称空间std中。array数组的长度是固定的，也使用栈来存储，因此效率跟数组相同，但是更加方便和安全。要创建array对象，需要包含头文件array。array对象的创建语法与vector稍有不同：
    ```cpp
    #include <array>
    ···
    using namespace std;
    array<int, 5> ai;   // 创建一个含有5个int型的数组
    array<double, 4> ad = {1.2, 2.1, 3.43, 4.3};    // 像普通数组一样初始化
    ```

    下面是通用格式：

    ```cpp
    array<typeName, n_elem> arr; 
    ```
    和vector不同的是，n_elem不能是变量
3. 数组、vector、array之间的对比 
   1. 无论是数组、vector还是array对象，我们都可以使用标准的数组表示法来访问各个元素。
   2. array 和数组存贮在相同的内存区域（栈）中，而vector储存在另一个区域中（堆）。
   3. 一个array对象可以赋给另一个array对象，但是数组必须一个一个复制
   4. 对于非法索引的处理：数组是直接强行使用非法索引（但是你并不知道会获得什么，vector和array也是允许使用非法索引的，但是他们有一个更好的保障方法：使用`at()`成员函数。使用`at()`后，我们会检查这个索引是否合法，不合法程序就会中断，同时运行时间也会更长（因为使用了函数进行检查）。
   ###### 进一步的说明在后面的模板类中，可以直接[跳转](#模板类vector)

#### 3.8.12 const 和数组
对于const和数组之间的关系有下面三种：
1. 常量指针（指向常量的指针）
   ```cpp
   const typeName *ptr;
   ```
   这里声明了一个常量指针，**是 typeName 类型的指针，但是所指的是对应类型的常量**。
2. 指针常量（指针是常量，**不能修改指向地址**）
   ```cpp
   typeName * const ptr;
   ```
   这里声明的是指针常量，**是 typeName 类型对应的指针，但是其所指的地址不允许改变**（就像数组名）
3. 指向常量的指针常量（什么也不能动）
   ```cpp
   const typeName * const ptr;
   ```
   这里声明的是指向常量的指针常量，**指向对象是常量，本身也是常量**。

常量变量的地址可以赋给常规指针，同时也可以赋值给事项const的指针（常量指针）。但是，**将const变量的地址赋给指向 const 的指针是可以的，赋给常规指针就不可以了**：
```cpp
const float number = 9.80;
const float *ptr = &number;     // valid

const float number = 1.63; 
float *ptr = &number;   // invalid
```
C++禁止将 const 的地址赋值给非 const 指针，但是正常的变量是可以赋值给 const 的指针的。

下面给出一个非常“不正常”的例子：
```cpp
const int **ptr2;
int *ptr1;
const int n = 13;
ptr2 = &ptr1;
*ptr2 = &n;
*ptr1 = 10;     // 修改了常量 n
```
上述的代码**慎用**，仅当只有一层间接关系（指针指向基本数据类型）时候，才可以将非 const 地址或指针赋值给 const 指针。

### 3.8.13 空指针
C++ 有两个版本的空指针：`NULL` 和 `nullptr`。
- `NULL`: 这里的“空指针”其实并不是真正的空指针。`NULL` 其实是一个字符，ASCII码为 0.
  - 本质是一个**宏定义**
  - 在 C++ 中，通常被定义为 0
  - 类型为 int 或 long。不是真的指针
- `nullptr`: nullptr 是 C++11 新增的关键字。专门用来表示**空指针**。
  - 本质是一个**关键字**
  - 类型是 `std::nullptr_t`
  - 是一个**指针字面量**，可以隐式转换，但是**不能直接转换成非零的整数**。

| 特性 | NULL | nullptr |
| :--- | :--- | :--- |
| **定义方式** | 宏定义 (`#define NULL 0`) | C++ 关键字 |
| **底层类型** | 整数类型 (`int`) | 指针类型 (`std::nullptr_t`) |
| **隐式转换** | 可转换为整数或指针 | 只能转换为指针 |
| **引入标准** | C 语言 / 早期 C++ | C++11 及更高版本 |
| **类型安全** | 低（容易与整数混淆） | 高（类型严格受限） |

使用 nullptr 可以避免[函数重载](#函数重载)的二义性：
```cpp
void func(int n) {
    std::cout << "调用了 int 版本" << std::endl;
}

void func(char* p) {
    std::cout << "调用了 指针 版本" << std::endl;
}

int main() {
    func(NULL);    // 报错或意想不到的结果：匹配 func(int)
    func(nullptr); // 正确：匹配 func(char*)
}
```
这个时候由于有两个对符合要求的指针，可能会出现**重载决议失败**


### 3.9 存储方式
C++有三种分配内存的方式：自动、静态和动态存储（或者叫**堆**）。这三种在存在时间长短的方面各不相同[^14]。
###### C++11中还新增了第四种类型——线程存储。
1. 自动存储
   在函数内部定义的常规变量使用自动存储空间，被称为**自动变量**。它们在所属的函数被调用时自动产生，在该函数结束时消亡。
   事实上，自动变量是一种**局部变量**。作用域是包含他的代码块。代码块是被包含在花括号中的一段代码。
   自动变量通常存储在**栈**中。这意味着执行代码块时，其中的变量将依次加入到栈中，而在离开代码块时，将按相反的顺序释放这些变量，这被称为**后进先出**。
   ###### 什么是局部变量？事实上局部变量都是自动变量，被存储在栈上，但是**静态局部变量**不是。他术语静态存储中的变量。
2. 静态存储
   **静态存储是整个程序执行期间都存在的存储方式**。使变量成为静态的方式有两种：一种是在函数外面定义它；另一种是在声明变量时使用关键字`static`：`static int number = 100;`
   自动存储和静态存储的关键在于：这些方法严格地限制了变量的寿命。变量可能存在于程序的整个生命周期（静态变量），也可能只是在特定函数被执行时存在（自动变量）。
3. 动态存储
   new和delete运算符提供了一种比自动变量和静态变量更灵活的方法。它们管理了一个内存池，这在C++中被称为自由存储空间（freestore）或**堆（heap）**。
   这个空间是独立于静态变量和自动变量内存空间的。数据的生命周期不完全受程序或函数的生存时间控制。然而，**内存管理也更复杂了**。在栈中，自动添加和删除机制使得占用的内存总是连续的，但new和delete的相互影响可能导致占用的自由存储区不连续，这使得跟踪新分配内存的位置更困难。

## 四、循环和关系表达式
### 4.1 for 循环
#### 4.1.1 for 循环组成
for循环组成步骤有下面几个：
1. 设置初始值
2. 执行测试
3. 执行循环操作
4. 更新用于测试的值

初始化、测试和更新操作构成了控制部分，这些操作由括号括起。其中每部分都是一个表达式，彼此由分号隔开。控制部分后面的语句叫作循环体，只要测试表达式为true，循环体就会被执行。通用格式如下：
```cpp
for(initialization; test-expression; update-expression)
    body
```
C++时将整个for看作一个语句。

循环只执行一次初始化，可以设置起始值，然后用对应的变量计算循环周期。

测试表达式决定循环体是否执行。通常这个表达式为关系表达式（将两个值进行比较）。

for循环是入口条件（entry-condition）循环。这意味着在每轮循环之前，都将计算测试表达式的值，当测试表达式为false时，将不会执行循环体。这种在循环之前进行检查的方式可避免程序遇到麻烦。
update-expression（更新表达式）在每轮循环结束时执行，此时循环体已经执行完毕。通常，它用来对跟踪循环轮次的变量的值进行增减。然而，它可以是任何有效的C++表达式，还可以是其他控制表达式。

for语句看这样一个函数调用，但是for在C++中是一个关键字，并且不允许将函数命名为for。

#### 4.1.2 for循环变量初始化 
在以前，for语句中是不能进行初始化的，也就是说，像`for(int i = 0; i < 2; i++)`这样的语句在以前是非法的。以前是可以同构一种新的表达式来是其合法的：
```cpp
for(for-init-statement condition; expression)
    statement;
```
这种语句中`for-init-statement`被视为一条语句，它既可以是表达式语句也可以是一种声明语句。这种表达式有一种好处：这种生命的变量作用域只用for语句中：
```cpp
for(int i = 0; i < 2; i++){
    cout << i << ' ' << endl;
}
cout << i;  // ERROR!
```

#### 4.1.3 循环步长 
for循环中的i变化程度就是**步长**。它可以是任何整数值，格式如下：
`i = i + by`
其中的 by 是我们的步长。
当然最常见的还是**自增和自减**：
```cpp
for (int i = 0; i < 2; i++);
for (int i = 0; i < 2; ++i);
for (int i = 0; i > -2; i--);
for (int i = 0; i > -2; --i);
```

#### 4.1.4 遍历字符串 
由于for循环有着便利的作用，我们可以使用for语句来访问字符串中的每一个元素，就像下面的例子：
```cpp
#include <iostream>
#include <string>

int main()
{
    using namespace std;
    cout << "Enter a word: ";
    string word;
    cin >> word;

    // display letters in reverse order
    for (int i = word.size() - 1; i >= 0; i--)
        cout << word[i];
    
    cout << "\nBye.\n";
    return 0;
}
```
下面是结果：
```
Enter a word: animal
lamina
Bye.
```
遍历数组也是一样的方法，字符串就是一种特殊的数组。

#### 4.1.5 自增 / 自减运算符 
这两个运算符是将一个变量进行加1和减1的操作，但是他们有两个版本：**前缀和后缀版**。前缀（prefix）版本位于操作数前面，如++x；后缀（postfix）版本位于操作数后面，如x++。两者的效果一样，但是影响的时间不同，返回值也不同。
```cpp
int a = 1;
cout << a++;    // 输出1，此时a变成了2.
cout << ++a;    // 输出3，此时a变成了3
cout << a;  // 输出3
```
前缀变体`++a`是先进行自增，在将增完后的值返回，后缀变体`a++`则是将变量值先返回，再进行自增。总的来说`++a`返回`a+1`，`a++`返回`a`。自减运算符同理。
这种运算符虽然方便，但是我们不能在一条语句中使用多次。这样会导致我们的行为未定义。
```cpp
x = 2 * (x++) * (3 - ++x);  // 未定义行为
```
###### 对于自增 / 自减运算符我们还有对应的副作用：
C++程序中，我们是存在**顺序点**的。在这里，进入下一步之前将确保对所有的副作用都进行了评估。在C++中，语句中的分号就是一个顺序点，这意味着程序处理下一条语句之前，赋值运算符、递增运算符和递减运算符执行的所有修改都必须完成。
我们有这样的程序：
```cpp
for(int i = 0; i < 2; i++){
    cout << i;
}
```
在这个语句中，括号内有三个顺序点。分别对应着三个表达式的末尾。这就保证了三个语句在运行时会严格按照我们的顺序点对效果进行评估。
这里的输出是`01`，为什么不是`12`?这还与我们的语句的执行顺序有关。for语句中的执行顺序是：
1. 先初始化循环变量（在第一轮）
2. 再进行条件判断
3. 执行循环体
4. 进行变量更新（调整循环变量）

像for语句这样的语句还可以叫做**完整表达式**，**因为他们并不在另一个更大的表达式中充当子表达式**。像这个例子：
```cpp
y = (4 + x++) + (6 + ++x);
```
像这样的表达式，`x++`和`++x`都不是完整表达式，括号中没有顺序点，我们无法对其进行评估，也就无法对x的值进行确定。

前缀和后缀版本虽然执行的操作效果相同，但是只是对内置类型看不出来。当我们在进行自定义类型的时候，前缀和后缀的差别就显现出来了。
**前缀的效率要比后缀效率高**。

#### 4.1.6 组合赋值运算符
C++语法中有能够合并简单运算和赋值的运算符，他们的功能都等价于先进行运算在进行赋值（虽然这个运算符本身也是这个效果。
```
// 一种方式：
number1 operatorAndEqual number2;

// 等价方式
number1 = number1 operator number2;
```
下边是对应组合赋值运算符和其含义：
| 操作符 | 作用 (L为左操作数，R为右操作数) |
| :--- | :--- |
| += | 将 L+R 赋给 L |
| -= | 将 L-R 赋给 L |
| *= | 将 L*R 赋给 L |
| /= | 将 L/R 赋给 L |
| %= | 将 L%R 赋给 L |

### 4.3 表达式和语句
#### 4.3.1 表达式
C++成为非常具有表现力的语言。任何值或任何有效的值和运算符的组合都是表达式。无论是算数、赋值还是任何能得出有效值的表达式。
```cpp
maids = (cooks = 4) + 3;
x = y = z = 0;
```
上面是两个很好的例子，第一个虽然在C++中是允许的（因为赋值表达式返回结果4），但是不提倡，第二个表达式时**链式赋值**，可以进行连续赋值，顺序是从左向右。
**任何表达式带上`;`都可以成为一个语句，但是不一定有编程含义，但是反过来就不一定正确。**就像下面两个例子：
```cpp
int number;
int fx = for(int i = 0; i < 2; i++) cout << "I love you.";
```
这两个语句第一个去掉分号不是一个表达式，因为没有值，第二个是非法的，因为for语句不是表达式，我们不能将他赋给fx。

#### 4.3.2 复合语句（语句块）
复合语句（代码块）由一对花括号和它们包含的语句组成，被视为一条语句。下面有一对对比例子：
```cpp
// 正常使用代码块的：
for (int i = 0; i < 10; i++){
    cout << "I Love China.";
    cout << "Now, we remained " << 10 - i << "times.";
}
cout << "Over";

// 没有花括号的：
for (int i = 0; i < 10; i++)
    cout << "I Love China.";
    cout << "Now, we remained " << 10 - i << "times.";
cout << "Over";
```
第一个程序会正常执行。但是第二程序就会报错。编译器会返回“不知道 i 是什么变量的错误”（当然也可能会输出在外界定义的 i 的值。用花括号将程序括起来会将`{}`中的内容视为一个语句。但是如果省略了花括号，只有缩进，编译器将忽略缩进，这时**只有第一条语句位于循环中。**
对于代码块中的**变量生命周期**[^15]。

复合语句还有一种有趣的特性。如果在语句块中定义一个新的变量，则仅当程序执行该语句块中的语句时，该变量才存在。执行完该语句块后，变量将被释放。在外部语句块中定义的变量在内部语句块中也是被定义了的。
如果在一个语句块中声明一个变量，而外部语句块中也有一个这种名称的变量，在声明位置到内部语句块结束的范围之内，新变量将隐藏旧变量；然后就变量再次可见。（也就是说，内部的变量会掩盖外部的变量，这里可以看Framework图）。

#### 4.3.3 逗号运算符
语句块允许把两条或更多条语句放到按C++句法只能放一条语句的地方。逗号运算符对表达式完成同样的任务，允许将两个表达式放到C++句法只允许放一个表达式的地方。给个例子：
```cpp
for (int i = 0, j = 0; i < 2, j < 2; i++, j++){
    ···
}
int i = 0, j = 0;
i++, j++;
cout << i << j;
```
到目前为止，逗号运算符最常见的用途是将两个或更多的表达式放到一个for循环表达式中。不过C++还为这个运算符提供了另外两个特性。首先，它确保先计算第一个表达式，然后计算第二个表达式（换句话说，逗号运算符是一个顺序点）。如下所示的表达式是安全的：
```cpp
i = 20, j = 2 * i;
```
其次，C++规定，逗号表达式的值是第二部分的值。上述表达式的值为 40，因为 j = 2 * i 的值为40。
在所有运算符中，**逗号运算符的优先级是最低的**。下面是一个典型例子：
```cpp
cats = 17, 240;
```
这里是被解释成：`(cats = 17), 240`。这里的 240 就不起作用，最后的
表达式效果就是`cats = 17;`。
但是，如果表达式是这样的：`cats = (17, 240);`，这样的结果就是`cats = 240`。由于逗号表达式是最后一个表达式的值。

#### 4.3.4 关系表达式
C++提供了6种关系运算符来对数字进行比较。由于字符用其ASCII码表示，因此也可以将这些运算符用于字符。不能将它们用于C-风格字符串，但可用于string类对象。对于所有的关系表达式，如果比较结果为真，则其值将为true，否则为false，因此可将其用作循环测试表达式。（老式实现认为结果为true的关系表达式的值为1，而结果为false的关系表达式为0。）
| 操作符 | 含义 |
| :--- | :--- |
| < | 小于 |
| <= | 小于或等于 |
| == | 等于 |
| > | 大于 |
| >= | 大于或等于 |
| != | 不等于 |

**关系运算符的优先级比算术运算符低**。例：
```cpp
// 原始表达式
x + 3 > y - 2              // Expression 1

// 实际对应的逻辑（算术运算优先）
(x + 3) > (y - 2)          // Expression 2

// 错误的理解（关系运算不优先）
x + (3 > y) - 2            // Expression 3
```
**注意事项**：对于`==`和`=`两个运算符，他们很相似，但是一定不能混用。对于将`==`用于进行判断的循环，两者混用会导致严重的后果——陷入死循环。发现这种错误的困难之处在于，代码在语法上是正确的，因此编译器不会将其视为错误。

#### 4.3.5 C-风格字符串的比较
对于这样的语句（其中的 word 是字符数组）：
```cpp
word == "mate";
```
这样的比较是不会得出我们想要的结果的，因为**数组名是数组的首地址**，这样的比较其实是在比较两个字符串的首地址是否是同一地址。显然不能得出我们想要的结果。，这种情况下就需要我们进行一个一个字符的比对，或者是使用头文件 `<cstring>` 中的 `strcmp()` 函数。
`strcmp()` 函数接受两个字符串地址作为参数。这意味着参数可以是指针、字符串常量或字符数组名。如果两个字符串相同，该函数将返回零；如果第一个字符串按字母顺序排在第二个字符串之前，则 `strcmp()` 将返回一个负数值；如果第一个字符串按字母顺序排在第二个字符串之后，则 `strcmp()` 将返回一个正数值。这里的字符比较是根据字符的系统编码来进行比较的。使用ASCII码时，所有大写字母的编码都比小写字母小，所以按排列顺序，大写字母将位于小写字母之前。

C-风格字符串是通过结尾的空值字符定义的，而不是由其所在数组的长度定义的。这意味着两个字符串即使被存储在长度不同的数组中，也可能是相同的：
```cpp
char big[80] = "Daffy";     // 5 letters plus \0
char little[6] = "Daffy";       // 5 letters plus \0
```

虽然不能用关系运算符来比较字符串，但却可以用它们来比较字符，因为字符实际上是整型。
```cpp
cout << ('1' == '2');     // 输出 0
```

总结：
1. **`strcmp()` 的基本功能**
    * 用于测试 C-风格字符串（以 `\0` 结尾的字符数组）是否相等或其排列顺序。

2. **判断字符串相等**
    * 当 `str1` 和 `str2` **完全相等**时，表达式返回 `true`：
    ```cpp
    strcmp(str1, str2) == 0
    ```

3. **判断字符串不相等**
    * 当 `str1` 和 `str2` **不相等**时，以下两个表达式均为 `true`：
    ```cpp
    strcmp(str1, str2) != 0
    strcmp(str1, str2)      // 在 C/C++ 中，非 0 即为 true
    ```

4. **判断字典序（排列顺序）**
    * 如果 `str1` 在 `str2` 的**前面**：
    ```cpp
    strcmp(str1, str2) < 0
    ```
    * 如果 `str1` 在 `str2` 的**后面**：
    ```cpp
    strcmp(str1, str2) > 0
    ```

5.  `strcmp()` 函数非常灵活，可以分别扮演 `==`、`!=`、`<` 和 `>` 运算符的角色。

#### 4.3.6 string类字符串的比较
如果使用string类字符串而不是C-风格字符串，比较起来将简单些，我们能够使用关系运算符进行比较。这之所以可行，是因为类函数重载（重新定义）了这些运算符。
string之间的比较规则和strcmp()的规则差不多。但是符号更加接近我们正常的使用：
1. **相等判断 (`==` 与 `!=`)**
    * `==`：如果两个字符串长度相同且每个对应位置的字符都相同，返回 `true`。
    * `!=`：只要长度不同或有任何一个字符不同，返回 `true`。
    ```cpp
    string s1 = "hello";
    string s2 = "hello";
    if (s1 == s2) { /* 结果为 true */ }
    ```

2. **顺序判断 (`>`、`<`、`>=`、`<=`)**
    * `<`：如果 `s1` 在字典中排在 `s2` 之前，返回 `true`。
    * `>`：如果 `s1` 在字典中排在 `s2` 之后，返回 `true`。
    ```cpp
    string a = "apple";
    string b = "banana";
    if (a < b) { /* 结果为 true，因为 'a' < 'b' */ }
    ```

### 4.4 while 循环
while循环是没有初始化和更新部分的for循环，它只有测试条件和循环体：
```
while (test-condition)
    body
```

首先，程序计算圆括号内的测试条件（test-condition）表达式。如果该表达式为true，则执行循环体中的语句。与for循环一样，循环体也由一条语句或两个花括号定义的语句块组成。执行完循环体后，程序返回测试条件，对它进行重新评估。如果该条件为非零，则再次执行循环体。测试和执行将一直进行下去，直到测试条件为false为止。
显然，如果希望循环最终能够结束，**循环体中的代码必须完成某种影响测试条件表达式的操作**。例如，循环可以将测试条件中使用的变量加1或从键盘输入读取一个新值。和for循环一样，while循环也是一种入口条件循环。因此，如果测试条件一开始便为false，则程序将不会执行循环体。

#### 4.4.1 for和while 
在C++中for和while的本质是相同的：
```cpp
for (init-expression; test-expression; update-expression)
{
    statement(s)
}
// 等价于下面的语句
init-expression;
while (test-expression)
{
    statement(s)
    update-expression;
}
// 同理还可以像下面一样等价。
for (; test-expression;)
    body
// 等价于
while (test-expression)
    body
```
for循环需要3个表达式（从技术的角度说，它需要1条后面跟两个表提示：错误的标点符号达式的语句），不过它们可以是空表达式（语句），只有两个分号是必需的。另外，省略for循环中的测试表达式时，测试结果将为true，因此下面的循环将一直运行下去：
```cpp
for ( ; ; )
    body
```
由于for循环和while循环几乎是等效的，因此究竟使用哪一个只是风格上的问题。它们之间存在三个差别:
1. 在for循环中省略了测试条件时，将认为条件为true；
2. 在for循环中，可使用初始化语句声明一个局部变量，但在while循环中不能这样做
3. 如果循环体中包括continue语句，情况将稍有不同.
通常，程序员使用for循环来为循环计数，因为for循环格式允许将所有相关的信息—初始值、终止值和更新计数器的方法—放在同一个地方。在无法预先知道循环将执行的次数时，程序员常使用while循环。[^16]

for循环和while循环都由用括号括起的表达式和后面的循环体（包含一条语句）组成。这条语句可以是语句块，其中包含多条语句。**语句块是由花括号，而不是由缩进定义的**。
当我们只有分号没有花括号进行括起时：**分号就会结束语句**。同理，如果在`while (test-exprssion)`后面紧跟这个一个分号，这个分号就会直接将这个while语句和后面的内容分开。容易造成死循环。

#### 4.4.2 延时循环 
ANSI C和C++苦衷有一个函数可以帮助我们进行延时循环（为了方便我们进行读取计算结果等）。函数名为`clock()`，他会返回层序开始执行后所用的系统时间。但是有两个问题：首先，`clock()`返回时间的单位不一定是秒；其次，该函数的返回类型在某些系统上可能是long，在另一些系统上可能是unsigned long或其他类型。
但是头文件`<ctime>`解决了这个问题：首先，它定义了一个符号常量`CLOCKS_PER_SEC`，该常量等于每秒钟包含的系统时间单位数。因此，将系统时间除以这个值，可以得到秒数。或者将秒数乘以`CLOCK_PER_SEC`，可以得到以系统时间单位为单位的时间。其次，ctime将`clock_t`作为`clock()`返回类型的别名[^17]。这意味着可以将变量声明为`clock_t`类型，编译器将把它转换为long、unsigned int或适合系统的其他类型。
下面给出一个例子：
```cpp
#include <iostream>
#include <ctime>
using namespace std;
int main(){
    cout << "Enter thew delay time, in senconds.";
    float secs;
    cin >> secs;
    clock_t delay = secs * CLOCK_PRE_SEC;

    cout << "starting\a\n:";
    clock_t start = clock();
    while (clock() - start < delay);
    cout << "done \a\n";
    return 0;
}
```

### 4.5 do while 循环
do while循环不同于另外两种循环，它是出口条件（exit condition）循环[^18]。这种循环将首先执行循环体，然后再判定测试表达式，决定是否应
继续执行循环。下面是对应的语法：
```
do 
    body
while (test-expreesion)
```
这里的循环体是一条语句或用括号括起的语句块。
通常，入口条件循环比出口条件循环好，因为入口条件循环在循环开始之前对条件进行检查。
给出个对比例子：
```cpp
int I = 0;
for(; ;){
    I++;
    // do something ···
    if (30 <= I) break;
}
// 等价于
int I = 0；
do {
    I++;
    // do something;
} while (30 > I);
```

### 4.6 基于范围的 for 循环
C++11 新增了一种循环：基于范围的for循环。这简化了一种常见的循环任务：对数组（或容器类，如vector和array）的每个元素执行相同的操作。
这里先给出格式：
```cpp
for (typeName variable : container/range)
    body
```
基于范围的for循环有很多用途：
1. 对数组或容器类中的元素进行相同的操作：
    ```cpp
    double prices[5] = {4.99, 10.99, 6.87, 7.99, 8.49};
    for (double x : prices)
        cout << x << std::endl;
    ```
2. 修改容器中的元素：
   ```cpp
   for (double &x : prices)
        x = x * 0.8;    // 打八折     
   ```
   这里的`&`表示引用，在[这里](#72-引用变量)有介绍。
3. 这里的容器没有规定必须是变量或者是常量，我们甚至可以使用初始化列表：
   ```cpp
    for (int x : {3, 5, 2, 8, 6})
        cout << x << " ";
    cout << '\n';
   ```

### 4.7 循环和文本输入
while循环常用的场景是逐字符的读取文本（用户输入）。
#### 4.7.1 cin输入 
为了让程序知道什么时候停止读取，我们可以设置**哨兵字符**作为停止标记。下面有一个简单的例子：
```cpp
#include <iostream>
int main()
{
    using namespace std;
    char ch;
    int count = 0;          // use basic input
    cout << "Enter characters; enter # to quit:\n";
    cin >> ch;              // get a character
    while (ch != '#')       // test the character
    {
        cout << ch;          // echo the character
        ++count;            // count the character
        cin >> ch;          // get the next character
    }
    cout << endl << count << " characters read\n";
    return 0;
}
```
运行情况：
```
Enter characters; enter # to quit:
see ken run#really fast
seekenrun
9 characters read
```
上面的程序有一个问题：我们无法记录空格和换行符，因为cin会忽略到这两个字符，同时发送给cin的输入被缓冲。这意味着只有在用户按下回车键后，他输入的内容才会被发送给程序。这就是在运行该程序时，可以在#后面输入字符的原因。按下回车键后，整个字符序列将被发送给程序，但程序在遇到#字符后将结束对输入的处理。

#### 4.7.2 使用cin.get(char)输入 
当我们想要进行一个一个字符读取的时候，会使用cin.get()来获取输入。这是cin所属的istream类中的成员函数。成员函数cin.get(ch)读取输入中的下一个字符（即使它是空格），并将其赋给变量ch。这样我们就能一个一个计数我们想要的字符了。

#### 4.7.3 cin.get()补充 
cin.get()一种版本接受两个参数：数组名 + 输入规模。另一种是不接受参数：只能读取一个字符。但是在这里我们有使用了一个新的格式：cin.get(char)。这种一个函数可以实现多个功能的情况叫做**函数重载**，可以直接[跳转](#74-函数重载)进行了解。
不接受任何参数的cin.get()成员函数返回输入中的下一个字符。我们可以这样使用：
```cpp
ch = cin.get();
```
该函数的工作方式与C语言中的`getchar()`相似，将字符编码作为int值返回；而`cin.get(ch)`返回一个对象，而不是读取的字符。同样，可以使用`cout.put()`函数来显示字符。
```cpp
cout.put(ch);
```
该函数的工作方式类似C语言中的`putchar()`，只不过其参数类型为char，而不是int[^21]。






#### 4.7.4 文件尾条件 
对于结束输入的哨兵字符的使用，可能会与我们正常的字符使用相冲突。毕竟像`#`在文件中也会有固定的含义，当我们进行文件读取的时候这个问题就会被放大。当我们的输入来自于文件的时候[^19]，我们可以使用**检测文件尾(EOF)**。
检测到EOF后，cin将两位（eofbit和failbit）[^20]都设置为1。可以通过
成员函数`eof()`来查看`eofbit`是否被设置；如果检测到EOF，则`cin.eof()`将返回bool值true，否则返回false。同样，如果`eofbit`或`failbit`被设置为1，则`fail()`成员函数返回true，否则返回false。注意，`eof()`和`fail()`方法报告最近读取的结果；也就是说，它们在事后报告，而不是预先报告。因此应将`cin.eof()`或`cin.fail()`测试放在读取后。
1. EOF状态的清除
   cin设置EOF后，cin将不读取输入，再次调用cin也不管用。这个时候我们就可以使用`cin.clear()`方法来清除EOF标记，但是在某些系统中这个是无效的。
2. 常见字符输入做法：
   直接给出一个例子：
   ```cpp
   cin.get(ch);
   while (cin.fail() == false) {
    ···
    cin.get(ch);
   }
   ```
   这里`cin.get(ch)`返回的其实是一个cin对象，但是C++中的istream类提供了一个将istream类转换成bool值的函数，这样我们就可以直接将cin用于条件判断了：
   ```cpp
    while (cin);    // while input is successful
   ```
   这样上方的程序就可以简化为：
   ```cpp
   while (cin.get(ch)){
    ···
   }
   ```

为了正确使用`cin.get()`，我们要知道如何让处理EOF。`cin.get()`返回的EOF是一种符号常量，该常量是在头文件iostream中定义的。EOF值必须不同于任何有效的字符值，以便程序不会将EOF与常规字符混淆。通常，**EOF被定义为值−1**。但是EOF不表示输入中的字符，而是指出没有字符。

对于有些系统，char类型是没有符号的，因此char变量可能为 EOF。我们在测试 EOF 的时候就必须使用 int 变量，但是这是如果我们要显示对应的 char 变量就必须将 int 变量转成 char 类型。

总结一下`cin.get(ch)`和`cin.get()`：
| 属性 | cin.get(ch) | ch = cin.get( ) |
| :--- | :--- | :--- |
| **传递输入字符的方式** | 赋给参数 ch | 将函数返回值赋给 ch |
| **用于字符输入时函数的返回值** | istream 对象（执行 bool 转换后为 true） | int 类型的字符编码 |
| **到达 EOF 时函数的返回值** | istream 对象（执行 bool 转换后为 false） | EOF |

对于这两种方式的使用，使用字符参数的版本更符合对象方式，因为其返回值是istream对象。这意味着可以将它们拼接起来：
```cpp
cin.get(ch1).get(ch2)
```
这是可行的，因为 cin.get(ch) 会返回一个 istream 对象。然后就可以通过这个对象调用 get(ch)。

### 4.8 嵌套循环和二维数组
前面第三大节说的是一维数组，这里记录的是二维数组。一维数组本身可以看成是一行数据，二维数组看起来更像一个表格————既有数据行也有数据列。
C++并没有提供二维数组类型，但是我们可以通过使用指针和嵌套循环来创建一个二维数组。

#### 4.8.1 静态二维数组 
创建二维数组的方式是将数组中的每一个元素看成是一个数组。就像下面的例子：
```cpp
int doubleDimensionArray [4][5];
```
这样我们就声明了一个 4 * 5 的二维数组————有四行，每行有5个 int 类型的值。
下面是通用格式：
```cpp
typeName marixName [row][col] = {{···}, {···}, ···};    // initialization
```

#### 4.8.2 动态二维数组 
和创建静态二维数组的思路一样，我们将一个数组的每一元素看成是另一个数组，但是这两层都是动态的数组。
```cpp
int row = 2, col = 3;
int **arr = new int*[rows];
for (int i = 0; i < row;i i++){
    arr[i] = new int [col];
}

for (int i = 0; i < row; i++){
    delete[] arr[i];
}
delete[] arr;
```
这里是使用 new 和二级指针来创建二维数组。上面的程序既包含了二维数组的创建，也包含了对应空间的释放。
1. 使用new来创建二维数组：
   二维数组本质上是一个指针数组，就像前面说的，数组名和指针其实在一些方面是等价的，我们可以使用指针来创建数组，元素对应的数组由于要看成数组，所以我们要使用指针来充当对应的数组元素。从而达到多维的目的。
   ```cpp
   typeName **matrixName = new typeName* [rows];    // 先开一个指针数组的空间
   for (int index = 0; index < rows; index++){
        matrix[index] = new typeName [cols];    // 在让指针数组中的每一个元素指向对应的空间。
   }
   ```
   我们先创建一个指针数组，这个数组由二级指针来表示（因为数组中的元素是指针，所以要用指向指针的指针）。然后我们再用for循环来对每一个元素分配空间，这时就是正经创建数组了。
2. 使用delete来释放内存：
   我们在创建动态二维数组的时候我们一共进行了两次大的分配内存的方式————一是为指针数组开辟内存，二是让指针数组中的元素指向new出来的空间。所以我们释放内存也要进行两次————**先释放元素，在释放指针数组**。
   ```cpp
   for (int index = 0; index < rows; index++){
        delete[] matrixName[index];
   }
   delete[] matrixName;
   ```
   如果先释放了对应的指针数组，就是释放了数组中的指针，**指针指向的内容就会丢失，发生内存泄露**。

以上方式是使用传统的 new 和 二级指针来创建二维数组的方法，我们还可以使用 vector 来创建二维数组（更推荐）。
```cpp
vector<vector<typeName>> matrix(rows, vector<typeName>(cols, initial_value));
```
或者是：
```cpp
vector<vector<typeName>> matrix = {
    {elements},
    {elements},
    {elements},
    ···
}
```
我们甚至可以逐行进行添加（即行数和列数是不固定的）
```cpp
vector<vector<typeName>> matrix;
// 添加一行
vector<typeName> row = {···};
matrix.push_back(row);

// 在循环中添加
for (int i = 0; i < 3; i++) {
    vector<typeName> temp;
    for (int j = 0; j < 4; j++) {
        temp.push_back(i+j);
    }
    matrix.push_back(temp);
}
```

#### 4.8.3 初始化二维数组 
创建二维数组时，可以初始化其所有元素。这项技术建立在一维数组初始化技术的基础之上：提供由逗号分隔的用花括号括起的值列表：
```cpp
int maxtemps[4][5] =   // 2-D array
{
    {96, 100, 87, 101, 105},   // values for maxtemps[0]
    {96, 98, 91, 107, 104},    // values for maxtemps[1]
    {97, 101, 93, 108, 107},   // values for maxtemps[2]
    {98, 103, 95, 109, 108}    // values for maxtemps[3]
};
```
当然，静态数组我们可以进行初始化，我们的动态数组也可以。
```cpp
int **matrix = new int* [rows];
for (int i = 0; i < rows; i++){
    matrix[i] = new int [cols] {0};
}
```
这时我们就创建了一个元素全为0的二维数组。

#### 4.8.4 嵌套循环和使用二维数组 
for循环和while循环都是可以嵌套的：
```cpp
// for 的嵌套
for (int i = 0; i < 10; i++){
    for (int j = 0; j < 10; j++){
        cout << "Now it's (" << i << "," << j << ")." << endl;
    }
}

// while 的嵌套
int i = 0, j = 0
while (i < 10){
    while (j < 10){
        cout << "Now it's (" << i << "," << j << ")." << endl;
        j++;
    }
    i++;
    j = 0;
}
```
上面的两个部分是等效的。都使用了循环嵌套，循环嵌套是遍历对应数组的一个很好的方法，但是需要注意的是，这种遍历的时间复杂度通常是$O(n^2)$
下面给出一个循环嵌套和遍历二维数组的例子。
```cpp
char matrix[5][30] = {
    "YaoYaoSiWuYaoSi",
    "YaoJiuYaoJiuBaYaoLing",
    "Hakimi",
    "GuGuGaGa",
    "What's dog doing"
}
const char* stringName[5] = {
    "BaGeYaLu",
    "BiBiLaBu",
    "Hello~",
    "Man",
    "OUT"
}
for (int i = 0; i < 5; i++){
    int j = 0;
    while (matrix[i][j]){
        cout.put(matrix[i][j]);
        j++;
    }
    cout << endl;
}
```
上方的字符数组换成 string 类也是可以的。
```cpp
const string cities[Cities] =    // array of 5 strings
{
    "Gribble City",
    "Gribbletown",
    "New Gribble",
    "San Gribble",
    "Gribble Vista"
};
```

## 五、分支语句和逻辑运算符
### 5.1 if 语句
当C++程序必须决定是否执行某个操作时，通常使用if语句来实现选择。if有两种格式：`if`和`if else`。如果测试条件为true，则if语句将引导程序执行语句或语句块；如果条件是false，程序将跳过这条语句或语句块。因此，if语句让程序能够决定是否应执行特定的语句。

if的格式和 while 很相似：
```
if (test-expression)
    statement
```
如果test-condition（测试条件）为true，则程序将执行statement（语句），后者既可以是一条语句，也可以是语句块。如果测试条件为false，则程序将跳过语句

和循环测试条件一样，if测试条件也将被强制转换为bool值，因此0将被转换为false，非零为true。整个if语句被视为一条语句。通常情况下，测试条件都是关系表达式。

### 5.2 if else 语句
if语句让程序决定是否执行特定的语句或语句块，而if else语句则让程序决定执行两条语句或语句块中的哪一条，这种语句对于选择其中一种操作很有用。下面是对应的格式：
```
if (test-expression)
    statement1
else
    statement2
```
如果测试条件为true或非零，则程序将执行statement1，跳过statement2；如果测试条件为false或0，则程序将跳过statement1，执行statement2。每条语句都既可以是一条语句，也可以是用大括号括起的语句块，从语法上看，整个if else结构被视为一条语句。

if else中的两种操作都必须是一条语句。如果需要多条语句，需要用大括号将它们括起来，组成一个块语句。
```cpp
// 有问题的语句
if (ch == 'Z')
    zorro++;        // if ends here
    cout << "Another Zorro candidate\n";
else                // wrong
    dull++;
    cout << "Not a Zorro candidate\n";

// 正确的语句
if (ch == 'Z')
{                   // if true block
    zorro++;
    cout << "Another Zorro candidate\n";
}
else
{                   // if false block
    dull++;
    cout << "Not a Zorro candidate\n";
}
```
C++是自由格式语言，因此只要使用大括号将语句括起，对大括号的位置**没有任何限制**。

### 5.3 if-else if-else 结构
if 和 else if语句只能分别处理一个语句块、两个语句块。当我们想进行多个语句的判断时，就要使用`if-else if-else`结构。
实际上，这种结构只是一个if else被包含在另一个if else中。判断顺序是`if->else(if->else(···))`，这样就会一层一层的向下判断。

### 5.4 逻辑表达式
为了进行条件判断，C++ 提供了三种逻辑运算符：OR(`||`), AND(`&&`), NOT(`!`)。
#### 5.4.1 OR运算符
OR运算符(`||`)表示**或运算**。即在一个表达式中，只要有一个是真值，那么整个表达式的值就是 true，否则就是 false。
C++规定，||运算符是个**顺序点**（sequence point）。也是说，先修改左侧的值，再对右侧的值进行判定（C++11的说法是，运算符左边的子表达式先于右边的子表达式）。也就是说我们的表达式是从左向右进行的。
下面是工作原理：
| | expr1 || expr2 的值 | |
| :--- | :--- | :--- |
| | expr1 == true | expr1 == false |
| expr2 == true | true | true |
| expr2 == false | true | false |

**注意**：对于这个`||`运算，我们有一个叫**短路求值**的东西，即**当我们在左侧已经能判断出整个表达式的值，我们便不再执行后面的语句了**：
```cpp
cout << 1 > 0 || 1 / 0;
```
这里的程序会正常运行，因为左面的判断已经决定了表达式的值为 true。所以就不会执行右侧的表达式，也就不会出现`ZeroDivisionError`（除零错误）。

#### 5.4.2 AND运算符
AND 与 OR 类似，但是他为**与运算**。即**所有的表达式都为真，这个表达式才为真**。
下面是运行原理：
| | expr1 && expr2 的值 | |
| :--- | :--- | :--- |
| | **expr1 == true** | **expr1 == false** |
| **expr2 == true** | true | false |
| **expr2 == false** | false | false |

对于 && 运算符，有一个要注意的点：如何表示 min <= number <= max，这种连环的表达式。对于这种情况，C++指出必须使用两个大小比较在进行 && 运算。
```cpp
int number = 15;
cout << (number >= 11 && number <= 19);     // 等价于数学上的 11 <= number <= 19
```
如果我们使用了像数学一样表示的方法，我们的结果就是：
```cpp
int number = 100;
cout << (17 <= number <= 35);     // 输出为 1 ，因为这个时候C++编译器会认为表达式为(17 <= 100) <= 35。前一个表达式的值为 1，而 1 <= 35。所以，使出 1（真值）。
```
与 OR 运算符一样，我们的 AND 运算符也有**短路求值**，当我们左面的表达式中有一个式子为假，这个表达式的值就为 0.

#### 5.4.3 NOT运算符
`!`运算符将它后面的表达式的真值取反。也是说，如果`expression`为`true`，则`!expression`是`false`；如果`expression`为`false`，则!expression是true。更准确地说，如果expression为true或非零，则!expression为false。

#### 5.4.4 运算符注意事项
1. C++中 OR 和 AND 运算符优先级**低于**关系运算符。
    ```cpp
    x > 5 && x < 10;    // 解释为 (x > 5) && (x < 10);
    ```
2. `!`运算符的优先级高于所有的关系运算符和算数运算符，所以当我们要对表达式取反就要用括号。
   ```cpp
   !(x > 5)    // 判断是否 x 大于 5，然后再求反
   !x > 5   // 0 / 1 是否比 5 大
   ```
3. AND 运算符比 OR 运算符优先级更高
   ```cpp
   int year = 1900;
   cout << (year % 4 == 0 && year % 100 != 0 || year % 400 == 0);   // 判断是否为闰年
   ```
   上述程序被解释为`(year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)`。
4. 短路求值：
   C++确保程序从左向右进行计算逻辑表达式，并在知道答案后立刻停止。
5. 其他表示方式
    | 运算符 | 另一种表示方式 |
    | :--- | :--- |
    | && | and |
    | || | or |
    | ! | not |
    这些都是 C++ 的保留字。

### 5.5 字符串库 cctype
C++从C语言继承了一个与字符相关的、非常方便的函数软件包，它可以简化诸如**确定字符是否为大写字母、数字、标点符号等工作**。这些函数都在头文件 `<cctype>` 中。判断字母可以使用 `isalpha()`，判断标点符号可以使用 `ispunct()`。判断数字字符可以使用 `isdigits()`，判断是否为空白可以使用 `isspace()`，当他们判断是对应的对象的时候就会返回 true。否则就返回 false。
** cctype() 中的字符函数 **
| 函数名称 | 返回值 |
| :--- | :--- |
| `isalnum()` | 如果参数是字母数字，即字母或数字，该函数返回 true |
| `isalpha()` | 如果参数是字母，该函数返回 true |
| `iscntrl()` | 如果参数是控制字符[^22]，该函数返回 true |
| `isdigit()` | 如果参数是数字（0~9），该函数返回 true |
| `isgraph()` | 如果参数是除空格之外的打印字符，该函数返回 true |
| `islower()` | 如果参数是小写字母，该函数返回 true |
| `isprint()` | 如果参数是打印字符（包括空格），该函数返回 true |
| `ispunct()` | 如果参数是标点符号，该函数返回 true |
| `isspace()` | 如果参数是标准空白字符，如空格、进纸、换行符、回车、水平制表符或者垂直制表符，该函数返回 true |
| `isupper()` | 如果参数是大写字母，该函数返回 true |
| `isxdigit()` | 如果参数是十六进制数字，即 0~9、a~f 或 A~F，该函数返回 true |
| `tolower()` | 如果参数是大写字符，则返回其小写，否则返回该参数 |
| `toupper()` | 如果参数是小写字符，则返回其大写，否则返回该参数 |

### 5.6 `? :` 运算符
C++ 中提供了一个三元运算符（也是唯一一个三元运算符）`? :`。他的通用格式为：
```cpp
expression1 ? expression2 : expression3
```
如果 expression1 表达式为 true，则表达式为 expression2 的值，否则就是 expression3 的值。
与if else序列相比，条件运算符更简洁，这两种方法之间的区别是，条件运算符生成一个表达式，因此是一个**值**，可以将其赋给变量或将其放到一个更大的表达式中，
虽然看起来很简洁，但是也有着不易理解的风险，当有过于复杂的逻辑时，我们应使用 `if-else` 语句。

### 5.7 switch 语句
switch 语句针对的是那些单一选项但是选项个数很多的条件语句，比如菜单。下面是通用格式：
```cpp
switch (inteegr-expression) {
    case label1 : statement(s)
    case label2 : statement(s)
    ···
    default : statement(s)
}
```
执行到switch语句时，程序将跳到使用integer-expression的值标记的那一行。顾名思义，integer-expression**必须是一个结果为整数值**的表达式。另外，每个标签都**必须是整数常量表达式**。最常见的标签是 int 或 char 常量，也可以是枚举量。如果integer-expression不与任何标签匹配，则程序将跳到标签为default的那一行。Default标签是可选的，如果被省略，而又没有匹配的标签，则程序将跳到switch后面的语句处执行。
**注意**：C++中的case标签只是行标签，而不是选项之间的界线。也是说，程序跳到switch中特定代码行后，将依次执行之后的所有语句，除非有明确的其他指示。程序不会在执行到下一个case处自动停止，要让程序执行完一组特定语句后停止，必须使用break语句。这将导致程序跳到switch后面的语句处执行。
举个例子：
```cpp
(using namespace std)
int order = 0;
cin >> order; 
switch (order) { 
    case 1 : cout << 1 << endl;
    case 2 : cout << 2 << endl;
    case 3 : cout << 3 << endl;
    default : cout << "Error" << endl 
}
```
当我们输入 1 时，程序不会像预期一样分开输出，而是要依次分行输出 `1 2 3 Error`.但是加上 break 就变得不一样了。
```cpp
(using namespace std)
int order = 0;
cin >> order; 
switch (order) { 
    case 1 : cout << 1 << endl;
        break;
    case 2 : cout << 2 << endl;
        break;
    case 3 : cout << 3 << endl;
        break;
    default : cout << "Error" << endl 
}
```
这个时候每一条语句都是分开的，只会执行其中一项。

#### 5.7.1 使用枚举量作为标签
当 switch 语句将 int 值和枚举量标签进行比较时，将枚举量提升为int。另外，在while循环测试条件中，也会将枚举量提升为 int 类型。
```cpp
enum {rad, blue, yellow, green, balck, white, pink}
int order = 0;
cin >> order; 
switch (order) {
    case red : cout << "Red.";
        break;
    ···
    default : cout << "This is a new color.";
}
```
这里的 switch 语句在进行比照的时候是将 enum 改成了 int 类型。
#### switch 和 if-else : 
switch语句和if else语句都允许程序从选项中进行选择。相比之下，if else更通用。
1. if-else 语句可以处理范围问题，但是 switch 语句不可以。
2. switch 语句中的每一个 case 标签都必须是一个单独的值。
3. 当所有的选项都可以使用**整数常量**来表示时。从性能和易读性来讲还是推荐使用 **switch 语句**。

### 5.8 break 和 continue 语句
break和continue语句都使程序能够跳过部分代码。可以在switch语句或任何循环中使用break语句，使程序跳到switch或循环后面的语句处执行。continue语句用于循环中，让程序跳过循环体中余下的代码，并开始新一轮循环。
- break 语句重点在于**停止循环**。
- continue 语句重点在于**跳过本轮循环**。

### 5.9 goto 语句
goto 被称为是**无条件跳转语句**。它允许程序直接跳转到同一函数内的某个特定位置（标签处）执行代码。
**虽然 goto 看起来非常强大但在现代编程中，它的使用是非常受限且不被推荐的。**[^23]
1. 基本语法：
   ```cpp
   goto label_name;
   ···
   label_name:    // 对应标签
        // 对应执行的代码，中间的部分全部跳过
   ```
2. 限制性的用途：
   - **跳出深层循环**，避免一层一层返回浪费时间。
   - **统一的错误处理**。在需要手动释放资源（如内存、文件句柄）时，可以用 goto 跳转到函数末尾的清理区域，避免在每个错误判断处都写重复的释放代码。
3. 限制：
   1. **只能在一个函数中跳转**，不同函数之间不能跳转。
   2. **不能跳过变量初始化**：
      ```cpp
      goto label;
      int x = 0;
      label:
      cout << x;    // ERROR! 变量没有初始化
      ```


## 六、函数
函数的使用的三个要求：
- 提供函数定义
- 提供函数原型
- 调用函数

库函数是已经定义好的函数，标准库中的头文件中提供了对应的原型。直接引用即可，但是自己编写的函数必须完成上述三个方面。
### 6.1 函数定义
按照函数是否有返回值可以将函数分为两类：有返回值的、无返回值的。
#### 6.1.1 void 函数
没有返回值的函数称为 void 函数，通用格式如下：
```cpp
void functionName(parameterList) {
    statement(s);
    return;     // optional
}
```
其中，parameterList指定了传递给函数的参数**类型和数量**。可选的返回语句标记了函数的结尾；否则，函数将在右花括号处结束。
这里的 parameterList 也可以没有，效果如下:
```cpp
void greeting(){
    std::cout << "Hello, world.";
}
```
其中的 () 也可以填入 void。

#### 6.1.2 有返回值的函数
有返回值的函数会生成一个值（一个副本），并将最后的返回值返回给调用函数。通用格式如下
```cpp
typeName functionName(parameterList) {
    statement(s)
    return value;   // value is type cast to type typeName
}
```
对于有返回值的函数，必须使用返回语句，以便将值返回给调用函数。值本身可以是常量、变量，也可以是表达式，只是其结果的类型必须为 typeName 类型或可以被转换为 typeName。对于有返回值的函数，必须使用返回语句，以便将值返回给调用函数。值本身可以是**常量、变量，也可以是表达式**，只是其结果的类型必须为 typeName 类型或可以被转换为 typeName。

函数在碰见 return 后结束，如果函数有多条返回语句，则取第一个 return 语句结束：
```cpp
int bigger(int a, int b) {
    if (a < b) return b;     // a < b 就会在这里停止
    else return a;  
}
```

### 6.2 函数原型和函数调用 
函数原型是一种**函数声明**，它提供了三个信息：
- 函数名
- 返回类型
- 参数列表

1. 函数原型的作用
   原型描述的函数到编译器的接口，告诉编译器这个函数的各个方面的信息，这样有助于提高编译效率和正确率。
2. 原型的语法
   函数原型是一个语句，因此必须是以分号结束。我们有两种方式：
   ```cpp
   double cube(double x);
   double cube(double);
   ```
   这两种方式都是可以的，函数原型可以不提供对应的变量名，有类型列表就够了。原型中的变量名相当于是占位符，甚至可以和函数定义中的变量名不一样。
3. 原型的功能
   原型可以保证编译的正常进行。包括下面几点：
   - 编译器正确处理函数返回值
   - 编译器检查使用的参数数目是否正确
   - 编译器检查使用的参数类型是否正确。如果不正确，则转换为正确的类型[^24]

编译器在编译阶段进行原型化称为**静态类型检查**，他可以看出许多错误。

### 6.3 函数参数和按值传递
C++是**按值传递参数**。就是将数值参数传递给函数，并将其赋值给一个新的变量：
```cpp
double cube(double x) {return x * x * x;}
double volume = cube(side);
```
这样 cube 函数的返回值就被赋值给了 volume 变量[^25]。

用于接收传递值得变量称为**形参**。传递给函数的值称为**实参**。C++标准使用参数来表示实参，使用参量表示形参。所以参数传递是将参数赋给参量。

函数声明的变量是函数**私有**的，这样的变量称为**局部变量**。两个独立的函数分别命名了一个同名的变量，这种变量称为**自动变量**。
###### 总结：无论是按值传递给被调用函数还是返回返回值，传递的或返回的是一个**副本**（引用除外）。两个函数之间的变量即使名字相同也是毫不相干的（引用除外）。

#### 6.3.1 传递多个参数
调用函数时可以传递多个参数，只需要用**逗号**将这些参数隔开即可。
```cpp
functionName(para1, para2, ···);
```
同样的，定义函数时，也是在函数头使用逗号来将参数列表中的参数分开。
```cpp
typeName funcName(type1 para1, type2 para2, ···);
```
**注意**：即使我们的参数类型一样我我们也要将参数分开。
```cpp
void func1(int a, int b);   // accept
void func2(int a, b);   // not accept
```

### 6.4 函数和数组
参数和返回值类型可以是基本类型，也可以是像数组或结构这样复杂的类型。
#### 6.4.1 传递数组
将数组传递给函数只需要将对应的函数名传递即可，格式如下：
```cpp
typeName func(typeName arr[], ···);
```
注意：传递数组时，函数原型必须在对应参数名后添加一个 `[]` 来表示传递数组。这里的方括号指出这个是一个数组，方括号为空表示可以是任意值。但是考究本质，这里函数传递的不是数组，而是**指针**，但是我们依旧可以将这个参数当作数组使用。
```cpp
int array = {1, 2, 3, 4};
int sumOfArray(int arr[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) sum += arr[i];
    return sum;
}
cout << sumOfArray(array, 4);   // 10
```
这里注意一下，下面的例子**不可以的**
```cpp
int sumOfArray(int arr[size]);      // "size" is initialized before
```

#### 6.4.2 处理数组
C++是将数组名视为指针的。C++将数组名解释为数组第一个元素的地址：
```cpp
std::cout << array == &array[0];    // true
```
在函数原型中数组名也可以使用指针：
```cpp
int sumOfArray(int *arr, int length);
int sumOfArray(int arr[], int length); 
```
上述两个原型是等效的，在C++中，**当（且仅当）用于函数头或函数原型中，typeName *arr和typeName arr[]的含义才是相同的**。它们都意味着arr是一个对应类型的指针。然而，数组表示法（typeName arr[]）提醒用户，arr不仅指向对应类型，还指向类型数组的第一个元素。
```cpp
array[i] == *(array + i);   // values in teo notations
&array[i] == array + i;     // addresses in two notations
```

传递常规变量时，函数将使用该变量的拷贝；但传递数组时，函数将使用原来的数组。这时的按值传递就不是传递的内容了，而是一个地址。为什么要这么做？将数组地址作为参数可以节省复制整个数组所需的时间和内存。如果数组很大，则使用拷贝的系统开销将非常大。既消耗空间，又消耗时间。**总之，接受
数组名参数的函数访问的是原始数组，而不是其副本，当在函数中对数组进行修改时，原调用函数中的数组也会跟着改变。**
如果不想修改原数组，我们可以添加 const 修饰符。
```cpp
void show_func(const int array[], int size) {
    for (int i = 0; i < size; i++) {
        std::cout << array[i];
    }
}
```

#### 6.4.3 使用数组区间的函数
一般的处理数组的函数需要两个参数：
1. 数组名
2. 数组长度

但是还可以使用另一种方法：**指定元素区间**。这可以通过传递两个指针来完成：一个指针标识数组的开头，另一个指针标识数组的尾部。对于数组而言，标识数组结尾的参数将是指向最后一个元素后面的指针。这在 STL 中叫做**超尾**。直接看一个例子：
```cpp
#include <iostream>
using namespace std;
void showArray(const int *, const int *);
int main() {
    const int scale = 4;
    int array[scale] = {1, 2, 3, 4};
    showArray(array, array+scale);
    return 0;
}
void showArray(const int *begin, const int *end) {
    const int *ptr;
    for (ptr = begin; ptr != end; ptr++) {
        cout << *ptr << endl;
    }
}
```
这里就是传递了两个常量指针：begin 和 end。分别作为范围的起始和终止。，再用常量指针遍历数组。但是需要注意，begin 和 end 不能传递反，否则会一直遍历。
通常，将指针作为函数参数来传递时，可以使用指向const的指针来保护数据。只要只有一层间接关系，就可以使用这种技术。但如果它们是指针或指向指针的指针，则不能使用const。

#### 6.4.5 函数和二维数组
将二维数组传递给函数时候，有两种格式：
```cpp
typeName func1(typeName (*arr)[size], int size);
typeName func2(typeName arr[][size], int size);
```
第一种是声明有 size（常量）个对应类型的指针。第二个和第一个是同理的，**注意，第二种情况后面的[size]是不允许删除的。**

上面两种方法都是固定了列数，安东尼是不限制行数，要使用对应的数组，可以将参数名当对应数组名使用。使用的原理如下：
```cpp
matrix[r][c] == *((matrix + r) + c);
```
下面是各种数组使用的辨析：
```cpp
matrix                     // pointer to first row of an array of 4 int
matrix + r                 // pointer to row r (an array of 4 int)
*(matrix + r)              // row r (an array of 4 int, hence the name of an array,
                           // thus a pointer to the first int in the row, i.e., matrix[r]

*(matrix + r) + c          // pointer int number c in row r, i.e., matrix[r] + c
*(*(matrix + r) + c)        // value of int number c in row r, i.e. matrix[r][c]
```

### 6.5 函数和C-风格字符串
由于 C-风格字符串本身就是一种数组，所以我们使用的方法和使用数组的方法一样。
#### 6.5.1 传递 C-风格字符串
将 C风格字符串传递给数组，测表示字符串的方式有三种：
- char数组
- 字符串常量（字符串字面值）
- char指针（指向字符串）

将字符串作为参数传递，实际上传递的是字符串第一个字符的地址。因此我们可以将对应参数设置成 char*类型。但是与常规数组有区别的地方是：字符串有内置的结束字符。因此不用将字符串长度传进去。当然如果只是进行**只读**，我们还可以加上 const 限定符。

#### 6.5.2 返回 C-风格字符串的数组 
同上方返回数组的方式一样，返回字符串也是返回字符串首元素的地址。
```cpp
char * returnStr(char ch, int n) {
    char *str = new char[n + 1];
    str[n] = '\0';
    while (n-- > 0) {
        str[n] = ch;
    }
    return str;
}
```
上方的程序是创建一个全是相同字符 ch 的字符串的函数。这里用 new 运算符分配的空间位于**堆**，不会随着函数结束而消亡，函数返回的是对应的首元素的地址，所以就相当于是返回了一个字符串。当我们不再需要的时候我们就可以使用 delete 运算符释放对应的内存（记得带上 `[]`）

### 6.6 函数与结构
结构虽然也是复杂的结构，但是传递的时候我们不需要像传递数组那样复杂。它更接近于传递简单类型变量。同样的，返回结构也和简单变量差不多。这样按值传递虽然简单，但是有时间和空间消耗太大的缺点。这个时候我们可以使用[引用传递](#722-引用用做函数参数)

#### 6.6.1 传递和返回结构
当结构较小的时候我们就可以按值传递结构，但是对于较大的结构还是要使用**引用传递**来减少开销。在默认情况下，C++函数按值传递参数，所以正常情况下我们还是传递了一个副本 / 返回一个副本。

#### 6.6.2 传递结构的地址
为了节省空间和时间的开支，我们可以传递结构的地址：
- 调用函数时，将结构地址（&variable）而不是本身进行传递。
- 形参声明为指向结构的指针，也是用 const 限定符进行修饰。
- 由于形参时指针而不是结构，访问成员时要使用间接成员运算符。
- 由于传递的是指针，所以谨慎修改对应的内容。

### 6.7 函数和string + array
对于这两种类型，直接像对待简单类型一样就可以。string类使用要有 <string> 头文件，array类使用要有 <array> 头文件。

### 6.8 函数指针
与普通的数组项相似，函数也是有地址的。有了地址，我们就可以使用对应的指针来指向对应的函数了。
#### 6.8.1 函数指针三要素
1. 获取函数的地址
   获取函数的地址很简单：只要使用函数名（后面不跟参数）即可。要将函数作为参数进行传递，必须传递函数名。一定要区分传递的是函数的地址还是函数的返回值。
   ```cpp
   process(think);      // 传递的是函数地址
   thought(think());    // 传递的是函数返回值
   ```
   这样 process 函数就可以在内部调用 think() 函数了。

2. 声明函数指针
   声明指向函数的指针时和声明其他指针一样，也**必须指定指针指向的类型**。声明必须指定函数的返回类型和函数的特征标（参数列表）：
   ```cpp
   double cube(int a);  // 声明了一个函数
   double (*calculate)(int);    // 声明了一个函数指针
   ```
   这里的 calculate 就是函数指针。他指向了一个接受 int 类型参数，并返回一个 double 类型变量的函数。
   **注意**：下面两个不是一个意思，由于 `*` 的优先级低于 `()` ，所以我们必须要用 () 将函数名和 * 括起来，否则就成为返回指针的函数了：
   ```cpp
   double cube(int a);
   double (*calculate)(int);    // 函数指针
   double *calculate(int);      // 返回指针
   ```
   函数指针声明完成后就可以进行地址赋值了，**注意对应的返回值和参数列表要相同：
   ```cpp
   double (*ptrf)(int);
   double func(int);
   ptrf = func;     // 这里的函数名就是对应的地址
   ```
3. 通过指针调用函数
   调用对应函数和解对应函数的地址等价，所以直接使用 `*ptrf` 即可。这个时候他和对应的函数名是一样的。
   ```cpp
   double func(int);
   double (*ptrf)(int);
   ptrf = func;
   double number = (*ptrf)(1);      // 正常调用 func
   ```
   这种写法是规范的，但是 C++ 也支持将函数指针直接当作对应函数名使用，还是推荐使用前一种更清晰：
   ```cpp
   double func(int);
   double (*ptrf)(int);
   ptrf = func;
   double number = ptrf(1);      // 正常调用 func
   ```

#### 6.8.2 函数指针数组
对于这样的函数声明：
```cpp
const double * f1(const double ar[], int n);
const double * f2(const double [], int);
const double * f3(const double *, int);
// 这三种都是合法的函数声明，且三者是等效的。
```
我们可以使用函数指针来指向：
```cpp
const double *(*ptrf)(const double *, int);     // 这一个声明就可以指向所有
```
我们还可以创建一个函数指针数组，来统一对上面三个进行指向：
```cpp
const double *(*ptrf[3])(const double *, int) = {f1, f2, f3};
```
这样就声明了一个函数指针数组。**注意，函数指针数组中的 `[]`，要在括号里面**，由于 **`[]` 优先级高于 `*`**，所以顺序是这样的：
```
确定函数名 ->  [] 表示是数组 -> *ptr[size] 表示指针数组 -> 其余部分确定所指向的函数类型 -> 声明函数指针
```
来看一个辨析：
```cpp
*ptrf[3];       // ptrf是一个指针数组
(*ptrf)[3];     // ptrf是一个指针
```
由于优先级问题，ptrf会优先与 `[]` 结合。第一个先声明了数组，后确定了元素类型——指针，第二个是先确定类型，再确定指向的内容 —— 一个 3 元素的数组。

这里的声明是不能用 auto 的[^26]。这是因为**自动类型推断只能用于单值初始化，而不能用于初始化列表。**但是声明了第一个对应的数组，我们就可以使用 auto 来对别的进行声明[^27]。

如果要调用函数可以直接像指针解引用，再使用函数调用运算符 `()` 进行调用：
```cpp
double x = *ptrf[0](arr, 3);    // 成功调用
```
当然我们还可以将函数数组名地址赋值给新的指针：
```cpp
auto ptrfunc = &ptrf;   // ptrfunc 为指向指针的指针
```

对于上面的**复杂的类型名称，我们可以使用 typedef 或者是 using 来对程序进行简化**：
```cpp
typedef const double *(*ptrf)(const double *, int);     // 现在 ptrf 就是一个新的类型名称了
ptrf p1 = f1;       // vaild 

using ptrf = const double *(*)(const double *, int);    // 现在 ptrf 也是一个新的类型，格式： using name = typeName;
ptrf p2 = f2;       // vaild
```     
使用这两个可以简化代码。减少出错。

### 6.9 递归
自己调用自己，就叫做**递归**。
#### 6.8.1 包含一个递归调用的递归 
如果递归函数调用自己，则被调用的函数也将调用自己，这将无限循环下去，除非代码中包含终止调用链的内容。通常的方法将递归调用放在if语句中。格式如下：
```cpp
typeName recure_func(argumentList) {
    statement1(s);
    if (test) {
        ···
        recure_func(arguments);
    }
    statement2(s);
}
```
由于递归调用的顺序性，statement1 会按照正常函数调用的方式执行，而statement2 由于在递归调用的后面，所以将会在递归执行完成后在执行（方向相反）。

#### 6.9.2 包含多个递归调用的递归
这种递归一般称为是**分治法**，由于一般是分成两种情况，所以要进行多次递归调用。如果要求的递归层次很多，这种递归方式将是一种糟糕的选择；然而，如果递归层次较少，这将是一种精致而简单的选择。

## 七、函数进阶
### 7.1 内联函数
**内联函数是为了提高运行速度创建的**，两者在编写方式没有明显的区别。
函数的执行过程在计算机眼中是一个一个的指令，他们有对应的内存地址，每一次调用计算机会记住调用函数的起始地址，再前往对应的函数地址执行函数指令，执行完毕会返回值（如有），再返回调用函数。这就意味着每一调用都会产生时间上的开销（递归调用的痛点也是在这里）。**内联函数是将对应函数编码直接替换对应的指令，这样就不用“来回跳跃”了，但是需要更多的空间开销**。换句话说，就是使用空间来换时间。
对于一些简单的函数（运行时间很短），建议使用内联函数，但是当执行时间远超调用时间，还是使用常规函数更好。

使用或声明函数为内联函数要在**声明或定义之前加上关键字 `inline`**。通常是省略原型，将整个定义（函数头 + 函数代码）放在提供原型的地方：
```cpp
inline typeName funcName(arguments) {body}  // inline function
```
一般将简短的函数作为内联函数，可以将整个定义放在一行，当函数定义占用了多行，就不太适合作为内联函数。

inline 与 C 语言中的**宏**很相像，但是有所不同。C 语言时使用预处理器语句 `#define` 来提供宏（也是内联代码的原始实现），这个过程不是通过参数传递实现的，而是通过文本替换来实现，所以会有一些奇怪的问题：
```cpp
#define SQUARE(X) X*X
a = SQUARE(5.0); // is replaced by a = 5.0*5.0;
b = SQUARE(4.5 + 7.5); // is replaced by b = 4.5 + 7.5 * 4.5 + 7.5;
d = SQUARE(c++); // is replaced by d = c++*c++;
```
由于是直接进行文本替换，所以不会考虑正确与否的问题。我们可以使用括号进行改进：
```cpp
#define SQUARE(X) ((X) * (X))
```
鉴于此，还是尽量使用 C++ 中的内联函数。

### 7.2 引用变量
**引用**也是C++的一种复合类型。**引用时已经定义的变量的别名**。但引用变量的主要用途是用作函数的形参。通过将引用变量用作参数，函数将使用原始数据，而不是其副本。这样除指针之外，引用也为函数处理大型结构提供了一种非常方便的途径。

#### 7.2.1 创建引用 
引用是通过 `&` 来进行声明的：
```cpp
typeName variable1;
typeName & variable2 = variable1;   // variable2 is equal to variable2
```
引用的变量和原变量是等价的，他们指向相同的值和内存单元。引用与指针很像，但是**声明引用时必须将其初始化，而不是先声明再进行赋值**。一旦与某个变量关联，就会一直指向被引用的对象。

**引用不能通过赋值来进行改变所引用的对象，赋值会改变引用对象的值**。

#### 7.2.2 引用用做函数参数 
引用经常被用作函数参数，使得函数中的变量名成为调用程序中的变量的别名。这种传递参数的方法称为按引用传递。按引用传递允许被调用的函数能够访问调用函数中的变量（因为传递的其实是原变量）。
**函数的引用参数被初始化为函数调用传递的实参。**
不对信息进行修改，同时又想使用引用则应该使用**常量引用**：
```cpp
double function(const double &variable);
```
普通的函数还是使用按值传递即可，对于参数规模较大的函数可以使用引用传递。
引用的必须是一个已经明确定义的值（左值），不能是一个临时变量（右值）。

#### 7.2.3 临时变量 
如果实参与引用参数不匹配，C++将生成临时变量。当前，仅当参数为const引用时，C++才允许这样做.
如果引用参数是const，则编译器将在下面两种情况下生成临时变量：
- 实参类型正确，但不是左值。
- 实参的类型不正确，但是可以转换成正确的类型。

**左值**：对应内存中**有确定存储地址的对象**。因为它有“身份”，所以你可以用 & 取地址符找到它。通常是变量名。包括变量、数组元素、结构成员、引用和解除引用的指针。
**右值**：**临时的数据**，通常没有确定的内存位置（或者说它们即将销毁）。你不能对右值取地址。包括字面常量（用引号括起的字符串除外）和包含多项的表达式。

左值就像有一个有房子的人，右值就是一个流浪汉：
```cpp
int a = 5;       // a 是左值，5 是右值
int b = a + 1;   // b 是左值，(a + 1) 是右值
// 5 = a;        // 错误！右值不能在等号左边（不能给 5 赋值）
// &5;           // 错误！不能对右值取地址
```
左值是持久的（有名字，有地址）；右值是短暂的（临时产生，用完即丢）。

如果接受引用参数的函数的意图是修改作为参数传递的变量，则创建临时变量将阻止这种意图的实现。C++标准禁止创建临时变量。以便避免这种情况发生[^28]。但是，如果声明将引用指定为const，C++将在必要时生成临时变量。实际上，对于形参为const引用的C++函数，如果实参不匹配，则其行为类似于按值传递，为确保原始数据不被修改，将使用临时变量来存储值。

将引用参数声明为常量数据的引用的理由有三个：
- 使用const可以避免无意中修改数据的编程错误
- 使用const使函数能够处理const和非const实参，否则将只能接受非const数据
- 使用const引用使函数能够正确生成并使用临时变量。

C++ 以前只能进行左值引用，现在可以进行**右值引用**了，这种引用指向右值，用 `&&` 来声明：
```cpp
double && rref = std::sqrt(36.00);
double && jref = 2.0 * j + 18.5;
```
右值引用主要集中在实现[移动语义](#移动语义)上。<a id="移动语义"></a>之前的常规引用现在叫做**左值引用**。

#### 7.2.4 引用结构 
引用主要是为了用于结构和类(大型变量)，而不是基本的内置类型。使用结构引用参数的方式与使用基本变量引用相同，只需在声明结构参数时使用引用运算符&即可:
```cpp
struct free_throws {
    std::string name;
    int made;
    int attempts;
    float percent;
};
void set_pc(free_throws & ft);      // use a reference to a structure
void set_pc(const free_throws & ft);      // use a const reference to a structure
```

#### 7.2.5 返回引用 
返回引用是为了避免传统按值返回的拷贝过程，按值返回是将 return 后面表达式的值评估出来，创建一个临时变量，再将这个临时变量赋值给要赋值的对象。直接使用引用传递会使得效率变得更高。因为返回引用的函数实际上返回的是被引用变量的别名。

但是需要注意，我们要避免返回函数终止时不再存在的内存单元引用（返回指针也是同样的道理）。解决方法有两种：
1. 返回传递过来的参数的引用（参数是引用传递）。
2. 使用 new 来分配新的内存空间。因为 new 分配的空间是在**堆**中的，而函数的临时变量是创建在**栈**中的，new 分配的空间不会因函数结束而释放。

常规（非引用）返回类型是右值——不能通过地址访问的值。这种表达式可出现在赋值语句的右边，但不能出现在左边。其他右值包括字面值（如10.0）和表达式（如x + y）。显然，获取字面值（如10.0）的地址没有意义，这种返回值位于临时内存单元中，运行到下一条语句时，它们可能不再存在。

如果我们不想修改返回的引用，我们还可以再函数声明时添加 const 来避免修改。同时可以使得代码变得更加清晰。

#### 7.2.6 引用参数 
使用引用参数的主要原因有两个:
- 为了能够修改调用函数中的数据对象
- 通过传递引用而不是整个数据对象，可以提高程序的运行速度。

对于使用传递的值但是不进行修改的函数：
- 数据对象较小（如内置结构或小型结构）：**按值传递**
- 数据对象是数组：**使用 const 指针**，并且这是唯一的选择
- 数据对象较大的结构：**使用 const 指针或 const 引用**。
- 数据对象是类对象：**使用 const 引用**，类的设计建议使用引用，并且传递类对象参数的标准方式就是**按引用传递**。

对于修改调用函数中数据的函数：
- 数据对象为内置类型：**使用指针**。
- 数据对象为数组：**只能使用指针**
- 数据对象为结构：**使用引用或指针**
- 数据对象为类：**使用引用**。

### 7.3 默认参数
默认参数指的是当函数调用中省略了实参时自动使用的一个值。当对应参数传进来对应实参时，该参数会将原来的默认参数覆盖。
设置默认值必须通过函数原型，语法如下：
```cpp
type func(type name=default_name);
```
对于带参数列表的函数，必须从右向左添加默认值。也就是说默认值都必须**滞后**。

实参按照从左向右的顺序依次进行赋值给形参，不允许跳过任何参数。
使用默认参数的函数可以在原型中声明，后面的定义可以省略对应的默认值。

### 7.4 函数重载
函数重载又称**函数多态**。允许函数可以有多种形式。可以有多个同名的函数。他们完成相同的工作但是使用不同的参数列表。
**函数重载的关键时函数的参数列表，又称函数特征标**，如果两个函数的参数数目和类型相同，同时参数的排列顺序也相同，则它们的特征标相同，而变量名是无关紧要的。
C++允许定义名称相同的函数，条件是它们的**特征标不同**。如果参数数目或参数类型不同，则特征标也不同。**重载对参数列表的要求非常严格，但是对返回值的要求不是很严**

使用函数重载时要尽量避免编写重复的函数参数列表，类型和对应类型的引用由于在传参形式上没有区别，可能会导致编译器不能识别使用哪一个，**所以要尽量避免同时使用对应的类型和对应引用**。

匹配函数时，不会区分const和非const变量。编译器将根据实参是否为const来决定使用哪个原型：
```cpp
void dribble(char* bits);
void dribble(const char * bits);    // overload.

const char p1[20] = "Hello, world.";
char p2[10] = "nihao";
dribble(p1);    // dribble(const char *)
dribble(p2);    // dribble(char *)
```
函数重载看重的是特征标，而不是由返回值来决定的，**只有返回值不同的函数不是重载，会导致相冲突**：必须是特征标有不同的地方。
```cpp
int gronk(int n, float m);
double gronk(int n, float m);       // 矛盾
```

#### 7.4.1 重载引用参数 
1. 左值引用参数与可修改的左值参数相匹配。
2. const 左值引用参数和可修改的左值参数、const 左值参数和右值参数相匹配。
3. 右值引用与右值相匹配。

#### 7.4.2 使用重载的时机 
仅当函数基本上执行相同的任务，但使用不同形式的数据时，才应采用函数重载。有时，我们甚至可以使用默认值来代替函数重载（这是甚至会更简单）。但是如果要使用不同类型的参数，还是要用函数重载。

#### 7.4.3 名称修饰 
C++ 是通过**名称修饰或叫名称矫正**来进行追踪重载函数的，他会根据函数原型中指定的形参类型对每一个函数名进行加密。
1. 为什么需要名称修饰：
   C 语言中的函数名是直接映射到汇编符号的。比如`void foo()`，汇编里叫做`_foo`
   但是C++允许函数重载，如果只按照名字映射，连接器不能区别这些函数，编译器会将函数参数类型也编码到对应的符号名中。

2. 名称拆解（Windows）
   ```cpp
   namespace MySpace {
       void func(int a, double b);
   }
   ```
   经过修饰，函数名会变成 `_ZN7MySpace4funcEid`。
   这里的对应含义如下：
   - `_Z`：全局前缀，表示这是一个C++修饰后的名称。
   - `N`：表示是一个嵌套名称（在命名空间中或类的内部）。
   - `7MySpace`：长度为 7 的字符串`MySpace`。
   - `4func`：长度为 4 的字符串 `func`。
   - `E`：嵌套名称的结束。
   - `i`：代表第一个参数为 `int` 。
   - `d`：代表第二个参数为 `double`。

3. extern "C"
   C 和 C++ 由于重载的问题，有时候不能相互调用，我们使用 `extern "C"` 告诉编译器：**“请按照 C 语言的方式处理，不要进行名称修饰”**。
   ```cpp
   extern "C" {
       void my_c_function(int x);   // 连接名依然是 my_c_function
   }
   ```
   **注意：被 `extern "C"` 修饰的函数不能被重载，一旦去掉了修饰，同名函数在符号表中就会冲突**。
   同理，还存在着 `extern "C++"` 告诉编译器：**按照C++规则对函数名称进行修饰**。

### 7.5 函数模板
**函数模板**是通用的函数描述，也就是说，它们使用泛型来定义函数，其中的泛型可用具体的类型（如int或double）替换。通过将类型作为参数传递给模板，可使编译器生成该类型的函数。由于模板允许以泛型（而不是具体类型）的方式编写程序，因此有时也被称为通用编程。由于类型是用参数表示的，因此模板特性有时也被称为**参数化类型**（parameterizedtypes）。
直接看一个实际的例子————交换数据：
```cpp
template <typename AnyType>
void Swap(AnyType &a, AnyType &b) {
    AnyType temp;
    temp = a;
    a = b;
    b = temp;
}
```
关键字 `template` 和 `typename`是必须的。其中的 typename 可以被 class 替换。另外必须使用 `<>`。 类型名可以任意选择，一般选择 `T`。但是**同名的类型名表示一种类型**。
使用时候只需向正常使用函数那样使用即可，编译器会自动将函数生成。

#### 7.5.1 重载的模板 
需要多个对不同类型使用同一种算法的函数时，可使用模板.重载的要求和常规函数重载一样，特征标不同即可。需要注意：**并非所偶的模板参数都必须是泛型**。
```cpp
template <typename T>
void Swap(T &a, T &b);      // 常规的函数模板

template <typename T>
void Swap(T *a, T *b, int c);   // 重载的函数模板
```

#### 7.5.2 模板的局限性 
```cpp
template <typename T>
void f(T a, T b) {
    ···
}
```
模板并不能完成所有的工作。对于一些运算或定义，直接使用模板会报错的。
```cpp
a = b;  // 当 a 和 b 都是数组时就会有问题
if (a > b);     // 当 a 和 b 是结构时会有问题      
```
总之，模板函数使用局限性的，有两种解决方案：
1. 使用**运算符重载**。
2. 提供具体化的定义。

#### 7.5.3 显式具体化
**显式具体化**可以解决模板重载不能解决的问题。它包含了所需的代码，当编译器找到与函数调用匹配的具体化定义时，将使用该定义，而不再寻找模板。
1. 具体化（ISO/ANSI C++）
   - 对于给定的函数名，可以有非模板函数、函数模板和显式具体化哦模板函数和对应的重载版本。
   - 显式具体化的原型和定义应该用 `template<>` 打头，并通过名称来指出对应的类型。
   - **具体化的优先级高于常规模板，非模板函数优先级高于具体化和常规模板**。
   
   ```cpp
   struct job {
       char name[40];
       double salaty;
       int floor;
   };
   // non template function prototype
   void Swap(job &, job &);
   // template prototype
   template <typename T>
   void Swap(T &a, T &b);
   // explicit specialization for the job type
   template <> void Swap<job>(job &, job &);
   ```
   如果有多个原型，优先级：常规函数 > 显式具体化函数模板 > 常规模板。
2. 实例化和具体化 
   在代码中包含函数模板本身并不会生成函数定义，它只是一个用于生成函数定义的方案。编译器使用模板为特定类型生成函数定义时，得到的是模板实例。当正常使用模板的时候进行的是**隐式实例化**。我们也可以进行**显式实例化**，只需要在函数名的后面加上`<>`即可：
   ```cpp
   template void Swap<int>(int, int);   // explicit instantiation
   ```
   先声明所需的种类，用 <> 来指定类型，最后在声明前加上关键字 template
   与实例化不同，显式具体化有两种形式：
   ```cpp
   template <> void Swap<int>(int &, int &);
   template <> void Swap(int &, int &);     // 两者等价，都是显式具体化
   ```
   显式具体化的原型后面必须有自己的函数定义，声明在关键字 template 后面包含着 <> ,但是显式实例化没有。**在同一个文件中使用同一种类型的显式实例化和显示具体化将会出错。

   我们也可以直接在使用时进行显式实例化：
   ```cpp
   template <typename T>
   T add(T a, T b) {
        return a + b;
   }
   ···
   int m = 6;
   double x = 10.2;
   cout << add<double>(x, m) << endl;   // 显式实例化
   ```
   这里的函数如果不进行实力化会报错，因为烈性不匹配，但是进行实例化后，函数会将 m 强制转换成 double 类型。这时候函数就匹配了。但是这种**不能用做引用**，因为实例化后函数还是只能引用对应的类型。

   **隐式实例化、显式实例化和显式具体化统称为具体化**。都是使用具体类型的函数定义，不是通用描述。区别在于第一个是编译器自己进行的，使用起来和常规函数没有区别，第二个和第三个需要自己声明，第二个 template 后面没有 <> ，但是第三个有，第二个函数名后面会紧跟一个 <> 但是第三个可以不跟，只需明确写出对应的特征标即可。**在声明中使用前缀 template 和 template <> 是区分显式实例化和显式具体化的标准**：
   ```cpp
    ...
    template <class T>
    void Swap (T &, T &);  // template prototype

    template <> void Swap<job>(job &, job &);  // explicit specialization for job
    int main(void)
    {
        template void Swap<char>(char &, char &); // explicit instantiation for char
        short a, b;
        ...
        Swap(a, b);    // implicit template instantiation for short
        job n, m;
        ...
        Swap(n, m);    // use explicit specialization for job
        char g, h;
        ...
        Swap(g, h);    // use explicit template instantiation for char
        ...
    }
   ```

#### 7.5.4 选择函数版本 
对于函数重载、函数模板、函数模板的重载，C++使用**重载解析**来判断使用的版本是哪一个。
1. 创建候选函数列表，包含被调用函数相同名称的函数和模板函数。
2. 使用候选函数列表创建可行函数列表，这些函数的参数数目是正确的，还有一个隐式转换序列，包含实参类型和与相应类型的实参类型完全匹配的情况。
3. 确定有无最佳的函数，有就调用，没有就报错。
   最佳到最差如下：
   1. 完全匹配，但是常规函数优先于模板
   2. 提升转换，char -> int -> double 
   3. 标准转换，int -> char， long -> double
   4. 用户定义的转换，类声明中定义的转换

##### 7.5.4.1 完全匹配和最佳匹配 
进行完全匹配时，C++ 允许某些“无关紧要的转换”：
| 从实参 | 到形参 |
| :--- | :--- |
| Type | Type & |
| Type & | Type |
| Type [ ] | * Type |
| Type (argument-list) | Type (*) (argument-list) |
| Type | const Type |
| Type | volatile Type |
| Type * | const Type * |
| Type * | volatile Type * |

Type 表示任意的类型，也可以是 & 类型，包含了一般变量到 const 变量和 volatile 变量[^29]的转化。Type(argument-list) 表示用作实参的函数名和用作形参的函数指针是要返回类型和参数列表相同就是匹配的。
**当有多个匹配的类型，编译就无法完成重载解析的过程，没有最佳的可行函数，编译器会返回一条错误信息（如 ambiguous 二义性）。**
对于 const ，即使两个函数都完全匹配，也是可以进行重载解析的。指向非 const 的指针或引用优先于
指向 const 的指针或者引用。**但是这只针对于指针和引用**，一般的实例就不行了。
```cpp
void recycle(int);  
void recycle(const int);    // 出现问题，函数重载解析不成功，有二义性错误

void recycle(int &);    
void recycle(const int &);  // 没问题，因为非 const 引用先于 const 引用。
```

两个完全匹配的函数都是模板函数，**较为具体[^30]的模板函数优先**。换句话说，**显式具体化优先于模板隐式生成的具体化**。
```cpp
struct blot {int a; char b[10];};
template <class Type> void recycle (Type t); // template
template <> void recycle<blot> (blot & t);   // specialization for blot
...
blot ink = {25, "spots"};
...
recycle(ink);  // use specialization
```

简而言之，重载解析僵毁寻找最匹配的函数，如果只存在一个这样的函数，就会选择它，如果存在多个函数，就会按照优先级进行排列：非模板函数（常规函数）-> 模板函数更具体的 -> 报错（二义性，函数重载解析失败）。

##### 7.5.4.2 自己选择函数 
有些情况我们也可以自行进行选择：
```cpp
template <typename T>
T lesser(T a, T b) {
    return a < b ? a : b;
}

int lesser(int a, int b) {
    a = a < 0 ? -a : a;
    b = b < 0 ? -b : b;
    return a < b ? a : b;
}

int m = 20, n = -30;
double x = 15.5, y = 25.9;

cout << lesser(m, n);   // 第二个
cout << lesser(x, y);   // 第一个
cout << lesser<>(m, n);     // 第一个
cout << lesser<int>(x, y);      // 第一个
```
很明显，对于最后两个，一个是显式实例化，必须要有模板，另一个也是显式实例化，虽然转换成了 int 类型，但是是在对应模板下的强制转换。

##### 7.5.4.3 多个函数参数的模板 
这种情况下，我们要考虑很多种情况，我们要格外地注意对应类型的重载解析问题，避免出现二义性还有没有匹配项的情况。

#### 7.5.5 关键字 deltype
关键字 deltype 是C++11新增的关键字，它可以自动推断对应变量的类型，并将该类型定位为对应变量的类型：
```cpp
int x = 0;
deltype(x) y = 0;   // legal, 'y' is type of int.
```
deltype 关键字提供的参数可以是表达式：
```cpp
int x = 0, y = 1;
deltype(x+y) z = 2;     // 这时 z 为 int 类型。
```
deltype的统一格式如下：
```cpp
deltype(expression) var;
```
1. 如果 expression 是没有被括号括起来的标识符，则 var 的类型 expression 对应的类型相同，包括 const 限定符。
2. 如果 ecpression 是一个函数调用，则 var 类型与函数返回值相同。
3. 如果 expression 是一个左值，则 var 指向其类型的引用
   ```cpp
   double x = 0.0;
   deltype((x)) y = x;      // 这个时候 y 是 double 类型的引用
   ```
4. 如果以上情况都不满足，则 var 与 expression 的类型相同。

对于经常使用的、但是事先不知道的类型的情况，我们可以混合使用 typedef 和 deltype。

#### 7.5.6 后置返回类型 
```cpp
auto h(int x, float y) -> double;   // 将返回类型后置
```
`->double` 称为后置返回类型。`auto` 是一个占位符。表示后置返回类型是提供的类型。与deltype关键字可以为一些模板函数提供更灵活的定义：
```cpp
template <typename T1, typename T2> 
auto func(T1 a, T2 b) -> deltype(a + b) {
    ···
    return x + y;
} 
```
这样就可以解决预先不知道表达式类型的问题。

## 八、内存模型和名称空间
### 8.1 单独编译
C++ 鼓励将组件放在独立的文件中，既可以单独编译，又可以连接成一个可执行的文件。
一般来讲，程序分为 3 个部分：
- 头文件：包含结构声明和使用这些结构的函数的原型
- 源代码文件1：包含结构有关的函数的代码
- 源代码文件2：包含调用与结构相关的函数的代码

一个文件（头文件）包含了用户定义类型的定义；另一个文件包含操纵用户定义类型的函数的代码。这两个文件组成了一个软件包，可用于各种程序中。

**注意，不要将函数定义或变量声明放到头文件中**，当这个头文件被多次引用，就会出现**重定义**，除非这个函数是内联的。下面是头文件经常包含的内容：
- 函数原型
- 使用 #define 或 const 定义的符号常量
- 结构声明
- 类声明
- 模板声明
- 内联函数

注意：包含头文件时，如果是自己编写的使用格式为 `"name.h"`，而不是 `<name.h>`，使用尖括号意味着是在编译器中的标准头文件中查找。

### 8.2 头文件及管理
编写头文件的格式如下:
```cpp
#ifndef COORDIN_H
#define COORDIN_H
...
#endif
```
在同一文件中只能将同一个头文件包含一次，可以使用`#ifndef`和`endif`来避免重复引用的问题。当头文件已经被引用，会直接跳到`endif`后面执行下面的语句。也就是说**仅当以前没有使用预处理器编译指令#define定义名称COORDINH时，才处理#ifndef和#endif之间的语句**。这种方案不能防止编译器将文件包含两次，但是由于进行了跳过，可以避免**重定义**的问题。

### 8.3 存储持续性、作用域和链接性
C++ 使用三种方案来存储数据：
- 自动存储连续性：在函数定义中声明的变量（包括函数参数）的存储时自动的。在程序开始时创建，结束被释放。称为**自动变量**。
- 精彩存储持续性：函数定义外的变量和使用关键字 static 定义的变量。称为**静态变量**。
- 动态存储持续性：使用 new 运算符分配的内存将一直存在，直到使用 delete 释放。他们的持续性为动态，称为**堆**。
- 线程存储持续性：使用关键字 thread_local 声明。生命周期和线程一样长。

#### 8.3.1 作用域和链接
**作用域**描述的是名称在文件的多大范围可见。**链接性**描述了名称如何让在不同的单元之间共享。链接性为外部的名称间可以共享，为内部的只能由一个文件中的函数共享。自动变量没有链接性，不能共享。
C++ 作用域有多种，作用域为局部的变量只在定义他的代码块中可用。代码块是由花括号括起的一系列语句。代码块之间可以嵌套。作用域为全局的（又称文件作用域）变量在定义位置到文件结尾都可以使用。
**自动变量的作用域是局部，静态变量的作用域是全局还是局部取决于是如何定义的**。
- 函数原型作用域中使用的名称只有在**包含参数列表的括号**可用（函数声明中的变量名不会影响其他位置的变量名的使用）。
- 类中声明的成员作用域是整个类，包括对应的成员函数。
- 名称空间声明的变量的作用域是整个名称空间。注意，**全局作用域是名称空间作用域的特例**[^31]。

C++函数的作用域可以是整个类或整个名称空间（包括全局），但**不能是局部的**。

#### 8.3.2 自动存储持续性
在默认情况下，**函数声明的函数参数和变量存储持续性都是自动的，作用域是局部，没有链接性**。就是说不同函数命名的变量互不干扰。当函数运行时分配内存，并进行使用，函数结束就会释放变量的内存。
如果是代码块的情况，变量的存在时间和作用域都是该代码块（for循环就是一个例子）。当外部变量和代码块中的变量重名，会发生**名称遮蔽**，代码块使用的是内部定义的变量（除非是用域名解析符或者是退出代码块才能重新使用外界的变量）。新定义可见，旧定义暂时不可见。

在 C++11 中，关键字 auto 用于自动判断类型，但是在 C 语言和之前的 C++ 版本中，auto用于显式的指出变量为自动存储。虽然现在不再使用了。

再来看看自动变量：
1. 自动变量的初始化
   可以使用任何在声明时其值为已知的表达式来初始化自动变量：
   ```cpp
   int w = 5;   // 5 为已知量
   int big = INT_MAX - 1;   // INT_MAX 为 climits 头文件中定义的变量
   int x = 2 * w;   // 表达式中的 w 为已知，表达式可以被评估。
   ```
2. 自动变量和栈
   由于自动变量的数目随函数的开始和结束而增减，因此程序必须在运行时对自动变量进行管理。常用的方法是留出一段内存，并将其视为栈，以管理变量的增减。栈的新数据是放在原有数据之上的，他们是相同的内存单元，而不是同一个。栈的默认长度取决于实现，但编译器通常提供改变栈长度的选项。程序使用两个指针来跟踪栈，一个指针指向栈底——栈的开始位置，另一个指针指向堆顶——下一个可用内存单元。当函数被调用时，其自动变量将被加入到栈中，栈顶指针指向变量后面的下一个可用的内存单元。函数结束时，栈顶指针被重置为函数被调用前的值，从而释放新变量使用的内存。
   **栈式后进先出的**。函数调用会将参数的值放在栈顶，然后重新设置栈顶指针。调用时将变量压入栈，结束后弹出。
3. 寄存器变量
   用关键字 register 声明，用于管理寄存器来存储自动变量。虽然被保留，但是基本上不再使用。

#### 8.3.3 静态持续变量
C++ 为静态存储提供了 3 中链接性：
- 外部链接性（其他文件可以访问）
- 内部链接性（只在当前文件中可以访问）
- 无链接性（只在当前函数或代码块中访问）。

静态存储的链接性在整个程序执行期间存在，寿命更长。编译器将分配固定的内存块来存储所有的静态变量，这些变量在整个程序执行期间一直存在。如果没有显式地初始化静态变量，编译器将把它设置为0。在默认情况下，静态数组和结构将每个元素或成员的所有位都设置为0。

```cpp
...
int global = 1000;              // static duration, external linkage
static int one_file = 50;       // static duration, internal linkage
int main()
{
    ...
}
void funct1(int n)
{
    static int count = 0;       // static duration, no linkage
    int llama = 0;
    ...
}
void funct2(int q)
{
    ...
}
```
1. **全局变量**：
   全局变量算是一种静态变量，是链接性在外部的变量。存储位置、生命周期还有哦人初始化都与静态变量相同。但是声明是**不用加 static 关键字**，只需要在代码块的外部进行声明即可。有外部链接性
2. **一般的静态变量**：
   使用 static 关键字，声明位置在全局作用域。只有内部链接性。
3. **局部静态变量**：
   使用 static 关键字，声明位置在局部域。无链接性，只能本函数或代码块使用，但是不会随着函数结束而消亡。

关键字 static 有两种用法：
1. **用于局部声明**，彳亍变量是无链接性的静态变量，static 表示的是存储的持续性。
2. **用于代码块之外的声明**，static 表示内部链接性，变量已经是静态持续性

下面是变量的储存方式：
| 存储描述 | 持续性 | 作用域 | 链接性 | 如何声明 |
| :--- | :--- | :--- | :--- | :--- |
| 自动 | 自动 | 代码块 | 无 | 在代码块中 |
| 寄存器 | 自动 | 代码块 | 无 | 在代码块中，使用关键字register |
| 静态，无链接性 | 静态 | 代码块 | 无 | 在代码块中，使用关键字static |
| 静态，外部链接性 | 静态 | 文件 | 外部 | 不在任何函数内 |
| 静态，内部链接性 | 静态 | 文件 | 内部 | 不在任何函数内，使用关键字static |

除了默认的零初始化，还可以对静态变量进行常量表达式初始化和动态初始化：
- **零初始化**：将变量设置成 0 .
- **常量表达式初始化**：
  - **特点**：速度最快，没有运行开销，不存在初始化顺序问题。
  - 使用字面量初始化或使用`constexpr`构造函数或常量表达式。
- **动态初始化**：
  - **特点**：在 `main` 函数执行前执行
  - **条件**：
    - 调用了非常量构造函数
    - 初始值依赖于函数调用、输入或运行时的计算 
动态初始化是我们一般初始化变量的方法。变量将在编译后初始化，零初始化和厂里狼表达式初始化统称为**静态初始化**，编译器处理文件时初始化变量。

**补充**：const 和 constexpr 之间区别：
| 特性 | `const` (只读) | `constexpr` (常量) |
| :--- | :--- | :--- |
| **语义** | 变量在初始化后**不可修改**。 | 变量是一个**编译时常量**。 |
| **初始化时间** | 可以是编译时，也可以是**运行时**。 | **必须**是编译时。 |
| **要求** | 初始值可以是函数返回值、用户输入。 | 初始值必须也是**常量表达式**。 |
| **修饰函数** | 修饰成员函数，表示不修改对象成员。 | 修饰函数，表示函数可在编译期计算。 |

- const 修饰成员函数：
  `void print() const;  // 表示不会修改数据`
- constexpr 修饰函数：
  如果传进来的时编译时常量，会在编译期计算结果，如果传入的时运行时变量，就会退化成普通函数
  ```cpp
  constexpr int square(int n) {return n * n;}
  int main() {
    constexpr int a = square(5);    // 编译期计算，a 变成了 25
    int x = 6;
    int b = square(x);  // 退化成了普通函数
  }
  ```
**凡是可以使用 constexpr 的地方，都可以使用 const，但是反过来不可以**。

#### 8.3.4 静态持续性、外部链接性
链接性为外部的变量通常简称为外部变量，它们的存储持续性为静态，作用域为整个文件。外部变量是在函数外部定义的，因此对所有函数而言都是外部的。
- 全局变量：是从**作用域**角度来说的。
- 外部变量：是从**存储类别和链接性**来说的，可以被其他文件通过 `extern` 来引用。
一般来说，外部变量也称为全局变量

1. 单定义规则：
   C++ 定义有**单定义规则**，即在**同一个局部域下**一个变量只能定义一次。但是外部变量有外部链接性，有文件公用的倾向，这个时候我们可以使用 `extern` 关键字来进行声明，这种 extern 声明不是**定义**（可以看看[这里](#1声明语句)），他不会分配空间，只是进行了声明，这叫引用声明。
   extern 声明使用 `extern` 并且不能进行初始化，否则声明为定义，失去了自己对应的效果。
   ```cpp
   double up;   // 定义，up 初始化为 0
   extern int blem;     // 声明
   extern char gr = 'z';    //定义，因为初始化分配了空间
   ```
   如果要在多个文件中使用外部变量，只需在一个文件中包含该变量的定义（单定义规则），但在使用该变量的其他所有文件中，都必须使用关键字extern声明它.

2. 全局变量和局部变量：
   局部变量适用于**需要数据隔离的情况**。全局变量使用于**多个函数公用一组数据的情况**，因此，全局变量极其适用于**常量数据管理**，可以使用 const 来保证数据不会被修改。

#### 8.3.5 静态持续性、内部链接性
将static限定符用于作用域为整个文件的变量时，该变量的链接性将为内部的。链接性为内部的变量只能在其所属的文件中使用；但常规外部变量都具有外部链接性，即可以在其他文件中使用.
如果文件定义了一个静态外部变量，其名称于kiln过一个文件中声明的常规外部变狼相同，则在该文件中，静态变量将隐藏常规外部变量。
```cpp
// file1.cpp
int errors = 0;
// file2.cpp
static int errors = 5;
void print() {
    cout << errors;     // 输出 5
}
```
**关键字 static 指出了标识符对应的链接性为内部**。

#### 8.3.6 静态持续性、无链接性
将static限定符用于在代码块中定义的变量。在代码块中使用static时，将导致局部变量的存储持续性为静态的。这意味着虽然该变量只在该代码块中可用，但它在该代码块不处于活动状态时仍然存在。因此在两次函数调用之间，静态局部变量的值将保持不变。**另外，如果初始化了静态局部变量，则程序只在启动时进行一次初始化。以后再调用函数时，将不会像自动变量再次被初始化。**

### 8.4 说明符和限定符
关于存储的 C++ 关键字分为两类：**存储说明符和cv-限定符**。
1. 存储说明符：
   - auto
   - register
   - static
   - extern
   - thread_local (C++11新增)
   - mutable
   thread_local和线程编程有关，mutable和 const 有关

2. cv-限定符：
   - const
   - volatile
   cv其实就是上面的 const 和 volatile 的简称。关键字 volatile 表明，即使没有对内存单元进行修改，值也会发生变换，使用 volatile 是为了告诉编译器：**不要将多次使用的变量放在寄存器中**（这是一个优化）。

下面我们看看 mutable 和 const
1. mutable
   mutable 可以用来指出：即使结构（或类）变量为 const ，他的莫格成员也可以被修改：
   ```cpp
   struct data {
       char name[20];
       mutable int accesses;
       ···
   };
   const data veep = {"Claybourne Clodde", 0, ···};
   strcpy(veep.name, "Joye Joux");      // NOT ALLOWED
   veep.accesses++;     // ALLOWED
   ```
2. const
   const 会影响变量的链接性，比如一般的全局变量，他的链接性是外部的，但是加上 const 就变成了内部的。在C++看来，全局 const 定义和 static 声明是一个效果（只不过 static 变量还可以进行修改）。
   当要求多个文件公用一个常量时，在常量前加入 extern 关键字：
   ```cpp
   // file1.cpp
   const char* months[12] = {"Januray", "Feburay", "Match", "April", "May", "June", "July", "Augest", "September", "Octber", "Novenber", "December"};
   // file2.cpp
   extern char* months[12];     // not allowed to initialized
   ```
   
### 8.5 函数和链接性
和变量一样，函数也有链接性。所有函数存储储蓄型都是静态的，在整个程序执行的期间一直存在。在默认情况下，函数链接性为**外部**。文件之间可以共享函数。当然，也可以使用关键字 static 来讲函数的链接性设置成内部，**必须同时在原型和函数定义中使用该关键字**：
```cpp
static int private(double x);
···
static int private(double x) {
    ···
}
```
这个函数将只有在该文件中才可见，还意味着可以在其他文件中定义同名的函数。这个时候文件会使用本文件中的静态函数，忽略其他文件中的同名函数（不会造成重定义的情况）。

对于单定义规则，非内联函数都适用，但是**内联函数没有这个束缚**。内联函数一般是放在头文件中，这样会避免内联函数反复定义（虽然可以，但是这些函数必须是**克隆级别**[^32]的相同）。

### 8.6 语言链接性
语言链接性对函数的存储有影响，C++允许函数重载，为了避免冲突，编译器会进行[名称矫正或修饰](#743-名称修饰)，为重载函数生成不同的符号名称。为了对对应标识进行认为规定，可以使用`extern "C"`或者是`extern "C++"`来进行人为规定。
```cpp
extern "C" void spiff(int);     // use C protocol
extern void spoff(int);     // use C++ protocol
extern "C++" void spaff(int);   // use C++ protocol 
```
第一个使用的是 C 语言的链接性，后两个都是 C++ 的，但是第二个是默认情况，第三个是显式的指出是 C++ 链接性。

### 8.7 动态内存分配
编译器一般使用三块地理的内存：
1. 静态变量区
2. 自动变量区
3. 动态变量区

存储方案不适用于动态内存，但是适用于用来跟踪动态内存的自动和静态指针变量。**注意，这两种方式对于局部使用的情况很危险，必须注意 delete 分配的内存**。

下面来看看动态内存分配的问题：
1. 使用 new 运算符进行初始化：
   如果要为内置的变量类型进行初始化和非陪空间，可以在类型名后面使用`()`括起对应的初始化值：
   ```cpp
   int *p = new int (6);
   double *ptr = new double (3.14);
   ```
   初始化常规结构和数组需要使用**大括号的列表初始化**：
   ```cpp
   struct position { double x; double y; double z;};
   position *ptr = new position { 1.0, 2.0, 3.0 };
   int *arr = new int [3] {1, 2, 3, 4};
   ```
   在 C++11 后就可以使用 `{}` 来初始化单值变量了：
   ```cpp
   int *ptr = new int {3};      // initialized 3
   ```

2. new 失败了
   new 可能会分配不了空间（空间满了），以前会返回空指针（如 `NULL`）。现在会返回一个错误：`std::bad_alloc`。
3. new 运算符、函数和替换函数
   new 运算符其实对应了两个**分配函数**：
   ```cpp
   void * operator new(std::size_t);    // used by new
   void * operator new[](std::size_t);      // used by new[]
   ```
   这两个函数位于全局名称空间中（那个没有名字的名称空间，域名解析时前面不用加`::`或`::对应名称`）。与分配函数相对应还有**释放函数**：
   ```cpp
   void operator delete(void *);
   void operator delete[](void *);
   ```
   new 和 delete 关键字都可用对应的函数进行替换：
   ```cpp
   int *pi = new(sizeof(int))   // 等价于 int *pi = new int
   int *pa = new(10*sizeof(int))    // 等价于 int *pa = new int [10]
   delete pi;    // 等价于 delete(pi);
   ```
   C++ 将这些函数称为**可替换的**。我们如有特殊需求，我们可以自己定义一个对应的 new 或 delete 来控制动态内存分配：
   ```cpp
   void operator delete(void *m) {
       std::cout << "正在释放内存" << m << std::endl;
       free(m);     // 这里调用的是底层的 C 函数
   }
   void * operator new(std::size_t size) {
       std::cout << "正在分配内存" << std::endl;
       void *p = std::malloc(size);     // 调用 malloc 分配内存
       if (!p) {
           throw std::bad_alloc();      // C++ 分配内存失败会抛出 bad_alloc() 错误
       }
       return p;    // 返回起始指针
   }
   ```
4. void 类型和 size_t 
   这两个类型主要是为了**描述内存**。
   1. `size_t` 是一个**无符号整数类型**。
      - **本质**：是一个**类型别名**(`typedef`)，通常指的是 `unsigned long long`。
      - **常见场景**：
        - `sizeof(T)` 返回的结果就是 `size_t`
        - 数组索引使用 `size_t`，防止索引越界
        - `strlen()`返回的是 `size_t`
   2. `void`：
      - **作为函数返回类型**：表示**不返回任何值**
      - **作为函数参数**：表示**不接受任何参数**
      - `void *`：这是**最关键的用法**，这是一个**纯粹的地址**
        - **特性**：直接记录内存的起始位置，但**不记录数据的类型**。
        - **注意**：不能进行解引用，不能进行加减法
        - **用途**：是内存操作的通用接口，任何指针都可以转换成 `void *`，但是使用时必须转化为具体的类型。

5. 定位 new 运算符
   通常的 new 是在在**堆**中找到一个满足要求的内存块。但是 new 运算符还有一种变体，称为**定位 new 运算符**，可以处理特定地址或在特定位置创建对象。
   使用定位 new 运算符，必须像包含 `<new>` 头文件，除了需要指定参数外，其他使用方式于 new 运算符相同：
   ```cpp
   #include <new>
   struct chaff {
       char dross[20];
       int slag;
   };
   char buffer1[50];
   char buffer2[50];
   int main() {
       chaff *p1, *p2';
       int *p3, *p4;
       
       p1 = new chaff;      // place structure in heap
       p3 = new int [20];   // place int array in heap

       p2 = new (buffer1) chaff;    // place structure in buffer1
       p4 = new (buffer2) int [20];     // place int array in buffer2

       ···
   }
   ```

6. 定位 new 的其他形式
   标准定位 new 运算符时调用一个接受两个参数的 new() 函数：
   ```cpp
   int *pi = new int;
   int p1 = new (buffer) int;
   int p2 = new (buffer) int [40];
   ```
   **定位 new 函数不可以替换，但是可以重载**，至少需要两个参数，一个是 std::size_t，保证请求的字节数，另外的任意。

### 8.8 名称空间
当变量增加时，名称可能冲突。C++标注提供了名称空间工具。
#### 8.8.1 传统的 C++ 名称空间
1. **声明区域**：
   声明区域指可以在其中进行声明的区域。比如在函数外面声明的全局变量，其生命区域时声明所在的文件。对于在函数中声明的变量。声明区域为对应的代码块。
2. **潜在作用域**：
   变量的潜在作用域是从**声明点**开始，到其声明点的结尾。**潜在作用域比声明区域小**。这是由于变量必须定义后才能使用。

**变量并非在其潜在作用域内的任何位置都是可见的**，这是因为有**名称遮蔽**，对于嵌套的代码块，块内的同名变量会覆盖掉外部的变量。变量对程序而言可见的范围被称为作用域（scope）。

C++关于全局变量和局部变量的规则定义了一种名称空间的层次。每个声明区域都可以声明名称，这些名称独立于在其他声明区域中声明的名称。在一个函数中声明的局部变量不会与在另一个函数中声明的局部变量发生冲突。（作用域问题）

#### 8.8.2 名称空间新特性
C++可以自行定义一种新的声明区来创建命名的名称空间。这样两个不同的名称空间的名称就不会相互冲突：
```cpp
namespace 名称空间名 {
    // 在这里定义变量、函数、类等
    int variable;
    void function() {
        // 代码逻辑
    }
    struct MyStruct { };
}
```
名称空间的范围是任意的，可以是全局，也可以是嵌套在另一个名称空间中。但是不能位于代码块中。默认名称空间中的声明链接性是外部的（除非是常量）[^33]

除了自定义的名称空间，还有**全局名称空间**（匿名且位于全局）。
名称空间是开放的，可以将名称加入到已有的名称空间中：
```cpp
namespace targetNameSpace {
    ··· // 想要添加的名称
}
```

##### 8.8.2.1 名称问题

访问名称空间中的名称使用的是域名解析符 `::`。名称又分为**未限定的名称**还有**限定的名称**：
1. **未限定名称**：
   不带名称空间前缀或类前缀。
   - **规则**：编译器根据作用域来寻找这个名称。
   - **风险**：容易名称冲突

2. **限定名称**：
   显式指出名称空间和类
   - **规则**：直接去对应的空间或类中找。
   - **优点**：精确，没有歧义。

##### 8.8.2.2 using 问题
关于 using 的使用[前面](#14-关键字-using)有提过，这里重点是名称的限制：
1. using 声明
   using声明将特定的名称添加到它所属的声明区域中。这样是的代码更加精简。
   在函数外使用 using 会将对应的变量名添加到全局名称空间中。
   对于重名的两个标识符，using 两个不同名称空间会有问题：
   ```cpp
   using name1::number;
   using name2::number;
   number = 3.14;   // 现在不知道是谁了
   ```
   这样使用容易造成二义性。
2. using 编译指令
   这个一般在函数中使用。using 声明是将一个名称在对应的作用域中可用，但是using 编译指令是将整个空间引用过来使用。使用编译指令时是将整个空间名称都解析。但是如果在已经声明名称函数中使用 using 编译指令所引入的对应的名称是函数内部的，而不是名称空间的。
3. 注意：
   名称空间或声明区域已经定义了相同的名称，使用 using 声明会**报错**。使用 using 编译指令会将名称导入该区域，但是被局部的名称所隐藏。

##### 8.8.2.3 其他问题
名称空间是可以进行嵌套的：
```cpp
namespace elements {
    namespace ele {
        int num;
        char *shape[20];
        ···
    }
    float concepts;
}
```
如果要使用 num 可以用 `elements::ele::num`。using 的使用也同理：
```cpp
using namespace elements::ele;      // 解析的是 ele，而不是 elements
```

名称空间的名称是可以组合的：
```cpp
namespace syntax {
    using Variable::Int;
    using Function::func_name;
    using NameSpace::name;
    ···
    using namespace namespace_name;
}
```
于是，如果想使用 `Int`，可以这样：
```cpp
std::cout << syntax::Int;   // 和 std::cout << Variable::Int; 是一个效果
```
**using编译指令是可以传递的**。A op B 且 B op C，则 A op C：
```cpp
using namespace syntax;
// 等价于
using namespace syntax;
using namespace namespace_name;
```

名称空间还可以创建别名：
```cpp
namespace S = syntax;   // 这样两者就等效了
```

有些名称空间还可以是匿名的（典型的就是全局名称空间）：
```cpp
namespace {
    int ice;
    int bandicoot;
}
```
在该名称空间中声明的名称的潜在作用域为：从声明点到该声明区域末尾。从这个方面看，它们与全局变量相似。这种名称空间没有名称，因此**不能显式地使用using编译指令或using声明**来使它在其他位置都可用。具体地说，不能在未命名名称空间所属文件之外的其他文件中，使用该名称空间中的名称。这提供了**链接性为内部的静态变量**的替代品:
```cpp
static int count = 0;
// 等价于
namespace {
    int count = 0;
}
```

## 九、类 <a id="类"></a>
这里的内容都是关于类的基本知识，从这里开始，后续都是类的问题。
### 9.1 C++中的类 <a id="C++中的类"></a>
一般来说，类的规范有两个部分组成：
- 类声明：以数据成员的方式表述数据，以成员函数的方式描述共有接口。
- 类方法定义：成员函数的实现。

通常，C++中的类声明放在头文件中，并将实现放在源代码文件中，最后进行文件的联编。
下面是类的一个例子：
```cpp
class Stock {
private:
    std::string company;
    long shares;
    double share_val;
    double total_val;
    void seT() {total_val = share * share_val;}
public:
    void acquiare(const std::steing & co; int n; double pr);
    void buy(int num, double price);
    void sell(long num, double price);
    void update(double price);
    void show();
}
```
**类中的 class 和模板中的 class 不一样，这里的 class 是对类的声明，不饿能使用 typename 来进行替换**。声明了类以后就可以声明对应的对象了。

### 9.2 private 和 public 关键字 <a id="private 和 public"></a>
使用类对象的程序都可以直接访问共有部分，但是只能通过共有成员函数









[^1]: **扩展名** ，也叫**后缀名**，是文件名中最后一个点 `.` 之后那部分的字母或者数字。他是文件的“身份标签”，告诉操作系统**这是一个什么类型的文件**和**怎么打开它**。一个完整的文件名有两部分组成：`文件名 + 扩展名`。其中的 `.` 叫**分隔符**。扩展名有以下三种作用：
    - **关联程序**：系统会查看扩展名并进行对应的操作。
    - **表示格式**：他表示文件内部数据的组织方式。如`.jpg`表示里面存的是像素颜色数据，`.txt`表示里面存的是纯文本字符。
    - **编译器识别**：在编程中，编译器会根据扩展名处理文件。
    下面是一些常见的扩展名：
    1. 源代码文件：
    - `.cpp`：**最标准**的 C++ 源文件
    - `.cc`：用于Unix环境的 C++ 源文件
    - `.c`：C 语言源文件
    1. 头文件：
    - `.h`：通用头文件（C 和 C++ 都能用
    - `.hpp`：C++ 专用头文件
    - 无后缀：标准库头文件
    1. 库文件：
    2. 静态库：链接时将代码直接拷贝到程序中
        - `.lib`：Windows
        - `.a`：Linux
    3. 动态库：程序运行时才会加载。
        - `.dll`：Windows
        - `.so`：Linux
    4. 中间目标文件和执行文件
    - `.obj`：目标文件（Windows）
    - `.o` 目标文件（Linux）
    - `.exe`：可执行文件

[^2]: **接口** 是一组函数或方法的声明。它定义了调用者如何与这个组件沟通（函数名、参数、返回值）。

[^3]: 这里我们对倒数第二点进行详细的说明： C/C++规定：任何以`__`和`_大写字母`开头的名字，保留给**实现**使用。普通程序员不要定义这种名字，避免与编译器或者标准库冲突。
    ```cpp
    int __myVar;  // ❌ 不要用，保留给编译器
    int _Xyz;     // ❌ 不要用
    ```
    这里讲的实现是C/C++语言本身提供的所有内部机制和资源，即`实现(implementation) = 编译器 + 标注库 + 系统提供的运行时支持`。
    - 编译器提供的：
      - 内建函数(bulit-in functions)
      `int x = __builtin_popcount(7); //GCC内建函数`
      - 内部类型、宏、符号(如`__FILE__`,`__LINE__`等)
    - 标准库提供的：
      - STL容器内部变量、函数
      ```cpp
        namespace std {
            int _S_empty_rep_storage; // 内部使用
        }
      ```
      - 内部辅助函数、模板实现
    - 操作系统或运行时库提供的：
      - 运行时的初始化函数、系统调用包装函数等

      总之，“实现”不是指你自己写的库函数，而是 由语言提供者提供的全部内部机制，包括： 
      - 编译器内置
      - 标准库内部
      - 运行时支持

[^4]: 字面量和常量还是有些区别的。 虽然它们都是“常量”（不可改变的值），但在 C++ 中，人们通常把它们分开称呼：
    | 特性 | 字面值 (Literal) | 具名常量 (const Variable) |
    | :--- | :--- | :--- |
    | **是否有名字** | 无 | 有 |
    | **是否有内存地址** | 通常没有（编译器直接编进指令） | 有（它是一个变量，只是不能改） |
    | **可读性** | 差（被称为“魔数” Magic Number） | 好（有意义的名字） |

[^5]: 在头文件iostream文件中也提供了我们的表示其他进制的方法(dec: 10, hex: 16, oct: 8)。下面是一些例子：
    ```cpp
    #include <iostream>
    using namespace std;
    int main()
    {
        using namespace std;
        int chest = 42;
        int waist = 42;
        int inseam = 42;

        cout << "Monsieur cuts a striking figure!" << endl;
        cout << "chest = " << chest << " (decimal for 42)" << endl;
        cout << hex;        // manipulator for changing number base
        cout << "waist = " << waist << " (hexadecimal for 42)" << endl;
        cout << oct;        // manipulator for changing number base
        cout << "inseam = " << inseam << " (octal for 42)" << endl;
        return 0;
    }
    ```
    这是输出结果：
    ```
    Monsieur cuts a striking figure!
    chest = 42 (decimal for 42)
    waist = 2a (hexadecimal for 42)
    inseam = 52 (octal for 42)
    ```
    对于dec，hex和oct，他们不会在终端中输出，仅会改变cout的输出形式，但是这种改变也是一直有效的，直到程序结束，也就是说我们在使用进制转换的时候别忘了在转回我们常用的10进制。

[^6]: Unicode提供了一种表示各种字符集的解决方案—为大量字符和符号提供标准数值编码，并根据类型将它们分组。例如，ASCII码为Unicode的子集，因此在这两种系统中，美国的拉丁字符（如A和Z）的表示相同。然而，Unicode还包含其他拉丁字符，如欧洲语言使用的拉丁字符、来自其他语言（如希腊语、西里尔语、希伯来语、切罗基语、阿拉伯语、泰语和孟加拉语）中的字符以及象形文字（如中国和日本的文字）。到目前为止，Unicode可以表示109000多种符号和90多个手写符号（script），它还在不断发展中。
Unicode给每个字符指定一个编号—码点。Unicode码点通常类似于下面这样：U-222B。其中U表示这是一个Unicode字符，而222B是该字符（积分正弦符号）的十六进制编号。
国际标准化组织（ISO）建立了一个工作组，专门开发ISO 10646—这也是一个对多种语言文本进行编码的标准。ISO 10646小组和Unicode小组从1991年开始合作，以确保他们的标准同步。

[^7]: 对于数字电子技术的电子书可以直接[跳转到这里](https://gitcode.com/Open-source-documentation-tutorial/ed458/blob/main/Thomas%20L%20Floyd%20-%20Digital%20Fundamentals%20A%20Systems%20Approach(2014,%20Pearson).pdf) 

[^8]: 注意，这里我们说数组也是可以进行相互赋值的，这里的相互赋值就是将两者的内容拷贝复制，不是公用地址。这点与一些简单的数组之间相互赋值不一样。

[^9]: 面向对象编程与传统的过程性编程的区别在于，OOP强调的是在运行阶段（而不是编译阶段）进行决策。运行阶段指的是程序正在运行时，编译阶段指的是编译器将程序组合起来时。运行阶段决策提供了灵活性，可以根据当时的情况进行调整。
使用常规变量时，值是指定的量，而地址为派生量。处理存储数据的新策略刚好相反，将地址视为指定的量，而将值视为派生量。**指针用于存储值的地址**，指针名表示的是地址，`*`运算符称为间接值或解引用运算符，用于指针就可以得到指针所存储的地址的对应量。

[^10]: 在C++中，`int*`是一种复合类型，是指向int的指针。

[^11]: 一定要在对指针应用解除引用运算符（*）之前，将指针初始化为一个确定的、适当的地址。这是关于使用指针的金科玉律。

[^12]: **不要尝试释放已经释放的内存块**，C++标准指出，这样做的结果将是不确定的，这意味着什么情况都可能发生。**另外，不能使用delete来释放声明变量所获得的内存：
    ```cpp
    int *ps = new int;
    delete ps;  // ok
    delete ps;  // not ok
    int jugs = 5;   // ok
    int *pi = &jugs;    // ok
    delete pi;  // not allowed, memory not allocated by new
    ```
[^13]: C++对于`char *`类型做出了**重载**，当我们正常使用cout输出char *类型的指针的时候，我们结果是输出字符串，但是当变成别的类型（像 int * ），这个时候我们得到的是指针的所指向的地址。

[^14]: ###### 栈、堆和内存泄漏：
    由于栈“用完即走”的特性，我们不用担心他的内存不会释放的问题，但是指针和指针指向的堆中的内存就不好办了，当代码块中的指针随着代码块运行结束被释放，其所指向的内存如果没有新的指针指向，就会成为一个无名的且无法被使用的但是还存在的一块内存，这叫**内存泄露**，这是很危险的，会占用大量的内存导致程序崩溃。

[^15]: **变量的生命周期（Lifetime / Scope & Duration）**是指一个变量从“出生”到“死亡”的整个过程。简单来说，就是从**计算机为这个变量分配内存空间**开始，到**这块内存被释放/回收**为止的时间跨度。
   变量生命周期分为三段：**分配，使用，回收**：
    1. **分配**：当你定义变量（如 int a = 10;）时，程序在内存里给它找了个“房间”。
    2. **使用**：在程序运行期间，你可以读写这个房间里的数据。
    3. **回收**：当变量不再需要时，它占用的“房间”会被退租，交给系统重新分配给别人。
    
    下面是各种常见变量的生命周期：
    4. **局部变量（自动变量）**
        * **寿命**：最短。
        * **规律**：通常定义在函数或代码块 `{ }` 内部。
        * **生存期**：进入代码块时出生，**离开代码块时立即死亡**。
        * **比喻**：像“快闪店”，只在特定活动期间存在。

    5. **全局变量 / 静态变量**
       * **寿命**：最长。
       * **规律**：定义在函数外部，或者使用了 `static` 关键字。
       * **生存期**：**从程序启动到程序结束**一直存在。
       * **比喻**：像“百年老店”，只要公司（程序）没倒闭，它就一直在。

    6. **堆变量（动态分配）**
       * **寿命**：由程序员手动控制。
       * **规律**：使用 `new` 或 `malloc` 创建。
       * **生存期**：从你创建它开始，直到你手动删除它（或被垃圾回收机制 GC 处理）。
       * **比喻**：像“长期租房”，租多久取决于你什么时候退房。

[^16]: 在设计循环时，有几条指导原则：
      *   **指定循环终止的条件。**
      *   **在首次测试之前初始化条件。**
      *   **在条件被再次测试之前更新条件。**
      `for` 循环的一个优点是，其结构提供了一个可实现上述 3 条指导原则的地方，因此有助于程序员记住应该这样做。但这些指导原则也适用于 `while` 循环。

[^17]: 类型别名：
    C++为类型建立别名的方式有两种：
    - 一种是使用预处理器：
    `#define BYTE char // preprocessor replaces BYTE with char`
    这样，预处理器将在编译程序时用char替换所有的BYTE，从而使BYTE成为char的别名。
    - 第二种方法是使用C++（和C）的关键字typedef来创建别名。例如，要将byte作为char的别名，可以这样做：
    `typedef char byte // make byte an alias for char`

    下面是通用格式：
    `typedef typeName aliasName;`
    我们也可以声明指针：
    `typedef char* byte_pointer;    // pointer to char type`
    也可以使用`#define`，但是在声明一系列变量的时候这个方法就不再适用:
    ```cpp
    #define FLOAT_POINTER float*
    FLOAT_POINTER pa, pb;
    ```
    由于define是直接将对应部分预处理替换成我们定义的部分所以上面的程序就变成了：
    ```cpp
    float *pa, pb;      // pa a pointer to float, pb just a float
    ```
    但是 typedef 不会发生这种情况，因为他是真的给这个变量气力一个别名。但是，**typedef不会创建新类型**，而只是为已有的类型建立一个新名称。如果将word作为int的别名，则cout将把word类型的值视为int类型。

[^18]: 出口条件循环（Exit-controlled loop）是指先执行循环体，再判断条件的循环结构。也称为后测试循环（Post-test loop）。
    - 特点：循环体**至少会执行一次**，然后才检查循环条件是否成立。
    - 如果条件成立（或不成立，取决于写法），就继续循环；否则退出循环。
    - 因为判断条件放在循环体的出口（最后），所以叫出口条件循环。

[^19]: 读取文件中的信息似乎同cin和键盘输入没什么关系，但其实存在两个相关的地方:
    1. 很多操作系统（包括Unix、Linux和Windows命令提示符模式）都支持重定向，允许用文件替换键盘输入:
    ```
    exe < fileName
    ```
    这样就告诉操作系统，我们的程序拒绝键盘输入，直接从文件中读取文本。其中的`<`是Unix和Windows命令提示符的重定向运算符。
    2. 很多操作系统都允许通过键盘来模拟文件尾条件。在Unix中，可以在行首按下`Ctrl+D`来实现；在Windows命令提示符模式下，可以在任意位置按`Ctrl+Z`和`Enter`。有些C++实现支持类似的行为，即使底层操作系统并不支持。用于PC的Microsoft Visual C++、Borland C++ 5.5和GNU C++ 都能够识别行首的Ctrl + Z，但用户必须随后按下回车键。总之，很多PC编程环境都将Ctrl+Z视为模拟的EOF，但具体细节各不相同。

[^20]: 在C++的iostream库中，`eofbit`和`failbit`是用来描述**流**当前状态的**标志位**。
    1. eofbit(End-Of-File bit)
    - 含义：eof 是 End Of File 的缩写。当程序尝试读取数据，但已经到达了文件的末尾（或者输入流的末尾）时，就会设置这个标志。
    - 触发时间：
        - 读取文件：使用 `<` 重定向读完一个文件的最后一个字符，但是还想继续读下去。
        - 键盘输入：使用`Ctrl + Z`然后回车。
    - 检测方法：使用 cin.eof()，如果是返回了 true，说明已经读完了。
    2. failbit(Failure bit) 
    - 含义：表示一个输入操作没能成功完成，通常是因为**数据格式不匹配**。
    - 触发时间：
        - 类型不匹配：比如 `int num; cin >> num;` 结果在键盘上敲了一个字母 `A`。`cin` 发现没法把 `A` 转换成整数，读取就失败了，此时会设置 `failbit`。
        - 文件打不开：试图读取一个不存在的文件。
        - 到达 EOF 的同时，读取到了文件的末尾，但是还是没有读取到我们想要的数据，这个时候`eofbit`和`failbit`都会被设置。
    - 检测方法：使用 `cin.fail()`

[^21]: 最初，put( )成员只有一个原型—put(char)。可以传递一个int参数给它，该参数将**被强制转换为char**。C++标准还要求只有一个原型。然而，有些C++实现都提供了3个原型：`put(char)`、`put(signed char)`和`put(unsigned char)`。在这些实现中，给`put()`传递一个int参数将导致错误消息，因为转换int的方式不止一种。使用显式强制类型转换的原型（如cin.put(char(ch))）可使用int参数。

[^22]: 控制字符： 是一组特殊的字符，它们在 ASCII 码表（及 Unicode）中占据前 32 个位置（号 0 到 31）以及最后一个位置（编号 127）。控制字符**不会被打印在屏幕上**，而是用来控制输出设备的行为或标记数据的结构。
    | 转义序列 | 含义 | ASCII 值 (十进制) | 说明 |
    | :--- | :--- | :--- | :--- |
    | `\n` | **换行 (Newline)** | 10 | 光标移动到下一行开头 |
    | `\t` | **水平制表符 (Tab)** | 9 | 跳到下一个制表位（通常用于对齐） |
    | `\v` | **垂直制表符** | 11 | 较少用，移动到垂直下一个制表位 |
    | `\b` | **退格 (Backspace)** | 8 | 光标向左退一格，但不删除字符 |
    | `\r` | **回车 (Carriage Return)** | 13 | 光标回到当前行的行首 |
    | `\a` | **响铃 (Alert)** | 7 | 触发系统警报声或闪烁 |
    | `\\` | **反斜杠** | 92 | 输出一个 `\` 符号 |
    | `\'` | **单引号** | 39 | 在字符常量中输出 `'` |
    | `\"` | **双引号** | 34 | 在字符串常量中输出 `"` |
    | `\?` | **问号** | 63 | 防止被解析为三字母词（Trigraph） |
    | `\0` | **空字符 (Null)** | 0 | 字符串的结束标志 |
    | `\ddd` | **八进制表示** | - | 1到3位八进制数（如 `\141` 是 'a'） |
    | `\xhh` | **十六进制表示** | - | 1到2位十六进制数（如 `\x61` 是 'a'） |

[^23]: 过度使用 goto 会导致以下问题：
      1. **“面条代码”（Spaghetti Code）**：程序逻辑会像面条一样缠绕在一起。因为可以随意跳来跳去，开发者很难跟踪程序的执行流。
      2. **破坏结构化编程**：while、for 和 if-else 等结构清晰地定义了代码的开始和结束，而 goto 破坏了这种结构。
      3. **变量初始化问题**：在 C++ 中，如果你使用 goto 跳过了一个变量的初始化语句，编译器通常会报错，因为这会导致程序进入一个不确定的状态。

[^24]: 函数原型的自动转换并不能解决所有的问题，C++中还存在着[函数重载](#74-函数重载)，这个时候进行自动转换可能会产生**二义性**。 对于缩窄转换，数据可能会有丢失，因此要慎用。
    而且，函数的参数或返回值的转换只有当转换有意义的时候参会发生（例如原型不会将整数转换成结构或者指针）。

[^25]: 函数调用的过程：接受参数 -> 进行操作 -> 返回**副本**（引用除外）。

[^26]: auto 变量可以看[这里](#210-c11-中的-auto-声明)，或者是看[这里](https://github.com/hangyu1234/Hakimi-s-Rough-Academic-Journey/blob/main/%E5%85%B6%E4%BB%96%E7%AC%94%E8%AE%B0/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B1%BB/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/%E7%8E%B0%E4%BB%A3C%2B%2B%EF%BC%8817_20%EF%BC%89%E5%B8%B8%E7%94%A8%E8%AF%AD%E6%B3%95.md)

[^27]: auto 必须先见识到这个声明的指针实例，才会进行自动类型推导。

[^28]: 如果函数调用的参数不是左值或与相应的const引用参数的类型不匹配，则C++将创建类型正确的匿名变量，将函数调用的参数的值传递给该匿名变量，并让参数来引用该变量。

[^29]: `volatile` 是一个**类型限定符**，和 `const` 是平级的，使用他是为了避免对变量进行优化的问题（我们并不想进行优化）。

[^30]: 这里的更具体不是说一定是显式具体化，而是**进行的转换更少**：
        ```cpp
        template <typename T> void recycle(T t);    
        template <typename T> void recycle(T *t);

        struct blot {int a; char b[10];};
        blot ink = {25, "spots"};

        recycle(&ink);      // 使用第二个，因为转换更少。
        ```
       这里两者都是可以的，第一个 T 被解释为是指向 T 类型的指针，但是第二个已经明确指出就是指向 T 类型的指针了，所以第二个“更具体”。

[^31]: 当我们不在任何 namespace、class 或 function 内部定义变量时，我们说这个变量是**全局变量**。但是在 C++ 标准看来，全局变量实际上是放在了一个**默认的、无名的名称空间中**，这个名称空间称为**全局名称空间**。
    全局名称空间有很多特殊之处：
    1. **是所有空间的根**：所有其他的名称空间都嵌套在其中。
    2. **是匿名的**：不需要使用名字来访问他
    3. **访问符号**，在局部作用域访问全局变量，可以使用作用域解析符`::`但是左边留空。
       ```cpp
        int count = 100;     // 全局作用域（即全局名称空间作用域）

        namespace School {
            int count = 50;  // School 名称空间作用域
        }

        int main() {
            int count = 10;  // 局部作用域
            
            // 1. 访问局部的 count
            int a = count;          // a = 10
            
            // 2. 访问 School 里的 count
            int b = School::count;  // b = 50
            
            // 3. 访问全局的 count (重点！)
            int c = ::count;        // c = 100
        }
       ```
       大多是情况下可以省略掉 `::` ，但是发生**名称遮蔽**时候必须使用 `::`，否则使用的是局部作用域的同名变量。
       - 不带 `::`: 编译器按照环境框架一步一步向上找，找到就停下。
       - 带 `::`: 直接到最初的全局作用域里找

[^32]: 这里其实是要求定义相同：不仅仅是函数名相同，而是所有的部分都要相同（避免二义性）：
        - **函数原型**：函数名、参数类型、参数个数、返回类型必须完全一致。
        - **函数体**：花括号中的每一个代码、操作符、变量名在逻辑上必须一模一样。
        - **语义一致**：引用的标识符（变量、函数等）指向同一个实体。

[^33]: 名称空间中的名称可以被多文件共用，但是加上 const 会使得对应的变量仅限于当前文件使用了。别的文件就不能使用 extern 语句来声明使用了。如果是公用常量就在前面加上 `extern` 关键字。