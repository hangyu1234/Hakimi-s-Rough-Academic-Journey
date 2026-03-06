# Linux的一些常见命令和操作

- 当前目录：你所在的位置
- 绝对路径：从根目录/开始，如/home/user/project
- 相对路径：相对当前目录，如./src, ../data
- 通配符 *任意字符 ?单个字符

创建练习目录
```linux_orders
mkdir -p ~/linux_practice
cd ~/linux_practice
```
其中 
mkdir 是 make dictionary，用于创建新文件夹
-p 是递归创建参数
>其作用：
1. 如果父目录不存在，自动创建
2. 如果已存在不报错

~/ 当前用户的家目录快捷表示符号，等价于/home/haoyang/

ls:列出目录内容
>ls -l
>
-l
(详细信息：权限，大小，时间)
>ls -la
>
-a（含隐藏文件，如.ssh）

>pwd 显示当前目录
```
cd :切换目录
cd /tmp
cd ~ 返回home(无论上下)
cd .. 返回上一级
```
>linux是多用户系统，每个目录都用明确的权限归属，只有在自己的家目录 /home/haoyang或者公共目录/tmp下普通用户才有写权限，可以自由创建内容

>像/home, /etc, /root这种系统级目录，只有root用户可以修改，普通用户只能查看

>touch 
创建空文件或者更新时间

```
例：1. touch notes.txt
    2. touch 文件1 文件2（批量处理多个文件）
    3. touch -d"2026-03-05"notes.txt 自定义文件的时间戳
```
>cp
复制文件/目录
```
cp notes.txt notes.bak（把notes.txt 复制一份名为 notes.bak）
cp -r project project_backup（-r 表示复制目录及所有内容，讲project完整复制为project_backup）
```
>mv
移动或重命名
```
mv notes.txt notes.bak(把notes.txt重命名为notes.bak，因为其已存在，所以会被覆盖)
mv backup.txt ./data/（把backup.txt移动到/data中）
```
>rm
删除（高风险）
```
    rm backup.txt(删除(只)文件)
    rm -r (递归删除目录及其中所有内容)
    rm -rf (强制删除，忽略不存在文件且不提示确认)
    ！！！慎用 
```
>cat/less 查看文件
```
    cat test1.txt (一次把所有内容输出到终端，非交互性)
    less test1.txt ：
    以分页方式打开，支持交互性浏览
    ↑ / ↓ ：上下滚动一行
    PageUp / PageDown:翻页
    / 关键词：搜索内容
    q ：退出查看器
```

>head / tail 查看开头和结尾

```
    head -n 5 /var/log/system.log 显示前五行内容
    tail -n 20 /var/log/system.log 显示后20行内容
    tail -f /var/log/system.log 实时跟踪新增内容，有新内容写入就显示在终端，按Ctrl + C终止
 ```
 
>grep 按模式筛选
```
grep "ERROR" app.log 
在app.log文件中，搜索所有包含字符串"ERROR" 的行，并且打印到终端
grep -n "timeout" app.log
在app.log文件中，搜索所有包含timeout的行，并且在每一行开头显示行号（-n 参数）
grep -R "main" ./src
在./src目录及其所有子目录下(-R)表示递归，搜索所有文件中包含字符串main的行
```
>find 按条件查找文件
```
find . -name "*.cpp" 
在当前目录（.）及其所有子目录中，查找文件名以.cpp结尾的文件
-name "*.cpp" 按文件名匹配，*是通配符，表示任意字符
find /var/log/ -type f -mtime -7
在/var/log 及子目录中，查找最近七天(-mtime -7)修改过的普通文件(-type f)
```
>wc 统计行/词/字节
```
wc notes.txt 统计文件的行数，单词数和字节数
wc -l app.log 只统计行数
-w 统计单词数
-c 统计字节数
-m 统计字符数（与-c 类似，但对多字节字符更准确）
```
>sort/uniq 排序与去重(不会修改原文件)
```
sort names.txt
对names.txt文件中的所有行，按字母顺序(或数字顺序)进行排序，并将结果输出到终端
常用自定义排序规则：
-n 按数字大小排序
-r 反向排序
-f 忽略大小写
-k -2 按指定列(第2列) 排序
sort names.txt | uniq
先对names.txt排序，然后通过管道符|将结果传给uniq命令，去除其中连续重复的行
sort names.txt | uniq -c
在去重的基础上，uniq -c 会在每一行开头显示该行出现次数(count)
sort -t "," -k 3 data.csv
按CSV文件第三列排序
-t "," 指定分隔符(配合-k使用)
```
>cut 按列切分
```
cut -d ',' -f 1,3 users.csv
cut 按列切分
-d ',' 指定字段之间用逗号,分隔
-f 1,3 提取第一列和第三列
users.csv 目标文件
``` 

>awk 列处理与脚本化
```
awk '{print $1,$3}' data.txt
从data.txt文件中提取每行的第一个和第三个字段并打印
awk默认以“任意空白字符（空格，制表符）作为字段分隔符，且自动忽略连续空格”
awk -F ',' '{print $1,$3}' users.csv
-F 显示指定以 ',' 为分隔符
```
>sed 流式替换
```
sed 's/http/https/g' urls.txt
在urls.txt文件中，把所有的http替换为https，并将结果输出到终端，不修改原文件
sed -i 's/localhost/127.0.0.1/g' config.ini
在config.ini文件中把所有出现的localhost替换为127.0.0.1，直接修改原文件
sed 's/http/https/g' urls.txt > new_urls.txt
把替换后的内容保存到新文件
```
>apt 软件包管理
>apt是Debian/Ubuntu常用包管理工具，用于安装，升级，删除软件。
```
sudo apt update 更新软件索引
sudo apt upgrade 升级已安装软件
sudo apt install git 安装软件
sudo apt remove git 删除软件
sudo apt purge git(删除软件，并且删除配置文件，比remove彻底)
sudo apt autoremove 清理无用依赖
sudo apt clean 清理无用缓存 
```
>常用查询命令
```
apt search nginx 
apt show nginx
apt list --installed | grep cmake
apt policy python3
```
- search 搜索包名
- show 看包详情（版本，依赖，描述）
- policy 看候选版本和源优先级

>tar 打包与解压 用于打包多个文件，常与压缩算法组合
- gzip (.tar.gz) 压缩速度快，是最常见的格式
- bzip2 (.tar.bz2) 压缩率高于gzip，但速度稍慢
- xz (.tar.xz) 压缩率最高，适合大文件，但压缩/解压缩耗时长

高频命令模板
1. 打包（不压缩）
> tar -cvf backup.tar project/
2. 打包并gzip压缩
> tar -czvf backup.tar.gz project/
3. 打包并xz压缩
> tar -cJvf backup.tar.gz project/
4. 解压 .tar.gz
> tar -xzvf backup.tar.gz
5. 解压到指定目录
> tar -xzvf backup.tar.gz -C /tmp/restore
6. 只查看归档内容，不解压
> tar -tzvf backup.tar.gz

常用参数速记
- -c create，创建归档
- -x extract，解压归档
- -t list 查看归档内容
- -v verbose，显示过程
- -f file，指定归档文件名
- -z gzip
- -j bzip2
- -J xz
- -c 切换到指定目录后再操作

参数顺序
1. 核心参数在前 c x t
2. 辅助参数中间 z j J v
3. 文件指定（必在最后） f
也可以用全拼参数，不用管顺序