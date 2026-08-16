---
tags:
  - 圏論/高次圏論
  - 高次圏
  - Segal 圏
  - 単体的対象
---

# Segal 型高次圏

Segal 条件は、高次の合成を単体的データによって同値として記述する条件である。

## Segal 条件

単体対象 $`A\colon\Delta^{\mathrm{op}}\to\mathcal{M}`$ に対し、各 $`n\geq2`$ の Segal 写像

```math
A_n\longrightarrow
A_1\times_{A_0}\cdots\times_{A_0}A_1
```

が同値であるとき、$`A`$ は **Segal 条件** を満たすという。
右辺には $`n`$ 個の $`A_1`$ が現れる。
この条件は、$`n`$ 段の合成を 1 段の合成の列から復元できることを表す。

## モデル

Segal 圏は、対象集合を離散的に固定した弱い圏のモデルである。
Segal 空間では、同値射を適切に検出する完全性条件を追加する。

通常圏の nerve は厳密な Segal 条件を満たす。
位相空間値の Segal データはループ空間と delooping の理論に現れる。
高次圏のモデル比較については [高次圏論](./higher_category_theory.md) を参照されたい。
