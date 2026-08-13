---
tags:
  - 圏論
  - 函手
  - 可換図式
  - 構造保存
---

# 自然変換

## 定義

> [!definition] 自然変換
> 函手 $`F,G\colon\mathcal{C}\to\mathcal{D}`$ の間の自然変換 $`\alpha\colon F\Rightarrow G`$ とは、各対象 $`X`$ に対する射 $`\alpha_X\colon F(X)\to G(X)`$ の族であって、任意の射 $`f\colon X\to Y`$ に対して $`G(f)\circ\alpha_X=\alpha_Y\circ F(f)`$ を満たすものである。

この等式を自然性条件という。
