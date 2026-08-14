---
tags:
  - 圏論
  - 函手
  - Hom
  - 表現可能性
---

# 表現可能函手

集合値函手がある対象への Hom 函手と自然同型になるとき、その函手を**表現可能**という。
この条件は、函手の値を圏内部の一つの対象と普遍元により記述する。

## 定義

> [!definition] 表現可能函手
> 局所小圏 $`\mathcal{C}`$ と反変函手 $`F\colon\mathcal{C}^{\mathrm{op}}\to\mathsf{Set}`$ に対して、対象 $`A`$ と自然同型 $`F\cong\mathcal{C}(-,A)`$ が存在するとき、$`F`$ は $`A`$ により表現可能であるという。

共変函手 $`G\colon\mathcal{C}\to\mathsf{Set}`$ が $`\mathcal{C}(A,-)`$ と自然同型である場合は、$`A`$ により余表現可能であるという。

## 例と普遍元

$`\mathsf{Set}`$ の恒等函手は一点集合により余表現可能であり、$`\mathrm{Id}_{\mathsf{Set}}\cong\mathsf{Set}(1,-)`$ である。
忘却函手 $`\mathsf{Grp}\to\mathsf{Set}`$ は $`\mathbb{Z}`$ により余表現可能であり、$`\mathsf{Grp}(\mathbb{Z},G)\cong U(G)`$ が成り立つ。

自然同型 $`\phi\colon\mathcal{C}(A,-)\Rightarrow G`$ は、元 $`\phi_A(1_A)\in G(A)`$ により定まる。
この元を普遍元という。
[米田の補題](./yoneda_lemma.md) により、表現対象は存在すれば同型を除いて一意である。
