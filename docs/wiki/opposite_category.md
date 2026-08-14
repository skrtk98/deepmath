---
tags:
  - 圏論
  - 双対性
  - 合成
---

# 反対圏

圏のすべての射の向きを反転すると、合成の順序も反転する。
この操作で得られる圏を **反対圏** (*opposite category*) といい、双対的な主張を統一的に表すために用いる。

## 定義

> [!definition] 反対圏
> 圏 $`\mathcal{C}`$ に対し、**反対圏** $`\mathcal{C}^{\mathrm{op}}`$ を次で定める。
>
> - $`\operatorname{Ob}(\mathcal{C}^{\mathrm{op}})=\operatorname{Ob}(\mathcal{C})`$ とする。
> - 任意の対象 $`A,B`$ に対して、$`\mathcal{C}^{\mathrm{op}}(A,B)=\mathcal{C}(B,A)`$ とする。
> - $`\mathcal{C}^{\mathrm{op}}`$ における合成は、$`\mathcal{C}`$ における合成を逆順に用いて定める。

$`\mathcal{C}`$ の射 $`f\colon A\to B`$ は、$`\mathcal{C}^{\mathrm{op}}`$ ではしばしば $`f^{\mathrm{op}}\colon B\to A`$ と書く。
$`f\colon A\to B`$ と $`g\colon B\to C`$ に対し、反対圏の合成は

```math
f^{\mathrm{op}}\circ g^{\mathrm{op}}=(g\circ f)^{\mathrm{op}}
```

である。
この定め方により、結合律と恒等射の条件は [圏](./category.md) $`\mathcal{C}`$ の対応する条件から従う。

## 例

前順序 $`(P,\leq)`$ を、$`x\leq y`$ のときただ一つの射 $`x\to y`$ がある圏とみなす。
この圏の反対圏は、逆向きの前順序 $`(P,\geq)`$ に対応する。

集合の圏 $`\mathsf{Set}`$ の反対圏では、射の向きだけが反転する。
これは通常の集合と写像の圏そのものではないが、余積、始対象、エピ射などを積、終対象、モノ射と対にして扱う際の記法を与える。

## 二重反対と双対原理

反対圏を二度とると、対象と射の向きが元に戻る。
したがって

```math
(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}}=\mathcal{C}
```

が、対象と射を同一視する標準的な定義の下で成り立つ。
より抽象的な実現では、この同一視は自然同型として表す。

圏に関する命題から、すべての射を反転し、始と終、積と余積、モノ射とエピ射のような対応する概念を交換して得られる命題を双対命題という。
この操作は形式的には $`\mathcal{C}`$ を $`\mathcal{C}^{\mathrm{op}}`$ に置き換えることである。
