---
tags:
  - 基礎論/集合論
  - 写像
  - 合成
---

# 写像

## 定義

> [!definition] 写像
> 集合 $`X,Y`$ に対して、**$`X`$ から $`Y`$ への写像** (*map from $`X`$ to $`Y`$*) とは、$`X`$ の各元 $`x`$ に $`Y`$ のただ一つの元 $`f(x)`$ を対応させる規則のことである。
>
> 写像 $`f`$ を $`f\colon X\to Y`$ と表す。
> このとき、$`X`$ を $`f`$ の**始域**、$`Y`$ を $`f`$ の**終域**という。

> [!definition] 合成写像
> 写像 $`f\colon X\to Y`$ と $`g\colon Y\to Z`$ に対して、**合成写像** $`g\circ f\colon X\to Z`$ を $`(g\circ f)(x)=g(f(x))`$ により定める。

写像 $`f\colon X\to Y`$ が**単射** (*injective*) であるとは、$`f(x)=f(x')`$ ならば $`x=x'`$ が成り立つことである。

写像 $`f\colon X\to Y`$ が**全射** (*surjective*) であるとは、任意の $`y\in Y`$ に対して $`f(x)=y`$ となる $`x\in X`$ が存在することである。

単射かつ全射である写像を**全単射** (*bijective*) という。

## 逆写像

全単射は、対応を逆向きにたどる写像を持つ。

> [!proposition] 全単射と逆写像
> 写像 $`f\colon X\to Y`$ が全単射であることと、$`g\colon Y\to X`$ であって $`g\circ f=\operatorname{id}_X`$ かつ $`f\circ g=\operatorname{id}_Y`$ を満たすものが存在することは同値である。
>
> このような $`g`$ は一意であり、$`f`$ の**逆写像**といって $`f^{-1}`$ と表す。

ここで $`\operatorname{id}_X\colon X\to X`$ は、$`x\mapsto x`$ で定まる恒等写像である。

## 例

集合 $`X`$ の部分集合 $`A`$ に対する包含 $`A\hookrightarrow X`$ は単射である。

写像 $`\mathbb{R}\to[0,\infty)`$、$`x\mapsto x^2`$ は全射であるが、単射ではない。

写像 $`\mathbb{R}\to\mathbb{R}`$、$`x\mapsto x^3`$ は全単射であり、逆写像は $`x\mapsto\sqrt[3]{x}`$ である。
