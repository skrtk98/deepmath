---
tags:
  - 幾何学/位相幾何学
  - 稠密性
  - 閉包
  - 内部
---

# どこにも稠密でない集合

どこにも稠密でない集合は、その閉包が開集合を一つも含まない部分集合である。

## 定義

> [!definition] どこにも稠密でない集合
> 位相空間 $`X`$ の部分集合 $`A`$ が **どこにも稠密でない** とは、
>
> ```math
> \operatorname{Int}(\overline{A})=\varnothing
> ```
>
> を満たすことである。

同値に、任意の非空開集合 $`U\subseteq X`$ は、$`U\cap\overline{A}=\varnothing`$ を満たす非空開部分集合をもつ。
閉包と内部については [閉包作用素](./closure_operator.md) および [開核作用素](./interior_operator.md) を参照されたい。
