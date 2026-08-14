---
tags:
  - 圏論
  - 構造保存
  - 合成
  - 反変性
---

# 函手

函手は、圏の対象と射を同時に対応させ、恒等射と合成を保つ構造である。

この条件により、圏における可換図式を別の圏の可換図式へ移せる。

## 定義

> [!definition] 共変函手
> 圏 $`\mathcal{C},\mathcal{D}`$ の間の **共変函手** $`F\colon\mathcal{C}\to\mathcal{D}`$ とは、次のデータからなる。
>
> - 各対象 $`X`$ に対する対象 $`F(X)`$。
> - 各射 $`f\colon X\to Y`$ に対する射 $`F(f)\colon F(X)\to F(Y)`$。
>
> これらは $`F(1_X)=1_{F(X)}`$ および $`F(g\circ f)=F(g)\circ F(f)`$ を満たす。

> [!definition] 反変函手
> $`\mathcal{C}^{\mathrm{op}}\to\mathcal{D}`$ の共変函手を、$`\mathcal{C}`$ から $`\mathcal{D}`$ への **反変函手** という。

反変函手は、射 $`f\colon X\to Y`$ を $`F(f)\colon F(Y)\to F(X)`$ へ送る。

## 可換図式の保存

射 $`f\colon X\to Y`$、$`g\colon Y\to Z`$、$`h\colon X\to Z`$ が $`h=g\circ f`$ を満たすとする。

函手 $`F`$ は次の可換三角形を可換三角形へ送る。

```latex {cmd=true latex_zoom=200% hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=1.5,yscale=1.3]
  \node (x) at (0,1) {$X$};
  \node (y) at (1.5,1) {$Y$};
  \node (z) at (.75,0) {$Z$};
  \draw[->] (x) -- node[above] {$f$} (y);
  \draw[->] (y) -- node[right] {$g$} (z);
  \draw[->] (x) -- node[left] {$h$} (z);
\end{tikzpicture}
\qquad$\longmapsto$\qquad
\begin{tikzpicture}[xscale=1.5,yscale=1.3]
  \node (x) at (0,1) {$F(X)$};
  \node (y) at (1.5,1) {$F(Y)$};
  \node (z) at (.75,0) {$F(Z)$};
  \draw[->] (x) -- node[above] {$F(f)$} (y);
  \draw[->] (y) -- node[right] {$F(g)$} (z);
  \draw[->] (x) -- node[left] {$F(h)$} (z);
\end{tikzpicture}
\end{document}
```

右側の可換性は $`F(h)=F(g\circ f)=F(g)\circ F(f)`$ による。

## 例

群から台集合を取る操作は、忘却函手 $`\mathsf{Grp}\to\mathsf{Set}`$ を定める。

集合にその集合を生成元とする自由群を対応させる操作は、自由群函手 $`\mathsf{Set}\to\mathsf{Grp}`$ を定める。

冪集合は、逆像を通じて反変函手 $`\mathcal{P}\colon\mathsf{Set}^{\mathrm{op}}\to\mathsf{Set}`$ を定める。

局所小圏 $`\mathcal{C}`$ と対象 $`A`$ に対して、$`\mathcal{C}(A,-)`$ および $`\mathcal{C}(-,A)`$ はそれぞれ共変および反変の Hom 函手である。

## 性質

函手は合成でき、各圏の恒等函手を単位元として、同じ始域と終域を持つ函手を対象とする函手圏を定める。

函手 $`F\colon\mathcal{C}\to\mathcal{D}`$ が **忠実** であるとは、各 Hom 集合上の写像が単射であることである。

$`F`$ が **充満** であるとは、各 Hom 集合上の写像が全射であることである。

$`F`$ が **本質的全射** であるとは、$`\mathcal{D}`$ の各対象がある $`F(X)`$ と同型であることである。

充満、忠実、本質的全射である函手は圏同値を与える。
