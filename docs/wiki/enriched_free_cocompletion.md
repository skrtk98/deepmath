---
tags:
  - 圏論/豊穣圏論
  - 前層
  - Kan 拡張
  - 重み付き極限と余極限
---

# 豊穣自由余完備化

豊穣前層圏は、小さい豊穣圏に小さい重み付き余極限を自由に付加した豊穣圏である。
この普遍性により、豊穣函手の余極限保存的な延長は、元の圏上での値だけから定まる。

以下で $`\mathcal{V}`$ を対称モノイダル閉圏、$`A`$ を小さい $`\mathcal{V}`$-圏とする。
豊穣前層圏 $`\widehat{A}=[A^{\mathrm{op}},\mathcal{V}]`$ が存在し、小さい重み付き余極限をもつと仮定する。

## 普遍性

> [!theorem] 豊穣自由余完備化
> $`C`$ を小さい重み付き余極限をもつ $`\mathcal{V}`$-圏とする。
> 米田埋め込み $`y\colon A\to\widehat{A}`$ による制限は、豊穣同値
>
> ```math
> \mathcal{V}\text{-}\mathsf{Cat}_{\mathrm{cocont}}(\widehat{A},C)
> \simeq
> \mathcal{V}\text{-}\mathsf{Cat}(A,C)
> ```
>
> を与える。

左辺は小さい重み付き余極限を保存する豊穣函手と豊穣自然変換からなる豊穣函手圏である。
この同値は、$`\widehat{A}`$ が $`A`$ の **豊穣自由余完備化** であることを表す。

## 米田拡張の公式

$`F\colon A\to C`$ に対し、上の同値で $`F`$ に対応する余極限保存豊穣函手を $`\widehat{F}\colon\widehat{A}\to C`$ と書く。
$`C`$ がテンソル化されているとき、$`\widehat{F}`$ は各前層 $`X`$ において

```math
\widehat{F}(X)
\cong
\int^{a\in A}X(a)\odot F(a)
```

と計算できる。
この式は、前層 $`X`$ を表現可能前層の重み付き余極限として表示し、その表示に $`\widehat{F}`$ を適用したものである。

$`\mathcal{V}=\mathsf{Set}`$ の場合、テンソル $`X(a)\odot F(a)`$ は $`F(a)`$ の $`X(a)`$ 個の余積であり、

```math
\widehat{F}(X)
\cong
\int^{a\in A}X(a)\cdot F(a)
```

となる。

## Kan 拡張との関係

米田埋め込みに沿う左 Kan 拡張 $`\operatorname{Lan}_yF`$ が存在するとき、これは $`\widehat{F}`$ に一致する。
したがって、前層圏は豊穣左 Kan 拡張を計算する標準的な舞台となる。

$`A`$ が大きい場合、全前層からなる函手圏はサイズの問題を生じ得る。
この場合には、通常、表現可能前層の小さい重み付き余極限として得られる小前層へ対象を制限して自由余完備化を定式化する。

豊穣米田埋め込みによる前層の表示は [豊穣米田の補題](./enriched_yoneda_lemma.md) を、左 Kan 拡張の普遍性は [豊穣 Kan 拡張](./enriched_kan_extension.md) を参照されたい。
