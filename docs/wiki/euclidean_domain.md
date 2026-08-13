---
tags:
  - 代数学/環論
  - 除法
  - 因数分解
  - アルゴリズム
---

# Euclid 整域

## 定義

> [!definition] Euclid 整域
> 整域 $`R`$ が **Euclid 整域** (*Euclidean domain*) であるとは、写像 $`\delta\colon R\setminus\{0_R\}\to\mathbb{N}`$ が存在して、任意の $`a\in R`$ および $`b\in R\setminus\{0_R\}`$ に対して、
> ```math
> a=bq+r
> ```
> を満たす $`q,r\in R`$ が存在し、$`r=0_R`$ または $`\delta(r)<\delta(b)`$ が成り立つことである。
> このような $`\delta`$ を Euclid 関数という。

この条件は、$`R`$ において余り付き除法を行えることを表す。

## 例

整数環 $`\mathbb{Z}`$ は、$`\delta(a)=|a|`$ により Euclid 整域となる。

体 $`k`$ 上の一変数多項式環 $`k[x]`$ は、$`\delta(f)=\deg f`$ により Euclid 整域となる。

## 性質

Euclid 整域は主イデアル整域である。

したがって、Euclid 整域は一意分解整域でもある。
