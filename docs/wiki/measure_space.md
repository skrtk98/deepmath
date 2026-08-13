---
tags:
  - 解析学/測度論
  - 可測性
  - 可算加法性
  - 積分
---

# 測度空間

## 定義

> [!definition] 測度空間
> 集合 $`X`$、$`X`$ 上の $`\sigma`$-代数 $`\mathcal{F}`$、写像 $`\mu\colon\mathcal{F}\to[0,\infty]`$ の組 $`(X,\mathcal{F},\mu)`$ が測度空間であるとは、$`\mu(\varnothing)=0`$ であり、互いに素な可算族 $`(A_n)_{n\ge1}`$ に対して
> ```math
> \mu\left(\bigcup_{n\ge1}A_n\right)=\sum_{n\ge1}\mu(A_n)
> ```
> が成り立つことである。

ここで、$`\sigma`$-代数とは補集合および可算和集合について閉じた部分集合族である。

## 例

実数直線の Borel $`\sigma`$-代数と Lebesgue 測度は測度空間をなす。

集合上の冪集合と数え上げ測度も測度空間をなす。
