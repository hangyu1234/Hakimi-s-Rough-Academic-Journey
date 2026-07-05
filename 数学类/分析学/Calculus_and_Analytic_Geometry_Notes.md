## 常用等价无穷小
当 \( x \to 0 \) 时：
* \( \sin x \sim \tan x \sim \arcsin x \sim \arctan x \sim x \)
* \( a^x - 1 \sim x \ln a \)
* \( e^x - 1 \sim x \)
* \( 1 - \cos x \sim \frac{1}{2}x^2 \)
* \( \ln(1+x) \sim x \)
* \( \log_a(1+x) \sim \frac{x}{\ln a} \)
* \( (1+x)^\alpha - 1 \sim \alpha x \)
* \( \sqrt[n]{1+x} - 1 \sim \frac{1}{n}x \)
* \( x - \sin x \sim \frac{1}{6}x^3 \)
* \( \tan x - x \sim \frac{1}{3}x^3 \)
* \( \arcsin x - x \sim \frac{1}{6}x^3 \)
* \( x - \arctan x \sim \frac{1}{3}x^3 \)
* \( \tan x - \sin x \sim \frac{1}{2}x^3 \)

### 等价无穷小代换规则
* 乘除式替代规则：若 \( \alpha \sim \alpha_1 \)，且 \( \lim \alpha_1 \cdot \varphi(x) \) 极限存在或有界，则 \( \lim \alpha \cdot \varphi(x) = \lim \alpha_1 \cdot \varphi(x) \)。
* 加减法取大规则（高阶吸收低阶）：若 \( \beta = o(\alpha) \)，则 \( \alpha \pm \beta \sim \alpha \)。
* 和差代替规则：若 \( \alpha \sim \alpha_1 \)，\( \beta \sim \beta_1 \)，且 \( \alpha_1 \) 与 \( \beta_1 \) 不等价，或满足极限 \( \lim \frac{\alpha - \beta}{\gamma} = \lim \frac{\alpha_1 - \beta_1}{\gamma} \)。
* 注：等价无穷小代换中必须满足该项趋于0才可以代换。

## 重要极限
* \( \lim_{x \to 0} \frac{\sin x}{x} = 1 \)
* \( \lim_{x \to \infty} (1 + \frac{1}{x})^x = e \) 或 \( \lim_{x \to 0} (1 + x)^{\frac{1}{x}} = e \)

## 反三角函数
* **反正弦函数** \( y = \arcsin x \)：定义域 \( [-1, 1] \)，值域 \( [-\frac{\pi}{2}, \frac{\pi}{2}] \)，单调递增奇函数。
* **反余弦函数** \( y = \arccos x \)：定义域 \( [-1, 1] \)，值域 \( [0, \pi] \)，单调递减。
* **反正切函数** \( y = \arctan x \)：定义域 \( (-\infty, +\infty) \)，值域 \( (-\frac{\pi}{2}, \frac{\pi}{2}) \)，单调递增奇函数。
* **反余切函数** \( y = \text{arccot} x \)：定义域 \( (-\infty, +\infty) \)，值域 \( (0, \pi) \)，单调递减。

## 三角函数公式
### 诱导公式
奇变偶不变，符号看象限。
* \( \sin(-\alpha) = -\sin \alpha \)
* \( \cos(-\alpha) = \cos \alpha \)
* \( \sin(\pi - \alpha) = \sin \alpha \)
* \( \cos(\pi - \alpha) = -\cos \alpha \)
* \( \sin(\frac{\pi}{2} - \alpha) = \cos \alpha \)
* \( \cos(\frac{\pi}{2} - \alpha) = \sin \alpha \)

### 同角基本关系式
* 倒数关系：\( \tan \alpha \cdot \cot \alpha = 1 \), \( \sin \alpha \cdot \csc \alpha = 1 \), \( \cos \alpha \cdot \sec \alpha = 1 \)
* 商的关系：\( \tan \alpha = \frac{\sin \alpha}{\cos \alpha} \), \( \cot \alpha = \frac{\cos \alpha}{\sin \alpha} \)
* 平方关系：\( \sin^2 \alpha + \cos^2 \alpha = 1 \), \( 1 + \tan^2 \alpha = \sec^2 \alpha \), \( 1 + \cot^2 \alpha = \csc^2 \alpha \)

