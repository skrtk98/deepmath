---
tags:
  - 圏論/高次圏論
  - 普遍性
  - 随伴
  - Kan 拡張
---

# 2 圏における普遍的性質

2 圏では、対象と 1 射に加えて 1 射の間の 2 射を比較する。
このため普遍性は、一意な因子化ではなく、因子化を与える Hom 圏の同値として記述される。

以下では厳密 2 圏 $`\mathcal{K}`$ を用いる。
双圏では、式に現れる合成は結合子と単位子を介して解釈し、等式は指定された可逆 2 射によるコヒーレンスへ置き換える。

## 2 圏における随伴

対象 $`A,B`$ と 1 射 $`F\colon A\to B`$、$`G\colon B\to A`$ に対し、2 射

```math
\eta\colon1_A\Rightarrow GF,
\qquad
\varepsilon\colon FG\Rightarrow1_B
```

が三角恒等式を満たすとき、$`F`$ は $`G`$ の左随伴である。

```latex {cmd=true latex_zoom=190% hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=1.45,yscale=1.15]
  \node (f) at (0,1) {$F$};
  \node (fgf) at (1.6,1) {$FGF$};
  \node (f2) at (.8,0) {$F$};
  \draw[->] (f) -- node[above] {$F\eta$} (fgf);
  \draw[->] (fgf) -- node[right] {$\varepsilon F$} (f2);
  \draw[->] (f) -- node[left] {$1_F$} (f2);
\end{tikzpicture}
\qquad
\begin{tikzpicture}[xscale=1.45,yscale=1.15]
  \node (g) at (0,1) {$G$};
  \node (gfg) at (1.6,1) {$GFG$};
  \node (g2) at (.8,0) {$G$};
  \draw[->] (g) -- node[above] {$\eta G$} (gfg);
  \draw[->] (gfg) -- node[right] {$G\varepsilon$} (g2);
  \draw[->] (g) -- node[left] {$1_G$} (g2);
\end{tikzpicture}
\end{document}
```

図の可換性は、$`(\varepsilon F)\circ(F\eta)=1_F`$ および $`(G\varepsilon)\circ(\eta G)=1_G`$ を表す。
通常の圏における随伴の図式と定義は [随伴函手](./adjoint_functor.md) を参照されたい。

## 2 圏における左 Kan 拡張

1 射 $`K\colon C\to D`$ と $`E\colon C\to U`$ に対し、$`E`$ の $`K`$ に沿う **左 Kan 拡張** は、1 射 $`L\colon D\to U`$ と 2 射 $`\eta\colon E\Rightarrow LK`$ の組である。

> [!definition] 左 Kan 拡張の普遍性
> 組 $`(L,\eta)`$ が左 Kan 拡張であるとは、任意の 1 射 $`S\colon D\to U`$ に対して、$`\eta`$ との鉛直合成で定まる函手
>
> ```math
> \mathcal{K}(D,U)(L,S)
> \longrightarrow
> \mathcal{K}(C,U)(E,SK)
> ```
>
> が圏同値となることである。

これは、2 射 $`E\Rightarrow SK`$ が本質的に一意な 2 射 $`L\Rightarrow S`$ を通じて $`\eta`$ から因子化することを表す。
右 Kan 拡張は 2 射の向きと Hom 圏を反転して双対的に定義される。

## コンマ対象

1 射 $`F\colon A\to C`$ と $`G\colon B\to C`$ に対する **コンマ対象** は、対象 $`F\downarrow G`$、射影 1 射 $`P\colon F\downarrow G\to A`$、$`Q\colon F\downarrow G\to B`$、および 2 射 $`\theta\colon FP\Rightarrow GQ`$ からなる。

```latex {cmd=true latex_zoom=190% hide=true}
\documentclass{standalone}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=1.55,yscale=1.25]
  \node (x) at (0,0) {$X$};
  \node (a) at (1.5,1) {$A$};
  \node (b) at (1.5,-1) {$B$};
  \node (c) at (3,0) {$C$};
  \draw[->] (x) -- node[above left] {$p$} (a);
  \draw[->] (x) -- node[below left] {$q$} (b);
  \draw[->] (a) -- node[above right] {$F$} (c);
  \draw[->] (b) -- node[below right] {$G$} (c);
  \draw[->,double] (1.72,.66) to[bend left=32] node[right] {$\alpha$} (1.72,-.66);
\end{tikzpicture}
\end{document}
```

普遍性は、任意の $`X`$ に対して $`\mathcal{K}(X,F\downarrow G)`$ が、上図のような組 $`(p,q,\alpha\colon Fp\Rightarrow Gq)`$ からなる圏と同値であることとして表される。
この同値は射影と 2 射 $`\theta`$ により自然に定まる。

2 射 $`\theta`$ が可逆であるコンマ対象を **iso-comma 対象** という。
iso-comma 対象は、2-射まで含めて引き戻しを比較する際に用いられる。

通常の圏における普遍射は [普遍性](./universal_property.md) を、コンマ圏は [コンマ圏](./comma_category.md) を参照されたい。
