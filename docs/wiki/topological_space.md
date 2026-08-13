---
tags:
  - 位相幾何学
  - 開集合
  - 閉集合
  - 包含関係
---

# 位相空間

## 定義

> [!definition] 位相空間
> 集合 $`X`$ の部分集合族 $`\mathcal{T}\subseteq\mathcal{P}(X)`$ が次を満たすとき、$`\mathcal{T}`$ を $`X`$ 上の **位相** (*topology*) といい、組 $`(X,\mathcal{T})`$ を **位相空間** (*topological space*) という。
>
> - $`\varnothing,X\in\mathcal{T}`$。
> - 任意の有限個の $`\mathcal{T}`$ の元の共通部分は $`\mathcal{T}`$ に属する。
> - 任意の $`\mathcal{T}`$ の元からなる族の和集合は $`\mathcal{T}`$ に属する。

$`\mathcal{T}`$ の元を開集合という。

$`X\setminus F`$ が開集合であるとき、$`F\subseteq X`$ を閉集合という。

## 例

冪集合 $`\mathcal{P}(X)`$ は $`X`$ 上の位相であり、これを離散位相という。

$`\{\varnothing,X\}`$ も $`X`$ 上の位相であり、これを密着位相という。

また、補集合が有限である部分集合と空集合からなる族は、$`X`$ 上の余有限位相を定める。

## 位相の比較

同じ集合 $`X`$ 上の二つの位相 $`\mathcal{T}_1,\mathcal{T}_2`$ について、$`\mathcal{T}_2\subseteq\mathcal{T}_1`$ が成り立つとき、$`\mathcal{T}_1`$ は $`\mathcal{T}_2`$ より細かいといい、$`\mathcal{T}_2`$ は $`\mathcal{T}_1`$ より粗いという。

離散位相は最も細かい位相であり、密着位相は最も粗い位相である。
