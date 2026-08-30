# PyTorch官方教程
___
## 目录<a id = "目录"></a>
- [Quickstart](#零)
- [Tensors](#一)
- [Datasets & DataLoaders](#二)
- [Transforms](#三)
- [Build the Neural Network](#四)
- [Automatic Differentiation with torch.autograd](#五)
- [Optimizing Model Parameters](#六)
- [Save and Load the Model](#七)
- [附录：Pytorch函数](#附录)
___
## 〇、Quickstart<a id = "零"></a>
未完待续
___
- [返回目录](#目录)
___
## 一、Tensors<a id = "一"></a>
张量是一种与数组和矩阵非常相似的专用数据结构，类似于NumPy的ndarray，不同之处在于张量可以在GPU或其他硬件加速器上运行，实际上张量和NumPy数组通常可以共享相同的底层内存，从而消除复制数据的需求
```python
import torch
import numpy as np
```
### 1. 张量初始化
- 直接数据：张量可以直接从数据中生成，数据类型会自动推断
- 来自NumPy数组：张量可以由Numpy数组创建（反之亦然）
- 另一个张量：新张量保留参数张量的性质（形状、数据类型），除非被显式覆盖
```python
>> data = [[1, 2], [3, 4]]
>> x_data = torch.tensor(data)

>> np_array = np.array(data)
>> x_np = torch.from_numpy(np_array)

>> x_ones = torch.ones_like(x_data)
tensor([[1, 1], [1, 1]])
>> x_rand = torch.rand_like(x_data, dtype=torch.float)
tensor([[0.9863, 0.4648], [0.3694, 0.5583]])
```
随机或恒定值：`shape`是张量维数的元组，在下面的函数中，它决定了输出张量的维数
```python
>>shape = (2, 3)

>>rand_tensor = torch.rand(shape)
tensor([[0.4747, 0.0370, 0.6094], [0.8139, 0.8121, 0.4904]])
>>ones_tensor = torch.ones(shape)
tensor([[1., 1., 1.], [1., 1., 1.]])
>>zeros_tensor = torch.zeros(shape)
tensor([[0., 0., 0.], [0., 0., 0.]])
```
### 2. 张量运算
张量运算包括：算术、线性代数、矩阵操作（置换， 索引、切片）、抽样等功能，这些操作都可以在CPU和加速器上运行，默认情况下张量是在CPU上创建的，需要在检查加速器的可用性后，显式地用方法将张量移动到加速器（复制大张量跨设备使用在时间和内存方面可能非常昂贵）
```python
if torch.accelerator.is_available():
    tensor = tensor.to(torch.accelerator.current_accelerator())
```
标准的类数字索引和切片
```python
>> tensor = torch.ones(4, 4)

# 取第一行
>> tensor[0]
tensor([1., 1., 1., 1.])
# 取第一列
>> tensor[:, 0]
tensor[1., 1., 1., 1.]
# 取最后一列
# tensor[..., -1]含义是前面的维度全部保留，最后一个维度取最后一个元素，...会自动展开成适当数量的:
>> tensor[..., -1]
tensor[1., 1., 1., 1.]

>> tensor[:, 1] = 0
>> tensor
tensor([[1., 0., 1., 1.], [1., 0., 1., 1.], [1., 0., 1., 1.], [1., 0., 1., 1.]])
```
连接张量cat：你可以用它在给定维度上串接一列张量
```python
>> tensor = torch.ones(4, 4)
>> tensor[:, 1] = 0
>> t1 = torch.cat([tensor, tensor, tensor], dim=1)
>> t1
tensor([[1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.], [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.], [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.], [1., 0., 1., 1., 1., 0., 1., 1., 1., 0., 1., 1.]])
```
算术运算
```python
# 矩阵乘法
# y1, y2, y3, y4 结果全部一样
>> y1 = tensor @ tensor.T
>> y2 = tensor.matmul(tensor.T)
>> y3 = torch.matmul(tensor, tensor.T)
>> y4 = torch.rand_like(y1)
# out表示矩阵相乘的结果写入并覆盖掉y4
>> torch.matmul(tensor, tensor.T, out=y4)

# 逐元素乘法
z1 = tensor * tensor
z2 = tensor.mul(tensor)
z3 = torch.rand_like(tensor)
torch.mul(tensor, tensor, out=z3)
```
单元张量：如果你有一个单元素张量，比如通过聚合所有将张量的值转换为一个值，你可以用item()将其转换为Python数值使用
```
>> agg = tensor.sum()
>> agg_item = agg.item

>> agg
tensor(12.0)
>> agg_item
12.0
```
原地操作：将结果存储到操作数中的操作为原地操作，它们用后缀`_`表示
```python
>> tensor.add(5)
>> tensor
tensor([[1., 0., 1., 1.], [1., 0., 1., 1.], [1., 0., 1., 1.], [1., 0., 1., 1.]])
>> tensor.add_(5)
>> tensor
tensor([[6., 5., 6., 6.], [6., 5., 6., 6.], [6., 5., 6., 6.], [6., 5., 6., 6.]])
```
### 3. 与NumPy的桥接
CPU和NumPy阵列上的张量可以共享它们底层内存的地址，改变一个地址会改变另一个

张量到NumPy数组：张量的变化会反映在NumPy数组中
```python
>> t = torch.ones(5)
>> n = t.numpy()

>> t.add(1)
>> n
array([2., 2., 2., 2., 2.])
```
NumPy数组到张量：NumPy阵列的变化会反映在张量上
```python
>> n = np.ones(5)
>> t = torch.from_numpy(n)

>> np.add(n, 1, out=n)
>> t
tensor([2., 2., 2., 2., 2.])
```
___
- [返回目录](#目录)
___
## 二、Datasets & DataLoaders<a id = "二"></a>
用于处理数据样本的代码很容易变得杂乱且难以维护，理想情况下我们希望将数据集处理代码与模型训练代码解耦，从而提高代码的可读性和模块化程度

pytorch提供了两个用于处理数据的基本组件，它们既可以用于pytorch已经准备好的数据集，也可以用于我们自己构建的数据集：
- torch.utils.data.Dataset：用于存储样本及其对应的标签
- torch.utils.data.DataLoader：在Dataset外部封装了一层可迭代对象，使我们能够方便地访问这些样本
### 1. 加载数据集
下面是一个使用 TorchVision 加载 Fashion-MNIST 数据集的例子。
- root：训练数据和测试数据保存的位置；
- train：指定加载训练集还是测试集；
- download=True：如果 root 路径下没有对应数据，就从互联网下载；
- transform 和 target_transform：分别指定对特征和标签所进行的变换。

```python
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import v2
import matplotlib.pyplot as plt


training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])
)
```
### 2. 数据集的迭代与可视化
我们可以像操作 Python 列表一样，通过索引手动访问 Dataset：
```python
training_data[index]
```
### 3. 为自己的文件创建自定义Dataset
一个自定义的Dataset类必须实现三个函数
```python
__init__
__len__
__getitem__
```
示例
```python
import os
import pandas as pd
from torchvision.io import decode_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = decode_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```
- `__init__`：函数在实例化Dataset对象时运行一次，在这里会初始化：
    - 保存图片的目录
    - 保存标注信息的文件
    - 对图片进行的transform
    - 对标签进行的target transform
- `__len__`：函数返回数据集中的样本数量
- `__getitem__`：函数负责根据给定的索引idx，加载并返回数据集中的一个样本，根据索引，它会完成下面几个步骤
    1. 找到对应图片在磁盘上的位置
    2. 使用decode_image将图片转换为Tensor
    3. 从self.img_labels中取出对应标签
    4. 如果定义了transform，就对图片执行transform
    5. 如果定义了target transform，就对标签执行transform
    6. 最后返回图片tensor和对应标签组成的元组
### 4. 准备你的数据以进行DataLoaders训练
Dataset每次负责取出一个样本的特征和标签，但在训练模型时，我们通常不会一次只训练一个样本
- 一次把一小批样本传给模型，即minibatch
- 在每一个epoch时重新打乱数据，以减少模型过拟合
- 使用python的multiprocessoring多进程机制，加速数据读取

DataLoader将这些复杂操作封装起来，为我们提供了一个非常容易使用的API
```python
from torch.utils.data import DataLoader

train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
```
### 5. 遍历DataLoader
现在我们已经把Dataset放进了DataLoader，因此可以按照需要遍历数据，每次迭代都会返回一批train_feature和train_labels
```python
# Display image and label.
train_features, train_labels = next(iter(train_dataloader))
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels batch shape: {train_labels.size()}")
img = train_features[0].squeeze()
label = train_labels[0]
plt.imshow(img, cmap="gray")
plt.show()
print(f"Label: {label}")
```
___
- [返回目录](#目录)
___
## 四、Build the Neural Network<a id = "六"></a>
神经网络由一系列层/模块组成，这些层或模块负责对数据执行各种操作

torch.nn命名空间提供了构建神经网络所需要的所有基础组件，pytorch中的每一个模块都继承自nn.Module

一个神经网络本身也是一个模块，而这个模块又由其他模块组成，这种嵌套结构使我们能够方便的构建和管理负责的网络结构

在接下来的内容中，我们将构建一个用于对FashionMNIST数据集中的图像进行分类的神经网络
```python
import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
```
### 1. 获取训练设备
如果当前存在可用的加速器，我们就使用它；否则使用 CPU。
```python
device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
print(f"Using {device} device")
```
### 2. 定义神经网络类
我们通过继承 nn.Module 来定义自己的神经网络，并在 `__init__` 方法中初始化神经网络所包含的各个层。

每一个 nn.Module 的子类都需要在 forward 方法中定义：输入数据应该经过哪些运算。
```python
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()

        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
```
接下来，我们创建一个 NeuralNetwork 实例，将其移动到指定的 device 上，并打印网络结构。
```python
model = NeuralNetwork().to(device)
print(model)
```
要使用这个模型，只需要把输入数据传给模型：
```python
model(X)
```
这样会自动执行模型中的 forward() 方法，同时还会执行 PyTorch 内部的一些后台操作。

调用模型后，我们会得到一个二维 Tensor。对于一批输入数据，每个样本都会对应 10 个原始预测值（raw predicted values），分别对应 10 个类别。这些原始值称为：logits 接下来，我们通过 nn.Softmax 将 logits 转换成各个类别对应的预测概率。
```python
X = torch.rand(1, 28, 28, device=device)

logits = model(X)

pred_probab = nn.Softmax(dim=1)(logits)

y_pred = pred_probab.argmax(1)

print(f"Predicted class: {y_pred}")
```
### 3. 模型的各个层
现在我们把 FashionMNIST 网络中的各个层拆开来看。

为了说明每一层的作用，我们生成一个包含 3 张 28×28 图像的 mini-batch，然后观察这些数据在网络中的变化。
#### nn.Flatten
我们初始化一个 nn.Flatten 层，将每一张二维的 28×28 图像转换成一个包含：28×28=784个像素值的一维数组
```python
flatten = nn.Flatten()

flat_image = flatten(input_image)

print(flat_image.size())
```
> 注意：mini-batch 这一维，即`dim=0`，会被保留下来
#### nn.Linear
线性层是一个模块，它会利用内部保存的权重和偏置对输入执行线性变换
```python
layer1 = nn.Linear(
    in_features=28*28,
    out_features=20
)

hidden1 = layer1(flat_image)

print(hidden1.size())
```
#### nn.ReLU
非线性激活函数（non-linear activations）使神经网络能够学习输入和输出之间复杂的映射关系。

它们通常被放在线性变换之后，以引入非线性（nonlinearity）从而帮助神经网络学习各种复杂现象。

在这里，我们在线性层之间使用：`nn.ReLU()`当然，除了 ReLU 之外，还有许多其他激活函数可以用于向模型中引入非线性。
#### nn.Sequential
nn.Sequential 是一个按照顺序组织模块的容器（ordered container）。

数据会按照定义模块时的顺序，依次通过里面的所有模块。

因此我们可以使用 Sequential 很方便地快速搭建一个网络：
```python
seq_modules = nn.Sequential(
    flatten,
    layer1,
    nn.ReLU(),
    nn.Linear(20, 10)
)

input_image = torch.rand(3,28,28)

logits = seq_modules(input_image)
```
#### nn.Softmax
神经网络最后一个线性层输出的是：logits，也就是范围可以在：(−∞,+∞)之间的原始数值。

这些 logits 会被输入到 nn.Softmax 中。Softmax 会将这些 logits 转换成：[0,1]

范围内的数值，这些数值可以表示模型对于每一个类别的：预测概率
```python
softmax = nn.Softmax(dim=1)
pred_probab = softmax(logits)
```
dim 参数指定：Softmax 应该沿着哪一个维度进行计算，使该维度上的所有数值之和等于 1。
### 4. 模型参数
神经网络中的许多层都是参数化的（parameterized）。

也就是说，这些层拥有与之关联的：
- 权重 weight
- 偏置 bias

这些参数会在训练过程中被不断优化。

继承 nn.Module 后，PyTorch 会自动追踪定义在模型对象中的所有模块和参数。

我们可以通过：`model.parameters()`或者：`model.named_parameters()`访问模型的所有参数。
___
- [返回目录](#目录)
___
## 五、Automatic Differentiation with torch.autograd<a id = "五"></a>
在训练神经网络时，最常用的算法是反向传播，在这个算法中，模型参数（也就是模型权重）会根据损失函数相对于这些参数的梯度进行调整

为了计算这些梯度，pytorch内置了一个自动微分引擎：torch.autograd，它支持对任意计算图中的梯度进行自动计算

考虑一个最简单的单层神经网络，其中输入为x，参数为w和b，还有一个损失函数

在pytorch中可以这样定义：
```python
import torch

x = torch.ones(5)  # 输入张量
y = torch.zeros(3)  # 期望输出
w = torch.randn(5, 3, requires_grad=True)
b = torch.randn(3, requires_grad=True)

z = torch.matmul(x, w) + b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y)
```
### 1. 张量、函数与计算图
为了让 PyTorch 记录与这些 Tensor 有关的计算过程，我们在创建 Tensor 时设置：requires_grad=True，一遍之后能够自动计算梯度

> 注意：你既可以在创建 Tensor 时设置：requires_grad=True，也可以之后调用：x.requires_grad_(True)来修改这个属性。

我们对Tensor所执行的、用于构建计算图的函数，实际上对应着Function类的对象，这个对象知道两件事
1. 如何在前向传播过程中计算函数结果
2. 如何在反向传播过程中计算它的导数

与反向传播有关的函数引用会存储在tensor的`grad_fn`属性中
### 2. 计算梯度
为了优化神经网络中的参数，我们需要计算损失函数对参数的偏导数

要计算这些倒数，只需要调用`loss.backword()`，随后就可以分别从`w.grad`和`b.grad`中获得梯度

注：
1. 默认情况下，只有计算图中的叶子节点能够直接通过`.grad`获取梯度，而且这些叶子节点必须满足`requires_grad=True`对于计算图中的其他中间节点，则，默认情况下不会保存它们的梯度
2. 默认情况下，同一个计算图中只能进行一次backward，如果确实要在同一个计算图上执行多次反向传播，就需要`loss.backward(retain_graph=True)`，表示反向传播后不要释放计算图
### 3. 禁用梯度追踪
默认情况下，所有`requires_grad=True`的tensor都会记录它们的计算历史，从而支持梯度计算，但是有些情况下我们并不需要计算 梯度，因此可以使用`torch.no_grad()`关闭梯度追踪

另一种实现类似效果的方法是调用`detach()`：意为从当前计算图中把这个Tensor分离出来，得到新的Tensor，与原tensor共享数据，但不会继续参与原来梯度的计算

关闭梯度追踪的原因：
1. 冻结神经网络中的某些参数
2. 加快前向计算
### 4. 更多关于计算图的内容
从概念上将，autograd会记录：
- Tensor数据
- 所执行的所有运算
- 每次运算得到的新Tensor

这些内容共同构成一个DAG，图中的节点主要对应Function对象
- 叶子：输入Tensor
- 根：输出Tensor

前向传播时autograd完成两件事
1. 执行实际运算
2. 记录梯度函数

反向传播时autograd做了什么
1. 根据每个节点的`.grad_fn`计算局部梯度
2. 将梯度累积到相应Tensor的`.grad`属性中
3. 利用链式法则不断向前传播
4. 最终一直传播到计算图的叶子Tensor


注：pytorch中的DAG是动态计算图，在每一次前向计算时动态生成
### 5. 可选阅读 ：Tensor梯度和Jacobian乘积
在许多情况下，我们有一个标量损失函数，需要计算相对于某些参数的梯度。然而，确实存在一些案例 当输出函数是任意张量时。在这里，PyTorch 允许你计算所谓的雅可比积，而不是实际的渐变。
## 六、Optimizing Model Parameters<a id = "六"></a>
现在我们已经有了模型和数据，接下来就是通过在数据上优化模型参数来训练、验证和测试模型。

训练模型是一个迭代过程。在每一次迭代中，模型会：
1. 对输出进行一次预测；
2. 计算预测中的误差，也就是 loss（损失）；
3. 计算损失相对于模型参数的导数；
4. 使用梯度下降来优化这些参数。

### 1. 前置代码
```python
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import v2

training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=v2.Compose([
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True)
    ])
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=v2.Compose([
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True)
    ])
)

train_dataloader = DataLoader(
    training_data,
    batch_size=64
)

test_dataloader = DataLoader(
    test_data,
    batch_size=64
)


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()

        self.flatten = nn.Flatten()

        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits


model = NeuralNetwork()
```
### 2. 超参数
超参数（Hyperparameters）是一些可以人工调整的参数，用于控制模型的优化过程。

不同的超参数取值会影响：
- 模型训练过程；
- 模型收敛速度。

这里定义三个训练过程中使用的超参数：
- Epoch数量：表示完整遍历整个数据集的次数
- Batch Size：表示在更新一次模型参数之前，有多少个数据样本会被送入神经网络
- Learning Rate：表示每个batch/epoch中模型参数更新的幅度
### 3. 优化循环
设置好参数后，就可以通过一个优化循环来训练和优化模型，优化循环中的每一次完整迭代称为一个epoch，每个epoch主要由两部分组成
1. Train Loop 训练循环：遍历训练数据集，并尝试让模型参数逐渐收敛到最优值
2. Validation/Test Loop 验证/测试循环：遍历测试数据集，检查模型性能是否在不断改善
#### 损失函数
对于一组训练数据，没有经过训练的神经网络通常不会给出正确答案

Loss Function 损失函数：用于衡量模型预测结果与真实目标值之间的差异程度，在训练过程中，我们的目标就是最小化损失函数

为了计算loss，我们首先使用输入数据生成预测结果，然后将预测结果和真实标签进行比较

常见的损失函数包括
- `nn.MSELoss`均方误差，通常用于回归任务
- `nn.NLLLoss`负对数似然损失，通常用于分类任务
- `nn.CrossEntropyLoss`交叉熵损失
#### 优化器
- 优化：在每一个训练步骤中调整模型参数，从而减少模型误差的过程
- 优化算法：定义具体如何调整该参数

pytorch将所有优化相关逻辑封装在optimizer对象中

在初始化optimizer时，需要向它提供
1. 需要训练的模型参数
2. learning rate
```python
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)
```
在训练循环内部，模型优化主要包含三个步骤
1. optimizer.zero_grad()：用于将模型参数的梯度清零，因为pytorch默认会累加梯度，如果不清零，那么新计算出的梯度会和上一次的梯度加在一起，为了防止梯度被重复计算，所以每一次迭代中都要显式清零
2. loss.backward()：用于对预测损失进行反向传播
3. optimizer.step()：使用反向传播中得到的梯度更新模型参数
### 4. 完整实现
训练循环
```python
def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)

    # 将模型设置为训练模式
    # 对 Batch Normalization 和 Dropout 层非常重要
    # 当前模型其实不需要，但作为最佳实践保留
    model.train()

    for batch, (X, y) in enumerate(dataloader):

        # 计算预测结果和损失
        pred = model(X)
        loss = loss_fn(pred, y)

        # 反向传播
        loss.backward()

        # 更新参数
        optimizer.step()

        # 清空梯度
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = (
                loss.item(),
                batch * batch_size + len(X)
            )

            print(
                f"loss: {loss:>7f}  "
                f"[{current:>5d}/{size:>5d}]"
            )
```
测试循环
```python
def test_loop(dataloader, model, loss_fn):

    # 将模型设置为评估模式
    # 对 Batch Normalization 和 Dropout 非常重要
    model.eval()

    size = len(dataloader.dataset)
    num_batches = len(dataloader)

    test_loss, correct = 0, 0

    # 测试过程中不计算梯度
    with torch.no_grad():

        for X, y in dataloader:

            pred = model(X)

            test_loss += loss_fn(pred, y).item()

            correct += (
                (pred.argmax(1) == y)
                .type(torch.float)
                .sum()
                .item()
            )

    test_loss /= num_batches
    correct /= size

    print(
        f"Test Error: \n"
        f" Accuracy: {(100*correct):>0.1f}%, "
        f"Avg loss: {test_loss:>8f} \n"
    )
```
开始训练
```python
loss_fn = nn.CrossEntropyLoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=learning_rate
)

epochs = 10

for t in range(epochs):

    print(
        f"Epoch {t+1}\n"
        "-------------------------------"
    )

    train_loop(
        train_dataloader,
        model,
        loss_fn,
        optimizer
    )

    test_loop(
        test_dataloader,
        model,
        loss_fn
    )

print("Done!")
```
___
- [返回目录](#目录)
___
## 七、Save and Load the Model<a id = "七"></a>
如何通过保存（saving）、加载（loading）以及运行模型预测，来持久化模型状态
```python
import torch
import torchvision.models as models
```
### 1. 保存和加载模型权重
pytorch模型会把学习到的参数保存在一个内部的状态字典`state_dict`

我们可以通过`torch.save`方法把这些参数保存下来
```python
model = models.vgg16(weights='IMAGENET1K_V1')
torch.save(model.state_dict(), 'model_weights.pth')
```
要加载模型权重，首先需要创建一个相同模型结构的实例，然后使用`load_state__dict()`加载保存好的参数
```python
model = models.vgg16()  # 不指定 weights，即创建未训练模型

model.load_state_dict(
    torch.load(
        'model_weights.pth',
        weights_only=True
    )
)

model.eval()
```
这里设置`weights_only=True`是为了在反序列化过程中，只允许执行加载模型权重所必需的功能
> 在进行推理之前，一定要调用`model.eval()`，这会把Dropout和Batch Normalization等层设置为评估模式，如果忘记调用，可能会导致模型在推理时产生不一致的结果
### 2. 保存和加载包含模型结构的模型
有时候我们可能希望把模型结构和模型参数一起保存，这个时候可以直接把`model`传给参数，而不是`model.state_dict`

之后可以通过下面的方式重新加载：
```python
model = torch.load(
    'model.pth',
    weights_only=False
)
```
> 在保存和加载 torch.nn.Module 时：保存 state_dict 仍然被认为是最佳实践。

> 这种保存整个模型的方法在序列化模型时会使用Python的pickle模块，因此它有一个重要限制：在加载模型时，实际的模型类定义必须仍然能够被找到 
___
- [返回目录](#目录)
___
## 附录：PyTorch函数<a id = "附录"></a>
Tensor：
- `torch.tensor()`：根据已有数据创建张量
- `torch.zeros()`：创建一个全部元素都是0的张量
- `torch.ones()`：创建一个全部元素都是1的张量
- `torch.arange()`：按照一定步长创建一个一维序列，类似Python的`range()`和NumPy的`np.arange()`
- `torch.randn()`：创建一个包含随机数的张量 ，这些随机数来自标准正态分布
- `tensor.shape()`：查看张量的形状
- `tensor.dtype()`：查看张量中元素的数据类型
- `tensor.device()`：查看张量存放在哪个计算设备上
- `reshape()`：在元素总数不变的情况下，改变张量的形状（当原张量连续时，它与原张量共享内存，当原张量非连续时，他会复制数据，此时新张量拥有独立的内存与原数据无关）
- `view()`：在元素总数不变的情况下，改变张量的形状（一定与原张量共享内存，是原始数据的一个新“视图”，修改视图中的数据，原张量的数据也会随之改变）
- `flatten()`：把多个维度“压平”，默认将所有维度压成一维，也可以通过`start_dim`和`end_dim`只压平指定范围，元素顺序不会改变
- `squeeze()`：删除长度为1的维度
- `unsqueeze()`：在指定位置插入一个长度为1的维度
- `transpose()`：交换两个维度
- `permute()`：按照指定顺序重新排列所有维度
- `contiguous()`：会返回具有连续内存布局，但数据内容相同的张量，如果原张量已经连续，则可以直接返回原张量
- `cat()`：沿着一个已经存在的维度拼接张量
- `stack()`：创建一个新的维度，再沿新维度排列张量

Dataset & DataLoader
- `Dataset`：数据集的抽象接口
    - `__len__()`：返回Dataset里面的样本数
    - `__getitem()`：返回第i条数据
- `DataLoader(dataset, batch_size, shuffle=True, drop_last=False)`：从dataset中取出数据，其中每个batch包含batch_size个样本，每个epoch开始时重新打乱数据顺序，最后一个batch不满batch_size时，不能把它扔掉

nn.Module
- `nn.Module`：是所有pytorch神经网络模块的基类
- `nn.Parameter`：表示这个tensor是模型需要学习的参数
- `forward()`：输入数据进入模型之后，具体如何计算输出
- `parameters()`：获取模型中所有注册的可训练参数
- `state_dict()`：模型当前状态的字典
- `train()`：把模型切换到训练模式
- `eval()`：把模型切换到评估/推理模式

Autograd
- `torch.tensor(requires_grad=True)`：我要对这个Tensor求梯度，请追踪和它有关的计算
- `loss.backward()`：从loss开始，沿计算图反向传播，计算所有需要的梯度
- `.grad`：存放已经算出来的梯度
- `detach()`：产生一个与当前Tensor共享数据、但与当前计算图断开的Tensor
- `zero_grad()`：重置被优化参数的梯度