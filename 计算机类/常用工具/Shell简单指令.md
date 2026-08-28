# Shell的一些简单指令

---
本篇算是对上一个文档的一个细致补充和整理，本文档的来源为 MIT 的 Missing Semester 这里的内容都是在Linux的终端运行的。由于每个用户的计算机存储内容是不一样的，所以下面的路径内容可能会有不同，核心命令是一样的

---
## 零、`man`
本文件已经尽可能详细讲解 shell 的各种常用命令，但是计算机的知识博大精深，我们还是
无法完全覆盖，因此读者在学习时如果想更深入了解，请用`man`命令
例：
```bash
man date
```
即会出现所有有关`date`的用法，看完后按 `q + 回车`退出即可。

---

## 一、`cd`
`cd` 应该熟悉，用来**切换到对应的目录**
1. **绝对路径**
   ```Bash
   cd /
   cd /~
   cd /bin
   cd /bin/home
   cd ~/bin/date
   cd ~/bin/sh
   ```
   相当于是地球的经纬度，以 root 根目录 `/` 
   
   单独的`cd ~/`和`cd ~`没有本质区别，但是如果想要在`~`后继续进入其他文件夹，就必须用`cd ~/`,因此推荐统一用`cd ~/`

   `/`叫做根目录 root，一般来说它就是整个文件系统的起点,`/`目录下有很多文件夹，而根目录 root 与家目录 home 的关系为`/Users/~/`
   
   我们电脑的目录大概是这样的（以Mac OS为例）：
   ```bash
   singlemie@singlemiedeMacBook-Pro / % ls
   Applications	dev		Library		sbin		Users		Volumes
   bin		etc		opt		System		usr
   cores		home		private		tmp		var
   singlemie@singlemiedeMacBook-Pro / % cd Users
   singlemie@singlemiedeMacBook-Pro /Users % ls
   Shared		singlemie
   singlemie@singlemiedeMacBook-Pro /Users % cd singlemie
   ```
2. **相对路径**
   ```Bash
   # 假设我们现在在 ~ 目录下
   cd bin   # 进入了 ~/bin
   cd date  # 进入了 ~/bin/date
   cd .     # 还是在 ~/bin/date
   cd ..    # 转到现在目录的父目录(parent dictionary)，也就是回到了 ~/bin
   ```
   cd 可以通过使用绝对路径和相对路径进行快速的切换 dict。当然，如果你足够闲的话，你也可以这样干：
   ```Bash
   USERNAME:/$ cd ~/bin/./../bin/date/./../../.    #这样你就又回到了家目录 ~
   ```
---
## 二、`echo`
`echo` 主要用于**标准输出中现实文本行或者是字符串**
1. 核心功能：
   `echo` 负责将传递给它的参数转换成字符穿，并发送至输出流，在环境中有两种形式：
   - **内置命令**：当你在 terminal 输入 echo 的时候运行的就是系统内置的 `echo` 实现
   - **独立的二进制文件**：这个位于文件系统中，主要用于兼容性或特定环境：
      ```Bash
      /usr/bin/echo  # 这里是系统内置的实现
      /bin/echo      # 这个就是第二点的例子
      ```

2. 核心语法：
   `echo` 的标准调用如下：
   `echo [选项][字符串]`
   常用选项：
   - **-n**：抑制末尾的自动换行符。默认情况下，`echo` 在输出内容后会附加一个换行符，该选项可取消此行为。
   - **-e**：激活反斜杠转义字符的解释功能。
   - **-E**：禁用反斜杠转义字符（默认设置）。

   在默认情况下，`echo` 是会将空白符(space)视为分隔符的，也就是说，当我们没有使用引号进行引用的时候，后面的字符串使用的空格就会被视为是分割符：
   ```Bash
   echo Hello world     # Hello world
   echo hello       world     # hello world，只有一个空格，因为没有引用，中间的空格都被视为了分隔符
   echo hello\ \ \ world   # hello   world，中间有三个空格
   echo "hello     world"  # hello     world，有了""进行引用，里面的所有内容都会被视为是字符
   echo -e "hello          world"   # hello world，有了 -e 选项，里面的空格又重新视为了分隔符
   ```

