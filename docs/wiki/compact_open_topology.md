---
tags:
  - 位相幾何学
  - 関数空間
  - コンパクト空間
  - 連続写像
  - 積位相
---

# コンパクト開位相

コンパクト開位相は、連続写像の空間を位相化する標準的な方法である。

## 定義

位相空間 $`X,Y`$ の間の連続写像全体の集合を $`C(X,Y)`$ と書く。
コンパクト部分集合 $`K\subseteq X`$ と開集合 $`G\subseteq Y`$ に対し、

```math
W(K,G)=\{f\in C(X,Y)\mid f(K)\subseteq G\}
```

と定める。

> [!definition] コンパクト開位相
> 集合族 $`\{W(K,G)\}`$ を部分基として $`C(X,Y)`$ に入る位相を **コンパクト開位相** という。

この位相では、コンパクト部分集合上で写像の像がある開集合に含まれることが、関数空間における開条件となる。

## Curry 化

連続写像

```math
f\colon X\times Y\longrightarrow Z
```

に対し、その **Curry 化** を

```math
\widehat f\colon X\longrightarrow C(Y,Z),
\qquad
\widehat f(x)(y)=f(x,y)
```

で定める。
$`C(Y,Z)`$ にコンパクト開位相を入れると、$`\widehat f`$ は連続である。

逆に、連続写像 $`g\colon X\to C(Y,Z)`$ に対して

```math
\check g\colon X\times Y\longrightarrow Z,
\qquad
\check g(x,y)=g(x)(y)
```

と定める。
この評価写像が連続となるためには、例えば $`Y`$ が局所コンパクト Hausdorff 空間であることが十分である。
この条件の下で、Curry 化と逆 Curry 化は連続写像の間の対応を与える。

積位相については [積位相空間](./product_topological_space.md) を参照されたい。
