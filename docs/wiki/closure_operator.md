---
tags:
  - 幾何学/位相幾何学
  - 閉集合
  - 包含関係
  - 作用素
---

# 閉包作用素

## 定義

位相空間 $`X`$ と部分集合 $`A\subseteq X`$ を考える。

> [!definition] 閉包
> $`A`$ を含む閉集合すべての共通部分を、$`A`$ の **閉包** (*closure*) といい、$`\overline{A}`$ と表す。

したがって、$`\overline{A}`$ は $`A`$ を含む最小の閉集合である。

## 性質

任意の部分集合 $`A,B\subseteq X`$ に対して、次が成り立つ。

```math
A\subseteq\overline{A},\qquad
\overline{\overline{A}}=\overline{A}.
```

また、$`A\subseteq B`$ ならば $`\overline{A}\subseteq\overline{B}`$ である。

有限和について $`\overline{A\cup B}=\overline{A}\cup\overline{B}`$ が成り立ち、$`\overline{\varnothing}=\varnothing`$ である。
したがって $`A\mapsto\overline{A}`$ は、冪集合上の広義単調、冪等、有限和を保つ閉包作用素である。

部分集合 $`A`$ が閉集合であることと、$`\overline{A}=A`$ が成り立つことは同値である。

## 点による特徴付け

点 $`x\in X`$ が $`\overline{A}`$ に属することと、$`x`$ の任意の近傍が $`A`$ と交わることは同値である。

逆に、この公理を満たす閉包作用素から、補集合が閉包で不変な集合を開集合と定めることで位相を復元できる。