3. 场景示例：打印`$PATH`
   ```Bash
   USERNAME:/$ echo $PATH
   ·········
   ·········   # 一系列路径
   ```
---
## 三、环境变量 $PATH:
环境变量PATH的重要功能就是**检索路径**，`echo $PATH` 后出现的一大片的路径就是PATH的遍历顺序，当我们使用程序的时候，计算机会从PATH的根目录出发，从左到右遍历寻找目标文件，找到了就执行，没找到返回错误

---
## 四、`date`
`date` 是一个**用来查询时间的一个程序**，当我们在终端输入该指令的时候，就会返回现在的时间
```Bash
USERNAME:/$ date
# WEEK MONTH DAY HOUR:MINUTE:SECOND TIME_ZONE TIME_DIFF
> YYYY-MM-DDTHH:mm:ssZ  # 完整格式
> YYYY-MM-DD            # 基本格式
```
---
## 五、`which`
`which` 是一个**程序**，他会遍历 PATH 列表并打印出它首次找到的程序位置
```Bash
which date
/usr/bin/date   # 返回了 date 的文件路径
which which
/usr/bin/which     # 返回了 which 的文件路径 
```
`which` 返回的是在 `$PATH` 中的路径，但是返回的是**首次找到的路径**，当我们想打印所有的参数，我们可以使用**选项(option)**，在 which 的后面跟一个 `-a` (all)
```Bash
which -a sh
/usr/bin/sh
/bin/sh
```
---
## 六、`ls`
`ls` 是 lizhist 的缩写，**也是一个程序**，其功能就是**列出指定文件夹的所有内容（包括文件夹和文件）**：
```Bash
cd /bin     # 转到 / 下的 bin 文件夹
ls          # 列出当前目录中的所有文件
ls /usr/bin # 直接列出后面目录下的所有文件
```
---
## 七、`cat`
`cat` 是一个**程序**，用来打印文件
1. 功能：
   `cat` 主要实现三种操作：
   - Reading（读取）：在终端显示单个或多个文件的内容。
   - Concatenating（连接）：将多个文件的内容合并，并定向输出到一个新文件中。
   - Creating（创建）：利用重定向功能快速创建简易文件。

2. 命令格式：
   `cat [option] [FILENAME]`

3. 样例：
   ```Bash
   cat /mnt/c/Users/LENOVO/Desktop/greet.cpp
   <!-- #include <iostream>
      using namespace std;
      int main() { cout << "Hello, world" << endl; } -->
   ```
