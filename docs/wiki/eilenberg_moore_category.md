---
tags:
  - 圏論
  - モナド
  - 代数構造
---

# Eilenberg–Moore 圏

モナドの単位と乗法に整合する対象を **モナド代数**という。
モナド代数とその準同型からなる圏を Eilenberg–Moore 圏という。

## 定義

> [!definition] Eilenberg–Moore 圏
> モナド $`T=(T,\eta,\mu)`$ に対し、Eilenberg–Moore 圏 $`\mathcal{C}^T`$ の対象は、射 $`a\colon TA\to A`$ で
>
> ```math
> a\circ\eta_A=1_A,
> \qquad
> a\circ\mu_A=a\circ T(a)
> ```
>
> を満たす組 $`(A,a)`$ である。
> 射 $`f\colon(A,a)\to(B,b)`$ は、$`b\circ T(f)=f\circ a`$ を満たす $`\mathcal{C}`$ の射 $`f\colon A\to B`$ である。

## 随伴と比較

自由代数を送る函手と忘却函手の間には随伴 $`F^T\dashv U^T`$ があり、$`U^TF^T=T`$ が成り立つ。
この圏は、モナドが記述する代数構造のモデルと準同型をすべて保持する。

[Kleisli 圏](./kleisli_category.md) も同じモナドから構成されるが、モナド射の合成を扱うためのより小さい標準構成である。
