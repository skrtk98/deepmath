---
tags:
  - 圏論
  - 射
  - 余核
---

# 余像

射の始域から、核に相当する部分を除いて得られる普遍的なエピ射因子を**余像**という。

## 定義

> [!definition] 余像
> 射 $`f\colon A\to B`$ の余像とは、エピ射 $`s\colon A\to\operatorname{CoIm}f`$ と射 $`\bar f\colon\operatorname{CoIm}f\to B`$ の因子化 $`f=\bar f\circ s`$ であって、$`f`$ の他のエピ射因子化を一意に媒介するものをいう。

零射と核・余核をもつ圏では、余像を $`\operatorname{coker}(\ker f)`$ として定める。
アーベル圏では像と余像の間に標準的な同型があるが、一般の圏では両者を同一視できない。

$`\mathsf{Ab}`$ では、$`\operatorname{CoIm}f\cong A/\ker f`$ である。
