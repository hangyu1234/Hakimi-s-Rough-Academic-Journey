# 对于命令行环境的介绍
---
大多数`shell`不只是个程序启动器，而是提供了整套的编程预言，但是 `shell`脚本的一切设计确实都是为例运行程序，并让程序之间能以简单、高效的方式通信。

---
## 一、 CLI程序的基本结构
---
### 程序执行过程
0. shell 中，空格的作用**就是**分隔参数！
1. 读取输入（Read）
当按下回车键时，shell会接收到一串原始字符串
2. 词法分析与拆分(Tokenization)
shell 将一长串字符拆分成一个个“单词”(Tokens)，它会根据空格、制表符和`;`,`|`,`&`等特殊符号来识别哪些是命令，哪些是参数
**！注：**如果使用了引号(`"my files.txt"`)，shell会把引号内的内容视为一个整体，**不会拆开！**
3. 展开(Expansions)
- 大括号展开：`{a,b}.txt` -> `a.txt b.txt`
- 波浪号展开：`~` -> `/home/user`
- 变量展开：`$PATH` -> 长串路径
- 命令替换：`$(date)` -> 当前的日期字符串
- 算数展开：`%((1+1))` -> `2`
- 通配符展开：`*.py` -> `a.py b.py`
4. 重定向处理(Redirections)
shell 检查是否有`>`,`<`,`2>&1`等符号。如果存在，会先打开相应的文件或管道，准备输入输出流，但此时还**没有**运行程序
5. 查找与执行(Execution)
- 检查别名/函数： 它是 alias 吗？是自定义函数吗？
- 检查内置命令： 它是 cd 或 echo 这种 Shell 自带的命令吗？
- 查找外部程序： 如果都不是，Shell 会去 $PATH 定义的目录里寻找名为该命令的可执行文件。
- 分叉与替换 (Fork & Exec)： Shell 调用系统函数创建一个子进程（Fork），然后在子进程中用找到的程序替换掉自己（Exec）。
---
### 参数
1. 参数的本质
在`shell`中，参数本质上就是纯字符串，由程序决定怎么解析这些字符串
2. 参数的访问
在`shell`脚本内部，可以通过语法访问这些参数。`$1`访问第一个参数，`$2`到`$9`依此类推，而`$@`以列表形式访问所有参数，`$#`获取参数个数，`$0`是程序本身名称。
例：
```bash
echo "$PATH"
```
输出：
```bash
/opt/miniconda3/condabin:/opt/homebrew/opt/python/libexec/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/opt/pkg/env/active/bin:/opt/pmk/env/global/bin
```
3. 参数的组成
一般来说，参数由**普通字符串** 和 **选项（flags）**组成
选项以`-`或`--`开头，可选，用来修改程序的行为
`ls -l`改变了`ls`的输出格式。
一般情况下，*双横线 + 完整词* 与 *单横线 + 首字母* 等价
```bash
ls --all #与ls -a 等价
```
单横线选项通常可以合并，且选项顺序无所谓
```bash
ls -al #与 ls -ls 等价
```
例：
```bash
singlemie@singlemiedeMacBook-Pro demo % ls
a.py		b.py		c.py		err.txt		files.txt	slow.py		test.md
singlemie@singlemiedeMacBook-Pro demo % ls -l
total 64
-rw-r--r--  1 singlemie  staff      0  5月  2 09:09 a.py
-rw-r--r--  1 singlemie  staff      0  5月  2 09:09 b.py
-rw-r--r--  1 singlemie  staff      0  5月  2 09:09 c.py
-rw-r--r--  1 singlemie  staff     43  5月  2 09:24 err.txt
-rw-r--r--  1 singlemie  staff     38  5月  2 14:27 files.txt
-rw-r--r--  1 singlemie  staff     57  5月  2 09:14 slow.py
-rw-r--r--@ 1 singlemie  staff  17163  5月  2 15:17 test.md 
```
4. 传入多个同类型参数
此时命令会对每个参数执行相同的操作
```bash
mkdir test1
mkdir test2
#等价于
mkdir test1 test2
```
---
## 二、 Globbing(通配符)
本部分内容详见`/Users/singlemie/Developer/Hakimi-s-Rough-Academic-Journey/其他笔记/计算机类/操作系统/Shell简单指令.md`的脚注[2],在此只做简单示例及关于通配符展开的注意事项
```bash
#递归删除当前目录下所有.py文件
for file in $(ls | grep -p '\.py');do
    rm "$file"
done
#采用通配符
rm *.py
```
**注：通配符展开**
示例：区分`rm *.py`和`rm "*.py"`：
前者为删除所有以`.py`结尾的文件，后者删除名为`*.py`的文件
本质即为 shell 命令的执行顺序

---
## 三、 Streams (流) 
**！核心**
每个程序都有三个流：一个输入流和两个输出流

