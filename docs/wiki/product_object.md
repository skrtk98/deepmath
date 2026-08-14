---
tags:
  - 圏論
  - 極限
  - 普遍性
---

# 積

二対象への射の組を一つの射として扱う普遍構成を**積**という。
積は離散な二対象からなる図式の極限である。

## 定義

> [!definition] 二項積
> 対象 $`X,Y`$ の **積** とは、対象 $`P`$ と射影 $`p_1\colon P\to X`$、$`p_2\colon P\to Y`$ であって、任意の $`f_1\colon A\to X`$ と $`f_2\colon A\to Y`$ に対して一意な射 $`\langle f_1,f_2\rangle\colon A\to P`$ が存在し、$`p_1\langle f_1,f_2\rangle=f_1`$、$`p_2\langle f_1,f_2\rangle=f_2`$ を満たすものをいう。

```tikz
\begin{tikzcd}[column sep=large, row sep=large]
& A \arrow[dl, "f_1"'] \arrow[d, dashed, "\langle f_1,f_2\rangle"] \arrow[dr, "f_2"] & \\
X & P \arrow[l, "p_1"] \arrow[r, "p_2"'] & Y
\end{tikzcd}
```

積は存在すれば同型を除いて一意であり、通常 $`X\times Y`$ と書く。
対象族 $`(A_i)_{i\in I}`$ に対しても、同じ普遍性で $`\prod_{i\in I}A_i`$ を定める。

## 例

$`\mathsf{Set}`$ では積は直積集合であり、射影は座標射影である。
$`\mathsf{Top}`$ では積位相を入れた直積空間である。
半順序を圏とみなすとき、積は存在すれば二元の下限 $`x\wedge y`$ に一致する。

二項積と [終対象](./terminal_object.md) をもつ圏では、有限個の対象の積を反復して構成できる。
