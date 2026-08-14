---
tags:
  - 圏論
  - 自然同型
  - 普遍性
  - 函手
---

# 随伴函手

随伴は、二つの函手の間にある Hom 集合の自然な対応である。

自由構成と忘却、積と指数のような普遍性は、この対応として記述される。

## Hom 集合による定義

> [!definition] 随伴
> 函手 $`L\colon\mathcal{C}\to\mathcal{D}`$ と $`R\colon\mathcal{D}\to\mathcal{C}`$ について、各 $`A\in\mathcal{C}`$、$`B\in\mathcal{D}`$ に対する全単射
> ```math
> \mathcal{D}(L(A),B)\cong\mathcal{C}(A,R(B))
> ```
> が $`A`$ と $`B`$ に自然に存在するとき、$`L`$ は $`R`$ の左随伴であるという。
> この関係を $`L\dashv R`$ と表す。

## 単位と余単位

随伴 $`L\dashv R`$ は自然変換
```math
\eta\colon1_{\mathcal{C}}\Rightarrow RL,
\qquad
\varepsilon\colon LR\Rightarrow1_{\mathcal{D}}
```
を定める。

$`\eta`$ を単位、$`\varepsilon`$ を余単位という。

逆に、この二つの自然変換が次の三角恒等式を満たすとき、随伴が定まる。

```latex {cmd=true latex_zoom=190% hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=1.5,yscale=1.25]
  \node (a) at (0,1) {$L$};
  \node (b) at (1.5,1) {$LRL$};
  \node (c) at (.75,0) {$L$};
  \draw[->] (a) -- node[above] {$L\eta$} (b);
  \draw[->] (b) -- node[right] {$\varepsilon L$} (c);
  \draw[->] (a) -- node[left] {$1_L$} (c);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[xscale=1.5,yscale=1.25]
  \node (a) at (0,1) {$R$};
  \node (b) at (1.5,1) {$RLR$};
  \node (c) at (.75,0) {$R$};
  \draw[->] (a) -- node[above] {$\eta R$} (b);
  \draw[->] (b) -- node[right] {$R\varepsilon$} (c);
  \draw[->] (a) -- node[left] {$1_R$} (c);
\end{tikzpicture}
\end{document}
```

## 例

自由群函手 $`F\colon\mathsf{Set}\to\mathsf{Grp}`$ は忘却函手 $`U\colon\mathsf{Grp}\to\mathsf{Set}`$ の左随伴である。

集合 $`A`$ に対して、直積函手 $`-\times A`$ は指数函手 $`(-)^A`$ の左随伴である。

離散位相を与える函手 $`\mathsf{Set}\to\mathsf{Top}`$ は、台集合を取る忘却函手の左随伴である。

## 性質

左随伴は存在すれば自然同型を除いて一意である。

左随伴は存在する余極限を保ち、右随伴は存在する極限を保つ。

随伴は、単位・余単位、普遍射、Hom 集合の自然同型という同値な形式で表現できる。

## 特殊随伴函手定理

特殊随伴函手定理は、極限保存性から左随伴の存在を導く十分条件を与える。

> [!theorem] 特殊随伴函手定理
> 圏 $`\mathcal{C}`$ が完備、局所小、well-powered であり、余生成集合をもつとする。
> 局所小圏 $`\mathcal{D}`$ への函手 $`G\colon\mathcal{C}\to\mathcal{D}`$ が極限を保存するとき、$`G`$ は左随伴をもつ。

ここで well-powered とは、各対象の部分対象の同型類が集合をなすことをいう。
余生成集合とは、射を検出する対象の集合である。
この定理は、右随伴の候補が極限を保存することを示した後に、その左随伴の存在を保証するために用いられる。

双対的に、余完備、局所小、co-well-powered で生成集合をもつ圏からの余極限保存函手について、右随伴の存在を得る形がある。
