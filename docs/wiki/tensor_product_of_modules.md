---
tags:
  - 代数学/加群論
  - 多重線形性
  - 普遍性
  - 商構成
---

# 加群のテンソル積

## 定義

可換環 $`R`$ 上の加群 $`M,N`$ を考える。

> [!definition] テンソル積
> $`R`$-加群 $`T`$ と双線形写像 $`\tau\colon M\times N\to T`$ の組が **$`M`$ と $`N`$ のテンソル積** (*tensor product*) であるとは、任意の $`R`$-加群 $`P`$ と双線形写像 $`b\colon M\times N\to P`$ に対して、
> ```math
> b=\widetilde b\circ\tau
> ```
> を満たす一意な $`R`$-線形写像 $`\widetilde b\colon T\to P`$ が存在することである。

この $`T`$ を $`M\otimes_RN`$ と表し、$`\tau(m,n)`$ を $`m\otimes n`$ と表す。

## 基本的な関係式

任意の $`m,m'\in M`$、$`n,n'\in N`$、$`r\in R`$ に対して、テンソル積では次が成り立つ。

```math
(m+m')\otimes n=m\otimes n+m'\otimes n,
```
```math
m\otimes(n+n')=m\otimes n+m\otimes n',
```
```math
(rm)\otimes n=m\otimes(rn).
```

## 例

自然数 $`m,n`$ に対して、
```math
\mathbb{Z}/m\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/n\mathbb{Z}
\cong\mathbb{Z}/\gcd(m,n)\mathbb{Z}
```
が成り立つ。

また、$`R^m\otimes_RR^n\cong R^{mn}`$ が成り立つ。
