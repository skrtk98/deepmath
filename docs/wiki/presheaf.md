---
tags:
  - 圏論
  - 前層
  - 函手圏
  - 米田埋め込み
---

# 前層圏

前層は、圏上で変化するデータを反変函手として表す。
射に沿ってデータを引き戻す操作が函手性として組み込まれる。

## 定義

> [!definition] 前層
> 小圏 $`\mathcal{C}`$ 上の **前層** とは、反変函手 $`F\colon\mathcal{C}^{\mathrm{op}}\to\mathsf{Set}`$ のことである。
> 前層全体は函手圏 $`[\mathcal{C}^{\mathrm{op}},\mathsf{Set}]`$ をなす。

射 $`f\colon X\to Y`$ に対し、前層は制限写像 $`F(f)\colon F(Y)\to F(X)`$ を与える。

## 米田埋め込みと計算

米田埋め込み $`y\colon\mathcal{C}\to[\mathcal{C}^{\mathrm{op}},\mathsf{Set}]`$ は、対象 $`X`$ を表現可能前層 $`\mathcal{C}(-,X)`$ へ送る。
この函手は充満忠実である。

前層圏の極限と余極限は点ごとに計算できる。
また、任意の前層は表現可能前層の余極限として標準的に表示される。
この表示を与える公式は [余米田の補題](./co_yoneda_lemma.md) を参照されたい。
米田の補題については [米田の補題](./yoneda_lemma.md) を参照されたい。
