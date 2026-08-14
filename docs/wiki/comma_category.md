---
tags:
  - 圏論
  - 函手
  - 可換図式
---

# コンマ圏

二つの函手の値を一本の射で結び、その射と両立する射を集める圏を**コンマ圏**という。
この構成はスライス圏、普遍射、随伴の記述に現れる。

## 定義

> [!definition] コンマ圏
> 函手 $`F\colon\mathcal{A}\to\mathcal{C}`$ と $`G\colon\mathcal{B}\to\mathcal{C}`$ に対し、コンマ圏 $`F\downarrow G`$ の対象は、$`A\in\mathcal{A}`$、$`B\in\mathcal{B}`$、射 $`f\colon F(A)\to G(B)`$ からなる三つ組 $`(A,B,f)`$ である。
> 射 $`(A,B,f)\to(A^{\prime},B^{\prime},f^{\prime})`$ は、射の対 $`(\alpha\colon A\to A^{\prime},\beta\colon B\to B^{\prime})`$ であって $`G(\beta)\circ f=f^{\prime}\circ F(\alpha)`$ を満たすものとする。

この等式は、射の対が指定された三つ組の間の可換正方形をなすことを表す。
恒等射と合成は $`\mathcal{A}`$ と $`\mathcal{B}`$ のものから成分ごとに定める。

## 例

対象 $`C\in\mathcal{C}`$ を終圏から $`\mathcal{C}`$ への定数函手とみなすと、$`\mathrm{id}_{\mathcal C}\downarrow C`$ はスライス圏 $`\mathcal{C}/C`$ である。
その対象は $`X\to C`$ の形の射である。

同様に、$`C\downarrow\mathrm{id}_{\mathcal C}`$ はコスライス圏 $`C/\mathcal{C}`$ である。
コンマ圏には二つの射影函手があり、対象の $`\mathcal{A}`$ 成分と $`\mathcal{B}`$ 成分をそれぞれ取り出す。
