---
tags:
  - 基礎論/集合論
  - 濃度
  - 同値関係
---

# 濃度

## 定義

集合の濃度は、元を重複なく対応させられるかによって比較する。

> [!definition] 同濃度
> 集合 $`X,Y`$ が **同濃度** (*equipotent*) であるとは、全単射 $`f\colon X\to Y`$ が存在することである。
>
> このとき、$`X`$ と $`Y`$ は同濃度であるといい、$`X\simeq Y`$ と表す。

同濃度であるという関係は、集合の間の同値関係である。

> [!definition] 濃度
> 集合 $`X`$ の **濃度** (*cardinality*) とは、$`X`$ と同濃度な集合全体からなる同値類のことである。
>
> 集合 $`X`$ の濃度を $`\lvert X\rvert`$ または $`\#X`$ と表す。

有限集合 $`X`$ が $`\{1,\dots,n\}`$ と同濃度であるとき、$`\lvert X\rvert=n`$ と書く。

空集合の濃度は $`0`$ である。

## 比較

> [!definition] 濃度の大小
> 集合 $`X,Y`$ に対して、$`X`$ から $`Y`$ への単射が存在するとき、$`\lvert X\rvert\le\lvert Y\rvert`$ と書く。

この定義は、$`X`$ の元を失わずに $`Y`$ の中へ埋め込めることを表す。

> [!proposition] Cantor--Schröder--Bernstein の定理
> 集合 $`X,Y`$ に対して、$`X\to Y`$ と $`Y\to X`$ の単射がともに存在するならば、$`X`$ と $`Y`$ は同濃度である。

したがって、$`\lvert X\rvert\le\lvert Y\rvert`$ かつ $`\lvert Y\rvert\le\lvert X\rvert`$ ならば $`\lvert X\rvert=\lvert Y\rvert`$ である。

## 例

自然数全体の集合 $`\mathbb{N}`$ と偶数全体の集合 $`2\mathbb{N}`$ は、写像 $`n\mapsto2n`$ によって同濃度である。

したがって、無限集合では真部分集合が集合全体と同じ濃度を持つことがある。
