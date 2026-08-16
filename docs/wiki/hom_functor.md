---
tags:
  - 圏論
  - 函手
  - Hom 集合
  - 表現可能函手
---

# Hom 函手

局所小圏の Hom 集合は、反変と共変の二変数函手としてまとめられる。

## 定義

> [!definition] Hom 函手
> 局所小圏 $`\mathcal{C}`$ の **Hom 函手** とは、函手
>
> ```math
> \operatorname{Hom}_{\mathcal{C}}
> \colon
> \mathcal{C}^{\mathrm{op}}\times\mathcal{C}
> \longrightarrow\mathsf{Set}
> ```
>
> である。
> これは対象対 $`(c,c')`$ を $`\mathcal{C}(c,c')`$ に送り、射 $`f\colon d\to c`$, $`g\colon c'\to d'`$ を
>
> ```math
> q\longmapsto g\circ q\circ f
> ```
>
> による写像 $`\mathcal{C}(c,c')\to\mathcal{C}(d,d')`$ に送る。

## 固定変数版

対象 $`c`$ を固定すると、

```math
\mathcal{C}(c,-)\colon\mathcal{C}\to\mathsf{Set},
\qquad
\mathcal{C}(-,c)\colon\mathcal{C}^{\mathrm{op}}\to\mathsf{Set}
```

が得られる。
後者は表現可能前層であり、米田埋め込みの値である。

第一の函手は存在する極限を集合の極限へ送る。
双対的に、第二の函手は存在する余極限を集合の極限へ送る。
Hom 集合については [Hom 集合](./hom_set.md) を参照されたい。
