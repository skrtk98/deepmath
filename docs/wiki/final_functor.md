---
tags:
  - 圏論
  - 函手
  - 極限と余極限
  - コンマ圏
---

# 終函手

終函手は、余極限を計算する添字圏を置き換えても結果を変えない函手である。

## 定義

> [!definition] 終函手
> 函手 $`u\colon I\to J`$ が **終函手** であるとは、任意の $`j\in J`$ に対してコンマ圏 $`(j\mathbin{\downarrow}u)`$ が空でなく連結であることである。

双対的に、各 $`j`$ について $`(u\mathbin{\downarrow}j)`$ が空でなく連結であるとき、$`u`$ を始函手という。

## 余極限との関係

$`u\colon I\to J`$ が終函手であり、$`F\colon J\to\mathcal{C}`$ の余極限が存在するとする。
このとき、$`F\circ u`$ の余極限も存在し、標準的な同型

```math
\operatorname*{colim}_{I}(F\circ u)
\cong
\operatorname*{colim}_{J}F
```

が成り立つ。

始函手については、同様に極限が保存される。
コンマ圏については [コンマ圏](./comma_category.md) を参照されたい。
