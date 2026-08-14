---
tags:
  - 代数学/環論/体論
  - 部分構造
  - 生成
---

# 体の拡大

## 定義

> [!definition] 体の拡大
> 体 $`K`$ が体 $`L`$ の部分体であるとき、組 $`L/K`$ を **体の拡大** (*field extension*) という。
> このとき、$`L`$ を $`K`$ の**拡大体**、$`K`$ を $`L/K`$ の**基礎体**という。

体の拡大 $`L/K`$ において、$`K\subseteq M\subseteq L`$ を満たす部分体 $`M`$ を **中間体** (*intermediate field*) という。

## 例

包含 $`\mathbb{Q}\subseteq\mathbb{R}`$ は体の拡大 $`\mathbb{R}/\mathbb{Q}`$ を与える。

また、$`\mathbb{R}\subseteq\mathbb{C}`$ は体の拡大 $`\mathbb{C}/\mathbb{R}`$ を与える。

後者では $`\mathbb{Q}`$ は $`\mathbb{C}/\mathbb{R}`$ の中間体ではなく、$`\mathbb{C}/\mathbb{Q}`$ の中間体である。

## 関連する概念

体の拡大 $`L/K`$ では、$`L`$ は $`K`$ をスカラーとするベクトル空間となる。

このベクトル空間の次元を拡大次数といい、$`[L:K]`$ と表す。

拡大次数が有限である拡大を有限次拡大という。

## 塔の法則

中間体 $`K\subseteq M\subseteq L`$ に対して、$`L/K`$ が有限次拡大ならば

```math
[L:K]=[L:M][M:K]
```

が成り立つ。
これは、$`L`$ の $`M`$-基底と $`M`$ の $`K`$-基底の積を取ることにより、$`L`$ の $`K`$-基底が得られることによる。
