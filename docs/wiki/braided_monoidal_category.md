---
tags:
  - 圏論
  - モノイダル圏
  - 組紐
---

# 組紐付きモノイダル圏

テンソル積の因子を自然に交換でき、その交換が結合子と整合するとき、モノイダル圏は組紐付きであるという。

## 定義

> [!definition] 組紐
> モノイダル圏 $`\mathcal{M}`$ の組紐とは、自然同型 $`\beta_{X,Y}\colon X\otimes Y\to Y\otimes X`$ の族であって、二つの六角形公理を満たすものである。

六角形公理は、三つの因子を交換する二通りの手順が結合子を介して一致することを要求する。

```tikz
\begin{tikzcd}[column sep=large, row sep=large]
(X\otimes Y)\otimes Z \arrow[r] \arrow[d] & X\otimes(Y\otimes Z) \arrow[d] \\
(Y\otimes X)\otimes Z \arrow[d] & (Y\otimes Z)\otimes X \arrow[d] \\
Y\otimes(X\otimes Z) \arrow[r] & Y\otimes(Z\otimes X)
\end{tikzcd}
```

$`\mathsf{Vect}_k`$ の交換写像 $`v\otimes w\mapsto w\otimes v`$ は組紐を与える。
