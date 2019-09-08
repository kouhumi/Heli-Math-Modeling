# 数学建模竞赛班 第一讲

## 知识点

``` flow
a=>operation: 线性回归的局限性
b=>operation: 逻辑回归的作用
c=>operation: 逻辑回归的实现
d=>operation: 逻辑回归的应用
a->b->c->d
```

## 课程内容回顾

### 逻辑回归的形式

$$
f_θ(X_i) = sigmoid(θ^TX_i) \\
sigmoid(a)=\frac{1}{1+e^{-a}}
$$

### 逻辑回归函数的意义

$$
假设f_θ(X_i)的值是1时为状态A，\\
则f_θ(X_i) = P(Y_i = A),即代表了Yi是事件A的概率。
$$

## 作业

1. 如果你没有理解Logistic Regression，请阅读以下链接补充学习：

   https://christophm.github.io/interpretable-ml-book/logistic.html

2. 如果你还不会调用Logistic Regression的程序解决问题，或者在Python环境安装上有问题，请联系我。

   邮箱: kouhumi@126.com

3. 请制作一个Excel表格（或者类似的玩意儿），B1格填Linear Regression，C1格填Logistic Regression，请在每一列下方列举至少五个**你能想到的或搜集到的应用场景**，必须严肃对待这一作业。

   **提示：如果你想不出，去网上搜索一下，或者在现实生活中找一找相应的情景。**

   例如：

   |      | Linear Regression    | Logistic Regression                       |
   | ---- | -------------------- | ----------------------------------------- |
   | 1    | 通过房产面积预测房价 | 通过学生作弊/非作弊的成绩判断学生是否作弊 |
   | 2    | 通过客流量预测进货量 | 通过病人的症状判断他是否感冒              |

   

 

 

​                                                      