---
## 八、`nvim`
`nvim` 全称**Neovim**，是一个基于**Vim**的文本编辑器，这里只讲解如何安装（因为大多数 shell自带vim，而非nvim），详情会有专门的笔记
```bash
#macOS
#如果已经安装homebrew
brew install neovim
#成功后
nvim --version #验证
#如果没安装过homebrew
curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh -o install.sh
bash install.sh   #安装homebrew
source ~/.zprofile #刷新
brew install neovim

#linux或者是WSL2
#法一：直接使用系统自带的安装包（版本较老
sudo apt update
sudo apt install neovim
#法二：使用 snap 工具
sudo snap install nvim --classic

#注意，如果你使用的是WSL2，可能会出现不支持 snap 的问题，可以直接执行下面的指令
sudo nano /ect/wsl.conf     # 这样你就进入了一个编辑界面,然后CV下面的代码
[boot]
systemd=true
# CV 完成后再用 Ctrl + O 保存，再 Ctrl + X 退出
#完成上述步骤以后就可以回到PowerShell中，输入下面的命令
wsl --shutdown    # 更新一下
#完成后回到 Ubuntu 中，运行：
systemctl is-system-running
#> running 或 degraded 就成功了，再运行上面的 snap 即可
```
---
## 九、`sort` 和 `uniq`
`sort`是**用来排序的程序**，`uniq`用来**去除连续重复的数据**(意味着如果重复但不连续就会都打印出来，可仔细观察下方示例)，我们可以将两个结合：
```Bash
sort -u data     # 这个 data 是我们的一个文本，里面会有一些数据
```
这里的 `-u` 是 `sort` 的一个 option，不加的话也没有事情
`sort` 是**根据字典序进行排序的**，也就是说会出现数值大小对不上的问题
```bash
--- txt文件提供数据
# data
1
1
1
2
1
56
14
35
doro
knight
apple
---

USERNAME:/$ sort data
1
1
1
1
14
2
35
56
apple
doro
knight

USERNAME:/$ uniq data
1
2
1
56
14
35
doro
knight
apple

USERNAME:/$ sort -u data
1
14
2
35
56
apple
doro
knight
```
---
## 十、`head`和`tail`
`head`和`tail`都是**在文件中取数据的程序**，**默认会取10行**

`head`是从头开始读，`tail`是从末尾读

我们也可以使用 `-n` 来指定取的行数
```Bash
head -n1 data
1

head -n3 data
1
2
56

tail -n3 data
doro
knight
apple
```

`head`和`tail`取出来的数据都是**正序**，即**跟原来文件的顺序是一样的**
---
## 十一、`grep`
`grep` 是一个**在文件中找到所有你给出的指定特征的程序**，注意范围是**文件内**，grep的强大不仅在于可以进行我们给出的内容，还可以找到带有这个特征的内容
```Bash
USERNAME:/$ grep 1 data
1
14
```

`grep` 还有一个非常好用的option：`-r`，这里的 `-r` 表示递归（recursion），他会递归你给出的目录下的所有相关文件
```Bash
USERNAME:/$ cd DICT
grep i greet.cpp
#include <iostream>
#using namespace std;
#int main() { cout << "Hello, world" << endl; }

#我的Ubuntu会将上方的输出标注为红色

USERNAME:/$ grep bin /     # 这里不建议这样做，运行时间长，并且“很壮观”
···
···
···
```
---
## 十二、`sed`
`sed` 是一个**流编辑器**，`grep` 是进行查找，而`sed`就是对文本内容进行操作了：
```Bash
# 假设你有一个有很多带有 'doro' 字符样式的 TXT 文件
sed -i 's/doro/knight/g' */*.md
```
```bash
#在 macOS中，这条命令需要在 -i 后加上 ''
sed -i '' 's/doro/knight/g' */*.md
```
```bash
#这样当前目录下的所有子目录中的所有以 .md 结尾的文件中的 'doro' 都会被替换成 'knight'
```
这个命令很复杂，我们一点点看：
- `sed` 流编辑器
- `-i` 表示原地替换
- `'s/···/···/g'` 是*替换命令**结构
   - `s`: 表示**替换**
   - `/doro/`：这个是**匹配模式**，就是你想要替换的内容
   - `/knight/`: 这个是**替换内容**，你的目标内容
   - `g`：表示**Global**全局，不加上 g 只会替换掉每行第一个出现的待替换内容
- `*/*.md` 这个是**Glob**通配符，表示匹配当前目录下所有子目录中的所有以 .md 结尾的 Markdown 文件

对这里的命令格式化就是：
`s/pattern/replacement/`，其中，`pattern`部分就是**正则表达式[^1]**，我们用来**定位我们要操作的对象**，
`*/*.md`，这部分是**通配符**[^2]

---
## 十三、 `find`
`find`命令表示在目录树里递归查找文件，并对他们进行操作

