---
tags:
  - 代数学/環論/体論
  - 多項式
  - 既約性
  - 生成
---

# 代数的元

## 定義

体の拡大 $`L/K`$ と元 $`\alpha\in L`$ を考える。

> [!definition] 代数的元
> $`\alpha`$ が **$`K`$ 上代数的** (*algebraic over $`K`$*) であるとは、$`f(\alpha)=0`$ を満たす零でない多項式 $`f(T)\in K[T]`$ が存在することである。
> $`K`$ 上代数的でない元を、$`K`$ 上**超越的** (*transcendental over $`K`$*) という。

## 最小多項式

> [!definition] 最小多項式
> $`K`$ 上代数的な元 $`\alpha`$ に対して、$`f(\alpha)=0`$ を満たすモニック多項式 $`f(T)\in K[T]`$ のうち次数が最小のものを、$`\alpha`$ の **$`K`$ 上の最小多項式** (*minimal polynomial*) という。

最小多項式は一意に定まり、既約多項式である。

また、$`\alpha`$ の最小多項式を $`m_{\alpha,K}(T)`$ とすると、任意の $`f(T)\in K[T]`$ について
```math
f(\alpha)=0
\quad\Longleftrightarrow\quad
m_{\alpha,K}(T)\mid f(T)
```
が成り立つ。

## 例

実数 $`\sqrt{2}`$ は、有理数体 $`\mathbb{Q}`$ 上の多項式 $`T^2-2`$ の根であるため、$`\mathbb{Q}`$ 上代数的である。

一方、円周率 $`\pi`$ は $`\mathbb{Q}`$ 上超越的である。
