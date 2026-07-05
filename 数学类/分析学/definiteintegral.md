# 定积分

上一章介绍了不定积分。本章介绍单变量函数的定积分，重点包括 Riemann 积分的定义、基本性质、微积分基本定理、积分计算方法以及可积性判别。

## 目录

1. [定积分的概念](#一定积分的概念)
2. [定积分的性质](#二定积分的性质)
3. [微积分基本定理](#三微积分基本定理)
4. [分部积分法与换元法](#四分部积分法与换元法)
5. [可积性理论](#五可积性理论)
6. [Lebesgue 定理](#六lebesgue-定理)

## 一、定积分的概念

定积分最早的重要应用来自几何和物理，例如求曲边梯形面积、位移、功等。Riemann 积分的核心思想是：把区间切成很多小段，在每一小段上取一个代表点，用矩形面积之和逼近整体量。

### 1. Riemann 和与定积分的定义

设函数 \(f(x)\) 在闭区间 \([a,b]\) 上有定义。

给定 \([a,b]\) 的一个分划

$$
P:\quad a=x_0<x_1<\cdots <x_n=b,
$$

记

$$
\Delta x_i=x_i-x_{i-1},\qquad \|P\|=\max_{1\le i\le n}\Delta x_i.
$$

在每个小区间 \([x_{i-1},x_i]\) 中任取一点 \(\xi_i\)，称为介点。对应的 Riemann 和为

$$
\sum_{i=1}^n f(\xi_i)\Delta x_i.
$$

如果存在常数 \(I\)，使得当 \(\|P\|\to 0\) 时，对于任意分划和任意介点的 Riemann 和都有

$$
\sum_{i=1}^n f(\xi_i)\Delta x_i \longrightarrow I,
$$

则称 \(f\) 在 \([a,b]\) 上 Riemann 可积，并记

$$
\int_a^b f(x)\,\mathrm{d}x=I.
$$

等价地，也可以写成 \(\varepsilon\)-\(\delta\) 形式：对任意 \(\varepsilon>0\)，存在 \(\delta>0\)，只要 \(\|P\|<\delta\)，就有

$$
\left|\sum_{i=1}^n f(\xi_i)\Delta x_i-I\right|<\varepsilon.
$$

注意：介点 \(\xi_i\) 是任取的。若函数已经知道 Riemann 可积，则为了计算积分，可以选取特殊介点，例如左端点、右端点或中点；但在证明可积性或使用定义时，不能只依赖某一种特殊介点。

### 2. 定积分的记号

定积分必须带有上下限：

$$
\int_a^b f(x)\,\mathrm{d}x.
$$

其中 \(a\) 是积分下限，\(b\) 是积分上限，\(f(x)\) 是被积函数，\(\mathrm{d}x\) 表示积分变量。

不带上下限的

$$
\int f(x)\,\mathrm{d}x
$$

通常表示不定积分，即原函数族，而不是定积分。

### 3. 定积分的简单性质

设 \(f,g\) 在 \([a,b]\) 上 Riemann 可积。

1. 若 \(f(x)\ge 0\)，则

   $$
   \int_a^b f(x)\,\mathrm{d}x\ge 0.
   $$

2. 若 \(f(x)\ge g(x)\)，则

   $$
   \int_a^b f(x)\,\mathrm{d}x\ge \int_a^b g(x)\,\mathrm{d}x.
   $$

3. 线性性质：

   $$
   \int_a^b \bigl(f(x)+g(x)\bigr)\,\mathrm{d}x
   =
   \int_a^b f(x)\,\mathrm{d}x
   +
   \int_a^b g(x)\,\mathrm{d}x,
   $$

   $$
   \int_a^b c f(x)\,\mathrm{d}x
   =
   c\int_a^b f(x)\,\mathrm{d}x,
   $$

   其中 \(c\) 为常数。减法情形由线性性质直接推出。

### 4. Newton-Leibniz 公式

设 \(f\) 在 \([a,b]\) 上 Riemann 可积，函数 \(F\) 在 \([a,b]\) 上连续、在 \((a,b)\) 上可导，并且

$$
F'(x)=f(x)\qquad (x\in(a,b)).
$$

则

$$
\int_a^b f(x)\,\mathrm{d}x=F(b)-F(a).
$$

这个公式是定积分计算中最重要的工具之一。证明通常使用分割区间、Lagrange 中值定理和 Riemann 和的定义。

在用 Riemann 和计算定积分时，常见思路是选择合适的介点，使和式出现裂项相消。由于定积分定义要求任意介点的极限一致，若先算出某个特殊和式的极限，还需要说明它与一般 Riemann 和的差趋于 \(0\)。

## 二、定积分的性质

本节整理定积分的常用性质和平均值定理。许多结论与连续性有关。

### 1. 基本性质

1. 若 \(f\) 在 \([a,b]\) 上 Riemann 可积，则 \(f\) 在 \([a,b]\) 上有界。

2. 若 \(f\) 在 \([a,b]\) 上连续，则 \(f\) 在 \([a,b]\) 上 Riemann 可积；反之不成立。Riemann 可积函数可以有间断点。

3. 积分区间可加性：若 \(c\in[a,b]\)，则

   $$
   \int_a^b f(x)\,\mathrm{d}x
   =
   \int_a^c f(x)\,\mathrm{d}x
   +
   \int_c^b f(x)\,\mathrm{d}x.
   $$

4. 若 \(f\) 在 \([a,b]\) 上连续，\(f(x)\ge 0\)，且 \(f\) 不恒等于 \(0\)，则

   $$
   \int_a^b f(x)\,\mathrm{d}x>0.
   $$

   这里的连续性很重要。若只知道 \(f\ge 0\) 且 \(f\) 可积，积分可能等于 \(0\)，例如只在一个点取正值的函数。

5. 绝对值不等式：

   $$
   \left|\int_a^b f(x)\,\mathrm{d}x\right|
   \le
   \int_a^b |f(x)|\,\mathrm{d}x.
   $$

### 2. 积分第一平均值定理

设 \(f\) 在 \([a,b]\) 上连续，\(g\) 在 \([a,b]\) 上 Riemann 可积，且 \(g\) 不变号，则存在 \(\xi\in[a,b]\)，使得

$$
\int_a^b f(x)g(x)\,\mathrm{d}x
=
f(\xi)\int_a^b g(x)\,\mathrm{d}x.
$$

证明时通常分 \(\int_a^b g(x)\,\mathrm{d}x=0\) 与不等于 \(0\) 两种情况；在非零情形中使用连续函数的最值定理。

## 三、微积分基本定理

### 1. 变限积分函数

设

$$
F(x)=\int_a^x f(t)\,\mathrm{d}t.
$$

这个函数称为变上限积分函数。

1. 若 \(f\) 在 \([a,b]\) 上 Riemann 可积，则 \(F\) 在 \([a,b]\) 上连续。

2. 若 \(f\) 在 \(x_0\in(a,b)\) 处连续，则 \(F\) 在 \(x_0\) 处可导，且

   $$
   F'(x_0)=f(x_0).
   $$

这两个结论主要由积分区间可加性和连续性的定义推出。

### 2. 微积分基本定理

第一种形式：若 \(f\) 在 \([a,b]\) 上连续，则

$$
F(x)=\int_a^x f(t)\,\mathrm{d}t
$$

在 \((a,b)\) 上可导，并且

$$
F'(x)=f(x).
$$

若按端点的一侧导数理解，也可在闭区间端点处作相应讨论。

第二种形式：若 \(F\in C^1([a,b])\)，则

$$
F(b)-F(a)=\int_a^b F'(x)\,\mathrm{d}x.
$$

更一般地，若 \(f\) 在 \([a,b]\) 上 Riemann 可积，并且存在 \(F\) 在 \([a,b]\) 上连续、在 \((a,b)\) 上可导，使得 \(F'(x)=f(x)\)，则仍有

$$
\int_a^b f(x)\,\mathrm{d}x=F(b)-F(a).
$$

### 3. 变限积分函数求导

若 \(f\) 连续，\(u,v\) 可导，则

$$
\frac{\mathrm{d}}{\mathrm{d}x}
\left(\int_{v(x)}^{u(x)} f(t)\,\mathrm{d}t\right)
=
f(u(x))u'(x)-f(v(x))v'(x).
$$

这是微积分基本定理和链式法则的直接应用。

### 4. 积分第二平均值定理

设 \(f\) 在 \([a,b]\) 上 Riemann 可积，\(g\) 在 \([a,b]\) 上单调，则存在 \(\xi\in[a,b]\)，使得

$$
\int_a^b f(x)g(x)\,\mathrm{d}x
=
g(a)\int_a^\xi f(x)\,\mathrm{d}x
+
g(b)\int_\xi^b f(x)\,\mathrm{d}x.
$$

特别地，若 \(g\ge 0\)、单调递减且 \(g(b)=0\)，则可化为

$$
\int_a^b f(x)g(x)\,\mathrm{d}x
=
g(a)\int_a^\xi f(x)\,\mathrm{d}x.
$$

这个定理也称 Bonnet 第二平均值定理，证明通常需要 Abel 变换或 Darboux 和等工具。

## 四、分部积分法与换元法

分部积分法和换元法在定积分中同样重要，但使用时要特别注意积分上下限的变化。

### 1. 分部积分法

若 \(u,v\in C^1([a,b])\)，则

$$
\int_a^b u(x)v'(x)\,\mathrm{d}x
=
u(b)v(b)-u(a)v(a)
-
\int_a^b u'(x)v(x)\,\mathrm{d}x.
$$

常写作

$$
\int_a^b u\,\mathrm{d}v
=
\left.uv\right|_a^b-\int_a^b v\,\mathrm{d}u.
$$

### 2. 换元法

设 \(f\) 在包含 \(\varphi([c,d])\) 的区间上连续，\(\varphi\in C^1([c,d])\)。则

$$
\int_c^d f(\varphi(t))\varphi'(t)\,\mathrm{d}t
=
\int_{\varphi(c)}^{\varphi(d)} f(x)\,\mathrm{d}x.
$$

如果 \(\varphi(c)=a\)、\(\varphi(d)=b\)，则

$$
\int_a^b f(x)\,\mathrm{d}x
=
\int_c^d f(\varphi(t))\varphi'(t)\,\mathrm{d}t.
$$

注意：右端必须有 \(\varphi'(t)\)，否则公式一般不成立。

### 3. 带积分余项的 Taylor 展开式

设 \(f\in C^{n+1}\)，则在适当区间内有

$$
\begin{aligned}
f(x)
&= f(a)+f'(a)(x-a)+\frac{f''(a)}{2!}(x-a)^2+\cdots
  +\frac{f^{(n)}(a)}{n!}(x-a)^n+R_n(x),\\
R_n(x)
&=\frac{1}{n!}\int_a^x f^{(n+1)}(t)(x-t)^n\,\mathrm{d}t.
\end{aligned}
$$

该公式可以由微积分基本定理和反复分部积分证明。

## 五、可积性理论

### 1. 可积函数有界

若 \(f\) 在 \([a,b]\) 上 Riemann 可积，则 \(f\) 在 \([a,b]\) 上有界。

因此，无界函数不可能是通常意义下的 Riemann 可积函数。

### 2. Darboux 上和与下和

设

$$
P:\quad a=x_0<x_1<\cdots <x_n=b
$$

是 \([a,b]\) 的一个分划。对每个小区间 \([x_{i-1},x_i]\)，记

$$
M_i=\sup_{x\in[x_{i-1},x_i]}f(x),\qquad
m_i=\inf_{x\in[x_{i-1},x_i]}f(x).
$$

Darboux 上和与下和分别定义为

$$
U(f,P)=\sum_{i=1}^n M_i\Delta x_i,
\qquad
L(f,P)=\sum_{i=1}^n m_i\Delta x_i.
$$

总有

$$
L(f,P)\le U(f,P).
$$

分划加细时，上和不增，下和不减。并且任意一个下和都不超过任意一个上和。

### 3. 上积分与下积分

把所有上和的下确界称为上积分，把所有下和的上确界称为下积分：

$$
\overline{\int_a^b} f(x)\,\mathrm{d}x
=
\inf_P U(f,P),
\qquad
\underline{\int_a^b} f(x)\,\mathrm{d}x
=
\sup_P L(f,P).
$$

函数 \(f\) 在 \([a,b]\) 上 Riemann 可积，当且仅当

$$
\overline{\int_a^b} f(x)\,\mathrm{d}x
=
\underline{\int_a^b} f(x)\,\mathrm{d}x.
$$

此时二者的共同值就是定积分

$$
\int_a^b f(x)\,\mathrm{d}x.
$$

### 4. 振幅

函数 \(f\) 在区间 \(I\) 上的振幅定义为

$$
\omega(f;I)=\sup_{x\in I}f(x)-\inf_{x\in I}f(x).
$$

等价地，它也是

$$
\sup\{|f(x)-f(y)|:x,y\in I\}.
$$

函数 \(f\) 在点 \(x\) 处的振幅可定义为

$$
\omega_f(x)=\lim_{r\to 0^+}\omega\bigl(f;(x-r,x+r)\cap[a,b]\bigr).
$$

若 \(\omega_f(x)=0\)，则 \(f\) 在 \(x\) 处连续；若 \(\omega_f(x)>0\)，则 \(f\) 在 \(x\) 处间断。

### 5. 可积性的等价命题

设 \(f\) 在 \([a,b]\) 上有界。以下命题等价：

1. \(f\) 在 \([a,b]\) 上 Riemann 可积。

2. 对任意 \(\varepsilon>0\)，存在 \(\delta>0\)，使得对任意满足 \(\|P\|<\delta\) 的分划 \(P\)，都有

   $$
   \sum_{i=1}^n \omega(f;[x_{i-1},x_i])\Delta x_i<\varepsilon.
   $$

3. 对任意 \(\varepsilon>0\)，存在某个分划 \(P\)，使得

   $$
   \sum_{i=1}^n \omega(f;[x_{i-1},x_i])\Delta x_i<\varepsilon.
   $$

4. Darboux 上积分等于下积分。

这里第 2 条和第 3 条常被称为 Riemann 可积的第一、第二充要条件。

### 6. 可积性的第三充要条件

在证明可积性时，常把区间分成两类：

1. 在大部分小区间上，函数振幅可以控制得很小；
2. 在少数小区间上，函数振幅可能较大，但这些小区间的总长度可以控制得很小。

这样仍可以使

$$
\sum_{i=1}^n \omega(f;[x_{i-1},x_i])\Delta x_i
$$

任意小，从而证明函数 Riemann 可积。

这个思想常用于证明 Thomae 函数，也常称 Riemann 函数，可积。它背后已经包含了零测度集的思想，这也引出下面的 Lebesgue 判别准则。

## 六、Lebesgue 定理

这个定理属于实变函数论中的内容，在 Riemann 积分理论中通常作为重要判别准则使用。

### 1. 零测度集

设 \(A\subset\mathbb{R}\)。若对任意 \(\varepsilon>0\)，都存在至多可数个开区间 \(I_n\) 覆盖 \(A\)，并且

$$
\sum_{n=1}^{\infty}|I_n|<\varepsilon,
$$

则称 \(A\) 为零测度集，或测度为零的集合。

有限集、可数集都是零测度集，但零测度集不一定是可数集。

### 2. Lebesgue 判别准则

设 \(f\) 是 \([a,b]\) 上的有界函数。则 \(f\) 在 \([a,b]\) 上 Riemann 可积的充分必要条件是：\(f\) 的间断点集合

$$
D(f)=\{x\in[a,b]: f \text{ 在 } x \text{ 处不连续}\}
$$

是零测度集。
