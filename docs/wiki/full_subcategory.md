---
tags:
  - 圏論
  - 部分構造
  - Hom
---

# 充満部分圏

部分圏の対象を選んだ後、その対象間にある元の圏の射をすべて残すことがある。
この条件を満たす部分圏を **充満部分圏** (*full subcategory*) という。

## 定義

> [!definition] 充満部分圏
> 部分圏 $`\mathcal{D}\subseteq\mathcal{C}`$ が **充満** であるとは、任意の $`A,B\in\operatorname{Ob}(\mathcal{D})`$ に対して
>
> ```math
> \mathcal{D}(A,B)=\mathcal{C}(A,B)
> ```
>
> が成り立つことをいう。

したがって、充満部分圏を指定するには対象の集まりだけを指定すれば足りる。
対象間の射は元の圏から自動的に定まる。
これに対して一般の [部分圏](./subcategory.md) では、対象の間の射をさらに制限してよい。

## 例

可換群の圏 $`\mathsf{Ab}`$ は $`\mathsf{Grp}`$ の充満部分圏である。
実際、可換群 $`A,B`$ の間の群準同型は、$`\mathsf{Ab}`$ でも $`\mathsf{Grp}`$ でも同じである。

コンパクト Hausdorff 空間と連続写像の圏 $`\mathsf{CompHaus}`$ は $`\mathsf{Top}`$ の充満部分圏である。
対象をコンパクト Hausdorff 空間に限るが、その二つの間の連続写像を除外しないためである。

任意の圏 $`\mathcal{C}`$ と対象の集まり $`S\subseteq\operatorname{Ob}(\mathcal{C})`$ に対し、対象を $`S`$ とし、Hom を $`\mathcal{C}`$ からそのまま取る圏を $`\mathcal{C}|_S`$ と書くことがある。
これは $`S`$ 上の充満部分圏である。

## 函手による特徴づけ

包含函手 $`i\colon\mathcal{D}\hookrightarrow\mathcal{C}`$ が充満であることは、各 $`A,B\in\mathcal{D}`$ に対する写像

```math
\mathcal{D}(A,B)\longrightarrow\mathcal{C}(iA,iB)
```

が全単射であることと同値である。
この形では、$`\mathcal{D}`$ を文字どおりの部分圏として置かない場合にも「充満函手」という概念へ一般化できる。
一方、[忠実函手](./functor.md) は上の写像が単射であることだけを要求し、充満函手は全射性も要求する。
