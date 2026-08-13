---
tags:
  - 圏論
  - 構造保存
  - 合成
  - 反変性
---

# 函手

## 定義

> [!definition] 函手
> 圏 $`\mathcal{C},\mathcal{D}`$ の間の共変函手 $`F\colon\mathcal{C}\to\mathcal{D}`$ とは、対象と射を対応させ、$`F(1_X)=1_{F(X)}`$ および $`F(g\circ f)=F(g)\circ F(f)`$ を満たすものである。

反対圏 $`\mathcal{C}^{\mathrm{op}}`$ からの共変函手を、$`\mathcal{C}`$ からの反変函手という。

## 例

群から台集合を取る操作は、忘却函手 $`\mathsf{Grp}\to\mathsf{Set}`$ を定める。
