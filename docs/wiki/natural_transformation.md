---
tags:
  - 圏論
  - 函手
  - 可換図式
  - 構造保存
---

# 自然変換

自然変換は、同じ始域と終域を持つ二つの函手を、対象ごとの射の族として比較する構造である。

射の族には、始域圏のすべての射に対する整合性を要請する。

## 定義

> [!definition] 自然変換
> 函手 $`F,G\colon\mathcal{C}\to\mathcal{D}`$ の間の **自然変換** $`\alpha\colon F\Rightarrow G`$ とは、各対象 $`X\in\mathcal{C}`$ に対する射 $`\alpha_X\colon F(X)\to G(X)`$ の族であって、任意の射 $`f\colon X\to Y`$ に対して
> ```math
> G(f)\circ\alpha_X=\alpha_Y\circ F(f)
> ```
> を満たすものである。

この等式を自然性条件という。

```latex {cmd=true latex_zoom=220% hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=1.5,yscale=1.3]
  \node (fx) at (0,1) {$F(X)$};
  \node (fy) at (1.5,1) {$F(Y)$};
  \node (gx) at (0,0) {$G(X)$};
  \node (gy) at (1.5,0) {$G(Y)$};
  \draw[->] (fx) -- node[above] {$F(f)$} (fy);
  \draw[->] (gx) -- node[below] {$G(f)$} (gy);
  \draw[->] (fx) -- node[left] {$\alpha_X$} (gx);
  \draw[->] (fy) -- node[right] {$\alpha_Y$} (gy);
\end{tikzpicture}
\end{document}
```

## 合成

自然変換 $`F\xRightarrow{\alpha}G\xRightarrow{\beta}H`$ の **垂直合成** は、$`(\beta\circ\alpha)_X=\beta_X\circ\alpha_X`$ により定める。

函手 $`F,F'\colon\mathcal{C}\to\mathcal{D}`$ と $`G,G'\colon\mathcal{D}\to\mathcal{E}`$、自然変換 $`\alpha\colon F\Rightarrow F'`$、$`\beta\colon G\Rightarrow G'`$ に対して、**水平合成** $`\beta\ast\alpha\colon GF\Rightarrow G'F'`$ を
```math
(\beta\ast\alpha)_X=\beta_{F'(X)}\circ G(\alpha_X)
=G'(\alpha_X)\circ\beta_{F(X)}
```
により定める。

## 例と函手圏

群 $`G`$ からその可換化 $`G_{\mathrm{ab}}`$ への商写像は、群の恒等函手から可換化函手への自然変換を定める。

函手を対象、自然変換を射とすると、圏 $`\mathcal{C},\mathcal{D}`$ に対して函手圏 $`[\mathcal{C},\mathcal{D}]`$ が定まる。
