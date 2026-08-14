---
tags:
  - 圏論
  - 圏の構成
  - 極限と余極限
---

# 直積圏

二つの圏を成分ごとに並べた圏は、圏の圏における積を与える。

## 定義

> [!definition] 直積圏
> 圏 $`\mathcal{A}`$ と $`\mathcal{B}`$ の **直積圏** $`\mathcal{A}\times\mathcal{B}`$ を次で定める。
>
> - 対象は対 $`(A,B)`$ である。
> - $`(A,B)`$ から $`(A',B')`$ への射は、射の対 $`(f,g)`$ である。ただし $`f\colon A\to A'`$ および $`g\colon B\to B'`$ とする。
> - 恒等射と合成は成分ごとに定める。

したがって、合成は

```math
(f',g')\circ(f,g)=(f'\circ f,g'\circ g)
```

である。

## 普遍性

射影函手

```math
\pi_{\mathcal{A}}\colon\mathcal{A}\times\mathcal{B}\to\mathcal{A},
\qquad
\pi_{\mathcal{B}}\colon\mathcal{A}\times\mathcal{B}\to\mathcal{B}
```

は、それぞれ第一成分と第二成分を取る。
任意の圏 $`\mathcal{X}`$ と函手 $`F\colon\mathcal{X}\to\mathcal{A}`$, $`G\colon\mathcal{X}\to\mathcal{B}`$ に対し、函手

```math
\langle F,G\rangle\colon\mathcal{X}\to\mathcal{A}\times\mathcal{B}
```

が一意に存在して、$`\pi_{\mathcal{A}}\langle F,G\rangle=F`$ および $`\pi_{\mathcal{B}}\langle F,G\rangle=G`$ を満たす。
従って $`\mathcal{A}\times\mathcal{B}`$ は $`\mathsf{Cat}`$ における積である。

## 例

$`\mathsf{Set}\times\mathsf{Grp}`$ の対象は、集合と群の対である。
その射は集合写像と群準同型の対である。
