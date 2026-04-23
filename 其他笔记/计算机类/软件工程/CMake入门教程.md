# CMake入门教程
支部编码 2026-3-2
___
## CMake概述
我们在编写`C`或`cpp`程序时，都是.c或.cpp源文件，这样的文件并不能直接运行，这时候就需要生成对应的可执行文件

这个过程的`toolchain`如下：

1. 预处理 （此时依然是.c,.cpp）
2. 编译
3. 汇编（.o文件）
4. 链接（链接器对这些.o文件进行链接）

文件较少时，可以直接通过命令进行编译

如`g++ main.cpp -o main`

`g++ date.cpp date_main.cpp -o date_main`

但是文件过多时编译命令会过于繁琐，不适合大型项目的开发

这时候我们就要使用`CMake/makefile`来解决

`makefile->make`(有平台限制，且命令复杂，不方便)

`CMakeLists.txt` -> `cmake` -> `makefile`文件 -> `make`命令

此时可以调用系统里的工具链

`CMake` 不仅可以生成可执行程序，还可以生成库文件（包括动态库和静态库）

生成第三方库的目的：
>1.第三方代码的保密

>2.在第三方可直接调用，比较直观简洁

总结一下，通过`CMake`，能很好地实现一个大型项目的管理


## 一些CMake的基础命令(只想粗略了解仅看此部分即可，详细了解可直接看下一部分)
1.注释行
>`CMake`使用`#`进行注释,可以放在任何位置

>例：#这是一个`CMakeLists.txt`文件

2.注释块
>`CMake`使用`#[[]]`形式进行块注释

>#[[     这是一个`CMakeLists.txt`文件
>这是一个`CMakeLists.txt`文件
>这是一个`CMakeLists.txt`文件   ]]

在`CMakeLists.txt`文件中添加的三个命令：
1. `cmake_minimum_required` : 指定使用的cmake的最低版本
2. `project(<项目名>)`(可选，非必须，如果不加可能会有警告)
3. `add_executable(<生成的可执行文件名> <依赖的源代码文件>)` : 定义工程会生成一个可执行程序（和`project`中的项目名字无任何关系）

```cmake
add_executable(app add.c div.c main.c mult.c sub.c)
#或
add_executable(app add.c;div.c;main.c;mult.c;sub.c)
```
>命令示例
```cmake
mkdir build 
cd build 
cmake -G"MinGW Makefiles" ..
cmake --build .
./main
```
>使用示例
```cmake
(base) PS C:\Users\lenovo\Desktop\note> mkdir build
----------------------------------------
目录: C:\Users\lenovo\Desktop\note

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          2026/3/4     23:41                build
----------------------------------------
(base) PS C:\Users\lenovo\Desktop\note> cd build
----------------------------------------
(base) PS C:\Users\lenovo\Desktop\note\build> cmake -G"MinGW Makefiles" ..

-- The C compiler identification is GNU 15.2.0
-- The CXX compiler identification is GNU 15.2.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: C:/msys64/mingw64/bin/cc.exe - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: C:/msys64/mingw64/bin/c++.exe - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Configuring done (1.3s)
-- Generating done (0.0s)
-- Build files have been written to: C:/Users/lenovo/Desktop/note/build
(base) PS C:\Users\lenovo\Desktop\note\build> cmake --build .
[ 33%] Building CXX object CMakeFiles/main.dir/integer.cpp.obj
[ 66%] Building CXX object CMakeFiles/main.dir/integer_main.cpp.obj
[100%] Linking CXX executable main.exe
[100%] Built target main
(base) PS C:\Users\lenovo\Desktop\note\build>
```
然后再使用./main命令即可运行程序了

## CMake 详细讲解

### 项目构建的标准流程
以`CMake + Make + GNU(GCC)`环境为例，一个完整的项目构建分为两个阶段：
#### 阶段一：Configure(配置阶段)
- **做了什么**：`CMake`会读取你手写的`CMakeLists.txt`文件，解析里面的依赖关系，设置好编译选项，并将缓存数据存入`CMakeCache.txt`，最终自动生成供机器读取的`Makefile`。
- **命令**：`cmake -B build`(注：Windows下使用MinGW时需要加-G参数，即`cmake -B build -G "MinGW Makefiles`)。
#### 阶段二：Build(构建阶段)
- **做了什么**：此时`CMake`的主要工作已经完成，底层构建工具(如`Make`)接管工作。它读取生成的`Makefile`，调用编译器(如`g++`)，编译每个源文件生成目标文件(`.o`)，最后链接生成`动态库`、`静态库`或`.exe`可执行文件
- **命令**：`cmake --build build`
#### 阶段三：Run(运行)
- **命令**：`./build/main_app.exe`
#### 小结
使用`CMake`运行程序的命令:
```cmake
cmake -B build
cmake --build build
./build/main_app.exe
# main_app只是示例程序名
```
### CMakeLists核心语法
CMake的核心在于如何编写CMakeLists.txt。
>在CMake里，静态库，动态库，可执行文件，统统被称为“目标(Target)”。
1. 基础框架与生成可执行文件

    每一个`CMakeLists.txt`开头都必须有这几句：
    1. 指定最低版本：`cmake_minimum_required(VERSION 3.21)`
    2. 设置项目名称：`project(hello_cmake)`
    3. 添加可执行文件(`Target`):`add_executable(hello_cmake main.cpp)`
    - 语法：`add_executable(<生成的可执行文件名> <依赖的源代码文件>)`
