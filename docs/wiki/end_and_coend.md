---
tags:
  - 圏論
  - 極限と余極限
  - 函手圏
  - 自然変換
---

# エンドとコエンド

エンドとコエンドは、二変数函手の対角成分を、二つの変数に関する作用が両立するようにまとめる構成である。
自然変換、重み付き極限と余極限、Kan 拡張の公式に現れる。

以下で $`T\colon\mathcal{C}^{\mathrm{op}}\times\mathcal{C}\to\mathcal{D}`$ を函手とする。

## 楔とエンド

> [!definition] 楔
> **楔**とは、対象 $`E\in\mathcal{D}`$ と射族 $`\omega_c\colon E\to T(c,c)`$ の組であって、任意の射 $`f\colon c\to c'`$ に対して
>
> ```math
> T(1_c,f)\circ\omega_c
> =
> T(f,1_{c'})\circ\omega_{c'}
> ```
>
> を満たすものである。

> [!definition] エンド
> **エンド**とは、$`T`$ 上の楔の圏における終対象である。
> 存在するとき、エンドを
>
> ```math
> \int_{c\in\mathcal{C}}T(c,c)
> ```
>
> と書く。

エンドへの射は、各対角成分への射であって、射 $`f`$ による反変作用と共変作用を両立させるものに一致する。

## 余楔とコエンド

> [!definition] 余楔
> **余楔**とは、対象 $`W\in\mathcal{D}`$ と射族 $`\nu_c\colon T(c,c)\to W`$ の組であって、任意の $`f\colon c\to c'`$ に対して
>
> ```math
> \nu_{c'}\circ T(1_c,f)
> =
> \nu_c\circ T(f,1_{c'})
> ```
>
> を満たすものである。

> [!definition] コエンド
> **コエンド**とは、$`T`$ 上の余楔の圏における始対象である。
> 存在するとき、コエンドを
>
> ```math
> \int^{c\in\mathcal{C}}T(c,c)
> ```
>
> と書く。

コエンドはエンドの双対概念である。

## 代表例

圏 $`\mathcal{B}`$ が局所小であり、必要なエンドが存在するとする。
函手 $`F,G\colon\mathcal{A}\to\mathcal{B}`$ に対し、自然変換の集合は

```math
\operatorname{Nat}(F,G)
\cong
\int_{a\in\mathcal{A}}\mathcal{B}(F(a),G(a))
```

と表される。
楔条件は、自然変換の自然性条件に一致する。

前層 $`X\colon\mathcal{C}^{\mathrm{op}}\to\mathsf{Set}`$ には、余米田の補題により

```math
X
\cong
\int^{c\in\mathcal{C}}X(c)\times y(c)
```

というコエンド表示がある。
ここで $`y(c)=\mathcal{C}(-,c)`$ である。

## 集合値の場合の計算

$`T\colon\mathcal{C}^{\mathrm{op}}\times\mathcal{C}\to\mathsf{Set}`$ に対し、コエンドは余等化子

```math
\coprod_{f\colon c\to c'}T(c',c)
\rightrightarrows
\coprod_{c\in\mathcal{C}}T(c,c)
\longrightarrow
\int^{c\in\mathcal{C}}T(c,c)
```

として計算できる。
二つの矢印はそれぞれ $`T(f,1_c)`$ と $`T(1_{c'},f)`$ から誘導される。

双対的に、エンドは適切な積の間の等化子として計算できる。
余米田の補題については [余米田の補題](./co_yoneda_lemma.md) を参照されたい。
