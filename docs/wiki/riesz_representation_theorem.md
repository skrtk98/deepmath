---
tags:
  - 解析学
  - 関数解析
  - Hilbert 空間
  - 双対空間
  - 内積
---

# Riesz 表現定理

Riesz 表現定理は、Hilbert 空間の連続双対を内積によって表す定理である。

## 定理

> [!theorem] Riesz 表現定理
> 複素 Hilbert 空間 $`H`$ の内積が第一変数について線形であるとする。
> 任意の連続線形汎関数 $`\varphi\in H^*`$ に対し、一意な $`y\in H`$ が存在して、任意の $`x\in H`$ について
>
> ```math
> \varphi(x)=\langle x,y\rangle
> ```
>
> が成り立つ。
> さらに $`\lVert\varphi\rVert=\lVert y\rVert`$ である。

従って $`y\mapsto\langle-,y\rangle`$ は $`H`$ から $`H^*`$ への等長共役線形同型を与える。
実 Hilbert 空間では、この同型は線形である。

この定理は直交射影や弱位相の理論に用いられる。
Hilbert 空間については [Hilbert 空間](./hilbert_space.md) を参照されたい。
