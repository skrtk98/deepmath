---
tags:
  - 解析学/関数解析
  - Hilbert 空間
  - 直交性
  - Fourier 解析
---

# 正規直交基底

正規直交基底は、Hilbert 空間の元を直交座標で展開する基底である。

## 定義

> [!definition] 正規直交系
> Hilbert 空間 $`H`$ の族 $`(e_i)_{i\in I}`$ が **正規直交系** であるとは、
>
> ```math
> \langle e_i,e_j\rangle=\delta_{ij}
> ```
>
> を満たすことである。

> [!definition] 正規直交基底
> 正規直交系 $`(e_i)_{i\in I}`$ が **正規直交基底** であるとは、その線形包の閉包が $`H`$ に一致することである。

## 展開と Parseval 等式

正規直交基底 $`(e_i)`$ と $`x\in H`$ に対し、

```math
x=\sum_{i\in I}\langle x,e_i\rangle e_i
```

がノルム収束の意味で成り立つ。
和は有限部分集合によるネットとして解釈する。

また Parseval 等式

```math
\lVert x\rVert^2
=
\sum_{i\in I}|\langle x,e_i\rangle|^2
```

が成り立つ。
Hilbert 空間については [Hilbert 空間](./hilbert_space.md) を参照されたい。
