---
tags:
  - 圏論
  - 豊穣圏
  - Kan 拡張
  - 重み付き極限と余極限
---

# 各点 Kan 拡張

豊穣圏における各点 Kan 拡張は、重み付き極限または重み付き余極限によって対象ごとに計算される Kan 拡張である。
以下で $`\mathcal{V}`$ を対称モノイダル閉圏とし、$`\mathcal{C}`$, $`\mathcal{D}`$, $`\mathcal{A}`$ を $`\mathcal{V}`$-豊穣圏とする。

## 左各点 Kan 拡張

> [!theorem] 左各点公式
> $`K\colon\mathcal{C}\to\mathcal{D}`$ と $`F\colon\mathcal{C}\to\mathcal{A}`$ を $`\mathcal{V}`$-函手とする。
> 必要な重み付き余極限が存在すれば、$`K`$ に沿う $`F`$ の左各点 Kan 拡張は
>
> ```math
> (\operatorname{Lan}_K F)(d)
> \cong
> \mathcal{D}(K-,d)\star F
> ```
>
> で与えられる。
> ここで $`\mathcal{D}(K-,d)\colon\mathcal{C}^{\mathrm{op}}\to\mathcal{V}`$ は重みであり、$`\star`$ はその重みによる余極限を表す。

重み $`\mathcal{D}(K-,d)`$ は、$`K(c)`$ から $`d`$ への豊穣 Hom を記録する。
したがってこの公式は、$`F(c)`$ を $`d`$ への射で重み付けして貼り合わせる操作を表す。

## 右各点 Kan 拡張

> [!theorem] 右各点公式
> 必要な重み付き極限が存在すれば、$`K`$ に沿う $`F`$ の右各点 Kan 拡張は
>
> ```math
> (\operatorname{Ran}_K F)(d)
> \cong
> \{\mathcal{D}(d,K-),F\}
> ```
>
> で与えられる。
> ここで $`\mathcal{D}(d,K-)\colon\mathcal{C}\to\mathcal{V}`$ は重みであり、$`\{-,-\}`$ は重み付き極限を表す。

## 通常の圏の場合

$`\mathcal{V}=\mathsf{Set}`$ の場合、左の重み付き余極限はコンマ圏 $`(K\mathbin{\downarrow}d)`$ 上の通常の余極限に一致する。
右の重み付き極限は $`(d\mathbin{\downarrow}K)`$ 上の通常の極限に一致する。

前層圏では、これらの公式をコエンドまたはエンドで展開できる。
通常の Kan 拡張の普遍性は [Kan 拡張](./kan_extension.md) を参照されたい。
