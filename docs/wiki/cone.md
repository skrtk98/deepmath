---
tags:
  - 圏論
  - 可換図式
  - 極限
  - 余極限
---

# 錐と余錐

図式の各対象へ整合的に射を出すデータを**錐**という。
錐は [極限](./limit.md) の普遍性を記述する基本単位であり、双対的に余極限には余錐を用いる。

## 定義

> [!definition] 錐と余錐
> 図式 $`D\colon I\to\mathcal{C}`$ と対象 $`A\in\mathcal{C}`$ に対して、頂点 $`A`$ の **錐** とは自然変換 $`\Delta A\Rightarrow D`$ である。
> すなわち、射 $`\lambda_i\colon A\to D(i)`$ の族であって、任意の $`u\colon i\to j`$ に対し $`D(u)\circ\lambda_i=\lambda_j`$ を満たすものをいう。
>
> **余錐** とは、自然変換 $`D\Rightarrow\Delta A`$ である。

錐の集合を $`\operatorname{Cone}(A,D)`$ と書くと、

```math
\operatorname{Cone}(A,D)\cong[I,\mathcal{C}](\Delta A,D)
```

が成り立つ。
この同一視は、錐を函手圏における自然変換として扱う。

## 極限との関係

極限は、図式 $`D`$ への錐の圏における終対象である。
余極限は、$`D`$ からの余錐の圏における始対象である。
したがって、積、等化子、引き戻しは特定の図式への普遍的な錐として記述できる。
