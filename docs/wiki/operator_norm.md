---
tags:
  - 解析学
  - 関数解析
  - 有界作用素
  - ノルム
---

# 作用素ノルム

作用素ノルムは、有界線形作用素の大きさを測るノルムである。

## 定義

> [!definition] 作用素ノルム
> ノルム空間 $`X,Y`$ の間の有界線形作用素 $`T\colon X\to Y`$ に対し、**作用素ノルム**を
>
> ```math
> \lVert T\rVert
> =
> \sup_{\lVert x\rVert\leq1}\lVert T x\rVert
> ```
>
> と定める。

この値は、$`\lVert Tx\rVert\leq C\lVert x\rVert`$ を満たす定数 $`C`$ の下限に一致する。

## 性質

すべての $`x\in X`$ について $`\lVert Tx\rVert\leq\lVert T\rVert\lVert x\rVert`$ が成り立つ。
また、合成可能な有界線形作用素 $`T,S`$ に対して

```math
\lVert S\circ T\rVert\leq\lVert S\rVert\lVert T\rVert
```

が成り立つ。

$`Y`$ が Banach 空間であれば、有界線形作用素全体の空間 $`\mathcal{B}(X,Y)`$ は作用素ノルムに関して Banach 空間となる。
有界性については [有界作用素](./bounded_operator.md) を参照されたい。
