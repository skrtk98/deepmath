---
tags:
  - 幾何学/位相幾何学
  - 開集合
  - 内部
  - 閉包作用素
---

# 開核作用素

開核作用素は、部分集合からその最大の開部分集合を取り出す操作を公理化したものである。

## 定義

> [!definition] 開核作用素
> 集合 $`X`$ 上の **開核作用素** とは、写像 $`u\colon\mathcal{P}(X)\to\mathcal{P}(X)`$ であって、任意の $`A,B\subseteq X`$ に対し
>
> ```math
> u(A)\subseteq A,
> \qquad
> u(X)=X,
> \qquad
> u(u(A))=u(A),
> \qquad
> u(A\cap B)=u(A)\cap u(B)
> ```
>
> を満たすものをいう。

これらの公理から単調性が従う。
すなわち $`A\subseteq B`$ ならば $`u(A)\subseteq u(B)`$ である。

## 位相との対応

位相空間 $`(X,\mathcal{T})`$ では、

```math
u(A)=\bigcup\{G\in\mathcal{T}\mid G\subseteq A\}
```

によって開核作用素が得られる。
この $`u(A)`$ は $`A`$ の内部 $`\operatorname{Int}(A)`$ である。

逆に、開核作用素 $`u`$ に対し

```math
\mathcal{T}_u=\{G\subseteq X\mid u(G)=G\}
```

は位相となる。
この二つの構成は互いに逆であり、位相と開核作用素は一対一に対応する。

開核作用素は、補集合を介して閉包作用素と双対である。
閉包作用素については [閉包作用素](./closure_operator.md) を、内点については [内点](./interior_point.md) を参照されたい。
