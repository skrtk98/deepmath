---
tags:
  - 圏論/高次圏論
  - 2-圏
  - 双圏
  - 函手
---

# 擬函手

擬函手は、双圏の合成と単位を等号ではなく可逆2-射によって保存する写像である。

## 定義

> [!definition] 擬函手
> 双圏 $`\mathcal{B},\mathcal{C}`$ の間の **擬函手** $`F\colon\mathcal{B}\to\mathcal{C}`$ は、対象写像と各 Hom 圏の函手
>
> ```math
> F_{A,B}\colon\mathcal{B}(A,B)
> \longrightarrow
> \mathcal{C}(FA,FB)
> ```
>
> に加え、合成可能な 1-射 $`f,g`$ に対する可逆2-射
>
> ```math
> Fg\circ Ff\Rightarrow F(g\circ f)
> ```
>
> および各対象 $`A`$ に対する可逆2-射
>
> ```math
> 1_{FA}\Rightarrow F(1_A)
> ```
>
> を備える。
> これらには、三重合成と単位に関する標準的なコヒーレンス条件を課す。

比較2-射が恒等2-射である擬函手は厳密2-函手である。
双圏では結合律が同型としてしか与えられないため、擬函手が自然な写像の概念となる。
