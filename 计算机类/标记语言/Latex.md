<a id="top" name="top"></a>

<div align="center">

# LaTeX2e 学习与速查笔记

</div>

---

笔记内容以 Tobias Oetiker 等人的《一份不太简短的 LaTeX2e 介绍》为主线，面向第一次接触 LaTeX 的读者。目标是既能从头学习 LaTeX 的工作机制，也能在写作时像字典一样快速查阅命令、环境、数学公式、图片、表格、BibTeX、交叉引用、自定义命令与常见错误。

本文默认使用 **UTF-8 + XeLaTeX + `ctex`** 排版中文。原书中基于传统 `latex`、DVI 和旧式编码的内容仍会说明其原理，但新建中文文档优先采用现代工作流。

本文统一采用以下阅读格式：

1. `##` 表示一章；
2. `###` 表示一个大知识点；
3. 大知识点下先给出内容简介，再用编号列出小知识点；
4. 单个命令写成行内代码，例如 `\section`；
5. 可以独立复制运行的源码放入带语言标识的代码块中；
6. LaTeX 源码与 Markdown 说明不放在同一个代码块中。

<div align="right">编者：DoroKnight</div>

---

<a id="toc" name="toc"></a>

## 目录

- [LaTeX2e 学习与速查笔记](#top)
  - [目录](#toc)
  - [一、认识 LaTeX](#sec-1)
    - [1.1 TeX、LaTeX 与排版引擎](#sec-1-1)
    - [1.2 安装、编辑与编译](#sec-1-2)
    - [1.3 第一个中文文档](#sec-1-3)
    - [1.4 源文件结构与编译产物](#sec-1-4)
  - [二、基本语法与文字排版](#sec-2)
    - [2.1 命令、参数、环境与分组](#sec-2-1)
    - [2.2 空白、换行、段落与注释](#sec-2-2)
    - [2.3 特殊字符与转义](#sec-2-3)
    - [2.4 字体、字号与强调](#sec-2-4)
    - [2.5 标点、引号、连字符与断词](#sec-2-5)
    - [2.6 对齐、间距与分页](#sec-2-6)
    - [2.7 编码、多语言与西文重音](#sec-2-7)
  - [三、文档结构与常用环境](#sec-3)
    - [3.1 文档类与常用宏包](#sec-3-1)
    - [3.2 标题、章节和目录](#sec-3-2)
    - [3.3 列表、引用与原样输出](#sec-3-3)
    - [3.4 脚注、边注与摘要](#sec-3-4)
    - [3.5 多文件工程](#sec-3-5)
  - [四、数学公式](#sec-4)
    - [4.1 数学模式与 AMS 宏包](#sec-4-1)
    - [4.2 上下标、分式、根式与运算符](#sec-4-2)
    - [4.3 括号、矩阵与分段函数](#sec-4-3)
    - [4.4 多行公式、编号与对齐](#sec-4-4)
    - [4.5 数学字体、定理与常用符号](#sec-4-5)
  - [五、图片、浮动体与表格](#sec-5)
    - [5.1 插入图片](#sec-5-1)
    - [5.2 浮动体机制](#sec-5-2)
    - [5.3 表格基础](#sec-5-3)
    - [5.4 进阶表格与子图](#sec-5-4)
  - [六、交叉引用与超链接](#sec-6)
    - [6.1 标签和引用](#sec-6-1)
    - [6.2 超链接、书签与 URL](#sec-6-2)
  - [七、参考文献、BibTeX 与索引](#sec-7)
    - [7.1 手写参考文献](#sec-7-1)
    - [7.2 BibTeX 数据库](#sec-7-2)
    - [7.3 编译 BibTeX](#sec-7-3)
    - [7.4 natbib 与 biblatex](#sec-7-4)
    - [7.5 索引与术语表](#sec-7-5)
  - [八、页面、字体与版式定制](#sec-8)
    - [8.1 页面尺寸与边距](#sec-8-1)
    - [8.2 行距、段落和分栏](#sec-8-2)
    - [8.3 颜色与盒子](#sec-8-3)
    - [8.4 页眉页脚与页码](#sec-8-4)
    - [8.5 XeLaTeX 字体](#sec-8-5)
  - [九、自定义命令与环境](#sec-9)
    - [9.1 新命令](#sec-9-1)
    - [9.2 新环境](#sec-9-2)
    - [9.3 计数器、长度与条件](#sec-9-3)
    - [9.4 自定义宏的工程原则](#sec-9-4)
  - [十、TikZ 绘图入门](#sec-10)
    - [10.1 TikZ 的基本结构与路径](#sec-10-1)
  - [十一、常见错误与调试](#sec-11)
    - [11.1 阅读错误信息](#sec-11-1)
    - [11.2 高频错误对照表](#sec-11-2)
    - [11.3 警告和版面问题](#sec-11-3)
    - [11.4 清理辅助文件](#sec-11-4)
    - [11.5 获取帮助](#sec-11-5)
  - [十二、完整项目模板](#sec-12)
    - [12.1 目录结构](#sec-12-1)
    - [12.2 `main.tex`](#sec-12-2)
    - [12.3 `.gitignore`](#sec-12-3)
  - [十三、命令速查表](#sec-13)
    - [13.1 文档与结构](#sec-13-1)
    - [13.2 文字与段落](#sec-13-2)
    - [13.3 数学](#sec-13-3)
    - [13.4 图片、表格和引用](#sec-13-4)
    - [13.5 编译流程](#sec-13-5)
  - [结语](#ending)

---

<a id="sec-1" name="sec-1"></a>

## 一、认识 LaTeX

<a id="sec-1-1" name="sec-1-1"></a>

### 1.1 TeX、LaTeX 与排版引擎

这一节用于区分 TeX、LaTeX 和具体编译引擎。三者处在不同层次，不能当作同一个软件名称使用。

1. **TeX 是什么**

   **TeX** 是 Donald Knuth 设计的底层排版系统，负责断行、分页、盒子和数学排版等基础工作。

2. **LaTeX 是什么**

   **LaTeX** 是建立在 TeX 之上的宏集合，由 Leslie Lamport 创建。它提供章节、目录、参考文献等高层结构。

3. **LaTeX 的排版思想**

LaTeX 的核心思想是**内容与表现分离**：作者标记“这是标题”“这是公式”，排版系统决定它们的字号、间距和编号。它尤其适合论文、书籍、技术报告和数学文档。

4. **常见编译引擎**

| 引擎       | 输入与输出      | 特点                               | 建议用途         |
| ---------- | --------------- | ---------------------------------- | ---------------- |
| `latex`    | `.tex` → `.dvi` | 传统流程，直接支持的图片格式有限   | 阅读旧工程       |
| `pdflatex` | `.tex` → `.pdf` | 稳定、资料丰富；传统字体与编码机制 | 英文旧工程       |
| `xelatex`  | `.tex` → `.pdf` | 原生 Unicode，可调用系统字体       | **中文文档首选** |
| `lualatex` | `.tex` → `.pdf` | Unicode、OpenType、可嵌入 Lua      | 高度可编程排版   |

> LaTeX 不是所见即所得（WYSIWYG），而是所想即所得（WYSIWYM）：编辑源代码，编译后查看 PDF。

<a id="sec-1-2" name="sec-1-2"></a>

### 1.2 安装、编辑与编译

LaTeX 发行版（distribution）提供编译引擎、宏包和管理工具，编辑器负责编辑源文件和调用编译命令。

1. **选择发行版**

   - Windows：TeX Live 或 MiKTeX；
   - WSL2 Ubuntu：`sudo apt install texlive-full`，体积较大但最省心；
   - 编辑器：VS Code + LaTeX Workshop、TeXstudio、TeXworks；
   - 在线环境：Overleaf，无需本地安装。

2. **检查安装结果**

```bash
xelatex --version
latexmk --version
```

3. **编译单个源文件**

```bash
xelatex main.tex
```

4. **使用 `latexmk` 自动构建**

推荐让 `latexmk` 自动判断需要编译几次：

```bash
latexmk -xelatex main.tex
latexmk -C                 # 清理中间文件
```

<a id="sec-1-3" name="sec-1-3"></a>

### 1.3 第一个中文文档

这一节给出一份可以直接编译的最小中文文档，并说明从源文件到 PDF 的基本流程。

1. **最小中文文档**

```latex
\documentclass[UTF8]{ctexart}

\title{我的第一份 \LaTeX{} 文档}
\author{DoroKnight}
\date{\today}

\begin{document}

\maketitle

\section{你好，LaTeX}
这是正文。行内公式为 $E=mc^2$。

\end{document}
```

2. **编译过程**

   1. 将代码以 UTF-8 保存为 `main.tex`；
   2. 使用 XeLaTeX 编译；
   3. 引擎读取源文件和宏包，生成 `main.pdf`；
   4. 修改源文件后重新编译。

3. **选择文档类**

   英文文档可将第一行换为 `\documentclass{article}`。在中文文档中，`ctexart`、`ctexrep`、`ctexbook` 分别对应文章、报告和书籍。

<a id="sec-1-4" name="sec-1-4"></a>

### 1.4 源文件结构与编译产物

LaTeX 工程由源文件、资源文件和编译产生的辅助文件组成。源文件结构决定内容，辅助文件负责在多轮编译之间传递编号等信息。

1. **源文件的基本结构**

```latex
\documentclass[选项]{文档类}  % 文档类声明

% 导言区（preamble）：加载宏包、设置版式、定义命令
\usepackage{amsmath}
\newcommand{\R}{\mathbb{R}}

\begin{document}             % 正文开始
正文
\end{document}               % 正文结束，后续内容被忽略
```

2. **常见编译产物**

| 扩展名                   | 含义                 | 是否提交版本库     |
| ------------------------ | -------------------- | ------------------ |
| `.tex`                   | LaTeX 源文件         | 是                 |
| `.bib`                   | 参考文献数据库       | 是                 |
| `.cls` / `.sty`          | 文档类 / 宏包        | 自己维护的应提交   |
| `.pdf`                   | 最终文档             | 按项目要求         |
| `.aux`                   | 标签、引用等辅助信息 | 否                 |
| `.log`                   | 编译日志             | 通常否，排错时有用 |
| `.toc` / `.lof` / `.lot` | 目录、图目录、表目录 | 否                 |
| `.bbl` / `.blg`          | BibTeX 输出 / 日志   | 通常否             |

3. **为什么需要多次编译**

   引用和目录依赖辅助文件，所以常需编译两次。第一次写出编号信息，第二次把信息读回正文。

---
<a id="sec-2" name="sec-2"></a>

## 二、基本语法与文字排版

<a id="sec-2-1" name="sec-2-1"></a>

### 2.1 命令、参数、环境与分组

LaTeX 语法主要由命令、参数、环境和分组组成，并且区分大小写。

1. **命令是什么**

命令以反斜杠 `\` 开头：

```latex
\command
\command{必选参数}
\command[可选参数]{必选参数}
```

2. **命令名后的空格**

反斜杠后的字母连续构成命令名。命令后的空格通常只负责终止命令名，不会输出：

```latex
\LaTeX is great.     % 输出 LaTeXis great.
\LaTeX{} is great.   % 用空分组终止命令，输出正确
```

3. **环境是什么**

环境具有开始和结束标记，且必须正确嵌套：

```latex
\begin{environment}[选项]
内容
\end{environment}
```

4. **分组是什么**

花括号也建立**分组（group）**，组内声明不会泄漏到外部：

```latex
普通文字 {\bfseries 仅这里是粗体} 又是普通文字。
```

<a id="sec-2-2" name="sec-2-2"></a>

### 2.2 空白、换行、段落与注释

LaTeX 不按照源文件的视觉空白机械排版，而是根据语法判断单词、行和段落。

1. **普通空格**：连续多个空格在正文中等价于一个空格。
2. **源文件换行**：单个换行通常也等价于一个空格。
3. **新段落**：一个或多个空行表示新段落。
4. **注释**：`%` 从当前位置注释到行尾。
5. **源文件缩进**：缩进主要用于提高可读性，不直接决定输出缩进。

6. **段落示例**

```latex
第一段仍在继续，
这里不会自动另起一行。

这里是第二段。
```

7. **强制换行**

强制换行可用 `\\` 或 `\newline`，但**不要用大量 `\\` 模拟段落或垂直间距**。新段落用空行，间距交给文档结构和样式控制。

```latex
第一行\\[0.5em]
第二行
```

8. **使用注释消除源码换行产生的空格**

```latex
这两个%
词之间没有空格。
```

<a id="sec-2-3" name="sec-2-3"></a>

### 2.3 特殊字符与转义

某些字符被 LaTeX 用作命令或结构标记。需要显示字符本身时，必须使用转义命令或原样输出命令。

1. **具有特殊意义的字符**

```text
特殊字符：#  $  %  &  _  {  }  ~  ^  \
```

2. **特殊字符的输出方法**

| 想输出 | 写法               | 想输出   | 写法              |
| ------ | ------------------ | -------- | ----------------- |
| `#`    | `\#`               | `$`      | `\$`              |
| `%`    | `\%`               | `&`      | `\&`              |
| `_`    | `\_`               | `{`、`}` | `\{`、`\}`        |
| `\`    | `\textbackslash`   | `~`      | `\textasciitilde` |
| `^`    | `\textasciicircum` | URL      | `\url{...}`       |

3. **原样输出代码**

`\verb+原样内容+` 适合短代码；两个 `+` 是分隔符，也可换成任意未出现在内容中的非字母字符。较长代码使用 `verbatim`、`listings` 或 `minted` 环境。

<a id="sec-2-4" name="sec-2-4"></a>

### 2.4 字体、字号与强调

这一节区分字体族、字体形状、字重、语义强调和字号。

1. **带参数的字体命令**

文本字体命令优先使用带参数的形式：

```latex
\textbf{粗体} \textit{意大利体} \textsl{倾斜体}
\texttt{等宽体} \textsf{无衬线体} \textrm{衬线体}
\textsc{Small Caps} \emph{语义强调}
```

2. **语义强调**

`\emph` 表示“强调”，在已经倾斜的上下文中会自动切回直立体；它比硬编码 `\textit` 更符合内容与表现分离。

3. **声明式字体命令**

声明式命令适合一段或一个环境：

```latex
{\bfseries 粗体} {\itshape 意大利体} {\ttfamily 等宽体}
```

4. **字号命令**

字号从小到大：

```latex
\tiny \scriptsize \footnotesize \small \normalsize
\large \Large \LARGE \huge \Huge
```

字号命令是声明，应限制作用域：`{\Large 标题}`。

<a id="sec-2-5" name="sec-2-5"></a>

### 2.5 标点、引号、连字符与断词

这一节说明西文排版中不能仅凭键盘字符外观判断最终输出的情况。

1. **英文引号**

英文引号不要直接键入两个相同的直引号：

```latex
`single quotes' and ``double quotes''
```

2. **三种横线**

```latex
daughter-in-law  % - 复合词连字符
pages 13--67     % -- 数值范围，en dash
yes---or no?     % --- 句中破折号，em dash
```

3. **常见文本符号**

常见文本符号包括 `\ldots`（省略号）、`\S`（节号）、`\P`（段落号）、`\dag`、`\ddag`、`\copyright`。

4. **自动断词与手动控制**

TeX 会自动断词。控制断词：

```latex
hyphen\-ation                 % 指定可断位置
\hyphenation{FORTRAN Hy-phen-a-tion} % 导言区声明
\mbox{不可拆开的内容}         % 完全禁止在内部换行
```

<a id="sec-2-6" name="sec-2-6"></a>

### 2.6 对齐、间距与分页

这一节分别处理内容对齐、水平或垂直间距，以及换行和分页建议。

1. **文字对齐**

```latex
\begin{flushleft} 左对齐 \end{flushleft}
\begin{center} 居中 \end{center}
\begin{flushright} 右对齐 \end{flushright}
```

2. **环境形式与声明形式的区别**

声明形式 `\raggedright`、`\centering`、`\raggedleft` 常用于浮动体或分组，不会像环境一样额外产生垂直间距。

3. **水平和垂直间距**

```latex
A\hspace{1cm}B
A\hfill B
上文\vspace{1em}下文
\vfill
```

4. **带星号的间距与长度单位**

带星号的 `\hspace*`、`\vspace*` 在行首或页首也保留间距。固定单位包括 `pt`、`mm`、`cm`、`in`；相对单位 `em` 约为当前字宽，`ex` 约为当前字体 x 高度。

5. **换行与分页控制**

| 命令              | 作用                       |
| ----------------- | -------------------------- |
| `\newpage`        | 立即换页                   |
| `\clearpage`      | 输出尚未排出的浮动体后换页 |
| `\pagebreak[n]`   | 建议分页，强度 `0`～`4`    |
| `\nopagebreak[n]` | 建议不要分页               |
| `\linebreak[n]`   | 建议换行并保持两端对齐     |
| `\nolinebreak[n]` | 建议不要换行               |

<a id="sec-2-7" name="sec-2-7"></a>

### 2.7 编码、多语言与西文重音

这一节用于理解现代 Unicode 工作流与旧式编码配置之间的区别。

1. **现代 Unicode 工作流**

现代 XeLaTeX / LuaLaTeX 直接读取 UTF-8，一般不加载 `inputenc`。

2. **旧式 pdfLaTeX 编码配置**

旧式 pdfLaTeX 文档常见：

```latex
\usepackage[utf8]{inputenc} % 输入编码；现代 LaTeX 中通常已是默认值
\usepackage[T1]{fontenc}    % 西文字体输出编码，改善断词与 PDF 复制
\usepackage[english]{babel} % 语言相关名称、断词规则和排版习惯
```

3. **三类配置的区别**

这些命令解决的问题不同：**输入编码**解释源文件字节，**字体编码**决定字形槽位，**语言宏包**决定断词和自动标题。不要把 `fontenc` 加入依赖 `fontspec` 的 XeLaTeX 字体方案。

4. **西文重音字符**

无法直接输入重音字符时可用命令：

```latex
H\^otel, na\"ive, fianc\'e
\`a, \~n, \c{c}
\aa, \AE, \oe, \ss
```

5. **多语言文档**

多语言 XeLaTeX 文档可使用 `polyglossia`，中文主导文档通常直接使用 `ctex`。切换语言不仅改变文字，还可能改变日期、章节名、断词规则和标点习惯。

---
<a id="sec-3" name="sec-3"></a>

## 三、文档结构与常用环境

<a id="sec-3-1" name="sec-3-1"></a>

### 3.1 文档类与常用宏包

文档类确定整份文档的基础结构，宏包在此基础上增加数学、图片、表格等功能。

1. **文档类声明**

```latex
\documentclass[11pt,a4paper,twoside]{article}
```

2. **常用标准文档类**

- `article`：短报告、论文，无 `\chapter`；
- `report`：较长报告，有章，默认标题单独成页；
- `book`：书籍，支持单双页、前言和章；
- `letter`：信件；
- `beamer`：演示文稿。

3. **常用文档类选项**

常用类选项有 `10pt/11pt/12pt`、`a4paper`、`oneside/twoside`、`onecolumn/twocolumn`、`landscape`、`draft/final`、`openright/openany`。

4. **加载宏包**

宏包扩展 LaTeX：

```latex
\usepackage[选项]{宏包名}
\usepackage{amsmath,amssymb,graphicx,booktabs}
```

5. **推荐基础宏包组合**

```latex
\usepackage{amsmath,amssymb,amsthm} % 数学
\usepackage{graphicx}               % 图片
\usepackage{booktabs,array}         % 表格
\usepackage{geometry}               % 页边距
\usepackage{xcolor}                 % 颜色
\usepackage{hyperref}               % 超链接，通常靠后加载
\usepackage[nameinlink]{cleveref}   % 智能引用，在 hyperref 后
```

<a id="sec-3-2" name="sec-3-2"></a>

### 3.2 标题、章节和目录

结构命令表达文档层级，并让 LaTeX 自动完成编号、目录和 PDF 书签。

1. **标题、作者与章节命令**

```latex
\title{标题}
\author{作者\thanks{单位或致谢}}
\date{\today}       % \date{} 可隐藏日期

\begin{document}
\maketitle
\tableofcontents

\section{一级标题}
\subsection{二级标题}
\subsubsection{三级标题}
\paragraph{段落标题}
\subparagraph{次段落标题}
\end{document}
```

2. **带星号的无编号标题**

`book` 和 `report` 还支持 `\part`、`\chapter`。带星号命令如 `\section*{致谢}` 不编号且默认不进入目录，可手动添加：

```latex
\section*{致谢}
\addcontentsline{toc}{section}{致谢}
```

3. **目录的编译机制**

目录需要至少编译两次。图目录和表目录分别用 `\listoffigures`、`\listoftables`。

4. **书籍的前置、正文和后置部分**

```latex
\frontmatter   % 前置部分：罗马页码，章通常不编号
\mainmatter    % 正文：阿拉伯页码，章编号
\appendix      % 后续章改用 A、B……编号
\backmatter    % 后置部分
```

<a id="sec-3-3" name="sec-3-3"></a>

### 3.3 列表、引用与原样输出

这些环境用于表达并列关系、引文语义和不应被 LaTeX 解释的源码。

1. **三种列表环境**

```latex
\begin{itemize}
  \item 无序项目
  \item[!] 自定义标签
\end{itemize}

\begin{enumerate}
  \item 第一项
  \item 第二项
\end{enumerate}

\begin{description}
  \item[LaTeX] 高层排版宏集合。
  \item[TeX] 底层排版系统。
\end{description}
```

2. **列表的嵌套与样式**

列表可嵌套，但不宜过深。需要细调缩进和间距时使用 `enumitem` 宏包。

3. **引用与诗歌环境**

```latex
\begin{quote}
较短的引用，每段首行不缩进。
\end{quote}

\begin{quotation}
较长、多段的引用。
\end{quotation}

\begin{verse}
第一行诗句\\
第二行诗句
\end{verse}
```

4. **原样输出环境**

```latex
\begin{verbatim}
if (x < 10) {
    printf("%d", x);
}
\end{verbatim}
```

<a id="sec-3-4" name="sec-3-4"></a>

### 3.4 脚注、边注与摘要

脚注补充正文细节，边注出现在页边，摘要用于集中概括文档内容。

1. **基本写法**

```latex
正文\footnote{这是脚注。}
正文\marginpar{这是边注。}

\begin{abstract}
摘要概括研究问题、方法和结论。
\end{abstract}
```

2. **脚注标记与移动参数**

脚注中若需再次使用标记，可分开用 `\footnotemark` 与 `\footnotetext{...}`。浮动体标题、章节标题等“移动参数”中的脚注和脆弱命令容易出错，应改写或用 `\protect`，但优先避免复杂标题。

<a id="sec-3-5" name="sec-3-5"></a>

### 3.5 多文件工程

长文档应按章拆分，但只保留一个主文件负责文档类、导言区和总体编译。

1. **主文件示例**

```latex
% main.tex
\documentclass{ctexbook}
\begin{document}
\include{chapters/introduction}
\include{chapters/method}
\input{chapters/conclusion}
\end{document}
```

2. **三个文件组织命令**

   1. `\input{file}`：在当前位置直接插入文件，可嵌套；
   2. `\include{file}`：通常用于章，会换页并产生独立 `.aux`；
   3. `\includeonly{chapters/method}`：仅编译指定的 `\include` 文件，仍保留其他章编号；
   4. 扩展名 `.tex` 通常可省略。

3. **工程约定**

建议只在 `main.tex` 写 `\documentclass` 和导言区，子文件只保留正文。

---
<a id="sec-4" name="sec-4"></a>

## 四、数学公式

<a id="sec-4-1" name="sec-4-1"></a>

### 4.1 数学模式与 AMS 宏包

LaTeX 将普通文字和数学公式放在不同的排版模式中。数学模式会改变字母字体、符号间距和上下标规则。

1. **AMS 宏包是什么**

`amsmath` 提供多行公式和高级数学环境，`amssymb` 提供额外数学符号，`amsthm` 提供定理环境，`mathtools` 在 `amsmath` 基础上继续扩展。

```latex
\usepackage{amsmath,amssymb,amsthm,mathtools}
```

2. **`$...$` 是什么**

`$...$` 是传统的行内数学定界符，公式会嵌入当前段落。例如 `$E=mc^2$`。LaTeX 文档也可使用语义更清晰的 `\(...\)`。

3. **`$$...$$` 是什么**

`$$...$$` 是 Plain TeX 的行间公式写法。它虽然经常能够编译，但不属于推荐的 LaTeX2e 写法，可能造成垂直间距、编号和错误检测不一致。LaTeX 中应使用 `\[...\]` 或公式环境。

4. **三种推荐的数学写法**

行内公式可以使用 `\(...\)`：

```latex
\(a^2+b^2=c^2\)
```

也可以使用 `$...$`：

```latex
$a^2+b^2=c^2$
```

无编号行间公式使用 `\[...\]`：

```latex
\[
  a^2+b^2=c^2
\]
```

有编号行间公式使用 `equation` 环境：

```latex
\begin{equation}
  E=mc^2
  \label{eq:energy}
\end{equation}
```

5. **数学模式的基本规则**

数学模式会忽略普通空格；变量默认用斜体，文字说明使用 `\text{...}`。需要公式编号时使用 `equation` 等环境，不要手工输入编号。

<a id="sec-4-2" name="sec-4-2"></a>

### 4.2 上下标、分式、根式与运算符

数学命令通常以一个符号或一组花括号内容为操作对象，多字符上下标和分子分母必须分组。

1. **上标与下标**

```latex
$x^2$
$x_i$
$x_i^2$
$x^{n+1}$
$a_{ij}$
```

`^` 表示上标，`_` 表示下标。它们默认只作用于后面的一个记号，多字符内容必须放入 `{}`。

2. **分式**

```latex
$\frac{a+b}{c+d}$
$\dfrac{1}{2}$
$\tfrac{1}{2}$
```

`\frac` 使用当前数学样式；`\dfrac` 强制使用行间样式；`\tfrac` 强制使用行内样式。

3. **根式**

```latex
$\sqrt{x}$
$\sqrt[n]{x}$
```

省略可选参数 `[n]` 时表示平方根，写出 `[n]` 时表示 `n` 次方根。

4. **求和、连乘、积分与极限**

```latex
$\sum_{i=1}^{n} i$
$\prod_{k=1}^{n} k$
$\int_a^b f(x)\,\mathrm{d}x$
$\lim_{x\to0}f(x)$
```

5. **分组与微分排版规则**

微分中的 `d` 通常使用 `\mathrm{d}` 保持直立，并在被积函数和微分符号之间加入细空格 `\,`。

6. **内置数学运算符**

常用函数应写成命令，从而获得直立字体和正确间距：

```latex
$\sin x \quad \cos x$
$\log x \quad \ln x$
$\exp x \quad \max A$
$\det A \quad \gcd(a,b)$
```

7. **自定义数学运算符**

```latex
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator*{\argmax}{arg\,max}
```

以上命令应写在导言区。带星号的形式会让大型运算符的上下限显示在正下方和正上方。

<a id="sec-4-3" name="sec-4-3"></a>

### 4.3 括号、矩阵与分段函数

括号需要匹配内容高度，矩阵和分段函数则使用按行列组织的数学环境。

1. **自动伸缩括号**

```latex
\left( \frac{a}{b} \right),\quad
\left\{ x\in\mathbb{R}\mid x>0 \right\}
```

2. **单边括号**

`\left` 与 `\right` 必须成对；单边括号用不可见定界符 `.`：

```latex
\left. \frac{\mathrm{d}f}{\mathrm{d}x} \right|_{x=0}
```

3. **固定大小括号**

固定大小可用 `\big`、`\Big`、`\bigg`、`\Bigg` 及其 `l/r/m` 变体。有时固定大小比自动伸缩更美观。

4. **矩阵环境**

```latex
\[
A=\begin{pmatrix}
  a & b \\
  c & d
\end{pmatrix},\qquad
B=\begin{bmatrix}1&0\\0&1\end{bmatrix}
\]
```

5. **矩阵定界符类型**

还有无括号 `matrix`、圆括号 `pmatrix`、方括号 `bmatrix`、花括号 `Bmatrix`、单竖线 `vmatrix` 和双竖线 `Vmatrix`。

6. **分段函数**

```latex
\[
f(x)=
\begin{cases}
  x^2, & x\ge 0,\\
  -x,  & x<0.
\end{cases}
\]
```

`&` 标记对齐点，`\\` 结束一行。

<a id="sec-4-4" name="sec-4-4"></a>

### 4.4 多行公式、编号与对齐

过长公式或推导过程不应依靠手工空格对齐，而应选择适合的 AMS 数学环境。

1. **使用 `align` 对齐多行公式**

```latex
\begin{align}
  (a+b)^2
    &= a^2+2ab+b^2 \label{eq:square}\\
    &= (a-b)^2+4ab. \notag
\end{align}
```

2. **多行公式环境的区别**

   1. `align` 每行编号，`align*` 全部不编号；
   2. `\notag` 或 `\nonumber` 取消当前行编号；
   3. 通常将 `&` 放在关系符号前；
   4. `gather` 用于多行居中但不对齐；
   5. `multline` 用于一个过长公式的折行；
   6. `split`、`aligned` 是可嵌入 `equation` 的子环境。

3. **在一个编号中拆分公式**

```latex
\begin{equation}
\begin{split}
  f(x) &= a_0+a_1x+a_2x^2\\
       &\quad+a_3x^3.
\end{split}
\end{equation}
```

4. **不要使用 `eqnarray`**

不要用 `eqnarray`；它的关系符号间距不正确，AMS 环境更可靠。

<a id="sec-4-5" name="sec-4-5"></a>

### 4.5 数学字体、定理与常用符号

数学字体用于表达变量类别和数学语义；定理环境负责统一编号与证明格式。

1. **数学字体命令**

```latex
\mathrm{d}       % 数学中的直立罗马体
\mathbf{A}       % 粗体拉丁字母
\boldsymbol{\alpha} % 粗体希腊字母
\mathit{ABC} \mathsf{ABC} \mathtt{ABC}
\mathcal{F}      % 花体大写字母
\mathbb{R}       % 黑板粗体，需要 amssymb/amsfonts
\mathfrak{g}     % 哥特体
\text{当 } x>0   % 数学公式中的普通文字
```

2. **定理环境**

```latex
\usepackage{amsthm}
\newtheorem{theorem}{定理}[section]
\newtheorem{lemma}[theorem]{引理}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{定义}

\begin{theorem}[勾股定理]
直角三角形满足 $a^2+b^2=c^2$。
\end{theorem}

\begin{proof}
证明过程。
\end{proof}
```

3. **常用数学符号**

| 类别     | 示例源码                                                  |
| -------- | --------------------------------------------------------- |
| 希腊字母 | `\alpha \beta \gamma \Gamma \Delta \Omega`                |
| 关系     | `= \ne < > \le \ge \approx \equiv \sim \propto`           |
| 集合     | `\in \notin \subset \subseteq \cup \cap \emptyset`        |
| 逻辑     | `\forall \exists \neg \land \lor \implies \iff`           |
| 箭头     | `\to \mapsto \leftarrow \Rightarrow \Longleftrightarrow`  |
| 运算     | `\pm \mp \times \div \cdot \ast \oplus \otimes`           |
| 其他     | `\infty \partial \nabla \ell \hbar \angle \triangle`      |
| 重音     | `\hat{x} \bar{x} \vec{x} \dot{x} \tilde{x} \overline{AB}` |

4. **数学间距**

数学间距从小到大常用 `\,`、`\:`、`\;`、`\quad`、`\qquad`，负间距为 `\!`。应先依赖 TeX 自动间距，只在语义明确时微调。

---
<a id="sec-5" name="sec-5"></a>

## 五、图片、浮动体与表格

<a id="sec-5-1" name="sec-5-1"></a>

### 5.1 插入图片

`graphicx` 宏包负责读取和变换外部图片，图片是否浮动则由外层 `figure` 环境决定。

1. **加载宏包并插入图片**

```latex
\usepackage{graphicx}

\includegraphics[
  width=0.7\textwidth
]{images/architecture.pdf}
```

2. **常用图片选项**

常用选项包括 `width`、`height`、`scale`、`angle`、`keepaspectratio`、`trim={左 下 右 上}`、`clip`。

```latex
\includegraphics[width=8cm,keepaspectratio,
  trim={10mm 5mm 10mm 5mm},clip]{figure.png}
```

3. **路径和图片格式**

路径推荐使用 `/`，文件名避免空格和中文以提高跨平台性。矢量图优先 PDF，照片优先 JPEG，界面截图和透明图优先 PNG。XeLaTeX 通常直接支持 PDF、PNG、JPEG。

4. **设置默认图片目录**

```latex
\graphicspath{{images/}{figures/}}
```

<a id="sec-5-2" name="sec-5-2"></a>

### 5.2 浮动体机制

浮动体让 LaTeX 根据整页布局移动图片或表格，从而避免页面出现不必要的大块空白。

1. **浮动体是什么**

`figure` 和 `table` 是**浮动体（float）**：LaTeX 可移动它们以减少大块空白。

2. **`[htbp]` 放置参数**

`[htbp]` 是放置偏好，不是绝对命令：

- `h`：当前位置附近；
- `t`：页顶；
- `b`：页底；
- `p`：专门的浮动页；
- `!`：放宽部分内部限制。

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.75\linewidth]{example-image}
  \caption{系统结构示意图}
  \label{fig:architecture}
\end{figure}
```

3. **完整图片浮动体**

图片标题通常在图下，表格标题通常在表上。`\label` 应紧跟 `\caption`，因为 `\caption` 才会更新计数器。

4. **限制浮动位置**

若确实必须固定位置，可加载 `float` 后使用 `[H]`，但滥用会破坏页面质量。积压浮动体可用 `\clearpage` 输出；`placeins` 的 `\FloatBarrier` 可限制浮动体越过位置。

<a id="sec-5-3" name="sec-5-3"></a>

### 5.3 表格基础

表格由两层结构组成：`table` 管理浮动、标题和编号，`tabular` 真正绘制行列。

1. **三线表示例**

```latex
\begin{table}[htbp]
  \centering
  \caption{算法复杂度比较}
  \label{tab:complexity}
  \begin{tabular}{lcc}
    \toprule
    算法 & 时间复杂度 & 空间复杂度 \\
    \midrule
    线性搜索 & $O(n)$ & $O(1)$ \\
    二分搜索 & $O(\log n)$ & $O(1)$ \\
    \bottomrule
  \end{tabular}
\end{table}
```

2. **列格式说明**

上述三线表需 `\usepackage{booktabs}`。列格式如下：

| 格式                | 含义                                   |
| ------------------- | -------------------------------------- |
| `l` / `c` / `r`     | 左 / 居中 / 右对齐                     |
| `p{3cm}`            | 固定宽度，顶部对齐且自动换行           |
| `m{3cm}` / `b{3cm}` | 垂直居中 / 底部对齐，需 `array`        |
| 竖线符号            | 生成列分隔线，不推荐在正式三线表中使用 |
| `@{内容}`           | 替换列间距，如 `@{}` 去除边缘空白      |
| `*{3}{c}`           | 重复三次 `c`                           |

3. **行列分隔与横线**

表内 `&` 分列，`\\` 换行，`\hline` 生成横线，`\cline{2-3}` 仅跨指定列。专业表格通常不使用竖线，并用留白代替密集网格。

<a id="sec-5-4" name="sec-5-4"></a>

### 5.4 进阶表格与子图

这一节介绍基础 `tabular` 无法直接完成的合并、跨页、自适应宽度和并排排版。

1. **合并单元格**

```latex
\usepackage{multirow}

\multicolumn{2}{c}{跨两列}
\multirow{2}{*}{跨两行}
```

2. **自适应宽度与长表**

- `tabularx`：用 `X` 列填满给定宽度；
- `longtable`：允许表格跨页，不能再放进 `table`；
- `siunitx`：用 `S` 列按小数点对齐数值和规范排版单位；
- `threeparttable`：规范组织表格注释。

3. **子图**

子图使用现代 `subcaption`，不要与过时的 `subfigure` 混用：

```latex
\usepackage{subcaption}

\begin{figure}[htbp]
  \centering
  \begin{subfigure}{0.45\textwidth}
    \centering
    \includegraphics[width=\linewidth]{a.png}
    \caption{方案 A}\label{fig:a}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.45\textwidth}
    \centering
    \includegraphics[width=\linewidth]{b.png}
    \caption{方案 B}\label{fig:b}
  \end{subfigure}
  \caption{两种方案比较}\label{fig:comparison}
\end{figure}
```

4. **并排放置非浮动内容**

并排放置非浮动内容可用 `minipage`：

```latex
\begin{minipage}[t]{0.48\textwidth}
左侧可以包含多段文字、图片或表格。
\end{minipage}
\hfill
\begin{minipage}[t]{0.48\textwidth}
右侧内容。minipage 内不能直接放普通 figure/table 浮动体。
\end{minipage}
```

5. **旧式 EPS 图片**

传统 `latex → DVI` 工作流主要使用 EPS 图片；现代 PDF 工作流优先 PDF/PNG/JPEG。遇到旧 EPS 资源可先转换成 PDF，或让合适的构建工具自动转换，而不要只修改扩展名。

---
<a id="sec-6" name="sec-6"></a>

## 六、交叉引用与超链接

<a id="sec-6-1" name="sec-6-1"></a>

### 6.1 标签和引用

交叉引用把“对象身份”和“最终编号”分开：作者引用标签，LaTeX 在编译时计算实际编号。

1. **创建标签并引用**

```latex
\section{实验}\label{sec:experiment}
见第~\ref{sec:experiment} 节。

\begin{equation}\label{eq:newton}
  F=ma
\end{equation}
由式~\eqref{eq:newton} 可知……

图~\ref{fig:architecture} 位于
第~\pageref{fig:architecture} 页。
```

2. **标签命名规则**

`~` 是不可断行空格，可避免“图”和编号分居两行。标签名仅供源代码使用，推荐统一前缀：

| 对象 | 前缀示例        |
| ---- | --------------- |
| 章节 | `chap:`、`sec:` |
| 公式 | `eq:`           |
| 图片 | `fig:`          |
| 表格 | `tab:`          |
| 定理 | `thm:`          |
| 代码 | `lst:`          |

3. **`??` 和标签重名**

交叉引用显示 `??` 时先再编译两次。若标签重名，日志会出现 `multiply defined`。

4. **智能引用**

`cleveref` 可自动生成对象名称：

```latex
\usepackage[nameinlink]{cleveref}
见 \cref{fig:a,fig:b} 和 \cref{eq:newton}。
```

<a id="sec-6-2" name="sec-6-2"></a>

### 6.2 超链接、书签与 URL

`hyperref` 将目录、引用、文献和 URL 转换成 PDF 中可点击的链接。

1. **配置链接样式**

```latex
\usepackage{xcolor}
\usepackage[
  colorlinks=true,
  linkcolor=blue,
  citecolor=teal,
  urlcolor=magenta,
  bookmarksopen=true
]{hyperref}

\url{https://www.ctan.org/}
\href{https://www.latex-project.org/}{LaTeX 官网}
\href{mailto:name@example.com}{发送邮件}
```

2. **宏包加载顺序**

`hyperref` 通常在大多数宏包之后加载，`cleveref` 在它之后加载。需要打印版全黑链接时可用 `hidelinks`。

3. **书签中的复杂内容**

书签中不能直接使用复杂数学命令，可给 PDF 字符串提供替代文本：

```latex
\section{\texorpdfstring{$E=mc^2$}{E=mc²}}
```

4. **PDF 文档元数据**

```latex
\hypersetup{
  pdftitle={LaTeX 学习笔记},
  pdfauthor={DoroKnight},
  pdfsubject={LaTeX2e},
  pdfkeywords={LaTeX, XeLaTeX, 数学排版}
}
```

---
<a id="sec-7" name="sec-7"></a>

## 七、参考文献、BibTeX 与索引

<a id="sec-7-1" name="sec-7-1"></a>

### 7.1 手写参考文献

参考文献较少时，可以不建立独立数据库，直接使用 `thebibliography` 环境。

1. **手写文献表示例**

```latex
正文引用 Lamport 的著作~\cite{lamport1994}。

\begin{thebibliography}{99}
  \bibitem{lamport1994}
  Leslie Lamport.
  \textit{LaTeX: A Document Preparation System}.
  Addison-Wesley, 2nd edition, 1994.
\end{thebibliography}
```

2. **`thebibliography` 参数**

`{99}` 用来预留最宽标签的宽度，并不表示有 99 篇文献。

<a id="sec-7-2" name="sec-7-2"></a>

### 7.2 BibTeX 数据库

BibTeX 将文献元数据保存在独立 `.bib` 文件中，使同一数据库可以配合不同样式重复使用。

1. **数据库条目示例**

```bibtex
@book{lamport1994,
  author    = {Leslie Lamport},
  title     = {LaTeX: A Document Preparation System},
  edition   = {2},
  year      = {1994},
  publisher = {Addison-Wesley}
}

@article{knuth1984,
  author  = {Donald E. Knuth},
  title   = {Literate Programming},
  journal = {The Computer Journal},
  volume  = {27},
  number  = {2},
  pages   = {97--111},
  year    = {1984},
  doi     = {10.1093/comjnl/27.2.97}
}
```

2. **常见条目类型**

常见条目包括 `@article`、`@book`、`@inproceedings`、`@incollection`、`@mastersthesis`、`@phdthesis`、`@techreport`、`@manual`、`@misc`。

3. **字段书写规则**

字段值用 `{}` 或双引号包围。BibTeX 可能改变标题大小写，必须保留的大写可再加花括号，如 `title = {The {TeX}book}`。作者用 `and` 分隔，不用中文顿号或逗号。

<a id="sec-7-3" name="sec-7-3"></a>

### 7.3 编译 BibTeX

BibTeX 不是 LaTeX 宏包，而是读取辅助文件和数据库的独立程序，因此构建过程包含多个步骤。

1. **正文中的文献命令**

正文：

```latex
如文献~\cite{lamport1994,knuth1984} 所述。
\nocite{knuth1984} % 列入文献表但正文不引用；\nocite{*} 列出全部

\bibliographystyle{plain}
\bibliography{references}
```

2. **经典 BibTeX 编译顺序**

```bash
xelatex main
bibtex main
xelatex main
xelatex main
```

3. **多轮编译机制**

第一次 XeLaTeX 将引用键写入 `.aux`；BibTeX 读取 `.aux` 和 `.bib`，生成 `.bbl`；后两次 XeLaTeX 读入文献表并稳定全部编号。

4. **常见参考文献样式**

`plain` 按作者排序并编号，`unsrt` 按引用顺序编号，`alpha` 使用字母标签，`abbrv` 缩写名字。

<a id="sec-7-4" name="sec-7-4"></a>

### 7.4 natbib 与 biblatex

`natbib` 扩展传统 BibTeX 的引用命令；`biblatex` 则提供另一套更现代、可配置的文献处理接口。

1. **`natbib` 的作者—年份引用**

```latex
\usepackage[authoryear,round]{natbib}
\citet{lamport1994}  % Lamport (1994)
\citep{lamport1994}  % (Lamport, 1994)
```

2. **`biblatex + biber` 工作流**

```latex
\usepackage[backend=biber,style=gb7714-2015]{biblatex}
\addbibresource{references.bib}

正文 \parencite{lamport1994}。
\printbibliography
```

3. **两套后端不能混用**

编译顺序为 XeLaTeX → Biber → XeLaTeX → XeLaTeX。**BibTeX 与 Biber 是两套后端，不要混用命令**。学校模板指定哪一套就使用哪一套。

<a id="sec-7-5" name="sec-7-5"></a>

### 7.5 索引与术语表

索引把术语映射到页码，术语表则集中解释术语或缩略语；两者都需要额外的构建步骤。

1. **创建基本索引**

基本索引：

```latex
\usepackage{makeidx}
\makeindex

LaTeX\index{LaTeX} 是排版系统。
数组\index{数据结构!数组}是一种数据结构。

\printindex
```

2. **索引编译流程**

```bash
xelatex main
makeindex main
xelatex main
```

3. **索引项的高级写法**

`\index{主项!子项}` 创建层级，`\index{显示键@排版文字}` 分离排序键和显示文本，`\index{术语|textbf}` 将页码加粗，`\index{范围|(}` 与 `\index{范围|)}` 建立页码范围。

4. **术语表和缩略语表**

术语表、缩略语表可用 `glossaries` 宏包，但它还需要额外的 `makeglossaries` 编译步骤。

---
<a id="sec-8" name="sec-8"></a>

## 八、页面、字体与版式定制

<a id="sec-8-1" name="sec-8-1"></a>

### 8.1 页面尺寸与边距

页面设置应交给统一的布局工具计算，以免手工修改多个底层长度后互相冲突。

1. **使用 `geometry` 设置页面**

```latex
\usepackage[a4paper,
  left=2.8cm,right=2.8cm,
  top=2.5cm,bottom=2.5cm]{geometry}
```

2. **双面文档与装订边距**

双面文档可设置 `inner`、`outer` 代替 `left`、`right`，为装订预留 `bindingoffset`。不要用大量手工空格模拟边距。

3. **底层页面长度**

页面布局长度包括 `\textwidth`、`\textheight`、`\oddsidemargin`、`\evensidemargin`、`\topmargin`、`\headheight`、`\headsep`、`\footskip`。通常应让 `geometry` 统一计算，而不是逐项直接改值。

<a id="sec-8-2" name="sec-8-2"></a>

### 8.2 行距、段落和分栏

行距、段落间距和分栏共同影响页面的信息密度，应按文档规范统一设置。

1. **行距和段落设置**

```latex
\usepackage{setspace}
\onehalfspacing

\setlength{\parindent}{2em}
\setlength{\parskip}{0pt}
```

2. **局部行距与段落风格**

局部行距可用 `singlespace`、`onehalfspace`、`doublespace` 环境。中文常首行缩进，西文常段间留白；按模板要求选择一种稳定风格。

3. **单栏与双栏**

```latex
\documentclass[twocolumn]{article} % 全文双栏
\twocolumn                         % 从此处双栏
\onecolumn                         % 从此处单栏
```

4. **局部多栏**

`multicol` 宏包适合局部多栏文字，但不能自然容纳普通跨栏浮动体。

<a id="sec-8-3" name="sec-8-3"></a>

### 8.3 颜色与盒子

颜色命令改变前景或背景，盒子命令把内容包装成不可分割或具有指定尺寸的对象。

1. **定义和使用颜色**

```latex
\usepackage{xcolor}
\definecolor{myblue}{RGB}{35,90,160}

\textcolor{myblue}{蓝色文字}
\colorbox{yellow}{黄色背景}
\fcolorbox{red}{white}{红框白底}
```

2. **基础盒子命令**

```latex
\mbox{不可断行的内容}
\makebox[5cm][c]{固定宽度居中}
\framebox[5cm][l]{有框且左对齐}
\parbox[t]{0.4\textwidth}{可包含多段文字的盒子}
\raisebox{1ex}{上移文字}
```

<a id="sec-8-4" name="sec-8-4"></a>

### 8.4 页眉页脚与页码

页眉页脚属于页面样式，页码格式则由独立的页码命令控制。

1. **使用 `fancyhdr` 定制页眉页脚**

```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{LaTeX 学习笔记}
\fancyhead[R]{\leftmark}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
```

2. **标准页面样式**

标准页样式有 `plain`、`headings`、`empty`。当前页临时切换用 `\thispagestyle{empty}`。

3. **页码格式与重置**

```latex
\pagenumbering{roman}  % i, ii, iii
\pagenumbering{arabic} % 1, 2, 3，并重置页码
\setcounter{page}{1}
```

4. **页眉高度警告**

若日志提示 `\headheight is too small`，按提示增大 `\headheight`，例如 `\setlength{\headheight}{14pt}`。

<a id="sec-8-5" name="sec-8-5"></a>

### 8.5 XeLaTeX 字体

XeLaTeX 通过 `fontspec` 使用 OpenType/TrueType 字体，中文字体通常由 `ctex` 调用 `xeCJK` 配置。

1. **设置西文字体**

```latex
\usepackage{fontspec}
\setmainfont{TeX Gyre Termes}
\setsansfont{TeX Gyre Heros}
\setmonofont{JetBrains Mono}
```

2. **设置中文字体**

`ctex` 已负责中文支持，必要时可用 `xeCJK` 接口设置中文字体：

```latex
\setCJKmainfont{SimSun}
\setCJKsansfont{Microsoft YaHei}
\setCJKmonofont{FangSong}
```

3. **跨平台字体问题**

系统字体名跨操作系统可能不同。需要可复现构建时，优先使用 TeX 发行版自带字体或在许可证允许时随项目提供字体文件。

---
<a id="sec-9" name="sec-9"></a>

## 九、自定义命令与环境

<a id="sec-9-1" name="sec-9-1"></a>

### 9.1 新命令

自定义命令用于封装重复写法和表达文档语义，是保持大型文档一致性的基础。

1. **定义新命令**

```latex
\newcommand{\R}{\mathbb{R}}
\newcommand{\vect}[1]{\boldsymbol{#1}}
\newcommand{\inner}[2]{\left\langle #1,#2\right\rangle}
\newcommand{\diff}[2][x]{%
  \frac{\mathrm d #2}{\mathrm d #1}%
}
```

2. **`newcommand` 参数规则**

   1. 基本语法是 `\newcommand{\name}[参数个数][第一个参数默认值]{定义}`；
   2. 最多有 9 个参数，以 `#1`～`#9` 引用；
   3. 只有第一个参数能直接设置默认值；
   4. `\newcommand` 在命令已存在时会报错，可防止误覆盖；
   5. `\renewcommand` 只用于重定义已有命令；
   6. `\providecommand` 仅在命令尚不存在时定义。

3. **调用自定义命令**

```latex
$\vect{x}\in\R^n$
$\inner{x}{y}$
$\diff{f}$ 与 $\diff[t]{f}$
```

4. **语义命令的作用**

自定义语义命令能集中修改样式：文中统一写 `\vect{x}`，以后只改一处定义即可切换粗体或箭头。

<a id="sec-9-2" name="sec-9-2"></a>

### 9.2 新环境

自定义环境把开始设置与结束设置封装在一起，适合反复出现的提示框、示例和证明结构。

1. **定义并使用新环境**

```latex
\newenvironment{important}
  {\begin{quote}\bfseries 重要：}
  {\end{quote}}

\begin{important}
不要删除正在被引用的标签。
\end{important}
```

2. **`newenvironment` 语法**

```latex
\newenvironment{name}[参数个数][默认值]
  {开始部分}
  {结束部分}
```

3. **重定义与复杂环境**

重定义已有环境使用 `\renewenvironment`。复杂彩色框推荐 `tcolorbox`，不要重复手工拼接底层盒子命令。

<a id="sec-9-3" name="sec-9-3"></a>

### 9.3 计数器、长度与条件

计数器保存整数状态，长度保存带单位的尺寸；自定义编号对象通常需要同时使用计数器和 `\label`。

1. **计数器的创建和修改**

```latex
\newcounter{example}[section]
\renewcommand{\theexample}{%
  \thesection.\arabic{example}%
}
\stepcounter{example}
\refstepcounter{example} % 同时使后续 \label 能引用它

\setcounter{section}{2}
\addtocounter{section}{1}
\value{section}
```

2. **计数器显示形式**

计数器显示形式有 `\arabic`、`\roman`、`\Roman`、`\alph`、`\Alph`、`\fnsymbol`。

3. **长度的创建和修改**

```latex
\newlength{\mylen}
\setlength{\mylen}{0.8\textwidth}
\addtolength{\mylen}{-2cm}
\rule{\mylen}{0.4pt}
```

4. **可伸缩长度**

TeX 长度可带伸缩量：`1cm plus 2mm minus 1mm`。LaTeX 用它在分页、段落与浮动体中寻找整体最优布局。

<a id="sec-9-4" name="sec-9-4"></a>

### 9.4 自定义宏的工程原则

自定义宏会影响整份文档，设计时应优先考虑语义、作用域、兼容性和可维护性。

1. 按语义命名，如 `\email`、`\vect`，不要按外观命名为 `\blueboldtext`；
2. 新命令名避免覆盖核心命令；
3. 参数始终用花括号包围，定义内注意分组；
4. 重复配置较多时放入自己的 `.sty` 宏包；
5. 修改模板前确认学校或期刊是否允许；
6. 复杂编程优先使用 LaTeX3 的 `expl3` 或成熟宏包，而不是堆叠脆弱技巧。

---
<a id="sec-10" name="sec-10"></a>

## 十、TikZ 绘图入门

<a id="sec-10-1" name="sec-10-1"></a>

### 10.1 TikZ 的基本结构与路径

TikZ 使用命令描述矢量图，适合流程图、几何图和论文示意图。复杂统计图可配合 `pgfplots`。

1. **完整流程图示例**

```latex
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning}

\begin{tikzpicture}[
  node distance=2cm,
  box/.style={draw,rounded corners,minimum width=2.5cm,
              minimum height=1cm,align=center},
  >={Stealth}
]
  \node[box] (source) {源文件\\main.tex};
  \node[box,right=of source] (engine) {XeLaTeX};
  \node[box,right=of engine] (pdf) {PDF};
  \draw[->,thick] (source) -- (engine);
  \draw[->,thick] (engine) -- (pdf);
\end{tikzpicture}
```

2. **基本路径命令**

```latex
\draw (0,0) -- (2,0) -- (2,1) -- cycle;
\draw[red,thick,dashed] (0,0) circle[radius=1];
\draw[->] (0,0) .. controls (1,2) and (2,2) .. (3,0);
\fill[blue!30] (0,0) rectangle (2,1);
\node[draw] at (1,0.5) {节点};
```

3. **坐标、选项与性能**

坐标可用直角坐标 `(x,y)` 或极坐标 `(角度:半径)`。选项写在 `[]`，作用域可用 `scope` 环境限制。TikZ 图是源代码，可复现且字体风格与正文一致，但非常复杂的图会拖慢编译，可用外部化或先单独生成 PDF。

---
<a id="sec-11" name="sec-11"></a>

## 十一、常见错误与调试

<a id="sec-11-1" name="sec-11-1"></a>

### 11.1 阅读错误信息

LaTeX 错误经常连锁出现，因此真正的首个错误最重要。编辑器可能一次列出几十条后续错误，应先修复日志中最早出现的错误再重新编译。

1. **日志中的关键标记**

- `!` 后通常是错误类型；
- `l.42` 表示引擎在源文件第 42 行附近发现问题；
- `?` 是传统交互提示，输入 `x` 可退出；
- Warning 不一定阻止生成 PDF，但引用、字体和溢出警告不应长期忽略。

2. **最小化调试法**

复制工程，逐段注释或使用二分法缩小问题；不要直接在唯一副本上大删内容。

<a id="sec-11-2" name="sec-11-2"></a>

### 11.2 高频错误对照表

下表将典型报错、底层原因和优先处理方法放在同一行，排错时应从日志中的第一个错误开始查找。

1. **错误信息速查**

| 报错或现象                                    | 常见原因                                   | 处理方法                                        |
| --------------------------------------------- | ------------------------------------------ | ----------------------------------------------- |
| `Undefined control sequence`                  | 命令拼错、缺宏包、命令在定义前使用         | 查命令拼写和所需宏包                            |
| `Missing $ inserted`                          | 在文本中直接写 `_`、`^`，或数学定界符缺失  | 转义为 `\_`，检查 `$` / `\(` 配对               |
| `Extra }, or forgotten $`                     | 多了 `}` 或数学模式未闭合                  | 从报错行向前检查括号和定界符                    |
| `Runaway argument?`                           | 少了 `}`，导致参数吞掉后续内容             | 检查报错前若干行的花括号                        |
| `LaTeX Error: \begin{...} ended by \end{...}` | 环境交叉嵌套或名字不一致                   | 保证后开始的环境先结束                          |
| `File ... not found`                          | 路径错误、宏包未安装、扩展名不匹配         | 检查相对路径、大小写和安装状态                  |
| `There were undefined references`             | 未重复编译、标签不存在                     | 检查标签并再编译两次                            |
| `Label ... multiply defined`                  | 标签键重复                                 | 给每个对象唯一标签                              |
| `Citation ... undefined`                      | `.bib` 无该键或没运行 BibTeX/Biber         | 检查键名和编译链                                |
| `Misplaced alignment tab character &`         | 文本中直接写 `&` 或表格列数不匹配          | 文本写 `\&`，表格核对列数                       |
| `There's no line here to end`                 | 在无可结束行的位置使用 `\\`                | 删除 `\\`，用空行或 `\vspace`                   |
| `Not in outer par mode`                       | 把 `figure` / `table` 放进不允许浮动的盒子 | 移出浮动体或只用 `tabular` / `\includegraphics` |

<a id="sec-11-3" name="sec-11-3"></a>

### 11.3 警告和版面问题

警告通常不阻止 PDF 生成，但可能表示溢出、过度拉伸或浮动体布局异常，需要结合 PDF 页面判断。

1. **Overfull `\hbox`**

某一行超出右边界，日志给出超出量。常见于长 URL、长等宽代码、不可断行盒子、表格或长公式。

处理顺序：

1. 改写句子或允许 URL 断行；
2. 长公式使用 `align` / `multline`；
3. 表格改用 `tabularx` 或合理缩短内容；
4. 检查是否误用 `\mbox`；
5. 最后才考虑局部 `\sloppy`，不要用全局粗暴设置掩盖问题。

2. **Underfull `\hbox` / `\vbox`**

内容被过度拉伸，可能只是提示，也可能说明窄栏、强制换行或分页不佳。应查看对应 PDF 页面再决定是否处理。

3. **浮动体跑远**

增加 `[htbp]` 的候选位置、缩小浮动体、减少连续浮动体、用 `\FloatBarrier`，不要连续堆叠 `[H]`。

4. **中文乱码或字体缺失**

确认文件为 UTF-8、编译器为 XeLaTeX、文档类为 `ctex...`，字体名在当前系统存在。不要给 XeLaTeX 文档再加载旧式 `inputenc` 来“修复”中文。

<a id="sec-11-4" name="sec-11-4"></a>

### 11.4 清理辅助文件

交叉引用或目录异常且代码已确认正确时，旧辅助文件可能已经过期或损坏。

1. **使用 `latexmk` 清理并重建**

```bash
latexmk -C
latexmk -xelatex main.tex
```

2. **手动清理的边界**

手动清理前应确认只删除可再生成的 `.aux`、`.toc`、`.out`、`.bbl` 等文件，不要删除 `.tex`、`.bib`、图片或自定义样式。

<a id="sec-11-5" name="sec-11-5"></a>

### 11.5 获取帮助

排错时优先阅读宏包自带手册，其次搜索完整错误信息；需要提问时提供最小可复现示例。

1. **查看本机宏包文档**

```bash
texdoc amsmath
texdoc graphicx
texdoc hyperref
```

2. **常用帮助来源**

   1. CTAN：查宏包主页和文档；
   2. `texdoc 包名`：打开本机宏包手册；
   3. TeX Stack Exchange：搜索完整报错；
   4. 提问时提供最小可复现示例（MWE）、编译引擎、发行版版本和首个错误，而不是只发截图。

3. **最小可复现示例**

最小可复现示例应能独立编译：

```latex
\documentclass{ctexart}
\usepackage{出问题的宏包}
\begin{document}
触发问题所需的最少内容。
\end{document}
```

---
<a id="sec-12" name="sec-12"></a>

## 十二、完整项目模板

<a id="sec-12-1" name="sec-12-1"></a>

### 12.1 目录结构

完整工程应将正文、章节、参考文献和图片分开存放，并保留唯一主入口。

1. **推荐目录结构**

```text
latex-project/
├── main.tex
├── references.bib
├── chapters/
│   ├── introduction.tex
│   └── method.tex
├── images/
│   └── architecture.pdf
└── .gitignore
```

<a id="sec-12-2" name="sec-12-2"></a>

### 12.2 `main.tex`

下面的主文件同时演示中文文档、数学、图表、交叉引用和 BibTeX 配置。

1. **完整主文件源码**

```latex
\documentclass[UTF8,11pt,a4paper]{ctexart}

\usepackage[
  left=2.8cm,
  right=2.8cm,
  top=2.5cm,
  bottom=2.5cm
]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{graphicx}
\usepackage{booktabs,tabularx}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage[nameinlink]{cleveref}

\graphicspath{{images/}}
\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  citecolor=teal,
  urlcolor=magenta,
  pdftitle={示例报告},
  pdfauthor={DoroKnight}
}

\newtheorem{theorem}{定理}[section]
\newtheorem{definition}[theorem]{定义}
\newcommand{\R}{\mathbb{R}}
\newcommand{\vect}[1]{\boldsymbol{#1}}

\title{LaTeX 示例报告}
\author{DoroKnight}
\date{\today}

\begin{document}

\maketitle
\begin{abstract}
本文演示中文、章节、公式、图片、表格、引用与参考文献。
\end{abstract}

\tableofcontents

\section{引言}\label{sec:introduction}
LaTeX 将内容结构与视觉样式分离。参考文献见~\cite{lamport1994}。

\section{数学公式}
对于 $a,b\in\R$，有
\begin{equation}\label{eq:square}
  (a+b)^2=a^2+2ab+b^2.
\end{equation}
式~\eqref{eq:square} 是完全平方公式。

\section{图片与表格}
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.7\linewidth]{architecture.pdf}
  \caption{系统结构图}\label{fig:architecture}
\end{figure}

\begin{table}[htbp]
  \centering
  \caption{工具比较}\label{tab:tools}
  \begin{tabular}{lll}
    \toprule
    工具 & 类型 & 用途 \\
    \midrule
    XeLaTeX & 引擎 & Unicode 与系统字体 \\
    BibTeX  & 程序 & 处理参考文献 \\
    \bottomrule
  \end{tabular}
\end{table}

如 \cref{fig:architecture,tab:tools} 所示，图表均可自动编号和引用。

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

<a id="sec-12-3" name="sec-12-3"></a>

### 12.3 `.gitignore`

Git 应跟踪不可再生成的源文件和资源，不跟踪编译过程中产生的临时文件。

1. **推荐忽略规则**

```gitignore
*.aux
*.bbl
*.bcf
*.blg
*.fdb_latexmk
*.fls
*.lof
*.log
*.lot
*.out
*.run.xml
*.synctex.gz
*.toc
*.xdv
_minted-*/
```

2. **不应忽略的文件**

不要忽略 `.tex`、`.bib`、图片和自定义 `.sty`。是否提交 PDF 取决于仓库用途。

---
<a id="sec-13" name="sec-13"></a>

## 十三、命令速查表

<a id="sec-13-1" name="sec-13-1"></a>

### 13.1 文档与结构

本表集中列出文档骨架和章节组织命令。

1. **文档结构命令速查**

| 需求     | 命令                                           |
| -------- | ---------------------------------------------- |
| 文档类   | `\documentclass[选项]{类}`                     |
| 加载宏包 | `\usepackage[选项]{包}`                        |
| 正文边界 | `\begin{document}` / `\end{document}`          |
| 标题     | `\title`、`\author`、`\date`、`\maketitle`     |
| 章节     | `\part`、`\chapter`、`\section`、`\subsection` |
| 目录     | `\tableofcontents`                             |
| 图表目录 | `\listoffigures`、`\listoftables`              |
| 插入文件 | `\input{}`、`\include{}`、`\includeonly{}`     |
| 附录     | `\appendix`                                    |

<a id="sec-13-2" name="sec-13-2"></a>

### 13.2 文字与段落

本表集中列出字体、脚注、原样输出、空白和对齐命令。

1. **文字排版命令速查**

| 需求               | 命令                                  |
| ------------------ | ------------------------------------- |
| 强调 / 粗体 / 斜体 | `\emph{}` / `\textbf{}` / `\textit{}` |
| 等宽 / 无衬线      | `\texttt{}` / `\textsf{}`             |
| 脚注 / 边注        | `\footnote{}` / `\marginpar{}`        |
| 原样短文本         | `\verb+...+`                          |
| 不换行空格         | `~`                                   |
| 换行 / 换页        | `\\` / `\newpage` / `\clearpage`      |
| 水平 / 垂直间距    | `\hspace{}` / `\vspace{}`             |
| 居中               | `center` 环境或 `\centering`          |

<a id="sec-13-3" name="sec-13-3"></a>

### 13.3 数学

本表集中列出数学模式、公式环境和常用数学结构。

1. **数学命令速查**

| 需求               | 命令                       |
| ------------------ | -------------------------- |
| 行内 / 行间        | `\(...\)` / `\[...\]`      |
| 编号公式           | `equation`                 |
| 多行对齐           | `align` / `align*`         |
| 分式 / 根式        | `\frac{}{}` / `\sqrt[]{}`  |
| 上下标             | `^{}` / `_{}`              |
| 求和 / 积分 / 极限 | `\sum` / `\int` / `\lim`   |
| 自动括号           | `\left` / `\right`         |
| 矩阵 / 分段        | `pmatrix` / `cases`        |
| 公式内文字         | `\text{}`                  |
| 黑板粗体 / 花体    | `\mathbb{}` / `\mathcal{}` |

<a id="sec-13-4" name="sec-13-4"></a>

### 13.4 图片、表格和引用

本表集中列出外部图片、表格结构、交叉引用和链接命令。

1. **图片、表格与引用命令速查**

| 需求            | 命令                                  |
| --------------- | ------------------------------------- |
| 插图            | `\includegraphics[width=...]{...}`    |
| 图浮动体        | `figure` + `\caption`                 |
| 表浮动体        | `table` + `tabular`                   |
| 分列 / 换行     | `&` / `\\`                            |
| 三线表          | `\toprule`、`\midrule`、`\bottomrule` |
| 标签            | `\label{}`                            |
| 编号 / 页码引用 | `\ref{}` / `\pageref{}`               |
| 公式引用        | `\eqref{}`                            |
| 文献引用        | `\cite{}`                             |
| URL / 链接      | `\url{}` / `\href{}{}`                |

<a id="sec-13-5" name="sec-13-5"></a>

### 13.5 编译流程

编译次数由目录、交叉引用、文献后端和索引工具决定。优先使用 `latexmk` 自动完成依赖判断。

1. **自动构建**

```bash
latexmk -xelatex main.tex
```

2. **传统 BibTeX 构建**

```bash
xelatex main
bibtex main
xelatex main
xelatex main
```

3. **`biblatex + biber` 构建**

```bash
xelatex main
biber main
xelatex main
xelatex main
```

4. **索引构建**

```bash
xelatex main
makeindex main
xelatex main
```

---

<a id="ending" name="ending"></a>

## 结语

学习 LaTeX 时，最重要的不是背下所有命令，而是理解三个机制：

1. **结构化标记**：描述内容是什么，而不是它“看起来怎样”；
2. **编译与辅助文件**：目录、交叉引用、文献表往往需要多轮处理；
3. **宏与抽象**：用自定义命令表达语义，让整篇文档保持一致且容易修改。

建议先掌握最小文档、章节、文字、公式、图片、表格和引用，再根据实际写作需求学习宏包。遇到错误时先看日志中的第一个错误，并构造最小可复现示例；这比盲目修改或堆叠宏包更有效。
