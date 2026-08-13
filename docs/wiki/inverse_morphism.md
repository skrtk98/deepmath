---
tags:
  - 圏論
  - 射
  - 可逆性
---

# 逆射

## 定義

> [!definition] 逆射
> [圏](./category.md) $`\mathcal{C}`$ の射 $`f\colon A\to B`$ に対して、射 $`g\colon B\to A`$ が
>
> ```math
> g\circ f=1_A,\qquad f\circ g=1_B
> ```
>
> を満たすとき、$`g`$ を $`f`$ の**逆射** (*inverse morphism*) という。

> [!proposition] 逆射の一意性
> 射 $`f`$ が逆射を持つとき、その逆射は一意である。

> [!proof]
> $`g,h\colon B\to A`$ がともに $`f`$ の逆射であるとする。
> 合成の結合律と逆射の定義から、
> ```math
> g=g\circ1_B=g\circ(f\circ h)=(g\circ f)\circ h=1_A\circ h=h
> ```
> が成り立つ。

この一意な逆射を $`f^{-1}`$ と表す。

集合と写像の圏では、逆射は全単射の逆写像に一致する。

## 性質

逆射を持つ射 $`f\colon A\to B`$ と $`g\colon B\to C`$ に対して、合成 $`g\circ f`$ は逆射を持ち、

```math
(g\circ f)^{-1}=f^{-1}\circ g^{-1}
```

が成り立つ。
