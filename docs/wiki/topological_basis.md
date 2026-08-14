---
tags:
  - 位相幾何学
  - 開集合
  - 生成
  - 可算性
---

# 開基

## 定義

> [!definition] 開基
> 集合 $`X`$ の部分集合族 $`\mathcal{B}`$ が **開基** (*basis for a topology*) であるとは、次の条件を満たすことである。
>
> - 任意の $`x\in X`$ に対して、$`x\in B`$ を満たす $`B\in\mathcal{B}`$ が存在する。
> - $`B_1,B_2\in\mathcal{B}`$ と $`x\in B_1\cap B_2`$ に対して、$`x\in B_3\subseteq B_1\cap B_2`$ を満たす $`B_3\in\mathcal{B}`$ が存在する。

開基 $`\mathcal{B}`$ は、$`\mathcal{B}`$ の元の任意の和集合からなる位相を定める。

この位相を $`\mathcal{B}`$ が生成する位相という。

## 例

実数直線 $`\mathbb{R}`$ において、開区間全体の族は通常の位相の開基である。

端点が有理数である開区間全体の族も、同じ位相の可算開基である。

## 生成と比較

任意の部分集合族 $`\mathcal{S}`$ に対し、$`\mathcal{S}`$ の有限共通部分全体を開基として用いれば、$`\mathcal{S}`$ を含む最も粗い位相が得られる。

二つの開基 $`\mathcal{B},\mathcal{C}`$ が同じ位相を定めるための必要十分条件は、各 $`B\in\mathcal{B}`$ と各点 $`x\in B`$ に対し、$`x\in C\subseteq B`$ を満たす $`C\in\mathcal{C}`$ が存在し、同じ条件が両者を入れ替えても成り立つことである。