### 两角和与差及倍半角公式
* \( \sin(\alpha \pm \beta) = \sin \alpha \cos \beta \pm \cos \alpha \sin \beta \)
* \( \cos(\alpha \pm \beta) = \cos \alpha \cos \beta \mp \sin \alpha \sin \beta \)
* \( \tan(\alpha \pm \beta) = \frac{\tan \alpha \pm \tan \beta}{1 \mp \tan \alpha \tan \beta} \)
* \( \sin 2\alpha = 2 \sin \alpha \cos \alpha \)
* \( \cos 2\alpha = \cos^2 \alpha - \sin^2 \alpha = 2\cos^2 \alpha - 1 = 1 - 2\sin^2 \alpha \)
* \( \tan 2\alpha = \frac{2 \tan \alpha}{1 - \tan^2 \alpha} \)
* 降幂公式：\( \sin^2 \alpha = \frac{1 - \cos 2\alpha}{2} \), \( \cos^2 \alpha = \frac{1 + \cos 2\alpha}{2} \)
* 半角公式：\( \sin(\frac{\alpha}{2}) = \pm\sqrt{\frac{1 - \cos \alpha}{2}} \), \( \cos(\frac{\alpha}{2}) = \pm\sqrt{\frac{1 + \cos \alpha}{2}} \), \( \tan(\frac{\alpha}{2}) = \frac{1 - \cos \alpha}{\sin \alpha} = \frac{\sin \alpha}{1 + \cos \alpha} \)

### 和差化积与积化和差公式
* 和差化积：
  * \( \sin \alpha + \sin \beta = 2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2} \)
  * \( \sin \alpha - \sin \beta = 2\cos\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2} \)
  * \( \cos \alpha + \cos \beta = 2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2} \)
  * \( \cos \alpha - \cos \beta = -2\sin\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2} \)
* 积化和差：
  * \( \sin \alpha \cos \beta = \frac{1}{2}[\sin(\alpha+\beta) + \sin(\alpha-\beta)] \)
  * \( \cos \alpha \sin \beta = \frac{1}{2}[\sin(\alpha+\beta) - \sin(\alpha-\beta)] \)
  * \( \cos \alpha \cos \beta = \frac{1}{2}[\cos(\alpha+\beta) + \cos(\alpha-\beta)] \)
  * \( \sin \alpha \sin \beta = -\frac{1}{2}[\cos(\alpha+\beta) - \cos(\alpha-\beta)] \)

### 万能公式与辅助角公式
* \( \sin \alpha = \frac{2\tan(\alpha/2)}{1 + \tan^2(\alpha/2)} \)
* \( \cos \alpha = \frac{1 - \tan^2(\alpha/2)}{1 + \tan^2(\alpha/2)} \)
* \( \tan \alpha = \frac{2\tan(\alpha/2)}{1 - \tan^2(\alpha/2)} \)
* \( a \sin x \pm b \cos x = \sqrt{a^2+b^2}\sin(x \pm \phi) \)，其中 \( \tan \phi = \frac{b}{a} \)