基本结构：
```bash
find [路径] [条件] [操作]
```
常见操作：
```bash
find .   # 在当前目录找文件
find . -name "*.py" #按名字找所有 python 文件
find . -type f  #只文件(file)
find . -type d  #只目录(dictionary)
find . -mtime -1 #最近一天
find . -mtime 1 #一到两天
find . -mtime +1 #超过一天
find . -size +100m #大于100MB
find . -size -10k #小于10KB
```
以上均是单个条件的命令，接下来介绍一些组合和复杂操作
```bash
find . -name "*.py" -type -f #找同时满足是.py且是文件,find默认是 and
# 条件部分的命令顺序执行，一般在没有or的情况下顺序可以随意更换
# or条件：
find .\( -name "*.py" -o -name "*.txt" \)  #注意空格，\( 和 \)是转义括号，不能分开
#执行操作
find . -name "*.txt" -delete #删除文件
find . -name "*.py" -exec ls -l {} \; #{} = 当前找到的文件路径 \防止shell提前解释， ; 是结束-exec命令
find . -name "*.py" -exec ls -l {} + #\;表示每个文件执行一次，+表示一次性批量执行
```
---
## 十四、 `awk`
`awk` = 按行读取 + 按列处理 + 条件判断 + 执行动作
基本结构：
```bash
awk '条件 { 动作 }' 文件
NR  #第几行(行号)
$1 # 第一列
$2 # 第二列
$0 # 整行
```
基础用法：
```bash
awk '{ print }'files.txt  #打印整行,等价于cat
awk '{ print $1,$2}' files.txt #打印某列(这里awk默认以空格分隔列)
awk '$1 > 10 { print }' files.txt #打印第一列大于10的行
awk '{ print "value:",$1}' files.txt #自定义输出
awk  '{count++} END {print count}' files.txt #统计行数，count默认初始值就是0
awk -F ',' '{print $1}' files.txt #改为用逗号分割
awk  '{print NR,$0}' files.txt #给输出加行号
```
---
## 十五、shell中的 if,for,while
`shell`中同样有执行条件语句，循环语句，下面做简单介绍
1. `if`
```bash
#传统写法 [] (>表示重定向，无法使用)
if [条件1];then
   ...
else if [条件2];then
   ...
else 
   ...
fi
#现代写法 [[]] (>等符号本质表示字符串，无法比较数值)
if [[条件1]];then
   ...
else if [[条件2]];then
   ...
else 
   ...
fi
#数值计算专用写法(>可进行数值比较)
if ((条件1));then
   ...
else if ((条件2));then
   ...
else 
   ...
fi
```
**注：条件写法(if,while通用)**
   1. 数值比较
   ```bash
   -eq # ==
   -ne # !=
   -gt # >
   -ls # <
   -ge # >=
   -le # <=
   #例：
   if [ "$a" -gt 10];then
      echo "big"
   fi
   ```
   2. 字符串比较
   ```bash
   =  #等于
   != #不等于
   #即字符串判断与其他编程预言一致
   ```
   3. 文件判断
   ```bash
   -f file #是否是文件
   -d dir  #是否是目录
   -e path #是否存在
   ```
**注：重要坑**
```bash
[ "$a" = "b"] #✅
[ "$a"="b" ]  #❌必须有空格
```
2. `while`
```bash
# 这里是分行命令
while 条件; do
   命令
done

```
3. `for`
```bash
for i in 列表;do
   命令
done
```

一般来说更推荐把 shell 的if ,for ,while 等内容写在`.sh`文件中,可读性好，可复用，具体写法后续会继续介绍

