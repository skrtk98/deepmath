---
tags:
  - 圏論
  - モノイダル圏
  - 加群圏
  - 函手
  - 豊穣圏
---

# 両側加群圏と加群射

モノイダル圏の作用を備えた圏では、作用と両立する函手を加群射として扱う。
この構造は、豊穣圏やプロファンクターに現れる左右の作用を一つの記法で記述する。

## 両側加群圏

以下で $`\mathcal{V}`$ と $`\mathcal{W}`$ をモノイダル圏とし、$`\operatorname{End}(\mathcal{C})`$ を圏 $`\mathcal{C}`$ の自己函手からなるモノイダル圏とする。
そのテンソル積は函手の合成である。

> [!definition] $`(\mathcal{V},\mathcal{W})`-両側加群圏
> 圏 $`\mathcal{C}`$ が **$`(\mathcal{V},\mathcal{W})`-両側加群圏** であるとは、強モノイダル函手
>
> ```math
> \varphi_{\mathcal{C}}\colon
> \mathcal{W}^{\mathrm{rev}}\times\mathcal{V}
> \longrightarrow
> \operatorname{End}(\mathcal{C})
> ```
>
> を備えることである。

したがって、対象 $`w\in\mathcal{W}`$ と $`v\in\mathcal{V}`$ は自己函手 $`\varphi_{\mathcal{C}}(w,v)`$ を定める。
強モノイダル性は、左右の作用の合成と、それぞれのモノイダル積および単位対象を整合させる自然同型を与える。
右の作用に逆転モノイダル圏 $`\mathcal{W}^{\mathrm{rev}}`$ を用いることにより、右からの逐次作用の順序を函手合成の順序と両立させる。

## 加群射

> [!definition] 加群射
> $`(\mathcal{V},\mathcal{W})`-両側加群圏 $`\mathcal{C}`$, $`\mathcal{D}`$ の間の **加群射** とは、函手 $`F\colon\mathcal{C}\to\mathcal{D}`$ と、$`w\in\mathcal{W}`$, $`v\in\mathcal{V}`$ に自然な同型
>
> ```math
> F\circ\varphi_{\mathcal{C}}(w,v)
> \cong
> \varphi_{\mathcal{D}}(w,v)\circ F
> ```
>
> の組である。
> この自然同型は、$`\mathcal{V}`$ と $`\mathcal{W}`$ のテンソル積および単位対象に関するコヒーレンス条件を満たさなければならない。

恒等函手は恒等加群射となる。
加群射の合成は上の自然同型を合成して定まり、$`(\mathcal{V},\mathcal{W})`-両側加群圏と加群射は圏 $`\mathsf{Mod}(\mathcal{V},\mathcal{W})`$ をなす。

## 特別な場合

$`\mathcal{V}=\mathcal{W}=\mathsf{Set}`$ の場合、この構造は集合の作用を備えた圏と、作用を保存する函手という通常の記述に還元される。

一方の作用だけを残すと、モノイダル圏が圏に作用する加群圏が得られる。
モノイド対象上の加群対象は、この作用を用いて定義できる。
その定義については [モノイド対象上の加群対象](./monoid_module_object.md) を参照されたい。
