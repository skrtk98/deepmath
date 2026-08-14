---
tags:
  - 圏論/豊穣圏論
  - 米田埋め込み
  - 前層
  - 重み付き極限と余極限
---

# 豊穣米田の補題

豊穣米田の補題は、豊穣前層への豊穣自然変換を、その表現対象における前層の値として記述する定理である。
通常の米田の補題は、基底圏を $`\mathsf{Set}`$ とする特別な場合に当たる。

以下では、$`\mathcal{V}`$ を対称モノイダル閉圏、$`A`$ を小さい $`\mathcal{V}`$-圏とする。
$`\mathcal{V}`$-前層とは $`\mathcal{V}`$-函手 $`F\colon A^{\mathrm{op}}\to\mathcal{V}`$ であり、そのなす豊穣函手圏を $`[A^{\mathrm{op}},\mathcal{V}]`$ と書く。

## 豊穣米田埋め込み

各 $`a\in A`$ に対し、Hom 対象による前層

```math
y(a)=A(-,a)\colon A^{\mathrm{op}}\longrightarrow\mathcal{V}
```

を定める。
この対応は豊穣函手

```math
y\colon A\longrightarrow[A^{\mathrm{op}},\mathcal{V}]
```

を与え、これを **豊穣米田埋め込み** という。

## 定理

> [!theorem] 豊穣米田の補題
> 任意の $`a\in A`$ と豊穣前層 $`F\colon A^{\mathrm{op}}\to\mathcal{V}`$ に対し、$`\mathcal{V}`$ において自然な同型
>
> ```math
> [A^{\mathrm{op}},\mathcal{V}](y(a),F)
> \cong F(a)
> ```
>
> が存在する。

左辺は豊穣函手圏の Hom 対象である。
この同型の $`I`$-点は、通常の自然変換 $`y(a)\Rightarrow F`$ と $`F(a)`$ の元との対応を与える。

$`F=y(b)`$ と置くと

```math
[A^{\mathrm{op}},\mathcal{V}](y(a),y(b))
\cong A(a,b)
```

を得る。
したがって、豊穣米田埋め込みは充満忠実である。

## テンソルによる表示

$`v\in\mathcal{V}`$ に対し、前層圏におけるテンソル $`v\odot y(a)`$ が存在すれば、豊穣米田の補題とテンソルの普遍性から

```math
[A^{\mathrm{op}},\mathcal{V}](v\odot y(a),F)
\cong [v,F(a)]
```

が得られる。
ここで右辺 $`[v,F(a)]`$ は $`\mathcal{V}`$ の内部 Hom を表す。

閉性を仮定せず、前層構成が左 $`\mathcal{V}`$-加群圏として定義される場合には、対応する集合値の普遍性

```math
\operatorname{Hom}(v\odot y(a),F)
\cong \mathcal{V}(v,F(a))
```

を用いることができる。
この式は、内部 Hom 対象を用いずにテンソルと表現可能前層の関係を述べる。

## 表現可能前層による生成

豊穣版の余米田の補題は、前層 $`F`$ が表現可能前層から標準的に再構成されることを述べる。
必要なテンソルとコエンドが存在するとき、前層圏で

```math
F\cong\int^{a\in A}F(a)\odot y(a)
```

が成り立つ。
右辺は、係数 $`F(a)`$ を重みとする表現可能前層の重み付き余極限である。
この表示は、豊穣前層圏が表現可能前層から重み付き余極限によって生成されることを示す。

通常の米田の補題と余米田の補題は、それぞれ [米田の補題](./yoneda_lemma.md) と [余米田の補題](./co_yoneda_lemma.md) を参照されたい。
重み付き余極限の一般形は [重み付き余極限](./weighted_colimit_enriched.md) を、基底圏と豊穣函手の定義は [豊穣圏](./enriched_category.md) を参照されたい。