[^1]: **正则表达式**：缩写为**Regex**或**Regexp**。 它不是一种编程语言，而是一种强大的**文本搜索与处理工具**。
      正则表达式主要就是三点：
      - **测试模式**：检查一个字符串是否符合某种规则
      - **查找匹配**：从大量文本中提取出符合规则的子字符串。
      - **替换文本**：识别特定的模式并将其替换为其他内容。
        | 符号    | 名称        | 描述 (Description)                                  | 示例                                  |
        | :------ | :---------- | :-------------------------------------------------- | :------------------------------------ |
        | `.`     | 任意字符    | 匹配除换行符以外的**任意单个字符**。                | `a.c` 匹配 `abc`, `a2c`               |
        | `^`     | 行首锚定    | 匹配字符串或行的**开始位置**。                      | `^Hello` 匹配以 Hello 开头的行        |
        | `$`     | 行尾锚定    | 匹配字符串或行的**结束位置**。                      | `end$` 匹配以 end 结尾的行            |
        | `*`     | 星号 (贪婪) | 匹配前面的子表达式**零次或多次**（$\ge 0$）。       | `ab*` 匹配 `a`, `ab`, `abbb`          |
        | `+`     | 加号        | 匹配前面的子表达式**一次或多次**（$\ge 1$）。       | `ab+` 匹配 `ab`, `abbb`（不匹配 `a`） |
        | `?`     | 问号        | 匹配前面的子表达式**零次或一次**（$0$ 或 $1$）。    | `apples?` 匹配 `apple` 或 `apples`    |
        | `[abc]` | 字符集      | 匹配方括号中的**任意一个**字符。                    | `[Hh]` 匹配 `H` 或 `h`                |
        | `\d`    | 数字转义    | 匹配**任意一个数字**，等同于 `[0-9]`。              | `\d\d` 匹配 `12`, `99`                |
        | `\w`    | 单词字符    | 匹配**字母、数字或下划线**，等同于 `[A-Za-z0-9_]`。 | `\w+` 匹配单词或变量名                |

[^2]: **通配符**是一种特殊的字符。 用于在执行文件操作（如搜索、删除、复制）时**代替一个或多个字符**。
     1. 通配符由 **Shell**（壳层程序）处理，主要用于**匹配文件名或路径**。
        | 符号 | 名称           | 描述 (Description)                       | 示例                                                                 |
        | :--- | :------------- | :--------------------------------------- | :------------------------------------------------------------------- |
        | `*`  | **星号**       | 匹配**任意数量**（包括零个）的字符。     | `*.jpg` 匹配所有 JPG 图片；`test*` 匹配 `test`, `test1`, `testing`。 |
        | `?`  | **问号**       | 匹配**单个**任意字符。                   | `data?.txt` 匹配 `data1.txt`，但不匹配 `data10.txt`。                |
        | `[]` | **字符集**     | 匹配方括号内定义的**任意一个**字符。     | `file[1-3].txt` 匹配 `file1.txt`, `file2.txt`, `file3.txt`。         |
        | `{}` | **花括号扩展** | 匹配括号内逗号分隔的**多个完整字符串**。 | `rm {cat,dog}.jpg` 会同时删除 `cat.jpg` 和 `dog.jpg`。               |

     2. 通配符 (Glob) vs 正则表达式 (Regex)
     虽然两者都用于模式匹配，但在使用场景和逻辑上有本质区别。
        | 特性         | 通配符 (Globbing)                      | 正则表达式 (Regular Expression)                     |
        | :----------- | :------------------------------------- | :-------------------------------------------------- |
        | **处理主体** | 由 **Shell** (如 Bash, Zsh) 直接处理。 | 由 **特定程序** (如 grep, sed, Python) 处理。       |
        | **应用对象** | **文件名、目录路径**。                 | **文件内部的文本内容、字符串**。                    |
        | **匹配逻辑** | 相对简单、宽泛。                       | 极其精确、功能强大。                                |
        | **示例对比** | `*` 匹配任意数量字符。                 | `.*` 匹配任意数量字符（`.`是任意字符，`*`是量词）。 |
        | **典型工具** | `ls`, `cp`, `mv`, `rm`                 | `grep`, `sed`, `awk`, `vim`                         |