## 初等函数的导数
### 基本初等函数的导数公式
1. \( (C)' = 0 \)
2. \( (x^\mu)' = \mu x^{\mu-1} \)
3. \( (a^x)' = a^x \ln a \) ； \( (e^x)' = e^x \)
4. \( (\log_a x)' = \frac{1}{x \ln a} \) ； \( (\ln x)' = \frac{1}{x} \)
5. \( (\sin x)' = \cos x \) ； \( (\cos x)' = -\sin x \)
6. \( (\tan x)' = \sec^2 x \) ； \( (\cot x)' = -\csc^2 x \)
7. \( (\sec x)' = \sec x \tan x \) ； \( (\csc x)' = -\csc x \cot x \)
8. \( (\arcsin x)' = \frac{1}{\sqrt{1-x^2}} \) ； \( (\arccos x)' = -\frac{1}{\sqrt{1-x^2}} \)
9. \( (\arctan x)' = \frac{1}{1+x^2} \) ； \( (\text{arccot} x)' = -\frac{1}{1+x^2} \)

### 双曲函数与反双曲函数
* 双曲正弦：\( \sinh x = \frac{e^x - e^{-x}}{2} \)，导数 \( (\sinh x)' = \cosh x \)
* 双曲余弦：\( \cosh x = \frac{e^x + e^{-x}}{2} \)，导数 \( (\cosh x)' = \sinh x \)
* 双曲正切：\( \tanh x = \frac{\sinh x}{\cosh x} \)，导数 \( (\tanh x)' = \frac{1}{\cosh^2 x} \)
* 反双曲正弦：\( \text{arsinh} x = \ln(x + \sqrt{x^2+1}) \)，导数 \( (\text{arsinh} x)' = \frac{1}{\sqrt{1+x^2}} \)
* 反双曲余弦：\( \text{arcosh} x = \ln(x + \sqrt{x^2-1}) \)，导数 \( (\text{arcosh} x)' = \frac{1}{\sqrt{x^2-1}} \)

### 高阶导数公式
1. \( (x^\mu)^{(n)} = \mu(\mu-1)\cdots(\mu-n+1)x^{\mu-n} \)
2. \( (e^x)^{(n)} = e^x \) ； \( (a^x)^{(n)} = a^x \ln^n a \)
3. \( (\sin kx)^{(n)} = k^n \sin(kx + n\frac{\pi}{2}) \)
4. \( (\cos kx)^{(n)} = k^n \cos(kx + n\frac{\pi}{2}) \)
5. \( [\ln(1+x)]^{(n)} = (-1)^{n-1} \frac{(n-1)!}{(1+x)^n} \)
6. \( (\frac{1}{x})^{(n)} = (-1)^n \frac{n!}{x^{n+1}} \)

## 常见函数的麦克劳林公式 (Maclaurin Series)
* \( e^x = 1 + x + \frac{1}{2!}x^2 + \cdots + \frac{1}{n!}x^n + o(x^n) \)
* \( \sin x = x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 + \cdots + o(x^{2n+1}) \)
* \( \cos x = 1 - \frac{1}{2!}x^2 + \frac{1}{4!}x^4 + \cdots + o(x^{2n}) \)
* \( \ln(1+x) = x - \frac{1}{2}x^2 + \frac{1}{3}x^3 + \cdots + o(x^n) \)
* \( (1+x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!}x^2 + \cdots + o(x^n) \)
* \( \frac{1}{1-x} = 1 + x + x^2 + x^3 + \cdots + o(x^n) \)

## 微分学中值定理
* **Rolle定理**：\( f(x) \) 在 \( [a,b] \) 连续，在 \( (a,b) \) 可导，且 \( f(a)=f(b) \)，则在 \( (a,b) \) 内至少存在一点 \( \xi \) 使 \( f'(\xi) = 0 \)。
* **Lagrange中值定理**：\( f(x) \) 在 \( [a,b] \) 连续，在 \( (a,b) \) 可导，则在 \( (a,b) \) 内至少存在一点 \( \xi \) 使 \( f'(\xi) = \frac{f(b)-f(a)}{b-a} \)。
* **Cauchy中值定理**：\( f(x), g(x) \) 在 \( [a,b] \) 连续，在 \( (a,b) \) 可导，且 \( g'(x) \neq 0 \)，则存在一点 \( \xi \) 使 \( \frac{f(b)-f(a)}{g(b)-g(a)} = \frac{f'(\xi)}{g'(\xi)} \)。

## 导数的应用
### 单调性与极值
* 单调性判定：若 \( f'(x) > 0 \)，函数单调递增；若 \( f'(x) < 0 \)，函数单调递减。
* 驻点判定：\( f'(x_0) = 0 \) 的点。
* 极值判定：若 \( f'(x_0) = 0 \) 且 \( f''(x_0) > 0 \)，则为极小值；若 \( f''(x_0) < 0 \)，则为极大值。

### 凹凸性与拐点
* 凹凸性判定：若 \( f''(x) > 0 \)，曲线为凹（下凸）；若 \( f''(x) < 0 \)，曲线为凸（上凸）。
* 拐点：曲线凹凸性改变的点，通常满足 \( f''(x_0) = 0 \) 且左右两侧二阶导数异号。

### 渐近线
* 水平渐近线：\( y = a \)，若 \( \lim_{x \to \infty} f(x) = a \)。
* 铅直渐近线：\( x = x_0 \)，若 \( \lim_{x \to x_0} f(x) = \infty \)。
* 斜渐近线：\( y = ax + b \)，其中 \( a = \lim_{x \to \infty} \frac{f(x)}{x} \)，\( b = \lim_{x \to \infty} (f(x) - ax) \)。

## 弧微分与曲率
* **弧微分**：
  * 直角坐标：\( ds = \sqrt{1 + y'^2} dx \)
  * 参数方程：\( ds = \sqrt{\varphi'(t)^2 + \psi'(t)^2} dt \)
  * 极坐标：\( ds = \sqrt{\rho(\theta)^2 + \rho'(\theta)^2} d\theta \)
* **曲率与曲率半径**：
  * 曲率 \( K = \frac{|y''|}{(1 + y'^2)^{\frac{3}{2}}} \)
  * 参数方程形式 \( K = \frac{|x'(t)y''(t) - y'(t)x''(t)|}{(x'^2(t) + y'^2(t))^{\frac{3}{2}}} \)
  * 曲率半径 \( R = \frac{1}{K} \)

## 基本积分表
1. \( \int x^\mu dx = \frac{x^{\mu+1}}{\mu+1} + C \quad (\mu \neq -1) \)
2. \( \int \frac{1}{x} dx = \ln|x| + C \)
3. \( \int a^x dx = \frac{a^x}{\ln a} + C \) ； \( \int e^x dx = e^x + C \)
4. \( \int \sin x dx = -\cos x + C \) ； \( \int \cos x dx = \sin x + C \)
5. \( \int \sec^2 x dx = \tan x + C \) ； \( \int \csc^2 x dx = -\cot x + C \)
6. \( \int \sec x \tan x dx = \sec x + C \) ； \( \int \csc x \cot x dx = -\csc x + C \)
7. \( \int \frac{1}{1+x^2} dx = \arctan x + C \) ； \( \int \frac{1}{\sqrt{1-x^2}} dx = \arcsin x + C \)
8. \( \int \frac{1}{a^2+x^2} dx = \frac{1}{a} \arctan\frac{x}{a} + C \) ； \( \int \frac{1}{\sqrt{a^2-x^2}} dx = \arcsin\frac{x}{a} + C \)
9. \( \int \frac{1}{x^2-a^2} dx = \frac{1}{2a} \ln|\frac{x-a}{x+a}| + C \)
10. \( \int \frac{1}{\sqrt{x^2+a^2}} dx = \ln(x + \sqrt{x^2+a^2}) + C \)
11. \( \int \frac{1}{\sqrt{x^2-a^2}} dx = \ln|x + \sqrt{x^2-a^2}| + C \)
12. \( \int \tan x dx = -\ln|\cos x| + C \) ； \( \int \cot x dx = \ln|\sin x| + C \)
13. \( \int \sec x dx = \ln|\sec x + \tan x| + C \) ； \( \int \csc x dx = \ln|\csc x - \cot x| + C \)

## 定积分的性质与应用
### 定积分性质
* 估值定理：若 \( m \le f(x) \le M \)，则 \( m(b-a) \le \int_a^b f(x) dx \le M(b-a) \)。
* 积分中值定理：\( \int_a^b f(x) dx = f(\xi)(b-a) \)。
* 原函数存在定理：\( \Phi(x) = \int_a^x f(t) dt \Rightarrow \Phi'(x) = f(x) \)。

### 华里士公式 (Wallis Formula)
\[ I_n = \int_0^{\frac{\pi}{2}} \sin^n x dx = \int_0^{\frac{\pi}{2}} \cos^n x dx \]
* 若 \( n \) 为正偶数：\( I_n = \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{1}{2} \cdot \frac{\pi}{2} \)
* 若 \( n \) 为大于1的奇数：\( I_n = \frac{n-1}{n} \cdot \frac{n-3}{n-2} \cdots \frac{2}{3} \cdot 1 \)

### 反常积分收敛性
* \( \int_1^{+\infty} \frac{1}{x^p} dx \) ：当 \( p > 1 \) 时收敛，\( p \le 1 \) 时发散。
* \( \int_0^1 \frac{1}{x^q} dx \) ：当 \( 0 < q < 1 \) 时收敛，\( q \ge 1 \) 时发散。

### 几何应用
* 平面图形面积：直角坐标 \( S = \int_a^b |f(x) - g(x)| dx \)；极坐标 \( S = \frac{1}{2} \int_\alpha^\beta |r_1^2(\theta) - r_2^2(\theta)| d\theta \)。
* 旋转体体积：绕x轴旋转 \( V = \pi \int_a^b |f(x)|^2 dx \)；绕y轴旋转（柱壳法）\( V = 2\pi \int_a^b x |f(x)| dx \)。

## 空间解析几何
### 向量代数
* **距离公式**：\( d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2} \)
* **数量积 (点乘)**：\( \vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos \theta = a_x b_x + a_y b_y + a_z b_z \)。判定垂直：\( \vec{a} \cdot \vec{b} = 0 \)。
* **向量积 (叉乘)**：模长 \( |\vec{a} \times \vec{b}| = |\vec{a}| |\vec{b}| \sin \theta \)。判定平行：\( \vec{a} \times \vec{b} = \vec{0} \)。
  \[ \vec{a} \times \vec{b} = \begin{vmatrix} i & j & k \\ a_x & a_y & a_z \\ b_x & b_y & b_z \end{vmatrix} \]
* **混合积**：\( [\vec{a}\vec{b}\vec{c}] = (\vec{a} \times \vec{b}) \cdot \vec{c} \)。判定共面：混合积为0。

### 平面及其方程
* 点法式方程：\( A(x-x_0) + B(y-y_0) + C(z-z_0) = 0 \)，法向量 \( \vec{n} = (A,B,C) \)。
* 一般方程：\( Ax + By + Cz + D = 0 \)。
* 截距式方程：\( \frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1 \)。
* 点到平面的距离：\( d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2+B^2+C^2}} \)。

### 空间直线及其方程
* 对称式方程：\( \frac{x-x_0}{m} = \frac{y-y_0}{n} = \frac{z-z_0}{p} \)，方向向量 \( \vec{s} = (m,n,p) \)。
* 参数方程：\( x = x_0 + mt, \quad y = y_0 + nt, \quad z = z_0 + pt \)。
* 一般方程：\( \begin{cases} A_1x + B_1y + C_1z + D_1 = 0 \\ A_2x + B_2y + C_2z + D_2 = 0 \end{cases} \)。
* 异面直线距离：\( d = \frac{|(\vec{s_1} \times \vec{s_2}) \cdot \vec{M_1M_2}|}{|\vec{s_1} \times \vec{s_2}|} \)。

### 二次曲面
* **球面**：\( (x-x_0)^2 + (y-y_0)^2 + (z-z_0)^2 = R^2 \)
* **椭球面**：\( \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1 \)
* **二次锥面**：\( \frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 0 \)
* **单叶双曲面**：\( \frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1 \)
* **双叶双曲面**：\( \frac{x^2}{a^2} - \frac{y^2}{b^2} + \frac{z^2}{c^2} = -1 \)
* **椭圆抛物面**：\( \frac{x^2}{2p} + \frac{y^2}{2q} = z \)
* **双曲抛物面**：\( \frac{x^2}{2p} - \frac{y^2}{2q} = z \)
* **柱面**：例如圆柱面 \( x^2+y^2=R^2 \)。
