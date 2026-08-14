---
tags:
  - 圏論
  - 豊穣圏
  - 重み付き極限と余極限
  - コエンド
---

# 重み付き余極限

重み付き余極限は、豊穣圏における余極限の基本形である。

以下で $`\mathcal{V}`$ を対称モノイダル閉圏、$`J`$ と $`A`$ を $`\mathcal{V}`$-圏、$`F\colon J\to A`$ と $`W\colon J^{\mathrm{op}}\to\mathcal{V}`$ を $`\mathcal{V}`$-函手とする。

> [!definition] 重み付き余極限
> 対象 $`W\star F\in A`$ が **$`W`$-重み付き余極限** であるとは、任意の $`a\in A`$ に自然な同型
>
> ```math
> A(W\star F,a)
> \cong
> [J^{\mathrm{op}},\mathcal{V}](W,A(F-,a))
> ```
>
> が存在することである。

双対的に、重み付き極限 $`\{W,F\}`$ は

```math
A(a,\{W,F\})
\cong
[J^{\mathrm{op}},\mathcal{V}](W,A(a,F-))
```

で定める。

$`\mathcal{V}=\mathsf{Set}`$ かつ $`W`$ が定数一点函手なら、通常の余極限が得られる。
$`A`$ がテンソル化され適切な余極限をもつとき、

```math
W\star F\cong\int^{j\in J}W(j)\odot F(j)
```

とコエンドで計算できる。
各点 Kan 拡張との関係については [各点 Kan 拡張](./pointwise_kan_extension.md) を参照されたい。
