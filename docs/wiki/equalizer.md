---
tags:
  - 圏論
  - 極限
  - 普遍性
---

# 等化子

二本の平行射が一致する部分を、因子化の一意性で取り出す構成を**等化子**という。
等化子は平行射図式の極限である。

## 定義

> [!definition] 等化子
> 平行射 $`s,t\colon A\rightrightarrows B`$ の **等化子** とは、射 $`e\colon E\to A`$ であって $`s\circ e=t\circ e`$ を満たし、この条件を満たす任意の射 $`\theta\colon Z\to A`$ が一意に $`\bar\theta\colon Z\to E`$ を用いて $`e\circ\bar\theta=\theta`$ と因子化するものをいう。

```tikz
\begin{tikzcd}[column sep=large, row sep=large]
Z \arrow[d, dashed, "\bar\theta"'] \arrow[dr, "\theta"] & \\
E \arrow[r, "e"'] & A \arrow[r, shift left, "s"] \arrow[r, shift right, "t"'] & B
\end{tikzcd}
```

等化子 $`e`$ は [モノ射](./monomorphism.md) である。
また、等化子は存在すれば同型を除いて一意である。

## 例

$`\mathsf{Set}`$ では、等化子は $`E=\{a\in A\mid s(a)=t(a)\}`$ と包含写像で与えられる。
群、環、加群の圏でも、対応する方程式を満たす部分構造とその包含が等化子になる。

零射をもつ圏では、射 $`f\colon A\to B`$ の核は $`f`$ と零射 $`0_{A,B}`$ の等化子として定義される。
