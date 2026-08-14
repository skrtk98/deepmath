---
tags:
  - 圏論/豊穣圏論
  - 前層
  - 重み付き極限と余極限
  - 完備化
---

# 豊穣 Cauchy 完成

豊穣 Cauchy 完成は、豊穣圏に絶対重み付き余極限を加える完備化である。
通常の圏では、これは冪等射の分裂を加える Karoubi 完成に一致する。

以下では、$`\mathcal{V}`$ を対称モノイダル閉圏とし、必要な豊穣函手圏と小余極限が存在すると仮定する。
$`A`$ は小さい $`\mathcal{V}`$-圏とする。

## 絶対重みと小射影前層

重み $`W\colon J^{\mathrm{op}}\to\mathcal{V}`$ が **絶対** であるとは、$`W`$-重み付き余極限を保存する豊穣函手がすべての豊穣函手であることである。
すなわち、$`W\star F`$ が存在するとき、任意の豊穣函手 $`H`$ に対して標準射

```math
W\star(HF)\longrightarrow H(W\star F)
```

が同型となる。

前層 $`P\in[A^{\mathrm{op}},\mathcal{V}]`$ が **小射影** であるとは、表現可能な Hom 函手

```math
[A^{\mathrm{op}},\mathcal{V}](P,-)
\colon[A^{\mathrm{op}},\mathcal{V}]
\longrightarrow\mathcal{V}
```

が小さい重み付き余極限を保存することである。
適切な完備性の仮定の下で、小射影前層は絶対重みを与える前層と同値に特徴付けられる。

## 定義

> [!definition] 豊穣 Cauchy 完成
> $`A`$ の **豊穣 Cauchy 完成** $`Q(A)`$ とは、豊穣前層圏 $`[A^{\mathrm{op}},\mathcal{V}]`$ における小射影前層全体がなす充満 $`\mathcal{V}`$-部分圏である。

各表現可能前層 $`y(a)=A(-,a)`$ は小射影である。
したがって、豊穣米田埋め込みは豊穣函手

```math
A\longrightarrow Q(A)
```

として因子化する。

## 普遍性

豊穣圏 $`C`$ が **Cauchy 完備** であるとは、絶対重みによるすべての重み付き余極限をもつことである。

> [!theorem] Cauchy 完成の普遍性
> $`C`$ を Cauchy 完備な $`\mathcal{V}`$-圏とすると、米田埋め込みによる制限は豊穣函手圏の同値
>
> ```math
> \mathcal{V}\text{-}\mathsf{Cat}(Q(A),C)
> \simeq
> \mathcal{V}\text{-}\mathsf{Cat}(A,C)
> ```
>
> を与える。

右辺の豊穣函手は、表現可能前層から得られる絶対重み付き余極限を用いて $`Q(A)`$ へ本質的に一意に延長される。
この意味で $`Q(A)`$ は、$`A`$ を含む Cauchy 完備豊穣圏のうち最小のものである。

## 通常の圏の場合

$`\mathcal{V}=\mathsf{Set}`$ のとき、Cauchy 完備性はすべての冪等射が分裂することと同値である。
ここで射 $`e\colon a\to a`$ が冪等であるとは $`e\circ e=e`$ が成り立つことであり、分裂とは射 $`r\colon a\to b`$ と $`s\colon b\to a`$ が

```math
s\circ r=e,
\qquad
r\circ s=1_b
```

を満たすことである。

この場合の $`Q(A)`$ は Karoubi 完成であり、対象は冪等射の組 $`(a,e)`$ として表せる。
射 $`f\colon(a,e)\to(b,d)`$ は $`A`$ の射 $`f\colon a\to b`$ であって

```math
d\circ f=f=f\circ e
```

を満たすものとする。

小射影前層と Morita 同値の関係は [豊穣小射影と Morita 同値](./enriched_small_projective_morita.md) を参照されたい。
豊穣前層の表現可能前層による表示は [豊穣米田の補題](./enriched_yoneda_lemma.md) を、重み付き余極限の定義は [重み付き余極限](./weighted_colimit_enriched.md) を参照されたい。
