---
tags:
  - 幾何学/位相幾何学
  - 積
  - 開集合
  - 近傍
---

# 積位相空間

積位相は、各座標への射影を連続にする最も粗い位相である。

## 定義

位相空間の族 $`(X_\lambda)_{\lambda\in\Lambda}`$ に対し、集合としての直積を

```math
X=\prod_{\lambda\in\Lambda}X_\lambda
```

と書く。

> [!definition] 積位相
> $`X`$ 上の **積位相** とは、各射影 $`p_\lambda\colon X\to X_\lambda`$ を連続にする最も粗い位相である。
> この位相を備えた空間を **積空間** という。

積位相は、部分基

```math
\{p_\lambda^{-1}(G)\mid \lambda\in\Lambda,\ G\subseteq X_\lambda\text{ は開}
\}
```

で生成される。
したがって基本開集合は、有限個の添字 $`\lambda_1,\ldots,\lambda_n`$ と開集合 $`G_i\subseteq X_{\lambda_i}`$ を用いて

```math
\bigcap_{i=1}^n p_{\lambda_i}^{-1}(G_i)
```

と表される。

## 普遍性と近傍基

位相空間 $`Y`$ と写像 $`f\colon Y\to X`$ に対し、$`f`$ が連続であることと、すべての $`\lambda`$ で $`p_\lambda\circ f`$ が連続であることは同値である。

点 $`x=(x_\lambda)\in X`$ において、各 $`X_\lambda`$ の $`x_\lambda`$ における近傍基を $`\mathcal{U}_\lambda(x_\lambda)`$ とする。
このとき、有限個の添字について選んだ近傍の逆像の共通部分

```math
\bigcap_{i=1}^n p_{\lambda_i}^{-1}(U_i),
\qquad U_i\in\mathcal{U}_{\lambda_i}(x_{\lambda_i})
```

全体は $`x`$ における積空間の近傍基をなす。

## 基本性質

各射影 $`p_\lambda`$ は開写像である。
部分集合 $`A_\lambda\subseteq X_\lambda`$ に対して、積空間における閉包は

```math
\overline{\prod_{\lambda\in\Lambda}A_\lambda}
=
\prod_{\lambda\in\Lambda}\overline{A_\lambda}
```

を満たす。

各写像 $`f_\lambda\colon X_\lambda\to Y_\lambda`$ が連続ならば、積写像

```math
\prod_{\lambda\in\Lambda}f_\lambda
\colon
\prod_{\lambda\in\Lambda}X_\lambda
\longrightarrow
\prod_{\lambda\in\Lambda}Y_\lambda
```

は連続である。
各 $`f_\lambda`$ が位相的埋め込み、または同相写像であれば、積写像もそれぞれ位相的埋め込み、または同相写像である。

開写像については [開写像](./open_map.md) を、近傍基については [近傍基](./neighbourhood_basis.md) を参照されたい。
