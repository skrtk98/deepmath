---
tags:
  - 圏論/モノイダル圏論
  - モノイダル圏
  - モノイド対象
  - モナド
---

# モノイド対象と余モノイド対象

モノイド対象は、通常のモノイドの乗法と単位をモノイダル圏の内部で定式化した構造である。

以下で $`(\mathcal{M},\otimes,I,\alpha,\lambda,\rho)`$ をモノイダル圏とする。

## モノイド対象

> [!definition] モノイド対象
> **モノイド対象**とは、対象 $`m`$ と射
>
> ```math
> \mu\colon m\otimes m\to m,
> \qquad
> \eta\colon I\to m
> ```
>
> の組である。
> これらは次の結合律と単位律を満たさなければならない。

結合律は、$`m`$ の三重テンソル積から $`m`$ への次の二つの合成が一致することである。

```latex {cmd=true latex_zoom=210% hide=true}
\documentclass{standalone}
\usepackage{mathtools}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=2.4,yscale=1.4]
  \node (a) at (0,1) {$(m\otimes m)\otimes m$};
  \node (b) at (1.8,1) {$m\otimes(m\otimes m)$};
  \node (c) at (0,0) {$m\otimes m$};
  \node (d) at (1.8,0) {$m$};
  \node (e) at (3.6,0) {$m\otimes m$};
  \draw[->] (a) -- node[above,scale=.75] {$\alpha_{m,m,m}$} (b);
  \draw[->] (a) -- node[left,scale=.75] {$\mu\otimes1_m$} (c);
  \draw[->] (c) -- node[below,scale=.75] {$\mu$} (d);
  \draw[->] (b) -- node[right,scale=.75] {$1_m\otimes\mu$} (e);
  \draw[->] (e) -- node[below,scale=.75] {$\mu$} (d);
\end{tikzpicture}
\end{document}
```

単位律は、$`I\otimes m`$ および $`m\otimes I`$ からの二つの積が、それぞれ左単位子および右単位子に一致することである。

```math
\mu\circ(\eta\otimes1_m)=\lambda_m,
\qquad
\mu\circ(1_m\otimes\eta)=\rho_m.
```

## 余モノイド対象と射

**余モノイド対象**は $`\mathcal{M}^{\mathrm{op}}`$ におけるモノイド対象である。
すなわち、余積 $`\delta\colon c\to c\otimes c`$ と余単位 $`\epsilon\colon c\to I`$ が、上の公理を双対化した公理を満たす。

モノイド対象 $`(m,\mu_m,\eta_m)`$ と $`(n,\mu_n,\eta_n)`$ の間の **モノイド射** とは、射 $`f\colon m\to n`$ であって

```math
f\circ\mu_m=\mu_n\circ(f\otimes f),
\qquad
f\circ\eta_m=\eta_n
```

を満たすものである。

## 例

- $`(\mathsf{Set},\times,1)`$ のモノイド対象は通常のモノイドである。
- $`(\mathsf{Top},\times,1)`$ のモノイド対象は位相モノイドである。
- 可換環 $`R`$ に対し、$`(R\text{-}\mathsf{Mod},\otimes_R,R)`$ のモノイド対象は単位的結合 $`R`$-多元環である。
- 自己函手のモノイダル圏 $`\operatorname{End}(\mathcal{C})`$ では、モノイド対象は $`\mathcal{C}`$ 上のモナドである。

文脈によって、モノイド対象は代数対象とも呼ばれる。
モナドとの対応については [モナド](./monad.md) を参照されたい。
