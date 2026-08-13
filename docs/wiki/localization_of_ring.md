---
tags:
  - 代数学/環論
  - 商構成
  - 普遍性
  - 可逆化
---

# 環の局所化

## 定義

可換環 $`R`$ の部分集合 $`S\subseteq R`$ が **乗法的集合** であるとは、$`1_R\in S`$ であり、任意の $`s,t\in S`$ に対して $`st\in S`$ が成り立つことである。

> [!definition] 環の局所化
> 乗法的集合 $`S`$ に対して、直積 $`R\times S`$ 上に
> ```math
> (r,s)\sim(r',s')
> \quad\Longleftrightarrow\quad
> \text{ある }u\in S\text{ が存在して }u(rs'-r's)=0_R
> ```
> により定める同値関係の商集合を $`S^{-1}R`$ と表す。
> この集合に
> ```math
> \frac{r}{s}+\frac{r'}{s'}\coloneqq\frac{rs'+r's}{ss'},\qquad
> \frac{r}{s}\frac{r'}{s'}\coloneqq\frac{rr'}{ss'}
> ```
> として定める演算により得られる環を、$`R`$ の $`S`$ による**局所化** (*localization*) という。

標準的な環準同型 $`R\to S^{-1}R`$、$`r\mapsto r/1_R`$ は、すべての $`s\in S`$ の像を単元にする。

## 普遍性

任意の環準同型 $`f\colon R\to A`$ が、すべての $`s\in S`$ に対して $`f(s)` を単元にすると仮定する。

このとき、$`f`$ は一意な環準同型 $`\bar f\colon S^{-1}R\to A`$ を通じて因子化する。

```math
\bar f\left(\frac{r}{s}\right)=f(r)f(s)^{-1}
```

この普遍性により、局所化は $`S`$ の元を可逆にする最も一般的な環と特徴付けられる。

## 例

整域 $`R`$ に対して、$`S=R\setminus\{0_R\}`$ による局所化 $`S^{-1}R`$ は $`R`$ の分数体である。

素イデアル $`\mathfrak p\subset R`$ に対して、$`R\setminus\mathfrak p`$ は乗法的集合である。

この局所化を $`R_{\mathfrak p}`$ と表す。
