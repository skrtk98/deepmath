---
tags:
  - 圏論
  - モノイダル圏
  - 函手
---

# モノイダル函手

モノイダル積と単位対象を保存するための構造をもつ函手を**ラックスモノイダル函手**という。

## 定義

> [!definition] ラックスモノイダル函手
> モノイダル圏 $`\mathcal{M},\mathcal{N}`$ の間のラックスモノイダル函手とは、函手 $`T\colon\mathcal{M}\to\mathcal{N}`$、自然な構造射 $`T(A)\otimes T(B)\to T(A\otimes B)`$、および単位構造射 $`I_{\mathcal N}\to T(I_{\mathcal M})`$ からなり、結合子と左右の単位子に関するコヒーレンス図式を可換にするものである。

構造射と単位構造射が同型であるとき強モノイダル函手という。
単位構造射だけが同型であるとき正規モノイダル函手という。
両者が恒等射であるとき厳格モノイダル函手という。

```tikz
\begin{tikzcd}[column sep=large, row sep=large]
(T A\otimes T B)\otimes T C \arrow[r] \arrow[d] & T A\otimes(T B\otimes T C) \arrow[d] \\
T(A\otimes B)\otimes T C \arrow[d] & T A\otimes T(B\otimes C) \arrow[d] \\
T((A\otimes B)\otimes C) \arrow[r] & T(A\otimes(B\otimes C))
\end{tikzcd}
```

この図式は、構造射と両圏の結合子が両立することを表す。
