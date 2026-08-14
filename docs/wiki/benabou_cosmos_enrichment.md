---
tags:
  - 圏論/豊穣圏論
  - モノイダル圏
  - 閉モノイダル圏
  - エンドとコエンド
---

# Bénabou cosmos 上の豊穣圏

豊穣圏論では、射の値を取る基底モノイダル圏の仮定が、函手圏と重み付き極限の存在を左右する。
この基底として対称モノイダル閉かつ完備余完備な圏を固定すると、豊穣圏論の基本構成を一つの枠組みで扱える。

## 定義

> [!definition] cosmos
> **cosmos** とは、対称モノイダル閉圏 $`(\mathcal{V},\otimes,I)`$ であって、完備かつ余完備なものである。

文献には仮定を強めたり緩めたりする用法がある。
本項では、豊穣函手圏、エンドとコエンド、重み付き極限と余極限を安定して定式化するための仮定としてこの意味で用いる。

## 基本構成

$`A`$ を小さい $`\mathcal{V}`$-圏とすると、豊穣前層圏 $`[A^{\mathrm{op}},\mathcal{V}]`$ が定まる。
二つの豊穣函手 $`F,G\colon A\to\mathcal{V}`$ の Hom 対象はエンド

```math
[A,\mathcal{V}](F,G)
\cong
\int_{a\in A}[F(a),G(a)]
```

で与えられる。
ここで $`[F(a),G(a)]`$ は $`\mathcal{V}`$ の内部 Hom である。

テンソルとコエンドが存在すれば、重み $`W\colon A^{\mathrm{op}}\to\mathcal{V}`$ と図式 $`H\colon A\to C`$ の重み付き余極限は

```math
W\star H
\cong
\int^{a\in A}W(a)\odot H(a)
```

と計算できる。

## 帰結と例

米田埋め込み $`y\colon A\to[A^{\mathrm{op}},\mathcal{V}]`$ は充満忠実である。
また、適切なテンソルと重み付き余極限をもつ豊穣圏では、左 Kan 拡張を各点の重み付き余極限として計算できる。

$`\mathsf{Set}`$ を直積モノイダル圏とすれば通常の圏論が得られる。
$`\mathsf{sSet}`$ を直積モノイダル圏とすれば simplicial 圏の基底となる。

豊穣函手圏は [豊穣函手圏](./enriched_functor_category.md) を、重み付き余極限は [重み付き余極限](./weighted_colimit_enriched.md) を、双圏への一般化は [双圏上の豊穣圏](./enriched_over_bicategory.md) を参照されたい。
