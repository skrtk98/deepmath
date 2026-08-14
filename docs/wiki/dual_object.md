---
tags:
  - 圏論
  - モノイダル圏
  - 双対性
  - 可換図式
---

# 双対対象

モノイダル圏における双対対象は、評価と余評価によりテンソル因子を消去または生成できる対象である。
結合子を含む三角恒等式が、この二つの操作の両立を定める。

以下で $`(\mathcal{M},\otimes,I,\alpha,\lambda,\rho)`$ をモノイダル圏とする。

## 右双対

> [!definition] 右双対
> 対象 $`x\in\mathcal{M}`$ の **右双対** とは、対象 $`x^*`$ と射
>
> ```math
> \operatorname{ev}_x\colon x^*\otimes x\to I,
> \qquad
> \operatorname{coev}_x\colon I\to x\otimes x^*
> ```
>
> の組である。
> これらは、次の二つの合成がそれぞれ恒等射になるという三角恒等式を満たす。
>
> ```math
> x
> \xrightarrow{\lambda_x^{-1}}
> I\otimes x
> \xrightarrow{\operatorname{coev}_x\otimes1_x}
> (x\otimes x^*)\otimes x
> \xrightarrow{\alpha_{x,x^*,x}}
> x\otimes(x^*\otimes x)
> \xrightarrow{1_x\otimes\operatorname{ev}_x}
> x\otimes I
> \xrightarrow{\rho_x}
> x
> =1_x,
> ```
>
> ```math
> x^*
> \xrightarrow{\rho_{x^*}^{-1}}
> x^*\otimes I
> \xrightarrow{1_{x^*}\otimes\operatorname{coev}_x}
> x^*\otimes(x\otimes x^*)
> \xrightarrow{\alpha_{x^*,x,x^*}^{-1}}
> (x^*\otimes x)\otimes x^*
> \xrightarrow{\operatorname{ev}_x\otimes1_{x^*}}
> I\otimes x^*
> \xrightarrow{\lambda_{x^*}}
> x^*
> =1_{x^*}.
> ```

第一の三角恒等式は、次の可換図式として表される。

```latex {cmd=true latex_zoom=220% hide=true}
\documentclass{standalone}
\usepackage{mathtools}
\usepackage{tikz}
\begin{document}
\begin{tikzpicture}[xscale=2.6,yscale=1.4]
  \node (a) at (0,1) {$I\otimes x$};
  \node (b) at (1.6,1) {$(x\otimes x^*)\otimes x$};
  \node (c) at (3.2,1) {$x\otimes(x^*\otimes x)$};
  \node (d) at (4.8,1) {$x\otimes I$};
  \node (e) at (2.4,0) {$x$};
  \draw[->] (a) -- node[above,scale=.7] {$\operatorname{coev}_x\otimes1_x$} (b);
  \draw[->] (b) -- node[above,scale=.7] {$\alpha_{x,x^*,x}$} (c);
  \draw[->] (c) -- node[above,scale=.7] {$1_x\otimes\operatorname{ev}_x$} (d);
  \draw[->] (a) -- node[left,scale=.75] {$\lambda_x$} (e);
  \draw[->] (d) -- node[right,scale=.75] {$\rho_x$} (e);
\end{tikzpicture}
\end{document}
```

## 左双対と一意性

**左双対**は、評価 $`x\otimes{}^*x\to I`$ と余評価 $`I\to{}^*x\otimes x`$ を用い、上の定義を左右反転して定める。
右双対と左双対は同じ概念ではないが、対称モノイダル圏では対称性によって一方から他方を構成できる。

右双対が存在するとき、その対象 $`x^*`$ は評価と余評価を保つ一意な同型を除いて定まる。

## 例と関連概念

体 $`k`$ 上の有限次元ベクトル空間 $`V`$ は、通常の双対空間 $`V^*=\operatorname{Hom}_k(V,k)`$ を右双対にもつ。
評価は $`\varphi\otimes v\mapsto\varphi(v)`$ であり、余評価は基底 $`(e_i)`$ と双対基底 $`(e^i)`$ を用いて $`1\mapsto\sum_i e_i\otimes e^i`$ と表される。
この余評価は基底の選び方に依存しない。

すべての対象が左双対と右双対をもつモノイダル圏を **剛モノイダル圏** または自律圏という。
対称モノイダル圏でこの条件を満たすものはコンパクト閉圏と呼ばれる。
モノイダル圏の基本データについては [モノイダル圏](./monoidal_category.md) を参照されたい。
