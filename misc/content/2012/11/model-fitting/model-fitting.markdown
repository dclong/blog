Status: published
Author: Ben Chuanlong Du
Date: 2012-11-22 12:21:02
Title: Model Fitting in ANOVA Analysis
Slug: model-fitting
Category: AI
Tags: model, R, SAS, formula, statistics
Modified: 2020-05-22 12:21:02

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**
 

## Contrast

1. Usually it does not matter what contrast(s) you use for factors in
    linear model problems[^20], so you can choose appropriate
    contrast(s) so that your problem is most simplified. In R, you can
    use `contr.helmert`, `contr.helmert`, `contr.poly`, `contr.sum`,
    `contr.treatment` and `contr.SAS` to create different kinds of
    contrasts. Among all these functions, the last three are popular. By
    default, R set the first level (whichever has the smallest order
    among all the levels in R) of a factor to be 0. If you want to set
    another level to be 0, you can use `contr.treatment` together with
    `contrasts`. For example, suppose you have a factor `brand` in R:

        > brand
        [1] Dell   Dell   Lenovo Lenovo Mac    Mac
        Levels: Dell Lenovo Mac

        > contrasts(brand)
               Lenovo Mac
        Dell        0   0
        Lenovo      1   0
        Mac         0   1
                

    You are interested in comparing `Dell` and `Lenovo` to `Mac`, i.e.
    Mac is the control treatment (level) here. It's more convenient to
    do tests if you set `Mac` as the control treatment. To do so, you
    can use the following command:

        > contrasts(brand) = contr.treatment(3,3)
                
    Now you can check the contrast again to see how R will constructs
    design matrix based factor `brand`:

        > contrasts(brand)
               1 2
        Dell   1 0
        Lenovo 0 1
        Mac    0 0
                
2. In anova, more often we data in hand and want to create the design
    matrix from the data according to different constraints. We can use
    function `lm` and `model.matrix` to achieve it. In order to obtain
    different kind of design matrix, we can change the options before we
    do the analysis of variance. To do this we can use function
    `options`. The parameter contrast in this function can be
    "contr.treatment", "contr.sum" and "contr.SAS" and so on.
    However, `model.matrix` only work for fixed effect factors. 

## Formulas

1. 统计中有很多不同的线性和非线性模型， 将它们写成R能识别的表达式是利用R来求解这些模型的第一步也是非常重要的一步， 这就决定了在R中书写
    Formula是非常重要的。 R中大部分处理模型的函数的Formula遵从通用的规则，
    但是有些Package里面的处理模型的函数有其自己的特殊规则， 比如说函数lme()和lmer()。

2. 函数lme()使用$\mid$来分隔低层因此和Group因子， 用/表示因子的嵌套结构。

3. 函数lmer()使用小括号来表示Random Effect， 亦即小括号内的表达式部分表示随机效应， 不在小括号里面的部分表示固定效应。
    符号$\mid$用来分隔低层因子和Group因子， $\mid$之前的事低层因子，其后的是Group因子。
    如果没有低层因子（也可以说低层因子只有一个水平）则低层因子可以用1表示。 这个在Split模型和Repeat Measure
    模型中很有用。

## Model Fitting

1. There're many different functions in R used to fit different models.
    Besides, there're some many useful functions to extract useful
    information from the fitted model, such as `vcov`,
    `fitted`,`residuals`,`effects` and `coef`. Also there's a function
    `aov` which can be used to compare different models.

