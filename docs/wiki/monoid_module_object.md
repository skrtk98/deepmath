---
tags:
  - 圏論/モノイダル圏論
  - モノイダル圏
  - モノイド対象
  - 加群
---

# モノイド対象上の加群対象

モノイド対象上の加群対象は、通常の加群の作用をモノイダル圏の内部で定式化した構造である。

以下で $`(m,\mu,\eta)`$ をモノイダル圏 $`\mathcal{M}`$ のモノイド対象とする。

## 左加群対象

> [!definition] 左加群対象
> **左加群対象**とは、対象 $`n\in\mathcal{M}`$ と作用射
>
> ```math
> a\colon m\otimes n\to n
> ```
>
> の組である。
> この作用は結合律と単位律を満たさなければならない。

結合律は、次の図式の可換性である。

```latex {cmd=true latex_zoom=210% hide=true}
\documentclass{standalone}
\usepackage{mathtools}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=2.55,yscale=1.4]
  \node (a) at (0,1) {$(m\otimes m)\otimes n$};
  \node (b) at (1.9,1) {$m\otimes(m\otimes n)$};
  \node (c) at (0,0) {$m\otimes n$};
  \node (d) at (1.9,0) {$n$};
  \node (e) at (3.8,0) {$m\otimes n$};
  \draw[->] (a) -- node[above,scale=.75] {$\alpha_{m,m,n}$} (b);
  \draw[->] (a) -- node[left,scale=.75] {$\mu\otimes1_n$} (c);
  \draw[->] (c) -- node[below,scale=.75] {$a$} (d);
  \draw[->] (b) -- node[right,scale=.75] {$1_m\otimes a$} (e);
  \draw[->] (e) -- node[below,scale=.75] {$a$} (d);
\end{tikzpicture}
\end{document}
```

単位律は $`a\circ(\eta\otimes1_n)=\lambda_n`$ である。
右加群対象は、作用射 $`n\otimes m\to n`$ を用いて双対的に定める。
これは、逆転モノイダル圏 $`\mathcal{M}^{\mathrm{rev}}`$ における左加群対象とみなせる。

## 作用するモノイダル圏の場合

モノイダル圏 $`\mathcal{M}`$ が圏 $`\mathcal{C}`$ に作用するとは、函手

```math
\odot\colon\mathcal{M}\times\mathcal{C}\to\mathcal{C}
```

と、テンソル積および単位対象との整合的な自然同型が与えられることである。
このとき $`\mathcal{M}`$ のモノイド対象 $`m`$ 上の左加群対象は、対象 $`N\in\mathcal{C}`$ と射 $`m\odot N\to N`$ が、上と同型の結合律および単位律を満たすデータとして定義される。

通常の環 $`R`$ を $`(\mathsf{Ab},\otimes,\mathbb{Z})`$ のモノイド対象とみなすと、左加群対象は通常の左 $`R`$-加群に一致する。
モノイド対象の定義については [モノイド対象と余モノイド対象](./monoid_object.md) を参照されたい。
