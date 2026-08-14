---
tags:
  - 圏論
  - 函手
  - 同値
  - 自然同型
---

# 圏同値

圏同値は、対象を同型まで区別する圏論における同一視を表す。
圏同型と異なり、逆函手との合成が厳密に恒等函手であることは要求しない。

## 定義

> [!definition] 圏同値
> 函手 $`F\colon\mathcal{A}\to\mathcal{B}`$ が **圏同値** を与えるとは、函手 $`G\colon\mathcal{B}\to\mathcal{A}`$ と自然同型 $`\eta\colon1_{\mathcal A}\Rightarrow GF`$、$`\varepsilon\colon FG\Rightarrow1_{\mathcal B}`$ が存在することをいう。

このとき $`G`$ を $`F`$ の擬逆といい、$`\mathcal{A}\simeq\mathcal{B}`$ と表す。

## 判定と例

函手 $`F`$ が充満忠実かつ本質的全射であれば、適切な代表対象の選択の下で圏同値を与える。
逆に、圏同値を与える函手は充満忠実かつ本質的全射である。

有限次元ベクトル空間の圏は、各次元ごとに代表対象を一つ選んだ骨格圏と同値である。
圏同値は [自然同型](./natural_isomorphism.md) を介した可逆性であり、厳密な逆函手をもつ圏同型より弱い。