2. 在ANOVA里面，线性模型的选择取决很多不同的因素。

    (i) 分析试验的设计方案，找出潜在的因子（包括我们实际感兴趣的因子， 以及block factors 等）

    (ii) 决定要不要加入因子的交互效应。这个步骤遵循几个原则：

    - 一般来说，我们不考虑block factor和感兴趣的factor的交互效应。这个不是绝对的，
        比如说split-plot design里面...(check
        it)。这个还是取决于试验的设计方案。在统计里面block里面的 EU性质是相近的，也就是观测值是正相关的。block
        factor 和一般因子的交互效应还是可以看作是新的sub-block.
        至于这个sub-block应不应该加入模型，可以看实际情况中sub-block 里面的EUs是不是正相关的。

    - 选择的统计模型必须能够估计Error（否则无法检验模型），这就决定
        了当观测值不是很多（比如说一个Treatment只有一个观测值时），
        不可能所有的interaction都加入模型中。根据DOE里面的...准则（check
        it)我们应该将低级interaction保留在模型中,
        而将高级interaction舍弃使得eroor可以被估计。当然这实属不得已而为之。
        如果你有足够的观测值，当然可以把高级interaction加入模型中。

    - 通常来说我倾向于首先选择一个尽量大的模型，但这不表示我们认为这个模型是
        正确的。这个大模型只是为了方便进一步选择更好的模型。如果基于这个大模型，
        你认为某个interaction是不显著的，你可以将其从模型移除。当然你还是遵循
        前面提到的..准则，也就是说如果你的模型包含的高级Interaction，那么它的所有
        子interaction都应该包含在模型里面。

    以上不过是纸上谈兵，实际操作中我们必须去fit很多模型。那么如何fit模型呢？我们知道在SAS 里面MIX procedure是fit
    mixed linear models 的利器。在R里面，我们以用`nlme`里面的`lme`或者`lme4`里面的`lmer`来fit
    mixed linear models.
    这两个函数的模型声明语法类似，但是`lmer`的模型声明语法更灵活简单一些。`lmer`的不足之
    处是fit完模型后不方便作统计检验。`anova` 作用在`mer`(`lmer`的输出对象)的结果输出不完整，比如说F
    test的自由度，以及Pvalues等都没有输出。这些信息只能根据自已对模型的了解来决定。而`anova`
    作用在`lme`(`lme`的输出对象）的输出结果很完整。当然这个函数在检测contrast的时候都不如SAS里面的 MIXED
    procedure 方便。在SAS的MIXED
    procedure里面，你只需要加入需要的contrast语句即可，但是在R厘米使用`lme`和[] `lmer`,
    你都必须自己去计算contrast，并作检验。综合来说`lme`比`lmer`更好使用。
    `~Device+(1|SET/Device)` `/`表示嵌套结构，也就是说Device的random
    效应是nested在SET里面的。当然你也可以认为是SET和Device的交互效应。 注意到你也可以fit
    `~Device+(Device|SET)`，但是这个模型假设每个SET下的device里面有一个不同的随机效应。
    这等价于假设了一个更加复杂的convariance matrix。这个假设和一般的关于covariance matrix的假设不一样。
    至于那个更好，取决于模型的比较结果以及你对实际问题的理解。 当然，通常我们不会采用这个复杂的covariance
    matrix假设。（....比较SAS里面的结果和R的结果，尤其是自由度，为什么一下子就变成
    205了，当然，从用复杂的假设后可能使用了approximation，也就是严格的理论结果不存在了..） 在`lmer`里面，
    random effect
    部分可以写为`~(1|SET/Device)`或者更明白的形式`~(1|SET)+(1|SET:Device)))`。
    `~Day+(Day|Subject)`我们想以Day为自变量（注意这里Day不是factor)fit一个线性模型，
    但是对于每个subject来说，这个线性模型的intercept和斜率都增加了一个随机效应（注意如果没有这个随机效应
    的话，那么所有的subject里面的线性模型都是一样的）。这有点类似于按某个factor(比如说性别)fit不同的
    线性模型，但是区别是一个是Fixed
    effect(比如说性别只有两种可能性)，而subject却有无数个（试验里面具体的subject只能被认为是一个群体里面
    随机选取的）。


2. Function `median` returns a vector of length one of two depending on
    whether the length of vector is odd or even. If the return result is
    a vector of 2, it might cause some bug while we can hardly notice it
    if all other vectors, matrices and arrays involved in the
    calculation with this result have even number of elements. So we
    have to be very careful about this function. My suggestion is that
    never use this function, instead, we can use `quantile(x,prob=0.5)`
    to find the median of vector `x`.

3. Function `summary` can give some statistics about the data. But not
    as specific as SAS does.

7. `rstudent` extracts studentized residuals of models from objects
    returned by modeling functions. However, it only works for some type
    of objects, e.g. `lm` and `glm`. It doesn't work for `lme` objects.
    For `lme` objects, you can use `residuals` to extract model
    residuals. Using option `type="normalized"`, you can extract
    studentized residuals of `lme` objects.

8. `IQR` calculate the interquartile range of a given data.

