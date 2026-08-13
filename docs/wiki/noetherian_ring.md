---
tags:
  - 代数学/環論
  - イデアル
  - 有限性
  - 鎖条件
---

# Noether 環

## 定義

> [!definition] Noether 環
> 可換環 $`R`$ が **Noether 環** (*Noetherian ring*) であるとは、任意のイデアルの昇鎖
> ```math
> I_1\subseteq I_2\subseteq I_3\subseteq\cdots
> ```
> がある自然数 $`N`$ に対して $`I_N=I_{N+1}=\cdots`$ を満たすことである。

この性質をイデアルに関する**昇鎖条件**という。

可換環 $`R`$ について、$`R`$ が Noether 環であることと、すべてのイデアルが有限生成であることは同値である。

## 例

主イデアル整域は Noether 環である。

したがって、整数環 $`\mathbb{Z}`$ は Noether 環である。

また、Hilbert の基底定理により、Noether 環 $`R`$ に対して多項式環 $`R[x]`$ も Noether 環である。

## 非例

体 $`k`$ 上の無限変数多項式環 $`k[x_1,x_2,\dots]`$ は Noether 環ではない。

実際、イデアルの列
```math
(x_1)\subsetneq(x_1,x_2)\subsetneq(x_1,x_2,x_3)\subsetneq\cdots
```
は停止しない。
