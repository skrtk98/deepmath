---
tags:
  - 圏論
  - 普遍性
  - 因子化
  - 一意性
---

# 普遍性

普遍性は、対象の具体的な構成ではなく、他の対象からの射または他の対象への射の一意な因子化によって対象を特徴付ける。

この特徴付けは同型に不変である。

## 普遍射

> [!definition] 普遍射
> 函手 $`T\colon\mathcal{A}\to\mathcal{B}`$ と対象 $`B\in\mathcal{B}`$ に対して、組 $`(A,\eta\colon B\to T(A))`$ が $`B`$ から $`T`$ への **普遍射** であるとは、任意の射 $`f\colon B\to T(A')`$ に対して、
> ```math
> f=T(u)\circ\eta
> ```
> を満たす一意な射 $`u\colon A\to A'`$ が存在することである。

双対的に、組 $`(A,\varepsilon\colon T(A)\to B)`$ が $`T`$ から $`B`$ への普遍射であるとは、任意の射 $`g\colon T(A')\to B`$ に対して、$`g=\varepsilon\circ T(u)`$ を満たす一意な射 $`u\colon A'\to A`$ が存在することである。

```latex {cmd=true latex_zoom=190% hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=1.5,yscale=1.2]
  \node (b) at (0,1) {$B$};
  \node (ta) at (1.5,1) {$T(A)$};
  \node (tap) at (1.5,0) {$T(A')$};
  \draw[->] (b) -- node[above] {$\eta$} (ta);
  \draw[->] (ta) -- node[right] {$T(u)$} (tap);
  \draw[->] (b) -- node[left] {$f$} (tap);
\end{tikzpicture}
\end{document}
```

## 例と一意性

自由群 $`F(X)`$ は、集合 $`X`$ から忘却函手 $`\mathsf{Grp}\to\mathsf{Set}`$ への普遍射として特徴付けられる。

積、余積、等化子、引き戻しは普遍性の特殊例である。

始対象は空図式の余極限であり、終対象は空図式の極限である。

同じ普遍性を満たす二つの対象は、一意な同型を除いて一致する。

## コンマ圏による特徴付け

組 $`(A,\eta\colon B\to T(A))`$ が $`B`$ から $`T`$ への普遍射であることは、コンマ圏 $`(B\downarrow T)`$ の始対象であることと同値である。

双対的に、$`(A,\varepsilon\colon T(A)\to B)`$ が $`T`$ から $`B`$ への普遍射であることは、$`(T\downarrow B)`$ の終対象であることと同値である。
