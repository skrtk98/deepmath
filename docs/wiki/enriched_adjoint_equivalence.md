---
tags:
  - 圏論/豊穣圏論
  - 随伴
  - 同値
  - 自然変換
---

# 豊穣随伴と豊穣同値

豊穣随伴は、二つの豊穣函手の間の普遍性を Hom 対象の同型として表す。
この定義は下部圏における通常の随伴より強く、基底圏に含まれる線形性、順序、または高次射の構造を保持する。

以下で $`\mathcal{V}`$ を [モノイダル圏](./monoidal_category.md)、$`A,B`$ を $`\mathcal{V}`$-圏、$`F\colon A\to B`$ と $`G\colon B\to A`$ を豊穣函手とする。

## 豊穣随伴

> [!definition] 豊穣随伴
> $`F`$ が $`G`$ の **豊穣左随伴** であるとは、各 $`a\in A`$ と $`b\in B`$ に $`\mathcal{V}`$ において自然な同型
>
> ```math
> B(Fa,b)\cong A(a,Gb)
> ```
>
> が存在することである。
> この関係を $`F\dashv G`$ と表す。

この同型から、豊穣自然変換

```math
\eta\colon1_A\Rightarrow GF,
\qquad
\varepsilon\colon FG\Rightarrow1_B
```

が得られる。
ここで $`\eta`$ は単位、$`\varepsilon`$ は余単位である。
逆に、これらの豊穣自然変換が三角恒等式

```math
(\varepsilon F)\circ(F\eta)=1_F,
\qquad
(G\varepsilon)\circ(\eta G)=1_G
```

を満たせば、上の Hom 対象の自然同型が定まる。

## 下部圏との関係

Hom 対象の同型に $`\mathcal{V}(I,-)`$ を適用すると、下部圏の Hom 集合の全単射

```math
B_0(Fa,b)\cong A_0(a,Gb)
```

が得られる。
したがって、豊穣随伴は通常の随伴 $`F_0\dashv G_0`$ を誘導する。

逆向きは一般には成り立たない。
下部圏での全単射が基底圏の射として自然な同型に持ち上がることを、豊穣随伴は追加で要請する。

## 豊穣同値

> [!definition] 豊穣同値
> 豊穣随伴 $`F\dashv G`$ の単位 $`\eta`$ と余単位 $`\varepsilon`$ がともに豊穣自然同型であるとき、$`F`$ は **豊穣同値** を与えるという。

このとき $`G`$ は $`F`$ の豊穣擬逆であり、$`A\simeq B`$ と書く。
豊穣同値は下部圏の圏同値を誘導する。

## 例

$`\mathcal{V}=\mathsf{Set}`$ のとき、豊穣随伴と豊穣同値は通常の随伴函手と圏同値に一致する。

$`\mathcal{V}=2`$ を順序 $`0\leq1`$ と論理積をモノイダル積とするモノイダル順序圏とみなすと、$`2`$-圏は前順序集合である。
この場合の豊穣随伴は Galois 接続であり、

```math
F(a)\leq b
\quad\Longleftrightarrow\quad
a\leq G(b)
```

と表される。

$`\mathcal{V}=\mathsf{Cat}`$ を直積モノイダル圏とすると、$`\mathsf{Cat}`$-圏は厳密 2-圏である。
この場合の豊穣随伴は、2-圏における随伴の Hom 圏同型による定式化に対応する。

通常の随伴の三角恒等式は [随伴函手](./adjoint_functor.md) を、豊穣自然変換の定義は [豊穣自然変換](./enriched_natural_transformation.md) を参照されたい。
