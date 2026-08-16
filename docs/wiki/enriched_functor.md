---
tags:
  - 圏論/豊穣圏論
  - 豊穣圏
  - 函手
---

# 豊穣函手

豊穣函手は、Hom 集合を Hom 対象へ置き換えた構造を保つ写像である。

## 定義

> [!definition] 豊穣函手
> [モノイダル圏](./monoidal_category.md) $`\mathcal{V}`$ 上の豊穣圏 $`\mathcal{A},\mathcal{B}`$ に対し、$`\mathcal{V}`$-豊穣函手 $`F\colon\mathcal{A}\to\mathcal{B}`$ とは、対象写像と、各 $`a,a'` に対する射
>
> ```math
> F_{a,a'}\colon\mathcal{A}(a,a')\to\mathcal{B}(Fa,Fa')
> ```
>
> からなり、単位射と合成射を保存するものをいう。

すなわち $`F_{a,a}\circ j_a=j_{Fa}`$ が成り立ち、合成に関する自然な正方形が可換であることを要求する。

## 例と性質

$`\mathcal{V}=\mathsf{Set}`$ の場合、豊穣函手は通常の函手に一致する。
$`\mathcal{V}=\mathsf{Ab}`$ の場合、各 Hom 群への準同型を与える加法函手に一致する。

豊穣函手は下部圏の函手を誘導する。
恒等と合成により、豊穣函手は $`\mathcal{V}`$-圏の間の 1-射をなす。