| 流名称 | 英文全称 | 中文全称 | 文件描述符 |
| :--- | :--- | :--- | :--- |
| stdin | Standard Input | 标准输入 | 0 |
| stdout | Standard Output | 标准输出 | 1 |
| stderr | Standard Error | 标准错误 | 2 |

`stdout`默认通过管道传给下一个命令，`stderr`用来输出警告和问题信息，这些内容不会传给下一个命令

先来看一个程序管道：
```bash
cat myfile.txt | grep -P '\d+' | uniq -c
```
>在使用管道运算符`|`时，`shell`的操作就是从前一个程序流向后一个程序的数据流

我们可能会理解为这三个程序是按顺序执行的，其实不然。这三个程序其实是**同时运行(并行)**的，实际过程是三个程序一起被启动，通过管道把程序的输入和输出流连接到一起，当前者的输出产生时，立刻被后者的输入消耗

**重定向**
```bash
> #输出覆盖
>> #输出追加
< #输入
2> #错误输出
```
示例：
```bash
# 将标准输出(stdout)重定向到文件(覆盖)
echo "hello" > output.txt
# 将标准输出(stdout)重定向到文件(追加)
echo "world" >> output.txt
# 将标准错误(stderr)重定向到文件
ls nonexistent 2> errors.txt
# 将标准输出和标准错误同时重定向到同一个文件
ls nonexistent &> all_output.txt
# 从文件中重定向标准输入(stdin)
grep "pattern" < input.txt
# 通过重定向到 /dev/null 来丢弃输出
cmd > /dev/null 2 >&1 #&1表示标准输出的引用，因此本命令相当于吧stderr和stdout都丢弃
```
接下来对比两个命令：
```bash
grep "pattern" input.txt # grep亲自打开文件，作为参数传入
grep "pattern" < input.txt #shell打开文件并传给grep的stdin
```
接着看一个命令的组合
```bash
grep "error" < log.txt > result.txt 2>&1
```
解释：
- 从`log.txt`读取内容(stdin)
- 从输入流中搜索`error`
- 把找到的结果存入 `result.txt`(stdout)
- 同时把可能出现的错误存入`result.txt`(stderr)
---
## 四、 Environment Variablee(环境变量)
在`bash`中，给变量赋值写成`foo=bar`，**等号两侧不能有空格**
示例：
```bash
foo=bar
echo "$foo"
# 打印 bar
echo 'foo'
# 打印 foo
```
注：
- shell 变量没有类型，本质上都是字符串。
- shell 中单引号和双引号的作用不同
- `'`包裹起来的时字面量字符串，不展开变量，不做命令替换，不处理转义序列。
- `"`包裹起来的会做上述事情

可以把一个变量的输出保存到变量里 --- 命令替换：
```bash
files = $(ls)
echo "files" | grep README
echo "files" | grep ".py"
```

ps:进程替换
`<( CMD )`会执行`CMD`,把输出存入临时文件，再用临时文件名替换掉 `<()`。这个小用法在要通过文件而不是`stdin`传值掉命令中很有用。
```bash
diff <(ls src) <(ls docs) # 展示 src 和 docs 两个目录中文件列表掉差异。
```

 Shell 中的变量是有作用域的，根据变量的可见性，shell中的变量可以分为两种：

| 特性           | 本地变量        | 环境变量 |
| :------------ | :------------- | :------ |
|定义方式        | `VAR=value`     | `export VAR=value`         |
| 可见范围  | 仅限于**当前Shell进程** |  当前 Shell 及其**所有子进程**|
|传递性|不传递给子进程/脚本|会传递(拷贝)给子进程/脚本|
|生命周期|随当前Shell结束而销毁|随当前Shell或引用它的进程结束而销毁|
|用途|脚本内的临时计算和循环索引|系统配置和(`PATH`)用户信息(`USER`)|

下面我们稍微详细地讲解环境变量：

每当 shell 程序调用另一个程序是，它会顺带传过去一组变量，这些就是*环境变量*。
在 shell 中可以通过`printenv`命令查看当前环境变量
```bash
printenv
```
输出：
```bash
...
...
...
...
```
这一长串内容即为**当前环境变量**

想显示给某个命令赋值有两种方法：
1. 在命令前面直接加赋值
```bash
tz=Asia/Shanghai date
echo $tz
```
输出：
```bash
Tue May  5 23:33:05 CST 2026

```
这是因为变量赋值发生在`date`命令之前，在执行完`date`进程后tz变量就自动销毁，所以第二个命令没有输出
2. 用内联命令`export`
这个命令会修改当前 Shell 的环境，之后启动的所有子进程都会继承这个变量。
**还是内存级操作，在关闭shell 后就不存在了**：
```bash
export DEBUG=1
#从此时起，所有程序的环境中都将具有 DEBUG=1
bash -c 'echo DEBUG'
# 打印 1
```

要删除一个变量，可以使用内建命令`unset`,例如`unset DEBUG`。