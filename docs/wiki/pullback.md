---
tags:
  - 圏論
  - 極限
  - 可換図式
---

# 引き戻し

同じ対象へ向かう二本の射に対し、その値が一致する組を普遍的に集める構成を**引き戻し**という。
繊維積とも呼ばれ、スパン図式の極限である。

## 定義

> [!definition] 引き戻し
> スパン $`A\xrightarrow{s}C\xleftarrow{t}B`$ の **引き戻し** とは、可換正方形
>
> ```tikz
> \begin{tikzcd}[column sep=large, row sep=large]
> P \arrow[r, "\pi_2"] \arrow[d, "\pi_1"'] & B \arrow[d, "t"] \\
> A \arrow[r, "s"'] & C
> \end{tikzcd}
> ```
>
> であって、$`s\circ\theta_1=t\circ\theta_2`$ を満たす任意の射 $`\theta_1\colon Z\to A`$、$`\theta_2\colon Z\to B`$ に対し、一意な $`u\colon Z\to P`$ が $`\pi_1u=\theta_1`$、$`\pi_2u=\theta_2`$ を満たすものをいう。

## 例と双対

$`\mathsf{Set}`$ では、引き戻しは $`\{(a,b)\in A\times B\mid s(a)=t(b)\}`$ と二つの座標射影で与えられる。
半順序圏では、引き戻しは該当する下限の構成に一致する。

二項積と [等化子](./equalizer.md) をもつ圏では、引き戻しを構成できる。
反対圏における引き戻しは押し出しであり、これは余極限側の対応する構成である。
