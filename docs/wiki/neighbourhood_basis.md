---
tags:
  - 位相幾何学
  - 近傍
  - 開基
  - フィルター
---

# 近傍基

近傍基は、各点の近傍系をより小さい集合族で指定する方法である。

## 定義

> [!definition] 近傍基
> 集合 $`X`$ の各点 $`x`$ に集合族 $`\mathcal{B}(x)`$ を対応させるとする。
> この対応が **近傍基** であるとは、次を満たすことである。
>
> - $`\mathcal{B}(x)`$ は有限共通部分について閉じたフィルター基である。
> - 任意の $`U\in\mathcal{B}(x)`$ は $`x`$ を含む。
> - 任意の $`U\in\mathcal{B}(x)`$ に対して、$`x\in V\in\mathcal{B}(x)`$ であって、各 $`y\in V`$ に対し $`W\in\mathcal{B}(y)`$, $`W\subseteq U`$ が存在するものがある。

各 $`\mathcal{B}(x)`$ が生成するフィルターを $`\mathcal{N}(x)`$ とすると、$`\mathcal{N}`$ は近傍系をなす。

## 開基との対応

開基 $`\mathfrak{B}`$ が与えられると、

```math
\mathcal{B}(x)=\{B\in\mathfrak{B}\mid x\in B\}
```

は近傍基となる。

逆に、近傍基 $`\mathcal{B}`$ に対し、各点 $`x\in B`$ で $`B\in\mathcal{B}(x)`$ を満たす部分集合 $`B`$ 全体は開基をなす。
この二つの構成は、生成される位相を保つという意味で互いに逆である。

## 比較

二つの近傍基 $`\mathcal{B},\mathcal{C}`$ に対し、任意の $`U\in\mathcal{B}(x)`$ がある $`V\in\mathcal{C}(x)`$ によって $`V\subseteq U`$ を満たすとき、$`\mathcal{C}`$ は $`\mathcal{B}`$ より細かい近傍基である。
この条件が各点で両方向に成り立つとき、両者は同じ近傍系、従って同じ位相を定める。

近傍系については [近傍系](./neighbourhood_system.md) を、開基については [開基](./topological_basis.md) を参照されたい。