2. 生成静态库/动态库
    1. 文件目录树结构(`Directory Structure`)

        我们将项目拆成3个部分：主程序、静态库模块(lib1_static)、动态库模块(lib2_dynamic)。每一个有独立代码文件夹和专属CMakeLists.txt。
        ```Text
        hello_cmake_project/
            │
            ├── CMakeLists.txt                 <-- 【总管】顶层配置
            ├── main.cpp                       <-- 主程序
            │
            ├── lib1_static/                   <-- 【基础静态库】
            │    ├── CMakeLists.txt
            │    ├── lib1_math.cpp             <-- (新增) 拆分为多个源文件
            │    ├── lib1_string.cpp           <-- (新增) 拆分为多个源文件
            │    └── lib1.h
            │
            ├── lib2_dynamic/                  <-- 【基础动态库】
            │    ├── CMakeLists.txt
            │    ├── lib2_net.cpp              <-- (新增) 拆分为多个源文件
            │    ├── lib2_file.cpp             <-- (新增) 拆分为多个源文件
            │    └── lib2.h
            │
            └── lib3_extra/                    <-- 【高级库】(它要调用 lib1 的功能)
                ├── CMakeLists.txt
                ├── lib3.cpp
                └── lib3.h
        ```
    2. 编写`CMakeLists.txt`代码
        1. 拥有多个源文件的底层库：`lib1`和`lib2`
        当一个库包含多个源文件时，直接把它们全部列在`add_library`后面即可(用空格或换行隔开)。
        `lib_static/CMakeLists.txt`:
        ```cmake
        # 直接把多个.cpp文件排开写上
        add_library(lib1 STATIC
            lib1_math.cpp
            lib1_string.cpp
        )
        target_include_directories(lib1 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
        ```
        `lib2_dynamic/CMakeLists.txt`:
        ```cmake
        add_library(lib2 SHARED
            lib2_net.cpp
            lib2_file.cpp
        )
        target_include_directories(lib2 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
        ```
        2. "库依赖库":`lib3_extra/CMakeLists.txt`
        
        - `lib3`也是一个独立的库，但它的实现代码(`lib3.cpp`)里需要用到`lib1`里的函数。所以，它必须链接`lib1`。
        ```cmake
        # 1.生成lib3库自身
        add_library(lib3 STATIC lib3.cpp)

        # 2. 暴露 lib3 自己的头文件目录
        target_include_directories(lib3 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

        # 3.让 lib3 链接 lib1
        # 这里的 PUBLIC 关键字：传递依赖
        target_link_libraries(lib3 PUBLIC lib1)
        ```
        3. 顶层大管家：`CMakeLists.txt`
        
        - 在根目录下，我们要把所有子目录包含进来，并且配置主程序。
        ```cmake
        cmake_minimum_required(VERSION 3.21)
        project(hello_cmake)

        #引入所有子模块(被依赖的基础库尽量写在前面)
        add_subdirectory(lib1_static)
        add_subdirectory(lib2_dynamic)
        add_subdirectory(lib3_extra)

        #生成主程序
        add_executable(hello_cmake main.cpp)

        #传递依赖：主程序只直接链接 lib2 和 lib3，没有写lib1!
        target_link_libraries(hello_cmake PRIVATE lib3 lib2)
        ```
        3. 深度解析 —— 为什么主程序不写 `lib1` / `C++`源码写法?
        ```C++
        // main.cpp
        #include "lib3.h"
        #include "lib1.h" // 主程序竟然可以直接 #include lib1 的头文件！
        #include "lib2.h" 

        int main() {
            lib3_func(); // 正常调用 lib3
            lib1_math(); // 竟然还能直接调用 lib1 ！
            lib2_net(); 
            return 0;
        }
        ```
        - 在 `lib3_extra/CMakeLists.txt` 里的 `target_link_libraries(lib3 PUBLIC lib1)`
        - 这里`PUBLIC`关键字，在`CMake`里叫“使用需求传播”：
            1. 它告诉 `CMake`：`lib3` 的内部实现需要用到 `lib1`（链接代码）。
            2. 它同时告诉 `CMake`：任何链接了 `lib3` 的（比如主程序），也会自动继承 `lib1` 的所有东西（包括 `lib1` 的代码和头文件搜索目录）。
