---
tags:
  - 圏論
  - 普遍性
  - 可換図式
  - 函手
---

# 極限

図式に含まれる複数の条件を同時に満たす対象を、因子化の一意性で特徴付ける構成が極限である。
積、等化子、引き戻しは、この一つの定義の異なる形である。

## 定義

図式 $`D\colon\mathcal{J}\to\mathcal{C}`$ と対象 $`A`$ に対し、$`A`$ を頂点とする**錐**とは、射の族 $`\lambda_j\colon A\to D(j)`$ であって、任意の $`u\colon j\to k`$ について $`D(u)\circ\lambda_j=\lambda_k`$ を満たすものである。

> [!definition] 極限
> 図式 $`D\colon\mathcal{J}\to\mathcal{C}`$ の **極限** とは、$`D`$ への錐の圏における終対象である。
> すなわち、錐 $`(L\xrightarrow{p_j}D(j))`$ であって、任意の錐 $`(A\xrightarrow{f_j}D(j))`$ に対して一意な射 $`\bar f\colon A\to L`$ が存在し、$`p_j\circ\bar f=f_j`$ をすべての $`j`$ について満たすものをいう。

この普遍性から、極限は存在すれば同型を除いて一意である。
また、錐の集合を対応させる函手 $`\operatorname{Cone}(-,D)\colon\mathcal{C}^{\mathrm{op}}\to\mathsf{Set}`$ が表現可能であることと、$`D`$ が極限をもつことは同値である。

## 例と保存

離散な二点図式の極限は二項積である。
二本の平行射の極限は等化子であり、スパン $`A\to C\leftarrow B`$ の極限は引き戻しである。
空図式の極限は [終対象](./terminal_object.md) である。

右随伴函手は、存在する極限を保存する。
さらに、小積と等化子をもつ圏は、すべての小さい図式の極限をもつ。
