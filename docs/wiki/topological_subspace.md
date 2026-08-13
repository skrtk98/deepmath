---
tags:
  - 位相幾何学
  - 部分構造
  - 開集合
  - 包含関係
---

# 部分空間

## 定義

> [!definition] 部分空間位相
> 位相空間 $`(X,\mathcal{T})`$ の部分集合 $`Y\subseteq X`$ に対して、
> ```math
> \mathcal{T}|_Y\coloneqq\{U\cap Y\mid U\in\mathcal{T}\}
> ```
> は $`Y`$ 上の位相となる。
> これを $`Y`$ の **部分空間位相** (*subspace topology*) という。

部分空間位相を備えた $`Y`$ を $`X`$ の部分空間という。

## 基本的な性質

包含写像 $`\iota\colon Y\hookrightarrow X`$ は連続である。

位相空間 $`Z`$ と写像 $`f\colon Z\to Y`$ に対して、$`f`$ が連続であることと、合成 $`\iota\circ f\colon Z\to X`$ が連続であることは同値である。

## 例

実数直線 $`\mathbb{R}`$ の部分集合 $`[0,1]`$ は、通常の位相から誘導される部分空間位相を持つ。

この位相において、集合 $`[0,1/2)`$ は開集合である。
