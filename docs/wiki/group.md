# 群

## 定義

> [!definition] 群
> **集合 $`G`$ 上の群構造** (*group structure on a set $`G`$*) とは、以下のデータ
>
> - 二項演算 $`\,\cdot\,\colon G\times G\to G`$, $`(a,b)\mapsto a\cdot b`$,
> - 逆元写像 $`\iota\colon G\to G`$, $`a\mapsto a^{-1}`$,
> - 単位元 $`e\in G`$,
>
> からなり、**群の公理** (*group axioms*) と呼ばれる次の条件を満たすときいう：
>
> - 結合律：任意の $`a,b,c\in G`$ に対して $`(a\cdot b)\cdot c=a\cdot(b\cdot c)`$,
> - 単位律：任意の $`a\in G`$ に対して $`a\cdot e=e\cdot a=a`$,
> - 逆元律：任意の $`a\in G`$ に対して $`a\cdot\iota(a)=\iota(a)\cdot a=e`$.
>
> 集合 $`G`$ と $`G`$ 上の群構造 $`(\,\cdot\,, \iota, e)`$ の組 $`(G; \,\cdot\,, \iota, e)`$ を**群** (*group*) といい、集合 $`G`$ をこの群の**台集合** (*underlying set*) という。

> [!proposition] 単位元と逆元の一意性
> 群において単位元は一意であり、各元の逆元も一意である。
> すなわち、台集合と演算が一致するような任意の 2 つの群 $`(G; \,\cdot\,, \iota, e)`$, $`(G; \,\cdot\,, \iota', e')`$ に対して、$`e=e'`$ かつ $`\iota=\iota'`$ が成り立つ。

> [!proof]
> 台集合と演算が一致するような 2 つの群 $`G_1 = (G; \,\cdot\,, \iota, e)`$, $`G_2 = (G; \,\cdot\,, \iota', e')`$ を任意に取り固定する。
> - $`e=e'`$ について
>   $`G_1`$ の単位律より $`e'\cdot e = e'`$ となり、$`G_2`$ の単位律より $`e'\cdot e = e`$ なため、$`e = e'\cdot e = e'`$ を得る。
>
> - $`\iota=\iota'`$ について
>   任意の $`a\in G`$ に対して、
>   ```math
>   \begin{align*}
>   \iota(a)
>   &=\iota(a)\cdot e'&\text{$G_2$ の単位律}\\
>   &=\iota(a)\cdot(a\cdot\iota'(a))&\text{$G_2$ の逆元律}\\
>   &=(\iota(a)\cdot a)\cdot\iota'(a)&\text{結合律}\\
>   &=e\cdot\iota'(a)&\text{$G_1$ の逆元律}\\
>   &=\iota'(a)&\text{$G_1$ の単位律}
>   \end{align*}
>   ```
>   であるため、$`\iota=\iota'`$ を得る。

この命題から、群の定義は次のように整理できる。

> [!definition] 群
> 群とは、集合 $`G`$ と二項演算 $`\,\cdot\,\colon G\times G\to G`$, $`(a,b)\mapsto a\cdot b`$ の組 $`(G,\,\cdot\,)`$ であって、次の条件を満たす：
>
> - 結合律：任意の $`a,b,c\in G`$ に対して $`(a\cdot b)\cdot c=a\cdot(b\cdot c)`$,
> - 単位元の存在：$`\exists e\in G\text{ s.t. }\forall a\in G,a\cdot e=e\cdot a=a`$,
> - 逆元の存在：$`\forall a\in G,\exists b\in G\text{ s.t. }a\cdot b=b\cdot a=e`$.

群 $`G`$ が [アーベル群 (*abelian group*)](./abelian_group.md) であるとは、2 つの元の積をとる順序が可換であるような群のことである。すなわち、次の可換性を満たす:
```math
\forall a,b\in G,a\cdot b = b\cdot a
```

