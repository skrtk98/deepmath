---
tags:
  - 幾何学/微分幾何学
  - 接続
  - 接束
  - 曲率
---

# アフィン接続

アフィン接続は、異なる点にある接空間のベクトルを比較する規則である。
共変微分、平行移動、曲率を定める。

以下で $`M`$ を滑らかな多様体とし、$`\mathfrak{X}(M)`$ を滑らかなベクトル場全体とする。

## 定義

> [!definition] アフィン接続
> **アフィン接続**とは、$`\mathbb{R}`$-双線形写像
>
> ```math
> \nabla\colon\mathfrak{X}(M)\times\mathfrak{X}(M)
> \longrightarrow\mathfrak{X}(M),
> \qquad
> (X,Y)\longmapsto\nabla_XY
> ```
>
> であって、任意の $`f\in C^\infty(M)`$ と $`X,Y\in\mathfrak{X}(M)`$ に対し
>
> ```math
> \nabla_{fX}Y=f\nabla_XY,
> \qquad
> \nabla_X(fY)=X(f)Y+f\nabla_XY
> ```
>
> を満たすものである。

局所座標 $`(x^1,\ldots,x^n)`$ では、係数 $`\Gamma^k_{ij}`$ を

```math
\nabla_{\partial_i}\partial_j
=
\sum_k\Gamma^k_{ij}\partial_k
```

で定める。
これらを Christoffel 記号という。

## 捩率と曲率

アフィン接続の **捩率** と **曲率** は、それぞれ

```math
T(X,Y)=\nabla_XY-\nabla_YX-[X,Y],
```

```math
R(X,Y)Z
=
\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z
```

で定める。

Riemann 計量が与えられるとき、捩率が零で計量と両立するアフィン接続が一意に存在する。
これを Levi–Civita 接続という。
接束については [接束](./tangent_bundle.md) を参照されたい。
