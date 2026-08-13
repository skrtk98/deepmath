---
tags:
  - 代数学/半群論/モノイド
  - 作用
  - 構造保存
---

# モノイド作用

## 定義

モノイド作用は、モノイドの元を集合上の変換として合成する構造である。

> [!definition] 左モノイド作用
> モノイド $`M`$ と集合 $`X`$ に対して、写像 $`\alpha\colon M\times X\to X`$ が **$`X`$ 上の左 $`M`$-作用** (*left action of $`M`$ on $`X`$*) であるとは、任意の $`m,n\in M`$ および $`x\in X`$ に対して、次を満たすことである。
>
> ```math
> \alpha(1_M,x)=x,\qquad
> \alpha(m,\alpha(n,x))=\alpha(mn,x).
> ```

通常、$`\alpha(m,x)`$ を $`m\cdot x`$ と書く。

右 $`M`$-作用は、写像 $`X\times M\to X`$、$`(x,m)\mapsto x\cdot m`$ であって、$`x\cdot1_M=x`$ および $`(x\cdot m)\cdot n=x\cdot(mn)`$ を満たすものとして定める。

## 例

モノイド $`M`$ は、自身への左乗法 $`m\cdot n\coloneqq mn`$ により自分自身に作用する。

自己写像 $`X\to X`$ 全体は合成を乗法とするモノイドをなし、各自己写像を $`X`$ に作用させる。

群作用は、作用するモノイドが群である場合のモノイド作用である。
