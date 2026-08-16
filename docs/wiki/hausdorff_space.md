---
tags:
  - 幾何学/位相幾何学
  - 分離公理
  - 収束
---

# Hausdorff 空間

異なる二点を互いに素な開集合で分離できる位相空間を **Hausdorff 空間**という。

## 定義

> [!definition] Hausdorff 性
> 位相空間 $`X`$ が Hausdorff であるとは、任意の相異なる点 $`x,y`$ に対して、$`x\in U`$、$`y\in V`$、$`U\cap V=\varnothing`$ を満たす開集合 $`U,V`$ が存在することをいう。

## 性質と例

Hausdorff 空間では、ネットまたはフィルターが収束する場合の極限は一意である。
また、Hausdorff 空間のコンパクト部分集合は閉集合である。

$`X`$ が Hausdorff であることは、積空間 $`X\times X`$ の対角集合 $`\{(x,x)\mid x\in X\}`$ が閉であることと同値である。
任意の距離空間は Hausdorff である。

Hausdorff 性を仮定しない位相も重要であるため、極限の一意性を使う箇所ではこの仮定を明示する。
