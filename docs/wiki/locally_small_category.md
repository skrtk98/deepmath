---
tags:
  - 圏論
  - Hom
  - 集合論
  - サイズ
---

# 局所小圏

圏全体の対象が真類であっても、二つの対象の間の射を集合として扱える場合が多い。
この局所的な集合性を表す条件が **局所小性** である。

## 定義

> [!definition] 局所小圏
> 圏 $`\mathcal{C}`$ が **局所小** (*locally small*) であるとは、任意の対象 $`A,B\in\operatorname{Ob}(\mathcal{C})`$ に対して Hom 類
>
> ```math
> \mathcal{C}(A,B)
> ```
>
> が集合であることをいう。

小圏ならば局所小である。
逆は一般には成り立たない。
局所小性は対象全体の大きさを制限しないので、大きな圏にも適用できる。

## 例

集合と写像の圏 $`\mathsf{Set}`$ は局所小である。
二つの集合 $`A,B`$ に対し、$`\mathsf{Set}(A,B)`$ は写像 $`A\to B`$ の集合である。

同じ理由で、群と群準同型の圏 $`\mathsf{Grp}`$、環と環準同型の圏 $`\mathsf{Ring}`$、位相空間と連続写像の圏 $`\mathsf{Top}`$ は局所小である。
これらはいずれも対象の全体が真類であるため、通常は小圏ではない。

## Hom 函手

局所小圏 $`\mathcal{C}`$ と対象 $`A`$ を固定すると、Hom は集合値函手

```math
\mathcal{C}(A,-)\colon\mathcal{C}\longrightarrow\mathsf{Set},
\qquad
\mathcal{C}(-,A)\colon\mathcal{C}^{\mathrm{op}}\longrightarrow\mathsf{Set}
```

を定める。
前者は射 $`f\colon B\to C`$ に $`g\mapsto f\circ g`$ を対応させ、後者は $`f\colon B\to C`$ に $`h\mapsto h\circ f`$ を対応させる。
局所小性により、これらの値は実際に集合となる。

表現可能函手、[自然変換](./natural_transformation.md)、および米田の補題は、この Hom 函手を集合値函手として用いる。
反対圏 $`\mathcal{C}^{\mathrm{op}}`$ の定義については [反対圏](./opposite_category.md) を参照されたい。

> [!note]
> 大小の扱いは採用する集合論的基礎づけに依存する。
> Grothendieck 宇宙を用いる場合には、どの宇宙に関して小さいかを指定する。
