---
tags:
  - 圏論
  - 射
  - 合成
---

# 圏

## 導入

**圏** (*category*) は「対象」と「対象間の射」からなる数学的構造を、分野横断で統一的に扱うための言語である。
群・位相空間・順序・代数構造を同じ形式で記述できるため、共通パターンの抽出に向いている。

## モチベーション

- 対象そのものより「射による関係」を主役に置く。
- 具体的構成を、普遍性と可換図式で再利用可能な形にする。
- 後続の函手・自然変換・随伴・極限の土台となる。

## アイディア

- 1945年の Eilenberg–Mac Lane により、ホモロジー論で使う「構造と構造写像」を統一する言語として定式化された。
- 以後の中心的発想は、対象の内部よりも射のネットワークを不変量として扱うこと。
- 「可換図式で証明を運ぶ」作法が、圏論的議論の標準形を与える。

## 定義

> [!definition] 圏
> 圏 $`\mathcal{C}`$ とは、次のデータからなる。
>
> - 対象の類 $`\operatorname{Ob}(\mathcal{C})`$,
> - 各 $`A,B\in\operatorname{Ob}(\mathcal{C})`$ に対する射の類 $`\mathcal{C}(A,B)`$,
> - 合成
>
>     ```math
>     \mathcal{C}(B,C)\times \mathcal{C}(A,B)\to \mathcal{C}(A,C),\quad (g,f)\mapsto g\circ f,
>     ```
>
> - 各対象 $`A`$ の恒等射 $`1_A\in\mathcal{C}(A,A)`$,
>
> これらは次を満たす。
>
> - 結合律：任意の $`f\in\mathcal{C}(A,B),g\in\mathcal{C}(B,C),h\in\mathcal{C}(C,D)`$ に対して $`h\circ(g\circ f)=(h\circ g)\circ f`$,
> - 単位律：任意の $`f\in\mathcal{C}(A,B)`$ に対して $`f\circ 1_A=f=1_B\circ f`$.
