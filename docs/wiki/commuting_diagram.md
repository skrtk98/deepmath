---
tags:
  - 圏論
  - 可換図式
  - 合成
  - 等式
---

# 可換図式

図式は対象を頂点、射を辺として、射の関係を視覚的に表す。

可換性は、同じ始点と終点を持つ経路の合成射が一致することを表す。

## 定義

> [!definition] 可換図式
> 圏における図式が **可換** であるとは、同じ始点と終点を持つ任意の二つの経路が定める合成射が一致することである。

可換三角形では、$`h=g\circ f`$ が可換性を表す。

可換四角形では、$`v\circ f=g\circ u`$ が可換性を表す。

```latex {cmd=true latex_zoom=190% hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=1.5,yscale=1.2]
  \node (a) at (0,1) {$A$};
  \node (b) at (1.5,1) {$B$};
  \node (c) at (0,0) {$C$};
  \node (d) at (1.5,0) {$D$};
  \draw[->] (a) -- node[above] {$f$} (b);
  \draw[->] (a) -- node[left] {$u$} (c);
  \draw[->] (b) -- node[right] {$v$} (d);
  \draw[->] (c) -- node[below] {$g$} (d);
\end{tikzpicture}
\end{document}
```

## 注意

ループを含む図式が可換であるならば、そのループが表す合成射は恒等射に等しい。

```math
A\xrightarrow{f}B\rightrightarrows^{g}_{h}C
```
という fork 図式全体を可換と呼ぶ場合は、通常 $`g=h`$ を意味する。

等化子に現れる条件 $`g\circ f=h\circ f`$ は、図式全体の可換性とは異なる条件である。

## 函手との関係

函手は合成と恒等射を保つため、可換図式を可換図式へ送る。

グラフから生成される自由圏を用いれば、図式はその自由圏からの函手として、可換性は平行射の像が一致する条件として定式化できる。
