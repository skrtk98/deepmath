---
tags:
  - 圏論
  - 函手
  - 普遍性
  - 随伴
---

# Kan 拡張

Kan 拡張は、函手 $`E\colon\mathcal{C}\to\mathcal{U}`$ を函手 $`F\colon\mathcal{C}\to\mathcal{D}`$ に沿って延長する普遍的な方法である。
左 Kan 拡張は自然変換の圏における始対象として、右 Kan 拡張は終対象として定義される。

## 左 Kan 拡張

> [!definition] 左 Kan 拡張
> 函手 $`F\colon\mathcal{C}\to\mathcal{D}`$ および $`E\colon\mathcal{C}\to\mathcal{U}`$ に対し、**$`F`$ に沿った $`E`$ の左 Kan 拡張** とは、函手 $`\operatorname{Lan}_F E\colon\mathcal{D}\to\mathcal{U}`$ と自然変換
>
> ```math
> \eta\colon E\Rightarrow (\operatorname{Lan}_F E)\circ F
> ```
>
> の組である。
> ただし、任意の函手 $`S\colon\mathcal{D}\to\mathcal{U}`$ と自然変換 $`\theta\colon E\Rightarrow S\circ F`$ に対して、一意な自然変換 $`\tau\colon\operatorname{Lan}_F E\Rightarrow S`$ が存在し、$`\theta=(\tau F)\circ\eta`$ を満たさなければならない。

したがって左 Kan 拡張は、$`E\Rightarrow S\circ F`$ という形の任意の延長データを一意に因子化する。
存在すれば、その普遍性から一意な自然同型を除いて定まる。

## 右 Kan 拡張

> [!definition] 右 Kan 拡張
> **$`F`$ に沿った $`E`$ の右 Kan 拡張** とは、函手 $`\operatorname{Ran}_F E\colon\mathcal{D}\to\mathcal{U}`$ と自然変換
>
> ```math
> \varepsilon\colon (\operatorname{Ran}_F E)\circ F\Rightarrow E
> ```
>
> の組である。
> 任意の $`S\colon\mathcal{D}\to\mathcal{U}`$ と $`\theta\colon S\circ F\Rightarrow E`$ に対し、一意な $`\tau\colon S\Rightarrow\operatorname{Ran}_F E`$ が存在して $`\theta=\varepsilon\circ(\tau F)`$ を満たすことを要請する。

この定義は左 Kan 拡張の双対である。

## 各点での計算

必要な余極限が存在するとき、左 Kan 拡張は対象 $`d\in\mathcal{D}`$ ごとにコンマ圏 $`(F\mathbin{\downarrow}d)`$ を用いて

```math
(\operatorname{Lan}_F E)(d)
\cong
\operatorname*{colim}_{(c,,F(c)\to d)\in(F\mathbin{\downarrow}d)}E(c)
```

と計算できる。
双対的に、必要な極限が存在するとき、右 Kan 拡張は

```math
(\operatorname{Ran}_F E)(d)
\cong
\operatorname*{lim}_{(c,,d\to F(c))\in(d\mathbin{\downarrow}F)}E(c)
```

と計算できる。
この各点公式を満たす Kan 拡張を各点 Kan 拡張という。
豊穣圏における重み付き極限と余極限による定式化は [各点 Kan 拡張](./pointwise_kan_extension.md) を参照されたい。
