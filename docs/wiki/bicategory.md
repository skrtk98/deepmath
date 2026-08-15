---
tags:
  - 圏論/高次圏論
  - 2-射
  - 合成
  - コヒーレンス
---

# 双圏

## 定義

> [!definition] 双圏
> 双圏とは、対象、各対象対 $`(A,B)`$ に対する Hom 圏、Hom 圏間の合成函手、および各対象の単位 1-射からなる構造である。
> 1-射の合成は結合子と単位子によって自然同型まで結び付けられ、これらは五角形公理と三角形公理を満たす。

Hom 圏の対象を 1-射、その射を 2-射という。

結合子と単位子が恒等自然変換である双圏を厳格 2-圏という。

## 例

圏、函手、自然変換からなる $`\mathsf{Cat}`$ は厳格 2-圏である。

## 豊穣圏の厳密 2 圏

基底 [モノイダル圏](./monoidal_category.md) $`\mathcal{V}`$ に対し、$`\mathcal{V}`$-圏、$`\mathcal{V}`$-函手、$`\mathcal{V}`$-自然変換は厳格 2 圏

```math
\mathcal{V}\text{-}\mathsf{Cat}
```

をなす。
この 2 圏の 0-射は $`\mathcal{V}`$-圏、1-射は $`\mathcal{V}`$-函手、2-射は $`\mathcal{V}`$-自然変換である。

2 射の垂直合成は成分ごとの合成であり、水平合成は whiskering と成分合成から定まる。
両合成は交換法則を満たす。

$`\mathcal{V}=\mathsf{Set}`$ の場合、$`\mathcal{V}\text{-}\mathsf{Cat}`$ は通常の 2 圏 $`\mathsf{Cat}`$ に一致する。
豊穣随伴と豊穣 Kan 拡張は、この 2 圏における随伴と Kan 拡張として扱える。

豊穣函手と豊穣自然変換の定義は [豊穣函手](./enriched_functor.md) と [豊穣自然変換](./enriched_natural_transformation.md) を参照されたい。
