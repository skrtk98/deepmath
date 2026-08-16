---
tags:
  - 圏論/モノイダル圏論
  - モノイダル圏
  - 自然変換
---

# モノイダル自然変換

ラックスモノイダル函手の間の自然変換が、積と単位に関する構造射を保つとき、これを**モノイダル自然変換**という。

## 定義

> [!definition] モノイダル自然変換
> ラックスモノイダル函手 $`F,G\colon\mathcal{M}\to\mathcal{N}`$ の自然変換 $`\sigma\colon F\Rightarrow G`$ がモノイダルであるとは、任意の $`A,B`$ に対して
>
> ```math
> \sigma_{A\otimes B}\circ\phi^F_{A,B}
> =\phi^G_{A,B}\circ(\sigma_A\otimes\sigma_B)
> ```
>
> が成り立ち、さらに単位構造射との合成が一致することをいう。

モノイダル圏 $`\mathcal{M},\mathcal{N}`$ に対し、ラックスモノイダル函手とモノイダル自然変換は圏 $`\mathsf{Mon}(\mathcal{M},\mathcal{N})`$ をなす。
強モノイダル函手の間のモノイダル自然同型は、モノイダル圏同値のデータに現れる。
