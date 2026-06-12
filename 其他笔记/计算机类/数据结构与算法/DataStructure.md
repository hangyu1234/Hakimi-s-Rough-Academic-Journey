<div align="center">

# Data Structure Notes
</div>

---

笔记内容为对校内教材《数据结构思想与实现》和 CS61B 知识点的整理与概括，细节可能略有误差，若发现问题，欢迎指正，邮箱：[2312786648@qq.com](https://mail.qq.com/)
<div align="right">编者：DoroKnight</div>

---
## 目录

- [Data Structure Notes](#data-structure-notes)
  - [目录](#目录)
  - [一、基础知识](#一基础知识)
    - [1.1 算法与数据结构](#11-算法与数据结构)
      - [(1) 逻辑结构](#1-逻辑结构)
      - [(2) 结构运算](#2-结构运算)
    - [1.2 存储实现](#12-存储实现)
    - [1.3 算法分析](#13-算法分析)
      - [(1) 时间复杂度](#1-时间复杂度)
  - [二、线性表](#二线性表)
    - [2.1 线性表的抽象](#21-线性表的抽象)
    - [2.2 线性表的顺序实现](#22-线性表的顺序实现)
    - [2.3 线性表的链接实现](#23-线性表的链接实现)
      - [单链表类](#单链表类)
      - [双链表类](#双链表类)
      - [循环链表类](#循环链表类)

## 一、基础知识
### 1.1 算法与数据结构

数据结构是专门研究信息的**存储与处理**的一门学科。负责处理三个问题：
1. 理清数据之间的逻辑关系和处理要求
2. 数据在计算机中的存储问题
3. 数据处理的实现（实现的过程就是我们常说的**算法**）

#### (1) 逻辑结构
逻辑结构分为四类：
1. **集合结构**：
   这种结构数据元素之间的次序是任意的。除了**属于同一集合**外，元素之间无其他关系
2. **线性结构**：
   元素之间构成一个**有序序列**，元素之间有前驱和后继的关系：
   - **前驱**：元素之前的元素（第一个元素可能没有）
   - **后继**：元素之后的元素（最后一个元素可能没有）
3. **树状结构**：
   数据之间为**层次关系**：即**除了根元素外，每个元素仅有一个前驱，可以有多个后继，根元素没有前驱**。
4. **图状结构**：
   图为最一般的逻辑结构，前驱和后继都没有要求。

**注意**：
- 逻辑结构和数据元素本身无关
- 逻辑结构和数据元素个数无关

#### (2) 结构运算
数据结构的处理称为**数据结构的操作或运算**，常见运算有以下 8 种：
1) **创建运算** (create): 创建一个空的数据结构。

2) **清除运算** (clear): 删除数据结构中的所有数据元素。

3) **插入运算** (insert): 在数据结构指定的位置上插入一个新数据元素。
   
4) **删除运算** (remove): 将数据结构中的某个数据元素删去。

5) **搜索运算** (search): 在数据结构中搜索满足特定条件的数据元素。

6) **更新运算** (update): 修改数据结构中的某个数据元素的值。

7) **访问运算** (visit): 访问数据结构中的某个数据元素。

8) **遍历运算** (traverse): 按照某种次序访问数据结构中的每一数据元素，使每个数据元素恰好被访问一次。

### 1.2 存储实现
数据的存储实现有下述 4 种：
1. **顺序实现**：数据位于连续空间，可用相对位置找到数据，比如**数组**
2. **链接实现**：空间不连续，但是逻辑是连续的，可以根据前驱找后继或反过来，比如**链表**
3. **散列存储**：又称**哈希存储**，用于集合结构的数据存储。
4. **索引存储**：按照生成顺序进行存储

### 1.3 算法分析
一般算法分析分析的是其**时空性能**，也就是常说的**时间复杂度**和**空间复杂度**。
#### (1) 时间复杂度
时间复杂度通常使用**Big O**、**Big Θ**分析（又称渐进分析）
1. **Big O Notation**：用于描述函数的**渐近上界**，也就是说，最糟糕的情况是 O(x).
2. **Big Θ Notation**：用于描述函数的**渐近紧确界**，是精确描述算法实现代价的方式
3. **Little o Notation**：用于描述**非紧确的渐近上界**，也就是说是下界，一般用来表示最好的情况。

| 函数       | 名称       | 函数  | 名称 |
| :--------- | :--------- | :---- | :--- |
| $1$        | 常量       | $N^3$ | 立方 |
| $\log N$   | 对数       | $2^N$ | 指数 |
| $N$        | 线性       | $N!$  | 指数 |
| $N \log N$ | $N \log N$ | $N^N$ | 指数 |
| $N^2$      | 平方       |       |      |

下方是算法分析的两个定理：
**求和定理（定理 1.1）**：假定 $T_1(n)$、$T_2(n)$ 是程序段 P₁、P₂ 的运行时间，并且 $T_1(n)$ 是 $O(f(n))$ 的，而 $T_2(n)$ 是 $O(g(n))$ 的。那么，先运行 P₁、再运行 P₂ 的总的运行时间是：
$$
T_1(n) + T_2(n) = O(\max(f(n), g(n)))
$$

**求积定理（定理 1.2）**：如果 $T_1(n)$ 和 $T_2(n)$ 分别是 $O(f(n))$ 和 $O(g(n))$ 的，那么：
$$
T_1(n) \times T_2(n) = O(f(n) \times g(n))
$$
**证明**：根据已知条件，可得在 $n \ge n_1$ 时，$T_1(n) \le c_1 f(n)$ 成立。在 $n \ge n_2$ 时，$T_2(n) \le c_2 g(n)$ 成立。其中 $c_1, n_1$ 及 $c_2, n_2$ 都是常数。所以，在 $n \ge \max(n_1, n_2)$ 时：
$$
T_1(n) \times T_2(n) \le c_1 c_2 f(n) g(n)
$$
因此 $T_1(n) \times T_2(n)$ 是 $O(f(n) \times g(n))$ 的。

--- 
## 二、线性表
### 2.1 线性表的抽象
线性表的操作有如下几方面：

1) 创建一个空线性表 $\text{create}$。
2) 删除线性表中的所有数据元素 $\text{clear}$。
3) 求线性表的长度 $\text{length}$。
4) 在第 $i$ 个位置插入一个元素 $\text{insert}(i, x)$，使线性表从 $(a_0, a_1, \cdots, a_{i-1}, a_i, \cdots, a_{n-1})$ 变成 $(a_0, a_1, \cdots, a_{i-1}, x, a_i, \cdots, a_{n-1})$，参数 $i$ 的合法取值范围是 $0$ 到 $n$。
5) 删除第 $i$ 个位置的元素 $\text{remove}(i, x)$，使线性表从 $(a_0, a_1, \cdots, a_{i-1}, a_i, a_{i+1}, \cdots, a_{n-1})$ 变成 $(a_0, a_1, \cdots, a_{i-1}, a_{i+1}, \cdots, a_{n-1})$，参数 $i$ 的合法取值范围是 $0$ 到 $n-1$。
6) 搜索元素 $\text{search}(x)$，检查某个元素 $x$ 在线性表中是否出现，并返回 $x$ 的位置。
7) 返回线性表中第 $i$ 个数据元素的值 $\text{visit}(i)$。
8) 按序访问线性表的每一数据元素 $\text{traverse}$。

<details>
<summary><strong>线性表的抽象类(cpp)</strong></summary>

```cpp
template <class elemType>
class list
{
public:
    virtual void clear() = 0;
    // Remove all data elements from the linear list.
    // (删除线性表中的所有数据元素。)

    virtual int length() const = 0;
    // Find the length of the linear list.
    // (求线性表的长度。)

    virtual void insert(int i, const elemType &x) = 0;
    // Insert an element at the i-th position.
    // (在第 i 个位置插入一个元素。)

    virtual void remove(int i) = 0;
    // Remove the element at the i-th position.
    // (删除第 i 个位置的元素。)

    virtual int search(const elemType &x) const = 0;
    // Search whether a certain element x exists in the linear list.
    // (搜索某个元素 x 在线性表中是否出现。)

    virtual elemType visit(int i) const = 0;
    // Return the value of the i-th data element in the linear list.
    // (返回线性表中第 i 个数据元素的值。)

    virtual void traverse() const = 0;
    // Visit each data element of the linear list in sequence.
    // (按序访问线性表的每一数据元素。)

    virtual ~list() {};
};
```
</details>

<details>
<summary><strong>线性表的接口(java)</strong></summary>

```java
public interface List<E> {
    /**
     * Remove all data elements from the linear list.
     * 删除线性表中的所有数据元素
     */
    void clear();

    /**
     * Find the length of the linear list
     * 求线性表的长度
     */
    int length();

    /**
     * Insert an element at the i-th position
     * 在第 i 个位置插入元素
     */
    void insert(int i, E x);

    /**
     * Remove the element at i-th position
     */
    void remove(int i);

    /**
     * Search whether a certain element x exists in the linear list.
     */
    int search(E x);

    /**
     * Return the value of the i-th data element in the linear list
     */
    E visit(int i);

    /**
     * Visit each data element of the linear list in sequence
     */
    void traverse();
}
```
</details>

### 2.2 线性表的顺序实现
正如之前所说，线性结构是可以进行顺序存储的。称为**顺序表**，下面是顺序表的定义
<details>
<summary><strong>顺序表的定义(cpp)</strong></summary>

```cpp
template <class elemType>
class seqList : public list<elemType> {
private :
    elemType *data;         // The array stored datas
    int currentLength;      // Note the length of current array
    int maxSize;            // Restrict the edge of array 
                            // and decide when to expand the space
    void doubleSpace();     // Expand array space.

public :
    seqList(int intSize = 10);          // Constructor of seqList
    ~seqList();                         // Destructor of seqList

    // The abstract method of the abstract class
    void clear();
    int length();
    void insert(int i, const elemType &x);
    void remove(int i);
    int search(const elemType &x) const;
    elemType visit(int i) const;
    void traverse() const;  
}
```
</details>

<details>
<summary><strong>顺序表的实现(cpp)</strong></summary>

```cpp
template <class elemType>
seqList<elemType>::seqList(int initSize) {
    data = new elemType[initSize];
    maxSize = initSize;
    currentLength = 0;
}

template <class elemType>
seqList<elemType>::~seqList() {
    delete [] data;
}

template <class elemType> 
void seqList<elemType>::clear() const {
    currentLength = 0;      // Equal to delete the seqList.
}

template <class elemType>
int seqList<elemType>::length() {
    return currentLength;
}

template <class elemType>
elemType seqList<elemType>::visit(int i) const {
    return data[i];
}

template <class elemType>
void seqList<elemType>::traverse() const {
    std::cout << std::endl;
    for (int i = 0; i < currentLength; i += 1) {
        std::cout << data[i] << ' ';
    }
}

template <class elemType>
int seqList<elemType>::search(const elemType &x) const {
    for (int i = 0; i < currentLength && data[i] != x; i += 1);
    if (i == currentLength) return -1;      // Not exist.
    else return i;
}

template <class elemType>
void seqList<elemType>::doubleSpace() {
    elemType *temp = data;
    maxSize *= 2;

    data = new elemType[maxSize];
    for (int i = 0; i < currentLength; i += 1) data[i] = temp[i];
    delete [] temp;
}

template <class elemType>
void seqList<elemType>::insert(int i, const elemType &x) {
    if (currentLength == maxSize) doubleSpace();

    for (int j = currentLength; j > i; j -= 1) data[j] = data[j-1];
    data[i] = x;
    currentLength += 1;
}

template <class elemType>
void seqList<elemType>::remove(int i) {
    for (int j = i; j < currentLength - 1; j += 1) {
        data[j] = data[j + 1];
    }
    currentLength -= 1;
}
```
</details>

<details>
<summary><strong>顺序表的实现(java)</strong></summary>

```java
import java.util.Arrays;

public class SeqList<E> implements List<E> {
    private E[] data;               // Array to store elements
    private int size;               // Current size of the linear list

    private static final int DEFAULT_CAPACITY = 10;         // Default initial capacity

    // Constructor: Initialize the sequential list with a specified capacity.
    public SeqList(int initialCapacity) {
        if (initialCapacity < 0) {
            throw new IllegalArgumentException("Capacity cannot be negative.");
        }
        this.data = new E[initialCapacity];
        this.size = 0;
    }

    // Default constructor
    public SeqList() {
        this(DEFAULT_CAPACITY);
    }

    @Override
    public void clear() {
        // Set references to null in the array to allow the garbage collector to reclaim memory
        for (int i = 0; i < size; i += 1) {
            data[i] = null;
        }
        size = 0;
    }

    @Override
    public int length() {
        return size;
    }

    @Override
    public void insert(int i, E x) {
        // Check the vaildity of the insertion position
        if (i < 0 || i > size) {
            throw new IndexOutOfBoundsException("Insertion index out of bound: " + i);
        }

        // Capacity expansion mechanism
        if (size == data.length) {
            ensureCapacity();
        }

        // Shift the element at index i and subsequent elements backward by one position
        System.arraycopy(data, i, data, i + 1, size - i);
        data[i] = x;
        size += 1;
    }

    @Override 
    public void remove(int i) {
        // Check index vaildity
        if (i < 0 || i > size) {
            throw new IndexOutOfBoundsException("Removal index out of bounds: " + i);
        }

        // Shift the elements after index i forword by one position
        int numMoved = size - i + 1;
        if (numMoved > 0) {
            System.arraycopy(data, i + 1, data, i, numMoved);
        }

        size -= 1;
        data[size] = null;      // Prevent memory leak
    }

    @Override 
    @SuppressWarnings("unchecked")
    public int search(E x) {
        if (x == null) {
            for (int i = 0; i < size; i += 1) {
                if (data[i] == null) return i;
            }
        } else {
            for (int i = 0; i < size; i += 1) {
                if (x.equals(data[i])) return i;     // Use equals to compare object values in Java
            }
        }
        return -1;
    }

    @Override
    @SuppressWarnings("unchecked")
    public E visit(int i) {
        if (i < 0 || i >= size) {
            throw new IndexOutOfBoundsException("Visit index out of bounds: " + i);
        }
        return data[i];
    }

    @Override 
    public void traverse() {
        for (int i = 0; i < size; i += 1) {
            System.out.print(data[i] + " ");
        }
        System.out.println();
    }

    // Internal private method: Dynamically expand capacity to 1.5 times the original capacity.
    private void ensureCapacoty() {
        int oldCapacity = data.length;
        int newCapacity = oldCapacity + (oldCapacity >> 1)   // 1.5x capacity
        if (newCapacity == 0) {
            newCapacity = 1;
        }
        data = Arrays.copyOf(data, newCapacity);
    }
}
```

**注释**：
1. `@Override`: 意为**重写**，类似与 C++ 中的 `override` 关键字，但是 Java 中的要求略松一些。只检查是否进行了实现
2. `@SuppressWarnings("unchecked")`: 这是一个**编译器注释**，告知编译器这里的转换风险不用检查，不要在编译时报错或提示
3. `Arrays.copyOf()`: 
   用于**复制旧数组并开辟一个指定长度的新数组**，实现**动态扩容**。下面是它的参数和用法：
   ```java
   public static <T, U> T[] copyOf(U[] original, int newLength);
   ```
   - 若 `newLength` 大于原数组长度，创建一个新数组，对应复制以后，在剩余的空位使用默认值（对象使用 `null`，数字使用 `0`）填充
   - 若 `newLength` 小于原数组长度，直接对原数组进行截断。

4. `System,arraycopy()`:
   这是 Java 中的原生的静态方法，**用于两个数组之间的高效的内存块复制**，下方是原型：
   ```java
   System.arraycopy(Object src, int srcPos, Object dest, int destPos, int length);
   ```
    | 参数          | 含义                         | 对应示例中的具体行为                             |
    | :------------ | :--------------------------- | :----------------------------------------------- |
    | **`src`**     | **源数组**（从哪里开始复制） | `data` （当前数组）                              |
    | **`srcPos`**  | **源数组的起始复制索引**     | `i` （从被插入的位置开始）                       |
    | **`dest`**    | **目标数组**（复制到哪里去） | `data` （还是当前数组，即**原地移动**）          |
    | **`destPos`** | **目标数组的开始粘贴索引**   | `i + 1` （向后错开一位，腾出空间）               |
    | **`length`**  | **总共需要复制的元素个数**   | `size - i` （当前位置 `i` 到末尾的所有元素总数） |
</details> 

### 2.3 线性表的链接实现
线性表是可以进行顺序存储的，但是正如上面的实现所显示的那样，**顺序实现不建议进行多次的插入与删除操作**，这样会导致时间复杂度很高（ O(N) ）。若要进行多次的插入与删除操作，建议使用**链接实现**

#### 单链表类
<details>
<summary><strong>单链表类的定义(cpp)</strong></summary>

```cpp
template <class elemType>
class sLinkList : public list<elemType> {
private:
    struct node {           // Node class in Single List
        elemType data;
        node *next;

        node(const elemType &x, node *n = nullptr) { 
            data = x;
            next = n;
        }
        node() : next(nullptr) {}
        ~node() {}
    };

    node *head;         // Head pointer
    int currentLength;  // The length of LinkList

    node *move(int i) const;    // Return the address of i-th node.

public:
    sLinkList();
    ~sLinkList() { clear(); delete head; }

    void clear();
    int length() const { return currentLength; }
    void insert(int i, const elemType &x);
    void remove(int i);
    int search(const elemType &x) const;
    elemType visit(int i) const;
    void traverse() const;
}
```
</details>

<details>
<summary><strong>单链表类的实现(cpp)</strong></summary>

```cpp
template <class elemType>
sLinkList<elemType>::node *sLinkList<elemType>::move(int i) const {
    node *p = head;
    while (i-- >= 0) {
        p = p->next;
    }
    return p;
}

template <class elemType>
sLinkList<elemType>::sLinkList() {
    head = new node;        // Set the sentinal node
    currentLength = 0;
}

template <class elemType>
void sLinkList<elemType>::clear() {
    node *p = head->next, *q;   // q is the helper pointer.
    head->next = nullptr;
    while (p != nullptr) {
        q = p->next;        // Store the next address temporary
        delete p;
        p = q;
    }
    currentLength = 0;
}

template <class elemType>
void sLinkList<elemType>::insert(int i, const elemType &x) {
    node *pos;

    pos = move(i - 1);          // Find the perdecessor
    pos->next = new node(x, pos->next);      // Set a new node, whose next is pos's next(now).
    currentLength += 1;
}

template <class elemType>
void sLinkList<elemType>::remove(int i) {
    node *pos, *delp;
    pos = move(i - 1);          // Find the predecessor
    delp = pos->next;           // Point the target node
    pos->next = delp->next;     // Link the next next node
    delete delp;
    currentLength -= 1;
}

template <class elemType>
int sLinkList<elemType>::search(const elemType &x) const {
    node *p = head->next;
    int i = 0;

    while (p != nullptr && p->data != x) {
        p = p->next;
        i += 1;
    }

    if (p == nullptr) return -1;        // Failed
    else return i;                      // Successfully
}

template <class elemType>
elemType sLinkList<elemType>::visit(int i) const {
    return move(i)->data;
}

template <class elemType>
void sLinkList<elemType>::traverse() const {
    node *p = head->next;       // Point the sentinal's next node.
    std::cout << std::endl;
    while (p != nullptr) {
        std::cout << p->data << " ";
        p = p->next;
    }
    std::cout << std::endl;
}
```
</details>

<details>
<summary><strong>单链表的 Java 接口</strong></summary>

```java
public interface List<E> {
    /**
     * Remove all elements from the list.
     */
    void clear();   
    
    /**
     * Return the length of the List.
     */
    int length();

    /**
     * Insert element x at index i.
     */
    void insert(int i, E x);

    /**
     * Remove the element at index i.
     */
    void remove(int i);

    /**
     * Search for element x and return its index.
     */ 
    int search(E x);

    /**
     * Print all elements in the list.
     */
    E visit(int i);

    /**
     * Print all elements in the list.
     */
    void traverse();
}
```
</details>

<details>
<summary><strong>单链表的 Java 实现</strong></summary>

```java
public class SlinkList<E> implements List<E> {
    /**
     * Node class in singly linked list.
     */
    private class Node {
        E data;
        Node next;

        /**
         * Create a node with data and next pointer.
         */
        Node(E data, Node next) {
            this.data = data;
            this.next = next;
        }

        /**
         * Create an empty node.
         */
        Node() {
            this(null, null);
        }
    }

    private Node head;          // Sentinal node.
    private int currentLength;  // Length of the list.

    /**
     * Create an empty singly linked list with a sentinel node.
     */
    public SLinkList() {
        head = new Node();
        currentLength = 0;
    }

    /**
     * Retrun the address/reference of the i-th node
     */
    private Node move(int i) {
        Node p = head;

        while (i >= 0) {
            p = p.next;
            i -= 1;
        }

        return p;
    }

    /**
     * Check whether the index is valid for visiting or removing.
     */
    private void checkIndexForVisitOrRemove(int i) {
        if (i < 0 || i >= currentLength) {
            throw new IndexOutOfBoundsException("Index: " + i + ", Length: " + currentLength);
        }
    }

    /**
     * Check whether the index is vaild for insertion.
     */
    private void checkIndexForInsert(int i) {
        if (i < 0 || i > currentLength) {
            throw new IndexOutOfBoundsException("Index: " + i + ", Length: " + currentLength);
        }
    }

    @Override
    public void clear() {
        Node p = head.next;
        Node q;

        head.next = null;

        while (p != null) {
            q = p.next;         // Store the next node temporarily
            p.next = null;      // Disconnect the current node.
            p = q;
        }

        currentLength = 0;
    }

    @Override 
    public int length() {
        return currentLength;
    }

    @Override 
    public void insert(int i, E x) {
        checkIndexForInsert(i);

        Node pos = move(i - 1);             // Find the predecessor
        pos.next = new Node(x, pos.next);   // Insert the new node.

        currentLength += 1；
    }

    @Override
    public void remove(int i) {
        checkIndexForVisitOrRemove(i);

        Node pos = move(i - 1);             // Find the predecessor
        Node delp = pos.next;               // Point to the target node.

        pos.next = delp.next;               // Link to the next node.
        delp.next = null;                   // Disconnect the deleted Node.

        currentLength -= 1;
    }

    @Override 
    public int search(E x) {
        Node p = head.next;
        int i = 0;

        while (p != null) {
            if (x == null) {
                if (p.data == null) {
                    return i;
                }
            } else {
                if (x.equals(p.data)) {
                    return i;
                }
            }

            p = p.next;
            i += 1;
        }

        return -1;          // Failed.
    }

    @Override
    public E visit(int i) {
        checkIndexForVisitOrRemove(i);

        return move(i).data;
    }

    @Override 
    public void traverse() {
        Node p = head.next;

        System.out.println();

        while (p != null) {
            System.out.print(p.data + " ");
            p = p.next;
        }

        System.out.println();
    }
}
```
</details>

#### 双链表类
双链表相对于正常的单链表来讲，有着**双向检索**的特点，可以节省部分遍历的时间（找直接前驱和直接后继）
<details>
<summary><strong>双链表的定义(cpp)</strong></summary>

```cpp
template <class elemType>
class dLinkList : public list<elemType> {
private :
    struct Node {                   // Node of DoubleLinkList
        elemType data;              
        Node *prev, *next;          // Predecessor Pointer and Successor Pointer

        Node(const elemType &x, Node *p = nullptr, Node *n = nullptr) {
            data = x;
            next = n;
            prev = p;
        }
        Node() : next(nullptr), prev(nullptr) {}
        ~Node() {}
    };

    Node *head, *tail;          // Head Pointer and Tail Pointer
    int currentLength;          // The length of the list

    Node *move(int i) const;    // Return the address of i-th Node.

public :
    dLinkList();
    ~dLinkList() { clear(); delete head; delete tail; }

    void clear();
    int length() const { return currentLength; }
    void insert(int i, const elemType &x);
    void remove(int i);
    int search(const elemType &x) const;
    elemType visit(int i) const;
    void traverse() const;
}
```
</details>

<details>
<summary><strong>双链表的实现(cpp)</strong></summary>

```cpp
template <class elemType>
dLinkList<elemType>::dLinkList() {
    head = new Node;                     // Head Sentinal Node
    head->next = tail = new Node;        // Tail pointer point the last node
    tail->prev = head;                   // Set the predecessor
    currentLength = 0;      
}

template <class elemType>
dLinkList<elemType>::Node *dLinkList<elemType>::move(int i) const {
    Node *p = head;
    while (i-- >= 0) p = p->next;
    return p;
}

template <class elemType>
void dLinkList<elemType>::insert(int i, const elemType &x) {
    Node *pos, *tmp;
    pos = move(i);                          // Find the i-th Node
    tmp = new Node(x, pos->prev, pos);      // Store the i-th Node, Set the predecessor as (i-1)-th node and successor as i-th node.
    pos->prev->next = tmp;                  // The predecessor of (i-1)-th is x
    pos->prev = tmp;                        // The predecessor of formal i-th is x
    currentLength += 1;
}

template <class elemType>
void dLinkList<elemType>::remove(int i) {
    Node *pos;

    pos = move(i);                  // pos point the deleted node
    pos->prev->next = pos->next;    // Set (i-1)-th node's successor is (i+1)-th
    pos->next->prev = pos->prev;     // Set (i+1)-th node's successor is (i-1)-th
    delete pos;
    currentLength -= 1;
}

template <class elemType>
int dLinkList<elemType>::search(const elemType &x) const {
    Node *p = head->next;
    int i;

    for (i = 0; p != tail && p->data != x; i += 1) p = p->next;
    if (p == tail) return -1;
    else return i;
}

template <class elemType>
elemType dLinkList<elemType>::visit(int i) const {
    return move(i)->data;
}

template <class elemType>
void dLinkList<elemType>::traverse() const {
    Node *p = head->next;
    std::cout << std::endl;
    while (p != tail) {
        std::cout << p->data << " ";
        p = p->next;
    }

    std::cout << std::endl;
}
```
</details>

<details>
<summary><strong>双链表的 Java 接口</strong></summary>

```java
public interface List<E> {
    /**
     * Remove all elements from the list.
     */
    void clear();   
    
    /**
     * Return the length of the List.
     */
    int length();

    /**
     * Insert element x at index i.
     */
    void insert(int i, E x);

    /**
     * Remove the element at index i.
     */
    void remove(int i);

    /**
     * Search for element x and return its index.
     */ 
    int search(E x);

    /**
     * Print all elements in the list.
     */
    E visit(int i);

    /**
     * Print all elements in the list.
     */
    void traverse();
}
```
</details>

<details>
<summary><strong>双链表的 Java 实现</strong></summary>

```java
public class DLinkList<E> implements List<E> {
    /**
     * Node class in doubly Linked list
     */
    private class Node {
        E data;
        Node prev;
        Node next;

        /**
         * Create a node with data, predecessor pointer, and successor pointer.
         */
        Node(E data, Node prev, Node next) {
            this.data = data;
            this.next = next;
            this.prev = prev;
        }

        /**
         * Create an empty doubly linked list with head and tail sentinel nodes.
         */
        public DLinkList() {
            head = new Node();
            tail = new Node();

            head.next = tail;
            tail.prev = head;

            currentLength = 0;
        }
    }

    /**
     * Return the reference of the i-th node.
     * If i == currentLength, return the tail sentinel node.
     */
    private Node move(int i) {
        Node p;

        /**
         * Serach from the nearer side.
         */
        if ( i < currentLength / 2 ) {
            p = head.next;

            while ( i > 0 ) {
                p = p.next;
                i -= 1;
            }
        } else {
            p = tail;

            while (i < currentLength) {
                p = p.prev;
                i += 1;
            }
        }

        return p;
    }

    /**
     * Check whether the index is vaild for visiting or removing
     */
    private void checkIndexForVisitOrRemove(int i) {
        if (i < 0 || i >= currentLength) {
            throw new IndexOutOfBoundsException("Index: " + i + ", Length: " + currentLength);
        }
    }

    /**
     * Check whether the index is vaild for insertion.
     */
    private void checkIndexForInsert(int i) {
        if (i < 0 || i > currentLength) {
            throw new IndexOutOfBoundsException("Index: " + i + ", Length: " + currentLength);
        }
    }

    @Override
    public void clear() {
        Node p = head.next;
        Node q;

        while (p != tail) {
            q = p.next;

            p.prev = null;
            p.next = null;

            p = 1;
        }

        head.next = tail;
        tail.prev = head;

        currentLength = 0;
    }

    @Override 
    public int length() {
        return currentLength;
    }

    @Override
    public void insert(int i, E x) {
        checkIndexForInsert(i);

        Node pos = move(i);                     // Find the i-th node.
        Node temp = new Node(x, pos.prev, pos)  // Create the new node.

        pos.prev.next = temp;                   // Link predecessor to new node
        pos.prev = temp;                        // Link current node back to new node

        currentLength += 1;
    }

    @Override
    public void remove(int i) {
        checkIndexForVisitOrRemove(i);

        Node pos = move(i);                     // Find the node to be deleted
        
        pos.prev.next = pos.next;               // Link predecessor to successor.
        pos.next.prev = pos.prev;               // Link successor back to predecessor

        pos.prev = null;
        pos.next = null;

        currentLength -= 1;
    }

    @Override
    public int search(E x) {
        Node p = head.next;
        int i = 0;

        while (p != tail) {
            if (x == null) {
                if (p.data == null) {
                    return i;
                }
            } else {
                if (x.equals(p.data)) {
                    return i;
                }
            }

            p = p.next;
            i += 1;
        }

        return -1;
    }

    @Override 
    public E visit(int i) {
        checkIndexForVisitOrRemove(i);

        return move(i).data;
    }

    @Override
    public void traverse() {
        Node p = head.next;

        System.out.println();

        while(p != tail)_ {
            System.out.print(p.data + " ");
            p = p.next;
        }

        System.out.println();
    }
}
```
</details>

#### 循环链表类
循环链表有一个好处，省去了尾节点，可以向两边遍历，理论存储上不会越界。
<details>
<summary><strong>循环链表的定义(cpp)</strong></summary>

```cpp
template <class elemType>
class cLinkList : public list<elemType> {
private:
    struct Node {
        elemType data;
        Node *next;

        Node(const elemType &x, Node *n = nullptr) {
            data = x;
            next = n;
        }

        Node() {
            next = nullptr;
        }

        ~Node() {}
    };

    Node *tail;          // Tail pointer. 
    int currentLength;   // Length of circular linked list.

    Node *move(int i) const;

public:
    cLinkList();
    ~cLinkList();

    void clear();
    int length() const;
    void insert(int i, const elemType &x);
    void remove(int i);
    int search(const elemType &x) const;
    elemType visit(int i) const;
    void traverse() const;
};
```
</details>

<details>
<summary><strong>循环链表的实现(cpp)</strong></summary>

```cpp
template <class elemType>
cLinkList<elemType>::cLinkList() {
    tail = nullptr;
    currentLength = 0;
}

template <class elemType>
cLinkList<elemType>::~cLinkList() {
    clear();
}

template <class elemType>
typename cLinkList<elemType>::Node *cLinkList<elemType>::move(int i) const {
    Node *p = tail->next;   // Start from the first node. 

    while (i > 0) {
        p = p->next;
        i -= 1;
    }

    return p;
}

template <class elemType>
void cLinkList<elemType>::clear() {
    if (tail == nullptr) {
        return;
    }

    Node *p = tail->next;   // First node. 
    Node *q;

    tail->next = nullptr;   // Break the circular link. 

    while (p != nullptr) {
        q = p->next;        // Store the next node temporarily. 
        delete p;
        p = q;
    }

    tail = nullptr;
    currentLength = 0;
}

template <class elemType>
int cLinkList<elemType>::length() const {
    return currentLength;
}

template <class elemType>
void cLinkList<elemType>::insert(int i, const elemType &x) {
    if (i < 0 || i > currentLength) {
        throw "Index out of range";
    }

    Node *tmp;

    if (currentLength == 0) {
        tmp = new Node(x);
        tmp->next = tmp;
        tail = tmp;
    } else if (i == 0) {
        tmp = new Node(x, tail->next);
        tail->next = tmp;
    } else if (i == currentLength) {
        tmp = new Node(x, tail->next);
        tail->next = tmp;
        tail = tmp;
    } else {
        Node *pos = move(i - 1);       // Find the predecessor. 
        tmp = new Node(x, pos->next);
        pos->next = tmp;
    }

    currentLength += 1;
}

template <class elemType>
void cLinkList<elemType>::remove(int i) {
    if (i < 0 || i >= currentLength) {
        throw "Index out of range";
    }

    Node *delp;

    if (currentLength == 1) {
        delete tail;
        tail = nullptr;
    } else if (i == 0) {
        delp = tail->next;             // First node. 
        tail->next = delp->next;       // Tail points to the new first node. 
        delete delp;
    } else {
        Node *pos = move(i - 1);       // Find the predecessor. 
        delp = pos->next;

        pos->next = delp->next;

        if (delp == tail) {
            tail = pos;
        }

        delete delp;
    }

    currentLength -= 1;
}

template <class elemType>
int cLinkList<elemType>::search(const elemType &x) const {
    if (tail == nullptr) {
        return -1;
    }

    Node *p = tail->next;
    int i = 0;

    while (i < currentLength && p->data != x) {
        p = p->next;
        i += 1;
    }

    if (i == currentLength) {
        return -1;
    } else {
        return i;
    }
}

template <class elemType>
elemType cLinkList<elemType>::visit(int i) const {
    if (i < 0 || i >= currentLength) {
        throw "Index out of range";
    }

    return move(i)->data;
}

template <class elemType>
void cLinkList<elemType>::traverse() const {
    if (tail == nullptr) {
        std::cout << std::endl;
        return;
    }

    Node *p = tail->next;

    std::cout << std::endl;

    for (int i = 0; i < currentLength; i += 1) {
        std::cout << p->data << " ";
        p = p->next;
    }

    std::cout << std::endl;
}
```
</details>

<details> 
<summary><strong>循环链表的 Java 实现</strong></summary>

```java
public class CLinkList<E> implements List<E> {
    /**
     * Node class in circular singly linked list.
     */
    private class Node {
        E data;
        Node next;

        /**
         * Create a node with data and next pointer.
         */
        Node(E data, Node next) {
            this.data = data;
            this.next = next;
        }

        /**
         * Create a node with only data.
         */
        Node(E data) {
            this(data, null);
        }
    }

    private Node tail;          // Tail pointer.
    private int currentLength;  // Length of the circular linked list. 

    /**
     * Create an empty circular linked list.
     */
    public CLinkList() {
        tail = null;
        currentLength = 0;
    }

    /**
     * Return the reference of the i-th node.
     */
    private Node move(int i) {
        Node p = tail.next;     // Start from the first node. 

        while (i > 0) {
            p = p.next;
            i--;
        }

        return p;
    }

    /**
     * Check whether the index is valid for visiting or removing.
     */
    private void checkIndexForVisitOrRemove(int i) {
        if (i < 0 || i >= currentLength) {
            throw new IndexOutOfBoundsException("Index: " + i + ", Length: " + currentLength);
        }
    }

    /**
     * Check whether the index is valid for insertion.
     */
    private void checkIndexForInsert(int i) {
        if (i < 0 || i > currentLength) {
            throw new IndexOutOfBoundsException("Index: " + i + ", Length: " + currentLength);
        }
    }

    @Override
    public void clear() {
        if (tail == null) {
            return;
        }

        Node p = tail.next;
        Node q;

        tail.next = null;       // Break the circular link. 

        while (p != null) {
            q = p.next;         // Store the next node temporarily. 
            p.next = null;      // Disconnect the current node. 
            p = q;
        }

        tail = null;
        currentLength = 0;
    }

    @Override
    public int length() {
        return currentLength;
    }

    @Override
    public void insert(int i, E x) {
        checkIndexForInsert(i);

        Node tmp;

        if (currentLength == 0) {
            tmp = new Node(x);
            tmp.next = tmp;
            tail = tmp;
        } else if (i == 0) {
            tmp = new Node(x, tail.next);
            tail.next = tmp;
        } else if (i == currentLength) {
            tmp = new Node(x, tail.next);
            tail.next = tmp;
            tail = tmp;
        } else {
            Node pos = move(i - 1);     // Find the predecessor. 
            tmp = new Node(x, pos.next);
            pos.next = tmp;
        }

        currentLength++;
    }

    @Override
    public void remove(int i) {
        checkIndexForVisitOrRemove(i);

        Node delp;

        if (currentLength == 1) {
            tail.next = null;
            tail = null;
        } else if (i == 0) {
            delp = tail.next;           // First node. 
            tail.next = delp.next;      // Tail points to the new first node. 
            delp.next = null;
        } else {
            Node pos = move(i - 1);     // Find the predecessor. 
            delp = pos.next;

            pos.next = delp.next;

            if (delp == tail) {
                tail = pos;
            }

            delp.next = null;
        }

        currentLength--;
    }

    @Override
    public int search(E x) {
        if (tail == null) {
            return -1;
        }

        Node p = tail.next;
        int i = 0;

        while (i < currentLength) {
            if (x == null) {
                if (p.data == null) {
                    return i;
                }
            } else {
                if (x.equals(p.data)) {
                    return i;
                }
            }

            p = p.next;
            i++;
        }

        return -1;
    }

    @Override
    public E visit(int i) {
        checkIndexForVisitOrRemove(i);

        return move(i).data;
    }

    @Override
    public void traverse() {
        if (tail == null) {
            System.out.println();
            return;
        }

        Node p = tail.next;

        System.out.println();

        for (int i = 0; i < currentLength; i++) {
            System.out.print(p.data + " ");
            p = p.next;
        }

        System.out.println();
    }
}
```
</details>

---