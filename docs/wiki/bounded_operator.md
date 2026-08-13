---
tags:
  - 解析学/関数解析
  - 線形写像
  - ノルム
  - 連続性
---

# 有界作用素

## 定義

> [!definition] 有界線形作用素
> ノルム空間 $`X,Y`$ の間の線形写像 $`T\colon X\to Y`$ が有界であるとは、ある定数 $`C\ge0`$ が存在して、すべての $`x\in X`$ に対して $`\lVert T(x)\rVert\le C\lVert x\rVert`$ が成り立つことである。

有界線形作用素は連続であり、ノルム空間間の線形写像については連続性と有界性は同値である。

作用素ノルムは $`\lVert T\rVert=\sup_{\lVert x\rVert\le1}\lVert T(x)\rVert`$ と定める。
