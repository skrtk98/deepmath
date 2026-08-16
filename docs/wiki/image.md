---
tags:
  - 基礎論/集合論
  - 写像
  - 部分構造
---

# 像

## 定義

> [!definition] 像
> 写像 $`f\colon X\to Y`$ と部分集合 $`A\subseteq X`$ に対して、$`A`$ の **$`f`$ による像** (*image of $`A`$ under $`f`$*) を
>
> ```math
> f(A)\coloneqq\{f(x)\mid x\in A\}\subseteq Y
> ```
>
> により定める。

特に、$`f(X)`$ を写像 $`f`$ の**像**といい、$`\operatorname{Im}f`$ と表す。

> [!definition] 逆像
> 写像 $`f\colon X\to Y`$ と部分集合 $`B\subseteq Y`$ に対して、$`B`$ の **$`f`$ による逆像** (*preimage of $`B`$ under $`f`$*) を
>
> ```math
> f^{-1}(B)\coloneqq\{x\in X\mid f(x)\in B\}\subseteq X
> ```
>
> により定める。

この $`f^{-1}(B)`$ は逆写像の存在を仮定せずに定義される。

## 基本的な性質

写像 $`f\colon X\to Y`$ と部分集合 $`A,A_i\subseteq X`$、$`B,B_i\subseteq Y`$ に対して、次が成り立つ。

```math
f\left(\bigcup_i A_i\right)=\bigcup_i f(A_i),\qquad
f^{-1}\left(\bigcup_i B_i\right)=\bigcup_i f^{-1}(B_i),
```

```math
f^{-1}\left(\bigcap_i B_i\right)=\bigcap_i f^{-1}(B_i).
```

像は一般に共通部分を保存しない。

実際、$`f`$ が単射でない場合には $`f(A\cap A')\subsetneq f(A)\cap f(A')`$ となることがある。

一方、逆像は補集合を保ち、$`f^{-1}(Y\setminus B)=X\setminus f^{-1}(B)`$ が成り立つ。

## 合成との関係

写像 $`f\colon X\to Y`$ と $`g\colon Y\to Z`$、部分集合 $`A\subseteq X`$、$`C\subseteq Z`$ に対して、

```math
(g\circ f)(A)=g(f(A)),\qquad (g\circ f)^{-1}(C)=f^{-1}(g^{-1}(C))
```

が成り立つ。
