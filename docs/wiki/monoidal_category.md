---
tags:
  - 圏論/モノイダル圏論
  - テンソル積
  - 自然同型
  - コヒーレンス
---

# モノイダル圏

モノイダル圏は、圏に対象と射を並べるためのテンソル積と、その単位対象を与える構造である。

テンソル積は通常、等号で結合的ではない。

そのずれを結合子と単位子で管理する。

## 定義

> [!definition] モノイダル圏
> **モノイダル圏** (*monoidal category*) とは、圏 $`\mathcal{C}`$、函手 $`\otimes\colon\mathcal{C}\times\mathcal{C}\to\mathcal{C}`$、単位対象 $`I`$、および次の自然同型からなる。
>
> - 結合子：$`\alpha_{X,Y,Z}\colon(X\otimes Y)\otimes Z\to X\otimes(Y\otimes Z)`$。
> - 左単位子：$`\lambda_X\colon I\otimes X\to X`$。
> - 右単位子：$`\rho_X\colon X\otimes I\to X`$。
>
> これらは五角形公理と三角形公理を満たす。

五角形公理は、四対象のテンソル積に異なる順序で結合子を適用しても同じ射が得られることを要請する。

```latex {cmd=true latex_zoom=180% hide=true}
\documentclass{standalone}
\usepackage{amsmath,mathtools}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=2.1,yscale=1.6]
  \node (a) at (0,1) {$((W\otimes X)\otimes Y)\otimes Z$};
  \node (b) at (1.7,1) {$(W\otimes(X\otimes Y))\otimes Z$};
  \node (c) at (3.4,1) {$W\otimes((X\otimes Y)\otimes Z)$};
  \node (d) at (0.85,0) {$(W\otimes X)\otimes(Y\otimes Z)$};
  \node (e) at (2.55,0) {$W\otimes(X\otimes(Y\otimes Z))$};
  \draw[->] (a) -- node[above,scale=.7] {$\alpha_{W,X,Y}\otimes1$} (b);
  \draw[->] (b) -- node[above,scale=.7] {$\alpha_{W,X\otimes Y,Z}$} (c);
  \draw[->] (a) -- node[left,scale=.7] {$\alpha_{W\otimes X,Y,Z}$} (d);
  \draw[->] (d) -- node[below,scale=.7] {$\alpha_{W,X,Y\otimes Z}$} (e);
  \draw[->] (c) -- node[right,scale=.7] {$1\otimes\alpha_{X,Y,Z}$} (e);
\end{tikzpicture}
\end{document}
```

三角形公理は、結合子と二つの単位子が両立することを要請する。

```latex {cmd=true latex_zoom=180% hide=true}
\documentclass{standalone}
\usepackage{amsmath,mathtools}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=2.2,yscale=1.5]
  \node (a) at (0,1) {$(X\otimes I)\otimes Y$};
  \node (b) at (2,1) {$X\otimes(I\otimes Y)$};
  \node (c) at (1,0) {$X\otimes Y$};
  \draw[->] (a) -- node[above,scale=.8] {$\alpha_{X,I,Y}$} (b);
  \draw[->] (a) -- node[left,scale=.8] {$\rho_X\otimes1_Y$} (c);
  \draw[->] (b) -- node[right,scale=.8] {$1_X\otimes\lambda_Y$} (c);
\end{tikzpicture}
\end{document}
```

これらの公理により、有限個の対象のテンソル積について、括弧の付け方を結合子で整合的に比較できる。

## 例

集合の圏 $`\mathsf{Set}`$ は、直積 $`\times`$ と一点集合を単位対象としてモノイダル圏となる。

可換環 $`R`$ 上の加群の圏 $`R\text{-}\mathsf{Mod}`$ は、テンソル積 $`\otimes_R`$ と $`R`$ を単位対象としてモノイダル圏となる。

体 $`k`$ 上のベクトル空間の圏 $`\mathsf{Vect}_k`$ は、$`\otimes_k`$ と $`k`$ によりモノイダル圏となる。

## 関連する構造

結合子と単位子が恒等射であるモノイダル圏を厳格モノイダル圏という。

対称性または組紐構造を加えると、テンソル積の二因子を交換する射を整合的に扱える。

モノイダル圏は、豊穣圏の基底を与える。
