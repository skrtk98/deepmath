---
tags:
  - 圏論
  - 函手
  - 自然変換
  - 表現可能性
---

# 米田の補題

局所小圏の対象は、その対象へ入るすべての射を記録する Hom 函手によって表現される。
米田の補題は、Hom 函手からの自然変換を一つの元に対応させる。

## 定理

> [!theorem] 米田の補題
> 局所小圏 $`\mathcal{C}`$、対象 $`X`$、および反変函手 $`F\colon\mathcal{C}^{\mathrm{op}}\to\mathsf{Set}`$ に対して、自然変換の集合 $`\operatorname{Nat}(\mathcal{C}(-,X),F)`$ と集合 $`F(X)`$ の間には自然な全単射が存在する。
> この対応は自然変換 $`\alpha`$ を $`\alpha_X(1_X)`$ に送り、$`x\in F(X)`$ を $`f\colon Y\to X`$ に対して $`F(f)(x)`$ を与える自然変換に送る。

## 系

米田埋め込み $`y\colon\mathcal{C}\to[\mathcal{C}^{\mathrm{op}},\mathsf{Set}]`$、$`X\mapsto\mathcal{C}(-,X)`$ は充満忠実である。
したがって、対象は Hom 函手によって圏論的に特徴付けられる。

この補題は [表現可能函手](./representable_functor.md) の普遍元と表現対象の一意性を与える。
