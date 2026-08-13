---
tags:
  - 圏論/モノイダル圏論
  - テンソル積
  - 自然同型
  - コヒーレンス
---

# モノイダル圏

## 定義

> [!definition] モノイダル圏
> モノイダル圏とは、圏 $`\mathcal{C}`$、函手 $`\otimes\colon\mathcal{C}\times\mathcal{C}\to\mathcal{C}`$、単位対象 $`I`$、および結合子と左右の単位子からなる構造である。
> これらの自然同型は五角形公理と三角公理を満たす。

結合子は $`(X\otimes Y)\otimes Z\cong X\otimes(Y\otimes Z)`$ を、単位子は $`I\otimes X\cong X\cong X\otimes I`$ を与える。

## 例

集合の圏は直積と一点集合によりモノイダル圏となる。

可換環上の加群の圏はテンソル積と係数環によりモノイダル圏となる。
