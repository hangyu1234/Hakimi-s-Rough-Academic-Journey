<div align="center">

# C Programming 笔记
</div>

---

笔记内容为对《 C Programming: A Modern Approach》的简单总结，目的是为了进行 C 语言的速成，细节可能略有误差，若发现问题，欢迎指正，邮箱：[2312786648@qq.com](https://mail.qq.com/)
<div align="right"> 编者：DoroKnight</div>

---
## 目录

- [C Programming 笔记](#c-programming-笔记)
  - [目录](#目录)
  - [一、预处理知识](#一预处理知识)
    - [1.1 格式](#11-格式)
    - [1.2 编译和链接](#12-编译和链接)
    - [1.3 注释](#13-注释)
  - [二、变量和赋值](#二变量和赋值)
    - [2.1 类型](#21-类型)
    - [2.2 声明](#22-声明)
    - [2.3 赋值](#23-赋值)
    - [2.4 初始化](#24-初始化)
    - [2.5 读入与输出](#25-读入与输出)
    - [2.6 常量](#26-常量)
    - [2.7 标识符](#27-标识符)
    - [2.8 关键字](#28-关键字)
  - [三、格式化输入与输出](#三格式化输入与输出)
    - [3.1 `printf` 函数](#31-printf-函数)
    - [3.2 `scanf` 函数](#32-scanf-函数)
    - [3.3 转义序列](#33-转义序列)
  - [四、表达式](#四表达式)
    - [4.1 算术运算符](#41-算术运算符)
    - [4.2 优先级与结合性](#42-优先级与结合性)
    - [4.3 赋值运算符](#43-赋值运算符)
    - [4.4 自增与自减](#44-自增与自减)
    - [4.5 表达式语句](#45-表达式语句)
  - [五、选择语句](#五选择语句)
    - [5.1 关系与逻辑表达式](#51-关系与逻辑表达式)
    - [5.2 `if` 语句](#52-if-语句)
    - [5.3 条件运算符](#53-条件运算符)
    - [5.4 `switch` 语句](#54-switch-语句)
  - [六、循环](#六循环)
    - [6.1 `while` 循环](#61-while-循环)
    - [6.2 `do` 循环](#62-do-循环)
    - [6.3 `for` 循环](#63-for-循环)
    - [6.4 退出与跳转](#64-退出与跳转)
    - [6.5 空语句](#65-空语句)
  - [七、基本类型](#七基本类型)
    - [7.1 整数类型](#71-整数类型)
    - [7.2 浮点类型](#72-浮点类型)
    - [7.3 字符类型](#73-字符类型)
    - [7.4 类型转换](#74-类型转换)
    - [7.5 类型定义](#75-类型定义)
    - [7.6 `sizeof` 运算符](#76-sizeof-运算符)
  - [八、数组](#八数组)
    - [8.1 一维数组](#81-一维数组)
    - [8.2 多维数组](#82-多维数组)
    - [8.3 常量数组](#83-常量数组)
    - [8.4 变长数组](#84-变长数组)
  - [九、函数](#九函数)
    - [9.1 函数定义与调用](#91-函数定义与调用)
    - [9.2 函数声明](#92-函数声明)
    - [9.3 参数传递](#93-参数传递)
    - [9.4 `return` 与程序终止](#94-return-与程序终止)
    - [9.5 递归](#95-递归)
  - [十、程序结构](#十程序结构)
    - [10.1 局部变量](#101-局部变量)
    - [10.2 静态局部变量](#102-静态局部变量)
    - [10.3 外部变量](#103-外部变量)
    - [10.4 程序块与作用域](#104-程序块与作用域)
    - [10.5 构建 C 程序](#105-构建-c-程序)
  - [十一、指针](#十一指针)
    - [11.1 指针变量](#111-指针变量)
    - [11.2 取地址与间接寻址](#112-取地址与间接寻址)
    - [11.3 指针赋值与空指针](#113-指针赋值与空指针)
    - [11.4 指针作为参数](#114-指针作为参数)
    - [11.5 指针作为返回值](#115-指针作为返回值)
  - [十二、指针与数组](#十二指针与数组)
    - [12.1 指针算术](#121-指针算术)
    - [12.2 数组名与指针](#122-数组名与指针)
    - [12.3 用指针处理数组](#123-用指针处理数组)
    - [12.4 指针与多维数组](#124-指针与多维数组)
    - [12.5 指针与变长数组](#125-指针与变长数组)
  - [十三、字符串](#十三字符串)
    - [13.1 字符串字面量](#131-字符串字面量)
    - [13.2 字符数组与字符指针](#132-字符数组与字符指针)
    - [13.3 字符串输入与输出](#133-字符串输入与输出)
    - [13.4 访问字符串](#134-访问字符串)
    - [13.5 字符串库](#135-字符串库)
    - [13.6 字符串数组与命令行参数](#136-字符串数组与命令行参数)
  - [十四、预处理器](#十四预处理器)
    - [14.1 工作原理](#141-工作原理)
    - [14.2 对象式宏](#142-对象式宏)
    - [14.3 函数式宏](#143-函数式宏)
    - [14.4 `#` 与 `##` 运算符](#144--与--运算符)
    - [14.5 预定义宏](#145-预定义宏)
    - [14.6 条件编译](#146-条件编译)
    - [14.7 其他指令](#147-其他指令)
  - [十五、大型程序](#十五大型程序)
    - [15.1 源文件与头文件](#151-源文件与头文件)
    - [15.2 `#include` 指令](#152-include-指令)
    - [15.3 多文件程序](#153-多文件程序)
    - [15.4 构建与链接](#154-构建与链接)
    - [15.5 `makefile`](#155-makefile)
  - [十六、结构、联合与枚举](#十六结构联合与枚举)
    - [16.1 结构变量](#161-结构变量)
    - [16.2 结构类型与别名](#162-结构类型与别名)
    - [16.3 嵌套结构与结构数组](#163-嵌套结构与结构数组)
    - [16.4 联合](#164-联合)
    - [16.5 枚举](#165-枚举)
  - [十七、指针的高级应用](#十七指针的高级应用)
    - [17.1 动态存储分配](#171-动态存储分配)
    - [17.2 动态字符串与数组](#172-动态字符串与数组)
    - [17.3 释放内存与悬空指针](#173-释放内存与悬空指针)
    - [17.4 链表](#174-链表)
    - [17.5 指向指针的指针](#175-指向指针的指针)
    - [17.6 函数指针](#176-函数指针)
    - [17.7 受限指针](#177-受限指针)
    - [17.8 灵活数组成员](#178-灵活数组成员)
  - [十八、声明](#十八声明)
    - [18.1 声明的组成](#181-声明的组成)
    - [18.2 存储类型](#182-存储类型)
    - [18.3 类型限定符](#183-类型限定符)
    - [18.4 解释复杂声明](#184-解释复杂声明)
    - [18.5 初始化](#185-初始化)
    - [18.6 内联函数](#186-内联函数)
  - [十九、程序设计](#十九程序设计)
    - [19.1 模块](#191-模块)
    - [19.2 信息隐藏](#192-信息隐藏)
    - [19.3 抽象数据类型](#193-抽象数据类型)
    - [19.4 接口设计](#194-接口设计)
  - [二十、底层程序设计](#二十底层程序设计)
    - [20.1 位运算符](#201-位运算符)
    - [20.2 位域](#202-位域)
    - [20.3 依赖机器的类型](#203-依赖机器的类型)
    - [20.4 联合与对象表示](#204-联合与对象表示)
    - [20.5 指针作为地址](#205-指针作为地址)
    - [20.6 `volatile` 对象](#206-volatile-对象)
  - [二十一、标准库](#二十一标准库)
    - [21.1 使用标准库](#211-使用标准库)
    - [21.2 名称限制](#212-名称限制)
    - [21.3 宏形式的库函数](#213-宏形式的库函数)
    - [21.4 C99 标准库更新](#214-c99-标准库更新)
  - [二十二、输入与输出](#二十二输入与输出)
    - [22.1 流](#221-流)
    - [22.2 打开与关闭文件](#222-打开与关闭文件)
    - [22.3 文件缓冲](#223-文件缓冲)
    - [22.4 格式化 I/O](#224-格式化-io)
    - [22.5 字符与行 I/O](#225-字符与行-io)
    - [22.6 块 I/O](#226-块-io)
    - [22.7 文件定位](#227-文件定位)
    - [22.8 文件末尾与错误](#228-文件末尾与错误)
  - [二十三、数值与字符数据的库支持](#二十三数值与字符数据的库支持)
    - [23.1 `<float.h>`](#231-floath)
    - [23.2 `<limits.h>`](#232-limitsh)
    - [23.3 `<math.h>`](#233-mathh)
    - [23.4 浮点分类与比较](#234-浮点分类与比较)
    - [23.5 `<ctype.h>`](#235-ctypeh)
    - [23.6 `<string.h>` 的内存函数](#236-stringh-的内存函数)
  - [二十四、错误处理](#二十四错误处理)
    - [24.1 `<assert.h>`](#241-asserth)
    - [24.2 `<errno.h>`](#242-errnoh)
    - [24.3 信号](#243-信号)
    - [24.4 非局部跳转](#244-非局部跳转)
  - [二十五、国际化特性](#二十五国际化特性)
    - [25.1 本地化](#251-本地化)
    - [25.2 多字节字符与宽字符](#252-多字节字符与宽字符)
    - [25.3 UTF-8](#253-utf-8)
    - [25.4 双字符与三字符](#254-双字符与三字符)
    - [25.5 宽字符 I/O](#255-宽字符-io)
  - [二十六、其他库函数](#二十六其他库函数)
    - [26.1 可变参数](#261-可变参数)
    - [26.2 数值转换](#262-数值转换)
    - [26.3 伪随机数](#263-伪随机数)
    - [26.4 与执行环境通信](#264-与执行环境通信)
    - [26.5 搜索与排序](#265-搜索与排序)
    - [26.6 整数算术](#266-整数算术)
    - [26.7 日期与时间](#267-日期与时间)
  - [二十七、C99 对数学计算的新增支持](#二十七c99-对数学计算的新增支持)
    - [27.1 `<stdint.h>`](#271-stdinth)
    - [27.2 `<inttypes.h>`](#272-inttypesh)
    - [27.3 复数](#273-复数)
    - [27.4 `<complex.h>`](#274-complexh)
    - [27.5 `<tgmath.h>`](#275-tgmathh)
    - [27.6 `<fenv.h>`](#276-fenvh)


---

## 一、预处理知识
### 1.1 格式
C 程序通常有下面的格式：
```
INSTRUCTION

int main(void) {
    STATEMENT
}
```

### 1.2 编译和链接
C 语言的执行通常有 3 步：
- **预处理**：程序交给**预处理器(cpp)**，进行预处理后得到`.i`文件
- **编译**：预处理后的程序交给**编译器**，翻译成`.s`文件
- **汇编和链接**：`.s`文件交给**汇编器(as)**，翻译成`.o`文件后，再交给**链接器(ld)**得到最终的**可执行目标文件**

这部分内容可以到《深入理解计算机系统》这本书中学

### 1.3 注释
C 语言有两种注释：
1.  `/*STATEMENT*/` 类型：
    ```c
    /* This is a comment */
    ```

    这种注释既可以单独占行也可以和其他程序文本出现在同一行中：
    ```c
    /* Name: Hakimi.c */

    #include <stdio.h>

    int main(void) {
        printf("はちみーをなめるとあしがー はやくーなる"); /* 小私货 */
        return 0;
    }
    ```

    这种注释还可以占用多行：
    ```c
    /*  Name: Hakimi.c
        Purpose: Print something interesting.
        Author: DoroKnight
    */
    ```

2. `//` 类型：
   ISO C99 提供了另一种类型的注释，用 `//` 开始
   ```c
   // Name: Hakimi.c
   // Purpose: Print something interesting.
   // Author: DoroKnight
   ```

## 二、变量和赋值
C 语言中临时储存数据的储存单元称为**变量**

### 2.1 类型
每一个变量都要有一个**类型**，用来说明**变量所存储的数据的种类**
基本类型如下：
```
基本类型
├── 整数类型
│   ├── char
│   ├── signed char
│   ├── unsigned char
│   ├── short
│   ├── unsigned short
│   ├── int
│   ├── unsigned int
│   ├── long
│   ├── unsigned long
│   ├── long long
│   └── unsigned long long
├── 浮点类型
│   ├── float
│   ├── double
│   └── long double
├── 布尔类型
│   └── _Bool
└── 空类型
    └── void
```

还有一些派生类型或自定义类型：
```c
int *ptr;          // 指针类型
int arr[10];       // 数组类型
int func(void);    // 函数类型
struct Student;    // 结构体类型
union Data;        // 联合体类型
enum Color;        // 枚举类型
```

### 2.2 声明
使用变量前**必须**进行声明，声明变量需要**先指定类型，再说明名字**
```c
int height;
float profit;
```

如果有多个变量都是统一类型，可以一起声明：
```c
int height, length, width, volume;
float profit, loss;
```

最重要的一点：**声明永远在应用该变量的语句之前**
```c
// Correct version
int main(void) {
    int height;
    scanf("%d", &height);
    printf("%d\n", height);
    return 0;
}
```

```c
// Incorrect version
int main(void) {
    scanf("%d", &height);
    int height;
    printf("%d\n", height);
}
```

### 2.3 赋值
变量通过**赋值**来获得值。
```c
int height, length, width;
height = 8;
length = 12;
width = 10;
```

这样上面的 3 个变量就都有一个确切的值了。

注意：整型的赋值和浮点型的赋值有一点区别
1. 整型的赋值较为宽松：
   ```c
   int height = 8;
   ```
   这里的 8 称为常量，这个过程称为**初始化**
2. 浮点型的赋值较为严格：
   ```c
   float profit;
   profit = 24.315f;
   ```
   这里的浮点数常量最好在最后添加一个 `f`，明确表示它是 `float` 类型；不添加时常量默认为 `double`，赋值时会发生类型转换。

### 2.4 初始化
当程序开始执行的时候某些变量会自动设置为 0，但是大部分变量是不会的，这些无默认值并未被赋值的变量称为是**未初始化的变量**

**初始化**就是将声明语句和赋值语句放在了一起，让一个变量在声明完成后直接获得了一个我们知道且确切的值

```c
int age = 18;
float weight = 53.4;
char word = 'w';
char *sentence = "To be or not to be, that is a question.";
```

### 2.5 读入与输出
C 语言中的标准库提供了标准的输入与输出函数：`printf` 和 `scanf`
- `printf`
  标准格式为：
  ```c
  printf("FORMAT_STRING", EXPRESSION1, EXPRESSION2, ...);
  ```
  比如：
  ```c
  int age = 10;
  double score = 95.5;
  printf("age = %d, score = %.1f\n", age, score);
  ```
  输出结果：
  ```
  age = 10, score = 95.5
  ```

- `scanf`
  标准格式为：
  ```c
  scanf("FORMAT_STRING", VALUE_ADDRESS1, VALUE_ADDRESS2, ...);
  ```
  比如：
  ```c
  int age;
  double score;

  scanf("%d %lf", &age, &score);
  ```

- 格式说明符：
    `printf`:
    | 类型 | 格式说明符 |
    | --- | --- |
    | `char`，按字符输出 | `%c` |
    | `char *` 字符串 | `%s` |
    | `int` | `%d` 或 `%i` |
    | `unsigned int` | `%u` |
    | 八进制整数 | `%o` |
    | 十六进制整数 | `%x`、`%X` |
    | `long` | `%ld` |
    | `long long` | `%lld` |
    | `float`、`double` | `%f` |
    | 科学计数法 | `%e`、`%E` |
    | 自动选择浮点格式 | `%g`、`%G` |
    | `long double` | `%Lf` |
    | 指针 | `%p` |
    | `size_t` | `%zu` |
    | 百分号 | `%%` |

    `scanf`
    | 变量类型 | 格式说明符 | 参数形式 |
    | --- | --- | --- |
    | `char` | `%c` | `&ch` |
    | 字符数组 | `%s` | `str` |
    | `int` | `%d` | `&value` |
    | `unsigned int` | `%u` | `&value` |
    | `short` | `%hd` | `&value` |
    | `long` | `%ld` | `&value` |
    | `long long` | `%lld` | `&value` |
    | `float` | `%f` | `&value` |
    | `double` | `%lf` | `&value` |
    | `long double` | `%Lf` | `&value` |
    | `size_t` | `%zu` | `&value` |

### 2.6 常量
当有常量的时候，建议给常量进行命名，可以采用**宏定义**的方式
```c
#define PI 3.1415926f
```

这里的 `#define` 是一种预处理指令，类似于 `#include` ，当进行编译的时候，预处理器会将每一个宏替换为所表示的值（是直接替换在原文位置）

**注意**：宏的名字大部分情况使用的都是大写字母（这是约定俗成的）。当然你也可以用小写字母，并不会影响编译和运行。

### 2.7 标识符
编写程序的时候，需要对变量、函数、宏和其他实体进行命名，这些名字称为**标识符**。

标识符可以含有字母、数字和下划线，**但是必须以字母或者是下划线开头**。
```c
int hakimi114514_, get_head, _done; // Correct version

float 3.14pi;                      // Incorrect version.
```

注意：C语言是**区分大小写的**。类似于`Job` 和 `job` 是两个不同的标识符的。
一般而言，对于标识符的命名是没有严格限制的（你甚至可以整点花活）

### 2.8 关键字
C 语言关键字如下：

| 关键字 | 关键字 | 关键字 | 关键字 |
| --- | --- | --- | --- |
| `auto` | `enum` | `restrict`¹ | `unsigned` |
| `break` | `extern` | `return` | `void` |
| `case` | `float` | `short` | `volatile` |
| `char` | `for` | `signed` | `while` |
| `const` | `goto` | `sizeof` | `_Bool`¹ |
| `continue` | `if` | `static` | `_Complex`¹ |
| `default` | `inline`¹ | `struct` | `_Imaginary`¹ |
| `do` | `int` | `switch` |  |
| `double` | `long` | `typedef` |  |
| `else` | `register` | `union` |  |

---

## 三、格式化输入与输出
### 3.1 `printf` 函数
`printf` 按照**格式串**输出数据。格式串由普通字符和以 `%` 开头的**转换说明**组成：
```c
printf("FORMAT_STRING", EXPRESSION1, EXPRESSION2, ...);
```

转换说明的一般形式为：
```text
%[标志][最小字段宽度][.精度][长度修饰符]转换说明符
```

下面是一些常见例子：
```c
int value = 40;
double price = 839.21;

printf("|%5d|\n", value);       // |   40|，右对齐
printf("|%-5d|\n", value);      // |40   |，左对齐
printf("|%05d|\n", value);      // |00040|
printf("|%10.2f|\n", price);    // |    839.21|
printf("%e %g\n", price, price); // 科学计数法、自动选择形式
```

常用标志如下：

| 标志 | 作用 |
| --- | --- |
| `-` | 在字段内左对齐 |
| `+` | 正数也显示正号 |
| 空格 | 正数前保留一个空格 |
| `0` | 用 `0` 填充字段 |
| `#` | 使用八进制、十六进制或浮点数的替代形式 |

**注意**：转换说明的数量和类型必须与后续参数匹配，否则会产生**未定义行为**。`printf` 是变参函数，编译器不一定能发现所有格式错误。

### 3.2 `scanf` 函数
`scanf` 根据格式串读取数据，并把结果写入变量，因此普通变量通常要传入地址：
```c
int age;
double score;

if (scanf("%d%lf", &age, &score) != 2) {
    printf("Invalid input\n");
}
```

`scanf` 的返回值是**成功赋值的数据项数量**；如果在读取任何数据前遇到文件末尾，则返回 `EOF`。检查返回值比默认输入永远正确更加安全。

格式串中的空白字符会匹配任意数量的空白。大多数数值转换会自动跳过输入前的空白，但 `%c`、`%[` 不会：
```c
char ch;
scanf(" %c", &ch); // %c 前的空格用于跳过换行符等空白
```

读取字符串时要限制最大宽度，防止数组越界：
```c
char name[20];
scanf("%19s", name); // 最后一个位置留给 '\0'
```

`scanf` 很适合结构规则的输入。对于整行文本或复杂输入，通常先用 `fgets` 读取，再用 `sscanf`、`strtol` 等函数解析会更稳妥。

### 3.3 转义序列
反斜杠开头的转义序列用于表示难以直接输入或具有特殊含义的字符：

| 转义序列 | 含义 | 转义序列 | 含义 |
| --- | --- | --- | --- |
| `\n` | 换行 | `\t` | 水平制表 |
| `\r` | 回车 | `\b` | 退格 |
| `\a` | 响铃 | `\f` | 换页 |
| `\\` | 反斜杠 | `\"` | 双引号 |
| `\'` | 单引号 | `\0` | 空字符 |

---

## 四、表达式
### 4.1 算术运算符
C 语言的基本算术运算符有：

| 运算符 | 含义 |
| --- | --- |
| `+`、`-` | 加、减，或一元正负号 |
| `*`、`/` | 乘、除 |
| `%` | 整数求余 |

当两个操作数都是整数时，`/` 执行整数除法，小数部分会被截去：
```c
7 / 2       // 3
7.0 / 2     // 3.5
7 % 2       // 1
```

从 C99 开始，整数除法的结果向 `0` 截断，余数与被除数同号。除数为 `0` 是未定义行为。

### 4.2 优先级与结合性
优先级决定运算符的结合顺序，结合性用于处理相同优先级的运算符：
```c
a + b * c      // 等价于 a + (b * c)
a = b = 0;     // 等价于 a = (b = 0)，赋值从右向左结合
```

完整的优先级表不适合死记。表达式稍复杂时直接加括号，使意图清晰：
```c
result = (a + b) * (c - d);
```

### 4.3 赋值运算符
赋值本身也是表达式，它的值是赋值后左操作数的值：
```c
int a, b;
a = b = 10;
```

复合赋值可以缩短表达式：
```c
x += 2; // x = x + 2
y *= 3; // y = y * 3
```

左操作数必须是可以被修改的**左值**，常量和计算结果不能放在赋值号左侧。

### 4.4 自增与自减
前缀形式先修改再取值，后缀形式先取值再修改：
```c
int i = 1;
int a = ++i; // i = 2, a = 2
int b = i++; // b = 2, i = 3
```

不要在同一个表达式中多次修改同一对象，也不要依赖函数实参或子表达式的求值顺序：
```c
i = i++ + 1;          // 未定义行为
printf("%d %d", i++, i++); // 求值顺序不确定，不要这样写
```

### 4.5 表达式语句
任何表达式后添加分号都可以成为语句：
```c
i++;
printf("Hello\n");
```

没有副作用的表达式语句通常没有意义：
```c
i + j; // 计算结果被丢弃
```

---

## 五、选择语句
### 5.1 关系与逻辑表达式
关系运算符有 `<`、`>`、`<=`、`>=`，判等运算符有 `==`、`!=`。比较结果为 `0` 或 `1`。

逻辑运算符如下：

| 运算符 | 含义 |
| --- | --- |
| `!expr` | 逻辑非 |
| `expr1 && expr2` | 逻辑与 |
| `expr1 || expr2` | 逻辑或 |

在 C 语言中，`0` 表示假，任何非零值表示真。`&&` 和 `||` 采用**短路求值**：
```c
if (denominator != 0 && numerator / denominator > 2) {
    /* 只有 denominator != 0 时才会执行除法 */
}
```

### 5.2 `if` 语句
```c
if (score >= 60) {
    printf("Pass\n");
} else {
    printf("Fail\n");
}
```

多个分支可以使用 `else if`：
```c
if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else {
    grade = 'C';
}
```

`else` 总与前面最近且尚未匹配的 `if` 配对。即使分支中只有一条语句，也建议写花括号。

### 5.3 条件运算符
条件运算符是 C 语言唯一的三目运算符：
```c
max = a > b ? a : b;
```

它适合表达简单的二选一逻辑，复杂分支仍应使用 `if`。

### 5.4 `switch` 语句
当一个整型表达式需要与多个常量比较时，可以使用 `switch`：
```c
switch (command) {
case 'a':
    add_item();
    break;
case 'd':
    delete_item();
    break;
case 'q':
    return 0;
default:
    printf("Unknown command\n");
    break;
}
```

`case` 标签必须是**整型常量表达式**，并且不能重复。没有 `break` 时会继续执行下一个分支，这称为**贯穿**；如果是有意为之，最好添加注释。

---

## 六、循环
### 6.1 `while` 循环
`while` 先判断条件，再执行循环体，因此循环体可能一次也不执行：
```c
int i = 1;
while (i <= 10) {
    printf("%d ", i);
    i++;
}
```

### 6.2 `do` 循环
`do` 先执行循环体，再判断条件，因此至少执行一次：
```c
do {
    printf("Enter a positive number: ");
    scanf("%d", &number);
} while (number <= 0);
```

注意最后的 `while` 后面有分号。

### 6.3 `for` 循环
`for` 把初始化、条件和更新写在一起：
```c
for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}
```

它大致等价于：
```c
int i = 0;
while (i < 10) {
    printf("%d ", i);
    i++;
}
```

三个表达式都可以省略。`for (;;)` 是常见的无限循环形式。C99 允许在初始化部分声明变量，这个变量的作用域限制在循环内。

### 6.4 退出与跳转
- `break`：退出最内层的循环或 `switch`
- `continue`：跳过本轮剩余语句，进入下一轮
- `goto label`：跳转到同一函数内的标签

```c
for (int i = 0; i < n; i++) {
    if (data[i] < 0) {
        continue;
    }
    if (data[i] == target) {
        break;
    }
}
```

`goto` 通常会降低可读性，但在多层资源清理中可以集中处理错误：
```c
if (step1_failed) goto cleanup;
if (step2_failed) goto cleanup;

cleanup:
    release_resources();
```

### 6.5 空语句
只包含一个分号的语句称为空语句：
```c
while (getchar() != '\n')
    ; // 丢弃本行剩余字符
```

循环条件后误加分号是常见错误：
```c
while (i < 10); // 循环体为空，可能成为死循环
```

---

## 七、基本类型
### 7.1 整数类型
整数类型可以组合 `signed`、`unsigned`、`short`、`long` 等说明符：
```c
short int s;
unsigned int u;
long int l;
long long int ll;
```

C 标准只规定类型之间的最小范围和相对大小，不保证 `int` 一定是 32 位。需要准确宽度时使用 `<stdint.h>` 中的 `int32_t` 等类型。

整数字面量可以使用十进制、八进制和十六进制：
```c
10      // 十进制
012     // 八进制，值为 10
0x0A    // 十六进制，值为 10
100U    // unsigned int
100L    // long
100ULL  // unsigned long long
```

**有符号整数溢出是未定义行为**；无符号整数按 $2^n$ 取模。在有符号数和无符号数混合运算时，要特别注意隐式转换。

### 7.2 浮点类型
C 提供 `float`、`double` 和 `long double`：
```c
float f = 3.14f;
double d = 3.14;
long double ld = 3.14L;
```

浮点数只能近似表示许多十进制小数，不应直接用 `==` 判断计算结果是否相等：
```c
#include <math.h>

if (fabs(a - b) < 1e-9) {
    /* a 和 b 足够接近 */
}
```

### 7.3 字符类型
字符常量本质上与整数编码有关：
```c
char ch = 'A';
ch = ch + 1; // 通常得到 'B'
```

普通 `char` 是有符号还是无符号由实现决定。若数据明确表示小整数，可使用 `signed char` 或 `unsigned char`；处理原始字节时通常使用 `unsigned char`。

`<ctype.h>` 提供字符分类与大小写转换函数：
```c
if (isalpha((unsigned char)ch)) {
    ch = (char)tolower((unsigned char)ch);
}
```

除 `EOF` 外，传给这些函数的值必须能表示为 `unsigned char`，直接传入负的 `char` 可能产生未定义行为。

### 7.4 类型转换
较小的整数类型在表达式中通常先进行**整数提升**。不同算术类型混合时，会通过**常用算术转换**变成共同类型：
```c
int i = 10;
double result = i / 4.0; // i 转换为 double
```

赋值也会把右侧转换为左侧类型，可能丢失信息：
```c
int n = 3.99; // n 为 3
```

强制类型转换的形式如下：
```c
average = (double)sum / count;
```

强制转换可以表达意图，但不能让本来非法或越界的数据自动变安全。

### 7.5 类型定义
`typedef` 为已有类型创建别名：
```c
typedef unsigned long ULong;
typedef char Name[40];

ULong counter;
Name student_name;
```

它能提高可读性和可移植性，但不会创建语义上完全不同的新类型。

**注意**：这里的 `typedef char Name[40]` 是将 `Name` 命名为了一个长度为40的 `char` 数组。
对于指针类型、数组类型、函数指针类型这些复合类型，下面是通用判断方法：
> 先去掉 `typedef`，把其中准备成为别名的标识符暂时当作普通变量名，判断“这个变量是什么类型”；加回 `typedef` 后，该标识符就不再表示变量，而是成为这个完整类型的别名。

### 7.6 `sizeof` 运算符
`sizeof` 返回对象或类型占用的字节数，结果类型为 `size_t`：
```c
printf("%zu\n", sizeof(int));
printf("%zu\n", sizeof array / sizeof array[0]);
```

除变长数组外，`sizeof` 通常在编译期求值，并且不会计算其中普通表达式的副作用。

---

## 八、数组
### 8.1 一维数组
数组是一组类型相同、连续存储的元素：
```c
int scores[5];
scores[0] = 90;
scores[4] = 95;
```

下标从 `0` 开始。C 不进行数组边界检查，越界访问会产生未定义行为。

数组可以在定义时初始化：
```c
int a[5] = {1, 2, 3, 4, 5};
int b[5] = {1, 2};          // 其余元素初始化为 0
int c[] = {1, 2, 3};        // 长度自动推断为 3
int d[10] = {[2] = 5, [7] = 9}; // C99 指定初始化
```

计算数组元素个数的常见方式为：
```c
size_t length = sizeof a / sizeof a[0];
```

这个写法只对真正的数组有效，不能用于已经退化为指针的函数参数。

### 8.2 多维数组
```c
int matrix[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

C 按**行优先**顺序存储多维数组。`matrix[i][j]` 中的每一行本身也是一个数组。

作为函数参数时，除第一维外的维度必须能够确定：
```c
void print_matrix(size_t rows, int matrix[][3]);
```

### 8.3 常量数组
不会被修改的查找表可以声明为 `const`：
```c
const int days_per_month[12] = {
    31, 28, 31, 30, 31, 30,
    31, 31, 30, 31, 30, 31
};
```

这样既能表达意图，也能让编译器阻止意外赋值。

### 8.4 变长数组
C99 支持在运行时确定长度的变长数组（VLA）：
```c
void clear(size_t n, int a[n]) {
    for (size_t i = 0; i < n; i++) {
        a[i] = 0;
    }
}
```

VLA 通常位于自动存储区，不适合非常大的数组；C11 起实现可以不支持 VLA。可移植程序常使用动态内存代替。

---

## 九、函数
### 9.1 函数定义与调用
函数把一段逻辑封装成可复用单元：
```c
double average(double a, double b) {
    return (a + b) / 2.0;
}

int main(void) {
    printf("%.2f\n", average(10.0, 20.0));
    return 0;
}
```

函数不能直接定义在另一个函数内部。返回类型为 `void` 表示没有返回值。

### 9.2 函数声明
函数在调用前应有声明，也称为**函数原型**：
```c
double average(double a, double b);
```

原型使编译器能够检查实参个数和类型。`f(void)` 表示函数不接收参数；旧式写法 `f()` 在 C 中表示参数未指定，不应混用。

### 9.3 参数传递
C 语言只有**值传递**。函数得到的是实参值的副本：
```c
void swap_wrong(int a, int b) {
    int temp = a;
    a = b;
    b = temp; // 不会修改调用者的变量
}
```

要修改调用者对象，需要传递指针：
```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
```

数组作为实参时会转换为指向首元素的指针，因此应另外传入长度：
```c
int sum_array(const int a[], size_t n) {
    int sum = 0;
    for (size_t i = 0; i < n; i++) {
        sum += a[i];
    }
    return sum;
}
```

参数中的 `const` 表明函数不会通过该指针修改数组。

### 9.4 `return` 与程序终止
非 `void` 函数应在所有正常路径上返回适当的值：
```c
int sign(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
}
```

从 `main` 返回 `0` 表示成功，非零值表示失败。也可以使用 `<stdlib.h>` 中的 `exit`：
```c
exit(EXIT_FAILURE);
```

`exit` 会执行通过 `atexit` 注册的函数并刷新、关闭标准 I/O 流；`_Exit` 则立即终止。

### 9.5 递归
函数可以调用自身，但必须存在可以停止递归的基本情况：
```c
unsigned long long factorial(unsigned int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
```

递归适合树、分治等天然递归的问题，但每次调用都会占用栈空间。简单线性过程通常用循环更直接。

---

## 十、程序结构
### 10.1 局部变量
在函数体或程序块内声明的变量是局部变量，具有**块作用域**：
```c
void function(void) {
    int count = 0;
    /* count 只在函数体内可见 */
}
```

普通局部变量具有自动存储期，每次进入程序块都会创建，离开时生命周期结束。未初始化的自动变量值不确定，读取它会产生未定义行为。

### 10.2 静态局部变量
`static` 局部变量具有静态存储期，只初始化一次，并在多次调用间保留值：
```c
int next_id(void) {
    static int id = 0;
    return ++id;
}
```

它仍然只在所在程序块内可见，但生命周期持续到程序结束。

### 10.3 外部变量
函数外定义的变量具有文件作用域和静态存储期：
```c
int global_count = 0; // 定义
```

其他源文件通过 `extern` 声明使用它：
```c
extern int global_count; // 声明，不分配新的对象
```

外部变量会形成隐式依赖，应尽量限制使用。只在当前源文件中使用的外部变量应加 `static`，获得内部链接：
```c
static int file_private_count;
```

### 10.4 程序块与作用域
一对花括号形成程序块，内层声明可以隐藏外层同名对象：
```c
int x = 1;
{
    int x = 2;
    printf("%d\n", x); // 2
}
printf("%d\n", x);     // 1
```

过度使用同名变量容易造成混乱。变量应在尽可能小、但足以清楚表达用途的作用域中声明。

### 10.5 构建 C 程序
一个较清晰的单文件程序通常按下面的顺序组织：
```text
#include 指令
#define 指令
类型定义
外部变量声明
函数原型
main 函数
其他函数定义
```

随着程序增大，应按照功能拆分函数和源文件，而不是让 `main` 承担全部逻辑。

---

## 十一、指针
### 11.1 指针变量
指针保存对象的内存地址。声明时，`*` 表示声明的是指针：
```c
int value = 10;
int *pointer = &value;
```

建议把 `*` 靠近变量名理解，因为同一条声明中它只修饰紧随其后的声明符：
```c
int *p, value; // p 是指针，value 是 int
```

### 11.2 取地址与间接寻址
- `&object`：取得对象地址
- `*pointer`：访问指针指向的对象，也称为解引用

```c
int value = 10;
int *p = &value;

*p = 20; // 通过 p 修改 value
printf("%d\n", value); // 20
```

指针必须指向有效对象后才能解引用。未初始化指针、空指针、悬空指针都不能解引用。

### 11.3 指针赋值与空指针
相同或兼容类型的指针可以赋值：
```c
int value = 10;
int *p = &value;
int *q = p;
```

空指针不指向任何对象：
```c
int *p = NULL;
if (p != NULL) {
    printf("%d\n", *p);
}
```

`NULL` 定义在多个标准头中。现代 C 也常直接使用 `NULL` 表达“没有对象”，而不是用魔法地址。

### 11.4 指针作为参数
指针可以让函数修改调用者对象，或一次返回多个结果：
```c
void max_min(const int a[], size_t n, int *max, int *min) {
    *max = *min = a[0];
    for (size_t i = 1; i < n; i++) {
        if (a[i] > *max) *max = a[i];
        if (a[i] < *min) *min = a[i];
    }
}
```

只读参数使用指向 `const` 的指针：
```c
void print_value(const int *p);
```

这里不能通过 `p` 修改 `*p`，但 `p` 自身仍可指向别处。`int *const p` 则表示指针本身不能改变。

### 11.5 指针作为返回值
函数可以返回指针，但返回的地址在函数结束后必须仍然有效：
```c
int *find(int a[], size_t n, int target) {
    for (size_t i = 0; i < n; i++) {
        if (a[i] == target) {
            return &a[i];
        }
    }
    return NULL;
}
```

**永远不要返回指向自动局部变量的指针**：
```c
int *wrong(void) {
    int value = 10;
    return &value; // value 的生命周期在函数返回时结束
}
```

---

## 十二、指针与数组
### 12.1 指针算术
若 `p` 指向数组元素，则 `p + n` 指向后面第 `n` 个元素，移动的字节数会自动乘以元素大小：
```c
int a[5] = {10, 20, 30, 40, 50};
int *p = &a[1];

printf("%d\n", *(p + 2)); // 40
```

合法的指针运算只限于同一数组及其末尾后一位置。末尾后一指针可以用于比较，但不能解引用。

同一数组中的两个指针可以相减，结果类型为 `ptrdiff_t`：
```c
ptrdiff_t distance = &a[4] - &a[1]; // 3
```

### 12.2 数组名与指针
数组名在大多数表达式中会转换为指向首元素的指针：
```c
a[i] == *(a + i)
&a[i] == a + i
```

但是数组和指针不是同一种对象。以下情况数组名不会退化：
- 作为 `sizeof` 的操作数
- 作为一元 `&` 的操作数
- 用字符串字面量初始化字符数组

```c
sizeof a; // 整个数组的字节数
sizeof p; // 指针本身的字节数
```

### 12.3 用指针处理数组
```c
int sum_array(const int *begin, const int *end) {
    int sum = 0;
    while (begin < end) {
        sum += *begin++;
    }
    return sum;
}

int total = sum_array(a, a + 5);
```

`*p++` 等价于 `*(p++)`，先取得当前元素，再移动指针。复杂时写成两条语句更易读。

### 12.4 指针与多维数组
二维数组可以看作“元素为一维数组的数组”：
```c
int matrix[3][4];
int (*row)[4] = matrix;

row[1][2] = 10;
```

`int (*row)[4]` 是指向“含 4 个 `int` 的数组”的指针；括号不能省略，否则会变成指针数组。

### 12.5 指针与变长数组
VLA 参数可以把维度写入函数原型：
```c
void clear_matrix(size_t rows, size_t cols,
                  int matrix[rows][cols]) {
    for (size_t i = 0; i < rows; i++) {
        for (size_t j = 0; j < cols; j++) {
            matrix[i][j] = 0;
        }
    }
}
```

维度参数必须在数组参数之前声明，编译器才能解释后面的类型。

---

## 十三、字符串
### 13.1 字符串字面量
C 字符串是以空字符 `\0` 结尾的字符序列：
```c
"Hello" // 实际包含 H e l l o \0，共 6 个字符
```

相邻的字符串字面量会在编译时连接：
```c
const char *message = "Hello, "
                      "world!";
```

字符串字面量不应被修改：
```c
const char *p = "Hello";
// p[0] = 'h'; // 未定义行为
```

### 13.2 字符数组与字符指针
```c
char array[] = "Hello";       // 创建可修改的数组副本
const char *pointer = "Hello"; // 指向字符串字面量
```

`array` 不能被重新赋值，但元素可以修改；`pointer` 可以改为指向其他字符串，但不应通过它修改字面量。

字符数组若没有 `\0` 就不是合法 C 字符串：
```c
char bad[3] = {'a', 'b', 'c'}; // 不是字符串
```

### 13.3 字符串输入与输出
```c
char line[100];

if (fgets(line, sizeof line, stdin) != NULL) {
    printf("%s", line);
}
```

`fgets` 最多读取 `size - 1` 个字符并添加 `\0`，如果空间足够还会保留换行符。可以移除换行：
```c
line[strcspn(line, "\n")] = '\0';
```

不要使用已从 C11 标准删除的 `gets`，它无法限制输入长度。

### 13.4 访问字符串
可以使用下标或指针遍历字符串：
```c
size_t count_spaces(const char *s) {
    size_t count = 0;
    while (*s != '\0') {
        if (*s == ' ') count++;
        s++;
    }
    return count;
}
```

### 13.5 字符串库
`<string.h>` 中常见函数如下：

| 函数 | 作用 |
| --- | --- |
| `strlen(s)` | 返回字符串长度，不含 `\0` |
| `strcpy(dst, src)` | 复制字符串 |
| `strcat(dst, src)` | 把字符串追加到末尾 |
| `strcmp(a, b)` | 按字典序比较字符串 |
| `strchr(s, ch)` | 查找字符 |
| `strstr(s, sub)` | 查找子串 |
| `strspn`、`strcspn` | 计算由指定字符集合构成或不构成的前缀长度 |
| `strtok` | 按分隔符切分字符串，会修改原字符串 |

```c
if (strcmp(name, "admin") == 0) {
    printf("Matched\n");
}
```

字符串不能用 `==` 比较内容，`==` 比较的是地址。

`strcpy` 和 `strcat` 不知道目标数组大小，调用者必须保证空间充足。处理外部输入时，优先使用带边界的设计，并在每次拼接前计算剩余空间。

### 13.6 字符串数组与命令行参数
字符串集合常用指针数组表示：
```c
const char *colors[] = {"red", "green", "blue"};
```

`main` 可以接收命令行参数：
```c
int main(int argc, char *argv[]) {
    for (int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }
    return 0;
}
```

`argc` 是参数数量，`argv` 是字符串指针数组；`argv[0]` 通常表示程序名，`argv[argc]` 保证为空指针。

---

## 十四、预处理器
### 14.1 工作原理
预处理器在编译前处理以 `#` 开头的指令，主要完成：
1. 头文件包含
2. 宏替换
3. 条件编译

预处理器处理的是**记号替换**，不了解 C 类型系统，因此宏尤其需要谨慎。

### 14.2 对象式宏
```c
#define BUFFER_SIZE 1024
#define PI 3.141592653589793
```

宏定义通常不加分号。若只是定义有类型的常量，在允许的场景中也可使用 `const` 对象或枚举常量。

### 14.3 函数式宏
```c
#define SQUARE(x) ((x) * (x))
```

参数和完整结果都应添加括号，否则运算符优先级可能改变含义：
```c
#define BAD_SQUARE(x) x * x
BAD_SQUARE(a + b) // 展开为 a + b * a + b
```

即使括号正确，宏参数也可能被求值多次：
```c
SQUARE(i++) // i 被修改两次，存在严重问题
```

能用普通函数或 `inline` 函数表达时，通常更安全。

### 14.4 `#` 与 `##` 运算符
`#` 把宏参数转换为字符串，`##` 拼接两个记号：
```c
#define STRINGIZE(x) #x
#define MAKE_NAME(prefix, number) prefix##number

const char *text = STRINGIZE(hello); // "hello"
int MAKE_NAME(value, 1) = 10;        // int value1 = 10;
```

### 14.5 预定义宏
常用预定义宏有：

| 宏 | 含义 |
| --- | --- |
| `__FILE__` | 当前源文件名 |
| `__LINE__` | 当前行号 |
| `__DATE__` | 编译日期 |
| `__TIME__` | 编译时间 |
| `__STDC__` | 实现符合标准时定义 |
| `__STDC_VERSION__` | 所支持 C 标准的版本值 |

C99 还提供 `__func__`，它是当前函数名对应的预定义标识符：
```c
printf("%s:%d %s\n", __FILE__, __LINE__, __func__);
```

### 14.6 条件编译
```c
#ifdef DEBUG
    printf("value = %d\n", value);
#endif
```

常用指令包括 `#if`、`#ifdef`、`#ifndef`、`#elif`、`#else`、`#endif`。`defined(NAME)` 可以在 `#if` 中检查宏是否定义。

头文件保护是条件编译的重要用途：
```c
#ifndef PROJECT_VECTOR_H
#define PROJECT_VECTOR_H

/* declarations */

#endif
```

### 14.7 其他指令
- `#error message`：主动产生编译错误
- `#line`：改变后续报告中的行号和文件名
- `#pragma`：向实现提供特定控制信息
- `_Pragma("...")`：可以出现在宏展开中的 C99 运算符形式

不同编译器支持的 `#pragma` 不同，使用时要考虑可移植性。

---

## 十五、大型程序
### 15.1 源文件与头文件
大型程序通常把**接口**放入 `.h` 文件，把**实现**放入 `.c` 文件：
```c
/* stack.h */
#ifndef STACK_H
#define STACK_H

#include <stdbool.h>

void stack_clear(void);
bool stack_push(int value);
bool stack_pop(int *value);

#endif
```

头文件中适合放：
- 函数声明
- 类型定义
- 宏和枚举常量
- 需要跨文件共享的 `extern` 声明

不要把普通外部变量定义或非 `inline` 函数定义直接放进头文件，否则多个源文件包含后容易产生重复定义。

### 15.2 `#include` 指令
```c
#include <stdio.h>  // 通常搜索实现提供的系统目录
#include "stack.h" // 通常先搜索当前项目目录
```

被包含的头文件也应自行包含它所依赖的头文件，使每个头文件可以独立使用。

### 15.3 多文件程序
一个对象通常只在某个 `.c` 文件中**定义一次**，在需要使用它的其他文件中通过头文件声明：
```c
/* config.h */
extern int log_level;

/* config.c */
#include "config.h"
int log_level = 1;
```

只供当前文件使用的函数和对象应声明为 `static`，避免污染外部命名空间。

### 15.4 构建与链接
```bash
cc -std=c99 -Wall -Wextra -Wpedantic -c main.c
cc -std=c99 -Wall -Wextra -Wpedantic -c stack.c
cc main.o stack.o -o app
```

编译错误发生在单个翻译单元内；链接错误通常来自：
- 声明了函数或对象，但没有提供定义
- 同一外部符号被定义多次
- 忘记链接所需对象文件或库
- 声明与定义不一致

### 15.5 `makefile`
`make` 根据依赖关系只重新构建发生变化的部分：
```makefile
app: main.o stack.o
	$(CC) main.o stack.o -o app

main.o: main.c stack.h
stack.o: stack.c stack.h
```

命令行开头必须是制表符。实际项目还会通过变量统一管理编译选项和目标文件。

---

## 十六、结构、联合与枚举
### 16.1 结构变量
结构把多个可能不同类型的成员组合成一个对象：
```c
struct Student {
    int id;
    char name[40];
    double score;
};

struct Student student = {1, "Hakimi", 95.5};
printf("%s %.1f\n", student.name, student.score);
```

C99 支持指定初始化：
```c
struct Student student = {
    .name = "Hakimi",
    .id = 1,
    .score = 95.5
};
```

同类型结构可以整体赋值、作为参数传递或作为返回值，但不能直接用 `==` 比较。

### 16.2 结构类型与别名
结构标记和 `typedef` 是两种常见命名方式：
```c
struct Point {
    double x;
    double y;
};

typedef struct {
    double x;
    double y;
} Point;
```

第一种使用 `struct Point`，第二种使用 `Point`。需要自引用结构时必须借助结构标记：
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

### 16.3 嵌套结构与结构数组
```c
struct Date {
    int year, month, day;
};

struct Event {
    char title[80];
    struct Date date;
};

struct Event events[100];
```

访问嵌套成员：
```c
events[0].date.year = 2026;
```

### 16.4 联合
联合的所有成员共享同一段存储空间，大小足以容纳最大成员：
```c
union Value {
    int integer;
    double real;
    char *string;
};
```

同一时刻只有最近写入的成员通常具有有效含义。为了记录当前保存的类型，常配合枚举构成**带标记联合**：
```c
enum ValueType { VALUE_INT, VALUE_DOUBLE, VALUE_STRING };

struct TaggedValue {
    enum ValueType type;
    union Value data;
};
```

### 16.5 枚举
枚举为一组整数常量命名：
```c
enum Color { RED, GREEN, BLUE };
enum Color color = GREEN;
```

默认从 `0` 开始递增，也可以显式指定：
```c
enum Permission {
    READ = 1,
    WRITE = 2,
    EXECUTE = 4
};
```

枚举提高可读性，但 C 通常不会阻止其他整数赋给枚举对象。

---

## 十七、指针的高级应用
### 17.1 动态存储分配
`<stdlib.h>` 提供动态内存函数：

| 函数 | 作用 |
| --- | --- |
| `malloc(size)` | 分配未初始化的内存 |
| `calloc(count, size)` | 分配并把所有位清零 |
| `realloc(ptr, size)` | 调整已有内存块大小 |
| `free(ptr)` | 释放内存 |

```c
size_t n = 100;
int *data = malloc(n * sizeof *data);
if (data == NULL) {
    return EXIT_FAILURE;
}

/* use data */
free(data);
data = NULL;
```

在 C 中不需要转换 `malloc` 的返回值；错误的转换反而可能掩盖没有包含 `<stdlib.h>` 的问题。

分配数组时要考虑乘法溢出：
```c
if (n > SIZE_MAX / sizeof *data) {
    /* size overflow */
}
```

### 17.2 动态字符串与数组
```c
char *copy_string(const char *source) {
    size_t length = strlen(source) + 1;
    char *copy = malloc(length);
    if (copy != NULL) {
        memcpy(copy, source, length);
    }
    return copy;
}
```

`realloc` 失败时原内存块仍然有效，因此应先保存到临时指针：
```c
int *new_data = realloc(data, new_count * sizeof *data);
if (new_data != NULL) {
    data = new_data;
}
```

### 17.3 释放内存与悬空指针
常见动态内存错误有：
- 忘记释放，造成内存泄漏
- 同一内存释放两次
- 释放后继续访问，形成悬空指针
- 越过分配区域读写
- 释放并非由分配函数返回的地址

`free(NULL)` 是安全的。把释放后的唯一指针设为 `NULL` 有助于避免误用，但不能自动处理指向同一对象的其他别名。

### 17.4 链表
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```

在表头插入节点：
```c
bool push_front(Node **head, int value) {
    Node *node = malloc(sizeof *node);
    if (node == NULL) {
        return false;
    }

    node->value = value;
    node->next = *head;
    *head = node;
    return true;
}
```

`p->member` 等价于 `(*p).member`。

删除整个链表时，要在释放当前节点前保存下一个指针：
```c
void clear_list(Node **head) {
    Node *current = *head;
    while (current != NULL) {
        Node *next = current->next;
        free(current);
        current = next;
    }
    *head = NULL;
}
```

### 17.5 指向指针的指针
二级指针常用于修改指针本身、管理动态二维结构或处理指针数组：
```c
void allocate(int **output, size_t n) {
    *output = malloc(n * sizeof **output);
}
```

使用输出参数时应明确所有权：由谁分配、谁释放、失败时输出值是什么。

### 17.6 函数指针
函数指针保存函数地址：
```c
int compare_int(const void *left, const void *right) {
    int a = *(const int *)left;
    int b = *(const int *)right;
    return (a > b) - (a < b);
}

qsort(data, count, sizeof data[0], compare_int);
```

声明形式为：
```c
int (*operation)(int, int);
```

函数指针可用于回调、查找表和策略选择。`qsort` 比较函数返回负数、零、正数分别表示小于、等于、大于；不要直接返回 `a - b`，因为可能溢出。

### 17.7 受限指针
C99 的 `restrict` 是给编译器的别名承诺：在该指针有效期间，相关对象主要通过它及派生指针访问。
```c
void add(size_t n,
         int result[restrict n],
         const int a[restrict n],
         const int b[restrict n]);
```

如果调用者违反承诺，行为未定义。只有能严格保证对象不重叠时才使用。

### 17.8 灵活数组成员
结构的最后一个成员可以是未指定长度的数组：
```c
struct Buffer {
    size_t length;
    unsigned char data[];
};

struct Buffer *buffer =
    malloc(sizeof *buffer + length * sizeof buffer->data[0]);
```

灵活数组成员不计入 `sizeof(struct Buffer)`，对象通常需要动态分配。

---

## 十八、声明
### 18.1 声明的组成
C 声明由**声明说明符**和**声明符**组成：
```c
static const unsigned long *values[10];
```

其中 `static const unsigned long` 是说明符，`*values[10]` 是声明符。复杂声明应从标识符开始，按照括号和运算符优先级向外阅读。

### 18.2 存储类型
常见存储类型说明符如下：

| 说明符 | 主要作用 |
| --- | --- |
| `auto` | 自动存储期，块内对象的默认值 |
| `static` | 静态存储期，或让文件作用域名称具有内部链接 |
| `extern` | 声明在其他位置定义的外部对象或函数 |
| `register` | 建议频繁访问，现代编译器通常自行决定 |

对象具有三个相关但不同的概念：
- **存储期**：对象何时存在
- **作用域**：名称在源代码的哪里可见
- **链接**：不同作用域或翻译单元中的声明是否指向同一实体

### 18.3 类型限定符
- `const`：不能通过该左值修改对象
- `volatile`：对象可能在程序不可见的情况下变化，每次访问都必须实际发生
- `restrict`：限定指针别名关系

`volatile` 不提供线程同步和原子性，不能代替互斥锁或 `<stdatomic.h>`。

### 18.4 解释复杂声明
```c
int *a[10];          // 含 10 个 int* 的数组
int (*b)[10];        // 指向含 10 个 int 的数组的指针
int (*f)(double);    // 指向函数的指针，该函数接收 double、返回 int
int *g(double);      // 函数，接收 double、返回 int*
```

当声明难以阅读时，用 `typedef` 分步表达：
```c
typedef int (*Comparator)(const void *, const void *);
Comparator compare;
```

### 18.5 初始化
具有静态存储期的对象在程序启动前初始化；未显式初始化时会进行零初始化。自动对象没有默认值：
```c
static int count; // 初始化为 0
int local;        // 值不确定
```

初始化式应与对象类型匹配。C99 的指定初始化可以让大型结构和数组更清楚，也减少成员顺序变化带来的影响。

### 18.6 内联函数
`inline` 建议编译器把调用替换为函数体，但是否内联由实现决定：
```c
static inline int max_int(int a, int b) {
    return a > b ? a : b;
}
```

头文件中的小型辅助函数常写成 `static inline`，避免外部定义规则带来的链接问题。内联的主要价值是允许优化，并不是保证消除函数调用。

---

## 十九、程序设计
### 19.1 模块
模块是具有明确职责的一组数据和操作。一个良好模块通常具有：
- **高内聚**：内部内容围绕同一目标
- **低耦合**：尽量少依赖其他模块的内部细节
- **小而稳定的接口**
- **隐藏的实现细节**

模块常由一个头文件和一个源文件组成，使用者只依赖头文件公开的接口。

### 19.2 信息隐藏
头文件公开“能做什么”，源文件保存“如何做到”：
```c
/* counter.h */
void counter_reset(void);
void counter_increment(void);
int counter_value(void);
```

```c
/* counter.c */
static int value;

void counter_reset(void) { value = 0; }
void counter_increment(void) { value++; }
int counter_value(void) { return value; }
```

`value` 被 `static` 隐藏，调用者无法绕过接口破坏约束。

### 19.3 抽象数据类型
抽象数据类型（ADT）通过接口描述一组值和操作，而不暴露内部表示。可以用不完整结构隐藏实现：
```c
/* stack.h */
typedef struct Stack Stack;

Stack *stack_create(void);
void stack_destroy(Stack *stack);
bool stack_push(Stack *stack, int value);
bool stack_pop(Stack *stack, int *value);
```

```c
/* stack.c */
struct Stack {
    int *data;
    size_t size;
    size_t capacity;
};
```

使用者只持有 `Stack *`，无法直接访问成员。实现可以从数组换成链表，而不改变客户端代码。

### 19.4 接口设计
设计 ADT 时需要明确：
1. 命名约定和操作语义
2. 谁拥有传入、返回的内存
3. 空对象和非法参数如何处理
4. 错误通过返回值、状态码还是终止程序报告
5. 是否允许同一对象被多个模块共享

通用 ADT 可以用 `void *` 保存任意对象，但会失去静态类型检查。另一种方法是使用宏为不同类型生成实现。

---

## 二十、底层程序设计
### 20.1 位运算符
位运算只适用于整数类型：

| 运算符 | 含义 |
| --- | --- |
| `~x` | 按位取反 |
| `x & y` | 按位与 |
| `x ^ y` | 按位异或 |
| `x \| y` | 按位或 |
| `x << n` | 左移 |
| `x >> n` | 右移 |

位掩码的常见操作：
```c
unsigned flags = 0;
unsigned mask = 1u << 3;

flags |= mask;        // 设置第 3 位
flags &= ~mask;       // 清除第 3 位
flags ^= mask;        // 翻转第 3 位
if ((flags & mask) != 0) {
    /* 第 3 位已设置 */
}
```

移位数量必须非负且小于类型位数。对有符号数移位有更多限制，底层位操作通常使用无符号类型。

### 20.2 位域
结构成员可以按位指定宽度：
```c
struct Status {
    unsigned ready : 1;
    unsigned error : 1;
    unsigned mode  : 3;
};
```

位域的布局、顺序和对齐依赖实现，适合节省内部标志空间，但不适合直接描述需要跨平台交换的文件或网络格式。

### 20.3 依赖机器的类型
与硬件寄存器或二进制协议交互时，使用 `<stdint.h>` 的固定宽度类型并明确字节序：
```c
uint32_t word;
uint8_t byte;
```

固定宽度类型只有在实现确实支持相应宽度时才会定义。`uint_least32_t` 和 `uint_fast32_t` 分别表示至少 32 位、适合快速运算的类型。

### 20.4 联合与对象表示
每个对象都可以通过 `unsigned char *` 查看它的字节表示：
```c
void print_bytes(const void *object, size_t size) {
    const unsigned char *bytes = object;
    for (size_t i = 0; i < size; i++) {
        printf("%02X ", bytes[i]);
    }
}
```

使用联合重新解释不同类型的可移植性有限。需要在对象表示之间复制时，`memcpy` 通常更清晰，也更符合严格别名规则。

### 20.5 指针作为地址
整数和指针之间的转换依赖实现。确有需要时可以使用 `<stdint.h>` 中可选的 `intptr_t`、`uintptr_t`，但普通程序不应把指针当作可随意计算的整数地址。

### 20.6 `volatile` 对象
内存映射硬件寄存器或被信号处理函数修改的简单对象可能需要 `volatile`：
```c
volatile unsigned int *status_register = /* platform address */;
while ((*status_register & READY_MASK) == 0) {
    /* wait */
}
```

`volatile` 只影响编译器对访问的优化，不保证访问是原子的，也不建立线程间的先后关系。

---

## 二十一、标准库
### 21.1 使用标准库
C 标准库通过头文件公开类型、宏和函数声明：
```c
#include <stdio.h>
#include <stdlib.h>
```

在调用库函数前包含正确头文件非常重要，否则参数和返回类型可能被错误解释。

常见标准头如下：

| 头文件 | 主要内容 |
| --- | --- |
| `<assert.h>` | 诊断断言 |
| `<ctype.h>` | 字符分类和大小写转换 |
| `<errno.h>` | 错误码 `errno` |
| `<float.h>` | 浮点类型范围与特性 |
| `<limits.h>` | 整数类型范围 |
| `<locale.h>` | 本地化信息 |
| `<math.h>` | 数学函数 |
| `<setjmp.h>` | 非局部跳转 |
| `<signal.h>` | 信号处理 |
| `<stdarg.h>` | 可变参数 |
| `<stdbool.h>` | 布尔类型宏 |
| `<stddef.h>` | `size_t`、`ptrdiff_t`、`NULL` 等 |
| `<stdint.h>` | 固定宽度整数类型 |
| `<stdio.h>` | 输入与输出 |
| `<stdlib.h>` | 内存、转换、排序等通用工具 |
| `<string.h>` | 字符串和内存块处理 |
| `<time.h>` | 日期与时间 |
| `<wchar.h>` | 宽字符与多字节字符 |
| `<wctype.h>` | 宽字符分类与转换 |

### 21.2 名称限制
标准库保留了一部分名称，程序不应自行定义：
- 任何包含两个连续下划线的标识符
- 任何以下划线和大写字母开头的标识符
- 文件作用域中以下划线开头的标识符
- 标准头声明的宏、类型和外部名称

因此项目内部名称不要模仿 `_Internal`、`__private` 这样的实现风格。

### 21.3 宏形式的库函数
部分库接口可能以宏实现，参数可能有特殊求值规则。若必须取得真实函数地址，可以用括号阻止函数式宏展开：
```c
int (*classifier)(int) = (isalpha);
```

不要对库函数名称做无根据的宏替换，也不要依赖某个实现恰好把接口实现为宏或函数。

### 21.4 C99 标准库更新
C99 新增或显著扩展了：
- `<stdbool.h>`、`<stdint.h>`、`<inttypes.h>`
- `<complex.h>`、`<tgmath.h>`、`<fenv.h>`
- `snprintf`、变长参数宏、宽字符接口
- 大量数学函数和浮点分类宏

编译时应明确标准版本，并用编译器警告检查可移植性：
```bash
cc -std=c99 -Wall -Wextra -Wpedantic program.c
```

---

## 二十二、输入与输出
### 22.1 流
C 把输入与输出抽象为**流**。程序启动时通常已有三个文本流：

| 流 | 宏 | 默认设备 |
| --- | --- | --- |
| 标准输入 | `stdin` | 键盘 |
| 标准输出 | `stdout` | 终端 |
| 标准错误 | `stderr` | 终端 |

流由 `FILE *` 表示。文本流可能对换行和文件末尾进行平台相关转换；二进制流尽量保持字节不变。

### 22.2 打开与关闭文件
```c
FILE *file = fopen("data.txt", "r");
if (file == NULL) {
    perror("data.txt");
    return EXIT_FAILURE;
}

/* use file */

if (fclose(file) == EOF) {
    /* 关闭或刷新失败 */
}
```

常用模式：

| 模式 | 含义 |
| --- | --- |
| `"r"` | 只读，文件必须存在 |
| `"w"` | 只写，创建或截断文件 |
| `"a"` | 追加，创建或写到末尾 |
| `"r+"` | 读写，文件必须存在 |
| `"w+"` | 读写，创建或截断 |
| `"a+"` | 读取并追加 |

添加 `b` 表示二进制模式，例如 `"rb"`、`"wb"`。

`freopen` 可以把已有流重新关联到文件；`tmpfile` 创建会在关闭时自动删除的临时文件。

### 22.3 文件缓冲
标准 I/O 通常有缓冲：
- 全缓冲：缓冲区满时写出
- 行缓冲：遇到换行时写出
- 无缓冲：尽快写出

`fflush(stream)` 把输出缓冲写入目标。`fflush(NULL)` 刷新所有输出流。不要用 `fflush(stdin)` 清空输入，它没有标准定义。

程序正常终止时会刷新并关闭流，但仍应显式检查关键文件的 `fclose`，因为磁盘写入错误可能到最后才出现。

### 22.4 格式化 I/O
文件版格式化函数：
```c
fprintf(file, "id=%d score=%.2f\n", id, score);
fscanf(file, "%d%lf", &id, &score);
```

字符串版格式化函数：
```c
char buffer[100];
int length = snprintf(buffer, sizeof buffer,
                      "id=%d score=%.2f", id, score);
```

`snprintf` 最多写入 `size - 1` 个字符并添加终止符（当 `size > 0`）。返回值是不受截断时本应写入的字符数，因此可以检测空间是否足够：
```c
if (length < 0 || (size_t)length >= sizeof buffer) {
    /* encoding error or truncation */
}
```

### 22.5 字符与行 I/O
```c
int ch;
while ((ch = fgetc(file)) != EOF) {
    fputc(ch, stdout);
}

if (ferror(file)) {
    /* read error */
}
```

字符输入函数返回 `int`，这样才能同时表示所有 `unsigned char` 值和 `EOF`。不要用 `char` 接收 `fgetc` 返回值。

行输入输出使用：
```c
char line[256];
while (fgets(line, sizeof line, file) != NULL) {
    fputs(line, stdout);
}
```

### 22.6 块 I/O
二进制对象或字节块可以用 `fread`、`fwrite`：
```c
size_t written = fwrite(data, sizeof data[0], count, file);
size_t read = fread(data, sizeof data[0], capacity, file);
```

返回值是成功处理的**元素数量**。直接写入结构体会受到填充、字节序和类型表示影响，不适合可移植文件格式；跨平台格式应显式编码每个字段。

### 22.7 文件定位
- `fseek`：移动文件位置
- `ftell`：获取当前位置
- `rewind`：回到文件开头并清除错误状态
- `fgetpos`、`fsetpos`：保存和恢复位置

```c
if (fseek(file, 0, SEEK_END) == 0) {
    long size = ftell(file);
}
```

文本流对 `fseek` 的合法偏移有限；二进制流更适合随机访问。大文件还要考虑实现对 `long` 范围的限制。

### 22.8 文件末尾与错误
读取函数失败后，用下面两个函数区分原因：
```c
if (feof(file)) {
    /* reached end of file */
} else if (ferror(file)) {
    /* input/output error */
}
```

`clearerr(file)` 清除文件末尾和错误标志。不要使用 `while (!feof(file))` 作为读取条件，因为文件末尾标志只有在一次读取失败后才会设置。

---

## 二十三、数值与字符数据的库支持
### 23.1 `<float.h>`
`<float.h>` 描述浮点实现的范围和精度：

| 宏 | 含义 |
| --- | --- |
| `FLT_DIG`、`DBL_DIG` | 可无损往返的十进制有效位数 |
| `FLT_MIN`、`DBL_MIN` | 最小正规格化正值 |
| `FLT_MAX`、`DBL_MAX` | 最大有限值 |
| `FLT_EPSILON`、`DBL_EPSILON` | `1` 与下一个可表示值之差 |
| `FLT_RADIX` | 浮点表示的基数 |

这些宏比假定某个平台一定使用特定 IEEE 格式更可移植。

### 23.2 `<limits.h>`
`<limits.h>` 给出整数类型范围：
```c
printf("int: %d to %d\n", INT_MIN, INT_MAX);
printf("unsigned int max: %u\n", UINT_MAX);
```

常见宏包括 `CHAR_BIT`、`CHAR_MIN`、`CHAR_MAX`、`SHRT_MIN`、`LONG_MAX`、`ULLONG_MAX` 等。

### 23.3 `<math.h>`
常见数学函数：

| 分类 | 函数示例 |
| --- | --- |
| 三角函数 | `sin`、`cos`、`tan`、`asin` |
| 指数与对数 | `exp`、`log`、`log10`、`log2` |
| 幂与根 | `pow`、`sqrt`、`cbrt`、`hypot` |
| 取整 | `ceil`、`floor`、`trunc`、`round` |
| 余数 | `fmod`、`remainder` |
| 绝对值 | `fabs` |
| 最大最小 | `fmax`、`fmin` |

许多系统使用数学库时需要显式链接：
```bash
cc program.c -lm
```

函数通常有 `float`、`double`、`long double` 三个版本，例如 `sinf`、`sin`、`sinl`。

### 23.4 浮点分类与比较
C99 提供分类宏：
```c
isfinite(x)
isinf(x)
isnan(x)
isnormal(x)
fpclassify(x)
```

NaN 与任何值（包括自身）做相等比较都为假。处理可能出现 NaN、无穷或上下溢的计算时，应显式检查分类结果和错误报告方式。

### 23.5 `<ctype.h>`
字符分类函数包括：

| 函数 | 检查内容 |
| --- | --- |
| `isalpha` | 字母 |
| `isdigit` | 十进制数字 |
| `isalnum` | 字母或数字 |
| `isspace` | 空白字符 |
| `isupper`、`islower` | 大写、小写字母 |
| `isxdigit` | 十六进制数字 |
| `ispunct` | 标点字符 |
| `isprint`、`isgraph` | 可打印、图形字符 |

`toupper`、`tolower` 进行大小写转换。参数必须是 `EOF` 或可表示为 `unsigned char` 的值。

### 23.6 `<string.h>` 的内存函数
除字符串函数外，`<string.h>` 还提供不依赖 `\0` 的内存块操作：
```c
memcpy(destination, source, size);  // 对象不能重叠
memmove(destination, source, size); // 允许重叠
memset(buffer, 0, size);
memcmp(left, right, size);
memchr(buffer, value, size);
```

`memset` 按**字节**填充。除全零等特定情况外，不要用它把整数数组设置为某个非零整数值。

---

## 二十四、错误处理
### 24.1 `<assert.h>`
断言用于检查程序员认为必然成立的内部条件：
```c
#include <assert.h>

double average(const int *data, size_t n) {
    assert(data != NULL);
    assert(n > 0);
    /* ... */
}
```

定义 `NDEBUG` 后，`assert` 会被禁用。因此断言表达式不能包含程序所需的副作用，也不应用于检查用户输入、文件是否存在等运行时可恢复错误。

### 24.2 `<errno.h>`
某些库函数失败时会把错误码存入 `errno`。只有函数已经明确报告失败后，`errno` 才有意义：
```c
errno = 0;
char *end;
long value = strtol(text, &end, 10);

if (errno == ERANGE) {
    /* out of range */
}
```

`perror` 根据当前 `errno` 输出说明，`strerror(errno)` 返回错误消息字符串：
```c
FILE *file = fopen(path, "r");
if (file == NULL) {
    fprintf(stderr, "%s: %s\n", path, strerror(errno));
}
```

### 24.3 信号
`<signal.h>` 提供异步事件的基本处理：
```c
volatile sig_atomic_t interrupted = 0;

void handle_signal(int signal_number) {
    interrupted = 1;
}

signal(SIGINT, handle_signal);
```

标准信号包括 `SIGINT`、`SIGTERM`、`SIGABRT`、`SIGFPE`、`SIGILL`、`SIGSEGV`。信号处理函数能安全执行的操作非常有限，通常只修改 `volatile sig_atomic_t` 对象，然后让正常控制流完成清理。

可以用 `raise(SIGINT)` 向当前程序发送信号。`signal` 的具体语义在不同平台上有差异，复杂系统程序常使用平台提供的更完善接口。

### 24.4 非局部跳转
`setjmp` 和 `longjmp` 可以跨越多层函数调用恢复控制：
```c
jmp_buf environment;

if (setjmp(environment) == 0) {
    /* normal path */
} else {
    /* returned through longjmp */
}
```

它们会绕过普通返回路径，容易跳过资源释放并使局部变量状态难以理解。除解析器、解释器等特殊场景外，应优先使用普通错误返回值和集中清理。

---

## 二十五、国际化特性
### 25.1 本地化
默认的 C 本地环境是 `"C"`。`setlocale` 可以查询或修改本地化类别：
```c
#include <locale.h>

setlocale(LC_ALL, ""); // 使用实现从环境中选择的本地设置
```

常见类别有 `LC_COLLATE`、`LC_CTYPE`、`LC_MONETARY`、`LC_NUMERIC`、`LC_TIME`。改变全局 locale 会影响多个库函数，在多线程程序中要格外谨慎。

`localeconv` 返回 `struct lconv *`，其中保存小数点、千位分隔符、货币符号等格式信息。

### 25.2 多字节字符与宽字符
- **多字节字符**：一个字符由一个或多个 `char` 字节编码，例如 UTF-8
- **宽字符**：使用 `wchar_t` 表示的字符值

```c
wchar_t ch = L'中';
const wchar_t *text = L"中文";
```

`mbrtowc`、`wcrtomb` 进行单个字符转换；`mbsrtowcs`、`wcsrtombs` 进行字符串转换。转换依赖当前 locale 和 `mbstate_t` 状态对象。

`wchar_t` 的大小和编码由实现决定，不能假定它一定是 Unicode 码点，也不能假定所有 Unicode 字符都能用一个 `wchar_t` 表示。

### 25.3 UTF-8
UTF-8 使用 1–4 个字节编码 Unicode 码点，并与 ASCII 兼容。对 UTF-8 字符串：
- `strlen` 返回字节数，不是字符数量
- 随机下标可能落在一个字符的中间
- 用户感知的“字符”还可能由多个码点组合而成

标准 C99 提供的是通用多字节/宽字符模型，并不直接提供完整 Unicode 文本分割、正规化等高级操作。

### 25.4 双字符与三字符
早期字符集可能缺少 `{`、`}`、`#` 等字符，因此 C 提供过三字符和双字符替代写法。现代环境几乎不需要三字符，并且 C23 已删除三字符支持。

`<iso646.h>` 为部分运算符提供拼写替代宏，例如 `and`、`or`、`not`、`bitand`。

### 25.5 宽字符 I/O
`<wchar.h>` 提供宽字符版本的 I/O 和字符串函数：
```c
wprintf(L"%ls\n", L"你好");
```

流一旦进行字节 I/O 或宽字符 I/O 后会具有方向，混合两种方向可能出错。`fwide` 可以查询或设置流方向。

常见宽字符串函数为 `wcslen`、`wcscpy`、`wcscat`、`wcscmp`、`wcschr`；`<wctype.h>` 提供 `iswalpha`、`towlower` 等宽字符分类和映射函数。

---

## 二十六、其他库函数
### 26.1 可变参数
`<stdarg.h>` 允许函数接收数量不定的参数：
```c
#include <stdarg.h>

double average(size_t count, ...) {
    va_list arguments;
    va_start(arguments, count);

    double sum = 0.0;
    for (size_t i = 0; i < count; i++) {
        sum += va_arg(arguments, double);
    }

    va_end(arguments);
    return sum / count;
}
```

可变部分没有自动的类型和数量信息，函数必须通过固定参数或格式串获得约定。`float` 会提升为 `double`，`char` 和 `short` 会提升为 `int`。用错误类型调用 `va_arg` 会产生未定义行为。

转发参数列表时使用 `va_copy` 创建独立副本，并对每个副本调用 `va_end`。

### 26.2 数值转换
不要优先使用无法报告错误的 `atoi`、`atof`。`strtol`、`strtoul`、`strtod` 等函数能报告解析结束位置和范围错误：
```c
char *end;
errno = 0;
long value = strtol(text, &end, 10);

if (end == text) {
    /* no digits */
} else if (errno == ERANGE) {
    /* out of range */
} else if (*end != '\0') {
    /* trailing characters */
}
```

### 26.3 伪随机数
```c
srand((unsigned)time(NULL));
int value = rand();
```

`rand` 产生的是伪随机序列，不适合密码学。`rand() % n` 还可能有分布偏差；安全或统计质量要求较高时，应使用平台或专业库提供的随机接口。

### 26.4 与执行环境通信
- `getenv(name)`：读取环境变量
- `system(command)`：交给宿主环境执行命令
- `atexit(function)`：注册正常终止时调用的函数
- `exit(status)`：正常终止并清理标准库资源
- `abort()`：异常终止

`system` 会引入命令注入和平台差异，不要把不可信输入拼入命令字符串。

### 26.5 搜索与排序
```c
qsort(array, count, sizeof array[0], compare);

int *found = bsearch(&key, array, count,
                     sizeof array[0], compare);
```

`bsearch` 要求数组已经按同一个比较函数排序。比较函数必须形成一致的顺序关系。

### 26.6 整数算术
`abs`、`labs`、`llabs` 返回绝对值；`div`、`ldiv`、`lldiv` 同时返回商和余数：
```c
div_t result = div(17, 5);
printf("%d remainder %d\n", result.quot, result.rem);
```

最小有符号整数的绝对值可能无法由同一类型表示，要注意溢出边界。

### 26.7 日期与时间
`time_t` 表示日历时间，`clock_t` 表示处理器时间：
```c
time_t now = time(NULL);
struct tm *local = localtime(&now);

char buffer[100];
strftime(buffer, sizeof buffer, "%Y-%m-%d %H:%M:%S", local);
printf("%s\n", buffer);
```

常用函数：

| 函数 | 作用 |
| --- | --- |
| `time` | 获取当前日历时间 |
| `difftime` | 计算两个日历时间之差 |
| `mktime` | 把本地分解时间转换为 `time_t` |
| `localtime` | 转换为本地分解时间 |
| `gmtime` | 转换为 UTC 分解时间 |
| `asctime`、`ctime` | 转换为固定格式字符串 |
| `strftime` | 按格式生成时间字符串 |
| `clock` | 获取处理器时间 |

`localtime`、`gmtime`、`ctime` 等函数可能返回指向共享静态对象的指针，后续调用会覆盖内容；多线程程序应使用平台提供的可重入版本或及时复制结果。

---

## 二十七、C99 对数学计算的新增支持
### 27.1 `<stdint.h>`
`<stdint.h>` 定义多组整数类型：
```c
int8_t value8;          // 恰好 8 位，如果实现支持
uint32_t value32;       // 恰好 32 位
int_least16_t compact;  // 至少 16 位、空间较小
uint_fast32_t fast;     // 至少 32 位、运算较快
intptr_t address_value; // 可容纳对象指针，如果实现支持
intmax_t widest;        // 最宽的有符号整数类型
```

对应的范围宏有 `INT32_MIN`、`INT32_MAX`、`UINT32_MAX` 等。构造常量时可使用 `INT64_C(123)`、`UINT32_C(10)`。

### 27.2 `<inttypes.h>`
固定宽度类型的底层实际类型可能因平台而异，因此格式化时使用宏：
```c
#include <inttypes.h>

int64_t value = INT64_C(123456789);
printf("%" PRId64 "\n", value);
```

读取时使用 `SCNd64` 等 `SCN...` 宏。该头文件还提供 `strtoimax`、`strtoumax`、`imaxabs`、`imaxdiv`。

### 27.3 复数
C99 提供复数类型：
```c
#include <complex.h>

double complex z = 1.0 + 2.0 * I;
double real_part = creal(z);
double imaginary_part = cimag(z);
```

`float complex`、`double complex`、`long double complex` 分别对应不同精度。普通算术运算符可以直接用于复数。

### 27.4 `<complex.h>`
复数库提供：
- `cabs`：复数绝对值
- `carg`：相角
- `conj`：共轭
- `cproj`：投影
- `cexp`、`clog`、`cpow`、`csqrt`
- `csin`、`ccos`、`ctan` 及双曲、反函数版本

大部分函数也有 `f`、`l` 后缀版本，例如 `cabsf`、`cabsl`。

### 27.5 `<tgmath.h>`
类型泛型数学宏根据参数类型选择合适函数：
```c
#include <tgmath.h>

double d = sqrt(2.0);            // 调用 double 版本
float f = sqrt(2.0f);            // 选择 float 版本
double complex z = sqrt(1.0 + I); // 选择 complex 版本
```

它减少了手动选择 `sqrtf`、`sqrt`、`sqrtl` 或 `csqrt` 的工作，但调试宏展开时可能不如显式函数名直观。

### 27.6 `<fenv.h>`
浮点环境包括异常状态标志和舍入方向。程序若要观察这些状态，需要允许实现保留浮点环境访问：
```c
#include <fenv.h>
#pragma STDC FENV_ACCESS ON

feclearexcept(FE_ALL_EXCEPT);
double result = calculation();

if (fetestexcept(FE_OVERFLOW)) {
    /* overflow occurred */
}
```

常见异常宏有 `FE_DIVBYZERO`、`FE_INEXACT`、`FE_INVALID`、`FE_OVERFLOW`、`FE_UNDERFLOW`。常见舍入方向有 `FE_TONEAREST`、`FE_DOWNWARD`、`FE_UPWARD`、`FE_TOWARDZERO`。

相关函数包括：
- `feclearexcept`、`feraiseexcept`、`fetestexcept`
- `fegetround`、`fesetround`
- `fegetenv`、`fesetenv`、`feholdexcept`、`feupdateenv`

编译器的快速数学优化可能忽略严格浮点环境语义，需要结合实现文档与编译选项使用。

