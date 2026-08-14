---
tags:
  - 圏論
  - 豊穣圏
  - 自然変換
---

# 豊穣自然変換

豊穣自然変換は、豊穣函手の間の比較を基底モノイダル圏の射として記述する。

## 定義

> [!definition] 豊穣自然変換
> $`\mathcal{V}`$-豊穣函手 $`F,G\colon\mathcal{A}\to\mathcal{B}`$ の豊穣自然変換 $`\alpha\colon F\Rightarrow G`$ とは、各対象 $`a`$ に対する射 $`\alpha_a\colon I\to\mathcal{B}(Fa,Ga)`$ であって、任意の $`a,b`$ に対し、$`F`$ と $`G`$ が誘導する二つの合成 $`\mathcal{A}(a,b)\to\mathcal{B}(Fa,Gb)`$ が一致するものをいう。

これは通常の自然性条件を、Hom 対象の間の射として表したものである。

垂直合成と水平合成が定まり、豊穣圏、豊穣函手、豊穣自然変換は 2-圏 $`\mathcal{V}\text{-}\mathsf{Cat}`$ をなす。
$`\mathcal{V}=\mathsf{Set}`$ の場合、通常の自然変換に一致する。
