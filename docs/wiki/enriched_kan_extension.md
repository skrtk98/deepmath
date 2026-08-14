---
tags:
  - 圏論
  - 豊穣圏
  - Kan 拡張
  - 重み付き極限と余極限
---

# 豊穣 Kan 拡張

豊穣 Kan 拡張は、豊穣自然変換の対象として定める函手の普遍的延長である。

以下で $`K\colon C\to D`$, $`F\colon C\to A`$ を $`\mathcal{V}`$-函手とする。

> [!definition] 左豊穣 Kan 拡張
> $`\operatorname{Lan}_K F\colon D\to A`$ が **左豊穣 Kan 拡張** であるとは、任意の $`S\colon D\to A`$ に自然な同型
>
> ```math
> [D,A](\operatorname{Lan}_K F,S)
> \cong
> [C,A](F,S\circ K)
> ```
>
> が存在することである。

右豊穣 Kan 拡張は双対的に

```math
[D,A](S,\operatorname{Ran}_K F)
\cong
[C,A](S\circ K,F)
```

で定める。

$`A`$ が十分な重み付き余極限をもつとき、左豊穣 Kan 拡張は各点で

```math
(\operatorname{Lan}_K F)(d)
\cong
D(K-,d)\star F
```

と計算できる。
各点公式については [各点 Kan 拡張](./pointwise_kan_extension.md) を参照されたい。
