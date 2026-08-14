---
tags:
  - 圏論/豊穣圏論
  - モノイダル圏
  - Hom
  - 構造保存
---

# 豊穣圏

通常の圏では、対象 $`X,Y`$ の間の射は集合 $`\mathcal{C}(X,Y)`$ をなす。

豊穣圏では、この射集合を、あらかじめ定めたモノイダル圏 $`(\mathcal{V},\otimes,I)`$ の対象に置き換える。

このとき $`\mathcal{C}(X,Y)`$ は集合とは限らず、アーベル群、ベクトル空間、半順序集合などの構造を持つ。

## 定義

> [!definition] $`\mathcal{V}`$-豊穣圏
> モノイダル圏 $`\mathcal{V}`$ 上の **豊穣圏** (*$`\mathcal{V}`$-enriched category*) $`\mathcal{C}`$ とは、次のデータからなる。
>
> - 対象の類 $`\operatorname{Ob}(\mathcal{C})`$。
> - 各対象 $`X,Y`$ に対する $`\mathcal{V}`$ の対象 $`\mathcal{C}(X,Y)`$。
> - 各対象 $`X,Y,Z`$ に対する合成射
>   ```math
>   \mathcal{C}(Y,Z)\otimes\mathcal{C}(X,Y)
>   \longrightarrow\mathcal{C}(X,Z).
>   ```
> - 各対象 $`X`$ に対する単位射
>   ```math
>   I\longrightarrow\mathcal{C}(X,X).
>   ```
>
> 合成射と単位射は、$`\mathcal{V}`$ の結合子および左右の単位子を介して結合律と単位律を満たす。

結合律は、$`\mathcal{C}(Z,W)\otimes\mathcal{C}(Y,Z)\otimes\mathcal{C}(X,Y)`$ から $`\mathcal{C}(X,W)`$ への二つの合成射が、結合子を除いて一致することを要請する。

単位律は、$`I`$ から得られる単位射を左右から合成しても、Hom 対象の恒等射が得られることを要請する。

## 豊穣函手

> [!definition] 豊穣函手
> $`\mathcal{V}`$-豊穣圏 $`\mathcal{C},\mathcal{D}`$ の間の **豊穣函手** $`F\colon\mathcal{C}\to\mathcal{D}`$ とは、対象写像 $`X\mapsto F(X)`$ と、各対象対に対する射
> ```math
> \mathcal{C}(X,Y)\longrightarrow\mathcal{D}(F(X),F(Y))
> ```
> からなり、合成射と単位射を保つものである。

> [!definition] 豊穣自然変換
> 豊穣函手 $`F,G\colon\mathcal{C}\to\mathcal{D}`$ の間の **豊穣自然変換** $`\alpha\colon F\Rightarrow G`$ とは、各対象 $`X`$ に対する射 $`I\to\mathcal{D}(F(X),G(X))`$ の族であって、豊穣合成に関する自然性条件を満たすものである。

基底が $`\mathsf{Set}`$ である場合、$`I`$ は一点集合であるため、この定義は通常の自然変換の定義に一致する。

## 例

基底を、直積をモノイダル積とする $`\mathsf{Set}`$ に取ると、$`\mathsf{Set}`$-豊穣圏は通常の圏である。

基底をテンソル積を持つ $`\mathsf{Ab}`$ に取ると、合成が双線形となる前加法圏が得られる。

体 $`k`$ 上のベクトル空間の圏 $`\mathsf{Vect}_k`$ に豊穣化すると、各 Hom 対象は $`k`$-ベクトル空間となり、合成は双線形写像となる。

Lawvere 距離空間は、モノイダル順序圏 $`([0,\infty],\ge,+,0)`$ 上の豊穣圏として表せる。

この場合、豊穣合成は三角不等式に、単位射は $`d(x,x)=0`$ に対応する。
