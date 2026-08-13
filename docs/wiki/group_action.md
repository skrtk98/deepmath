---
tags:
  - 代数学/群論
  - 作用
  - 対称性
  - 軌道
---

# 群作用

## 定義

群作用は、群の元を集合上の変換として実現する構造である。

> [!definition] 左群作用
> 群 $`G`$ と集合 $`X`$ に対して、写像 $`\alpha\colon G\times X\to X`$ が **$`X`$ 上の左 $`G`$-作用** (*left action of $`G`$ on $`X`$*) であるとは、任意の $`g,h\in G`$ および $`x\in X`$ に対して、次を満たすことである。
>
> ```math
> \alpha(1_G,x)=x,\qquad
> \alpha(g,\alpha(h,x))=\alpha(gh,x).
> ```

通常、$`\alpha(g,x)`$ を $`g\cdot x`$ と書く。

この記法では、作用の公理は $`1_G\cdot x=x`$ および $`g\cdot(h\cdot x)=(gh)\cdot x`$ となる。

右作用は、写像 $`X\times G\to X`$、$`(x,g)\mapsto x\cdot g`$ が $`x\cdot1_G=x`$ および $`(x\cdot g)\cdot h=x\cdot(gh)`$ を満たすものとして定める。

## 軌道と安定化部分群

> [!definition] 軌道
> 左 $`G`$-集合 $`X`$ の元 $`x\in X`$ に対して、$`x`$ の **軌道** (*orbit*) を
>
> ```math
> G\cdot x\coloneqq\{g\cdot x\mid g\in G\}
> ```
>
> により定める。

> [!definition] 安定化部分群
> 左 $`G`$-集合 $`X`$ の元 $`x\in X`$ に対して、$`x`$ の **安定化部分群** (*stabilizer*) を
>
> ```math
> G_x\coloneqq\{g\in G\mid g\cdot x=x\}
> ```
>
> により定める。

> [!proposition] 安定化部分群
> $`G_x`$ は $`G`$ の部分群である。

> [!proof]
> $`1_G\cdot x=x`$ であるから、$`1_G\in G_x`$ である。
> 実際、$`h\cdot x=x`$ の両辺に $`h^{-1}`$ を作用させると、$`h^{-1}\cdot x=x`$ を得る。
> したがって、$`g,h\in G_x`$ に対して、$`(gh^{-1})\cdot x=g\cdot(h^{-1}\cdot x)=g\cdot x=x`$ が成り立つ。
> よって、部分群判定法から $`G_x`$ は部分群である。

## 例

群 $`G`$ は、自身への左乗法 $`g\cdot x\coloneqq gx`$ によって自分自身に作用する。

対称群 $`S_n`$ は、集合 $`\{1,\dots,n\}`$ に置換として作用する。

ベクトル空間 $`V`$ の可逆線形写像全体は、ベクトルへの作用によって $`V`$ に作用する。
