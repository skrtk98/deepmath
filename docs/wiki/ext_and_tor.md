---
tags:
  - 代数学/ホモロジー代数
  - 導来関手
  - テンソル積
  - 完全性
---

# Ext と Tor

## 定義

> [!definition] Ext と Tor
> 加群 $`M,N`$ に対して、$`\operatorname{Ext}_R^n(M,N)`$ は函手 $`\operatorname{Hom}_R(M,-)`$ の右導来関手として定める。
> $`\operatorname{Tor}_n^R(M,N)`$ は函手 $`M\otimes_R-`$ の左導来関手として定める。

$`\operatorname{Ext}`$ は拡大と障害を、$`\operatorname{Tor}`$ はテンソル積の完全性の失敗を測る。

## 性質と例

$`\operatorname{Ext}^1_R(M,N)`$ は、両端が $`N`$ と $`M`$ である短完全系列の同値類と対応する。
$`\operatorname{Tor}_1^R(M,N)=0`$ がすべての $`N`$ について成り立つことは、$`M`$ が平坦であることと同値である。

正整数 $`m,n`$ に対して、$`\operatorname{Tor}_1^{\mathbb{Z}}(\mathbb{Z}/m\mathbb{Z},\mathbb{Z}/n\mathbb{Z})\cong\mathbb{Z}/\gcd(m,n)\mathbb{Z}`$ である。
体上のベクトル空間は自由加群であるため、高次の Ext と Tor は消える。
