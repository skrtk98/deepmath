---
tags:
  - 代数学/群論
  - 双対性
  - 逆元
  - 同型
---

# 反対群

## 定義

> [!definition] 反対群
> 群 $`G`$ に対して、反対モノイド $`G^{\mathrm{op}}`$ を $`G`$ の **反対群** (*opposite group*) という。
> すなわち、$`G^{\mathrm{op}}`$ の積は $`a\ast b=ba`$ で定める。

## 性質

写像
```math
G\longrightarrow G^{\mathrm{op}},\qquad g\longmapsto g^{-1}
```
は群同型である。

実際、任意の $`g,h\in G`$ に対して、$`(gh)^{-1}=h^{-1}g^{-1}`$ であるから、逆元写像は $`G`$ の積を $`G^{\mathrm{op}}`$ の積に保つ。

したがって、任意の群はその反対群と同型である。
