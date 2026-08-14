---
tags:
  - 圏論
  - 函手
  - 自然変換
  - モノイド対象
---

# モナド

**モナド** (*monad*) は、自己函手に単位と合成を与える構造である。
代数的構造の自由構成、随伴、計算の文脈を同じ形式で表す。

## 定義

> [!definition] モナド
> 圏 $`\mathcal{C}`$ 上のモナドとは、自己函手 $`T\colon\mathcal{C}\to\mathcal{C}`$、自然変換 $`\eta\colon1_{\mathcal{C}}\Rightarrow T`$ と $`\mu\colon T^2\Rightarrow T`$ の組であって、
>
> ```math
> \mu\circ T\mu=\mu\circ\mu T,
> \qquad
> \mu\circ T\eta=1_T=\mu\circ\eta T
> ```
>
> を満たすものをいう。

第一式は乗法 $`\mu`$ の結合律を、第二式は $`\eta`$ が単位であることを表す。

```tikz
\begin{tikzcd}[column sep=large, row sep=large]
T^3 \arrow[r, "T\mu"] \arrow[d, "\mu T"'] & T^2 \arrow[d, "\mu"] \\
T^2 \arrow[r, "\mu"'] & T
\end{tikzcd}
```

## 例と随伴

集合の冪集合函手 $`\mathcal{P}`$ は、要素を一点集合へ送る単位と、部分集合族の和集合を取る乗法によりモナドとなる。

随伴 $`F\dashv G`$ が与えられると、合成 $`GF`$ はモナドをなす。
単位は随伴の単位であり、乗法は余単位を用いて $`G\varepsilon F\colon GFGF\Rightarrow GF`$ と定まる。

モナドは、自己函手の圏 $`\operatorname{End}(\mathcal{C})`$ におけるモノイド対象と同じデータである。
Kleisli 圏と Eilenberg–Moore 圏は、モナドから得られる二つの標準的な圏である。
