---
tags:
  - 圏論
  - 圏の構成
  - 極限と余極限
---

# 余積圏

二つの圏を、対象と射の共通部分を持たない成分として合わせた圏は、圏の圏における余積を与える。
この構成は直和圏とも呼ばれる。

## 定義

> [!definition] 余積圏
> 圏 $`\mathcal{A}`$ と $`\mathcal{B}`$ の **余積圏** $`\mathcal{A}\sqcup\mathcal{B}`$ は、次で定まる圏である。
>
> - 対象は $`\operatorname{Ob}(\mathcal{A})`$ と $`\operatorname{Ob}(\mathcal{B})`$ の互いに素な和である。
> - 同じ成分に属する対象間の射は元の圏の射である。
> - 異なる成分に属する対象の間には射が存在しない。

恒等射と合成は、それぞれの成分のものから定める。

## 普遍性

標準包含函手

```math
i_{\mathcal{A}}\colon\mathcal{A}\to\mathcal{A}\sqcup\mathcal{B},
\qquad
i_{\mathcal{B}}\colon\mathcal{B}\to\mathcal{A}\sqcup\mathcal{B}
```

を考える。
任意の圏 $`\mathcal{X}`$ と函手 $`F\colon\mathcal{A}\to\mathcal{X}`$, $`G\colon\mathcal{B}\to\mathcal{X}`$ に対して、一意な函手

```math
[F,G]\colon\mathcal{A}\sqcup\mathcal{B}\to\mathcal{X}
```

が存在し、$`[F,G]i_{\mathcal{A}}=F`$ および $`[F,G]i_{\mathcal{B}}=G`$ を満たす。
従って $`\mathcal{A}\sqcup\mathcal{B}`$ は $`\mathsf{Cat}`$ における余積である。

## 例

終圏 $`\mathbf{1}`$ との余積 $`\mathbf{1}\sqcup\mathbf{1}`$ は、二つの対象だけを持つ離散圏である。
