---
tags:
  - 圏論
  - 部分構造
  - 射
---

# 部分圏

ある圏から対象または射の一部を選んでも、恒等射と合成が保たれれば再び圏になる。
そのように得られる圏を **部分圏** (*subcategory*) という。

## 定義

> [!definition] 部分圏
> 圏 $`\mathcal{D}`$ が圏 $`\mathcal{C}`$ の **部分圏** であるとは、次を満たすことをいう。
>
> - $`\operatorname{Ob}(\mathcal{D})\subseteq\operatorname{Ob}(\mathcal{C})`$ である。
> - 任意の $`A,B\in\operatorname{Ob}(\mathcal{D})`$ に対して、$`\mathcal{D}(A,B)\subseteq\mathcal{C}(A,B)`$ である。
> - $`\mathcal{D}`$ における恒等射と合成は、$`\mathcal{C}`$ における恒等射と合成の制限である。

最後の条件は、$`A\in\mathcal{D}`$ なら $`1_A\in\mathcal{D}(A,A)`$ であり、$`f\in\mathcal{D}(A,B)`$ と $`g\in\mathcal{D}(B,C)`$ なら $`g\circ f\in\mathcal{D}(A,C)`$ であることを含む。
したがって、対象だけでなく許容する射を選ぶ場合にも、合成で閉じていることを確認しなければならない。

## 例

有限集合と写像の圏 $`\mathsf{FinSet}`$ は $`\mathsf{Set}`$ の部分圏である。
有限集合の間の任意の写像は有限集合の間の写像であり、恒等写像と写像の合成は有限集合の範囲にとどまる。

可換群と群準同型の圏 $`\mathsf{Ab}`$ は $`\mathsf{Grp}`$ の部分圏である。
この例では、可換群の間の群準同型をすべて採るので、より強く [充満部分圏](./full_subcategory.md) である。

一方、任意の圏 $`\mathcal{C}`$ に対し、すべての対象を残して同型射だけを残す部分圏を作れる。
これは $`\mathcal{C}`$ の最大部分群oidと呼ばれる。
この例は、部分圏が対象を減らす操作だけではないことを示す。

## 包含函手

部分圏のデータは、対象と射をそのまま送る函手

```math
i\colon\mathcal{D}\hookrightarrow\mathcal{C}
```

として表せる。
この包含函手は、各 Hom 集合への写像が単射であるという意味で忠実である。
ただし忠実函手が与えられたとき、その定義域が文字どおり部分圏として実現されているとは限らない。
部分圏という語は、ここで指定した対象と射の包含を伴う状況に用いる。
