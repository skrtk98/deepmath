---
tags:
  - 位相幾何学
  - 閉包
  - 近傍
---

# 境界点と境界

部分集合とその補集合のいずれにも、どの近傍からも到達できる点を境界点という。

## 定義と性質

> [!definition] 境界点
> 位相空間 $`X`$ の部分集合 $`A`$ に対し、任意の近傍 $`U`$ が $`A`$ と $`X\setminus A`$ の両方と交わる点を $`A`$ の境界点という。
> 境界点全体を $`\partial A`$ と書く。

境界は

```math
\partial A=\overline{A}\cap\overline{X\setminus A}
```

と表せる。
さらに $`\overline{A}=A^\circ\sqcup\partial A`$ が成り立つ。
