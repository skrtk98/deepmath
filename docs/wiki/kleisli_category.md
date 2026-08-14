---
tags:
  - 圏論
  - モナド
  - 随伴
---

# Kleisli 圏

モナドの射 $`A\to TB`$ を通常の射として合成する圏を **Kleisli 圏**という。
これはモナドが表す計算的な合成を記述する標準構成である。

## 定義

> [!definition] Kleisli 圏
> 圏 $`\mathcal{C}`$ 上のモナド $`(T,\eta,\mu)`$ に対し、Kleisli 圏 $`\mathcal{C}_T`$ は次で定まる。
>
> - 対象は $`\mathcal{C}`$ の対象と同じである。
> - Hom は $`\mathcal{C}_T(A,B)=\mathcal{C}(A,TB)`$ とする。
> - 恒等射は $`\eta_A\colon A\to TA`$ とする。
> - $`f\colon A\to TB`$ と $`g\colon B\to TC`$ の合成は $`\mu_C\circ T(g)\circ f\colon A\to TC`$ とする。

モナドの結合律と単位律により、この合成は圏の結合律と単位律を満たす。

## 随伴

Kleisli 圏には随伴 $`F_T\dashv U_T`$ があり、$`F_T`$ は通常の射 $`f\colon A\to B`$ を $`\eta_B\circ f\colon A\to TB`$ へ送る。
この随伴が与えるモナドは元の $`T`$ と一致する。

Kleisli 圏は、同じモナドから得られる [Eilenberg–Moore 圏](./eilenberg_moore_category.md) よりも、自由な構成に重点を置く。
