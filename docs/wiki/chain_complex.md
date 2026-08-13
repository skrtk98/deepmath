---
tags:
  - 代数学/ホモロジー代数
  - 複体
  - 完全性
  - 商構成
---

# 鎖複体

## 定義

> [!definition] 鎖複体
> 加群の列 $`(C_n)_{n\in\mathbb{Z}}`$ と線形写像 $`d_n\colon C_n\to C_{n-1}`$ が、任意の $`n`$ について $`d_{n-1}\circ d_n=0`$ を満たすとき、組 $`(C_\bullet,d)`$ を鎖複体という。

> [!definition] ホモロジー
> 鎖複体の $`n`$ 次ホモロジーは、
> ```math
> H_n(C_\bullet)=\ker d_n/\operatorname{im}d_{n+1}
> ```
> で定める。

条件 $`d_n\circ d_{n+1}=0`$ により、$`\operatorname{im}d_{n+1}\subseteq\ker d_n`$ が成り立つため、この商加群は定義される。
