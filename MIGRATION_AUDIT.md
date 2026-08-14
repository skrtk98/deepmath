# 草稿・Wiki 対応監査台帳

この台帳は、`drafts/` の草稿を `docs/wiki/` に移行する際の対応関係と内容照合を記録する。
各行の「確認事項」は、草稿にある定義、例、性質、図式、参考文献のうち、移行先で保持した項目または統合先を示す。
`照合済み` は、草稿を読み直して移行先の記述を確認済みであることを表す。
移行先が未作成または照合が未了の草稿は、完了として扱わない。

## 圏論の基礎構造

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- | --- |
| `drafts/source_and_target/index.md` | `docs/wiki/source_and_target.md` | 始域、終域、型が合う合成、恒等射、可換三角形 | 照合済み |
| `drafts/commuting_diagram/index.md` | `docs/wiki/commuting_diagram.md` | 可換図式の定義、経路の合成、三角形と四角形の例、TikZ 図式 | 照合済み |
| `drafts/universal_property/index.md` | `docs/wiki/universal_property.md` | 普遍性、存在と一意性、終対象、積、可換図式 | 照合済み |
| `drafts/functor/index.md` | `docs/wiki/functor.md` | 共変・反変函手、恒等射と合成の保存、例、忠実・充満・本質的全射 | 照合済み |
| `drafts/natural_transformation/index.md` | `docs/wiki/natural_transformation.md` | 自然変換、自然性四角形、垂直合成、水平合成、函手圏 | 照合済み |
| `drafts/adjoint_functor/index.md` | `docs/wiki/adjoint_functor.md` | Hom の自然同型、単位と余単位、三角恒等式、TikZ 図式、例 | 照合済み |
| `drafts/small_category/index.md` | `docs/wiki/small_category.md` | 小圏の定義、有限集合・有限群・終圏の例、局所小圏との区別、前層圏との関係 | 照合済み |
| `drafts/locally_small_category/index.md` | `docs/wiki/locally_small_category.md` | 局所小性、標準例、Hom 函手、表現可能函手と米田の補題への前提 | 照合済み |
| `drafts/subcategory/index.md` | `docs/wiki/subcategory.md` | 部分圏の対象・Hom・合成の条件、有限集合・可換群の例、包含函手 | 照合済み |
| `drafts/full_subcategory/index.md` | `docs/wiki/full_subcategory.md` | 充満性、可換群・コンパクト Hausdorff 空間の例、充満函手との関係 | 照合済み |
| `drafts/opposite_category/index.md` | `docs/wiki/opposite_category.md` | 反対圏の定義、前順序の例、二重反対、双対原理 | 照合済み |
| `drafts/monomorphism/index.md` | `docs/wiki/monomorphism.md` | 左消去則、集合・群の例、分裂モノ射、等化子、エピ射との双対性 | 照合済み |
| `drafts/epimorphism/index.md` | `docs/wiki/epimorphism.md` | 右消去則、集合・群の例、分裂エピ射、余等化子、モノ射との双対性 | 照合済み |
| `drafts/retraction/index.md` | `docs/wiki/retraction.md` | レトラクション、断面、分裂射、直積の例、同型射との区別、TikZ 図式 | 照合済み |
| `drafts/initial_object/index.md` | `docs/wiki/initial_object.md` | 始対象、空集合・整数環・最小元の例、同型を除く一意性、空図式の余極限 | 照合済み |
| `drafts/terminal_object/index.md` | `docs/wiki/terminal_object.md` | 終対象、一点集合・一点空間・最大元の例、同型を除く一意性、空図式の極限 | 照合済み |
| `drafts/zero_object/index.md` | `docs/wiki/zero_object.md` | 零対象、可換群・ベクトル空間の例、零射、核と余核への接続 | 照合済み |
| `drafts/limit/index.md` | `docs/wiki/limit.md` | 錐、極限、表現可能性、積・等化子・引き戻し、存在の一意性、右随伴による保存 | 照合済み |
| `drafts/colimit/index.md` | `docs/wiki/colimit.md` | 余錐、余極限、余積・余等化子・押し出し、存在の一意性、左随伴による保存 | 照合済み |
| `drafts/product_object/index.md` | `docs/wiki/product_object.md` | 二項積と一般積、普遍図式、集合・位相空間・半順序の例、有限積 | 照合済み |
| `drafts/equalizer/index.md` | `docs/wiki/equalizer.md` | 等化子の普遍性、TikZ 図式、集合・代数構造の例、モノ射性、一意性 | 照合済み |
| `drafts/pullback/index.md` | `docs/wiki/pullback.md` | 引き戻しの普遍性、TikZ 図式、集合と半順序の例、積・等化子による構成、押し出しとの双対性 | 照合済み |
| `drafts/kernel/index.md` | `docs/wiki/kernel.md` | 零射に関する普遍性、等化子としての記述、可換群の例、モノ射性、余核との双対性 | 照合済み |
| `drafts/cokernel/index.md` | `docs/wiki/cokernel.md` | 零射に関する普遍性、余等化子としての記述、可換群の例、エピ射性、核との双対性 | 照合済み |
| `drafts/representable_functor/index.md` | `docs/wiki/representable_functor.md` | 共変・反変の表現可能性、集合・群の例、普遍元、表現対象の一意性 | 照合済み |
| `drafts/yoneda_lemma/index.md` | `docs/wiki/yoneda_lemma.md` | 反変の米田対応、対応式、米田埋め込み、表現対象の一意性 | 照合済み |
| `drafts/category_equivalence/index.md` | `docs/wiki/category_equivalence.md` | 擬逆と自然同型、充満忠実かつ本質的全射による判定、骨格圏の例、圏同型との区別 | 照合済み |
| `drafts/comma_category/index.md` | `docs/wiki/comma_category.md` | 三つ組と可換条件による定義、スライス圏とコスライス圏の例、射影函手 | 照合済み |

## 体論

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- | --- |
| `drafts/algebraic_element/index.md` | `docs/wiki/algebraic_element.md` | 代数的元と超越的元、最小多項式、既約性と可除性、共役元、具体例 | 照合済み |

## ホモロジー代数

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- | --- |
| `drafts/exact_sequence/index.md` | `docs/wiki/exact_sequence.md` | 完全性、短完全系列、商加群の列、函手による完全性、分裂条件 | 照合済み |
| `drafts/chain_complex/index.md` | `docs/wiki/chain_complex.md` | 鎖複体、ホモロジー、単体複体と射影解消の例、完全複体 | 照合済み |
| `drafts/derived_functor/index.md` | `docs/wiki/derived_functor.md` | 左右導来関手、入射・射影解消、選択からの独立性、長完全系列 | 照合済み |
| `drafts/ext_and_tor/index.md` | `docs/wiki/ext_and_tor.md` | Ext と Tor の定義、短完全系列の分類、平坦性、整数加群の例 | 照合済み |

## 位相の基礎

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- | --- |
| `drafts/neighbourhood_system/index.md` | `docs/wiki/neighbourhood_system.md` | 近傍、フィルター性、近傍系と位相の相互復元、粗細の比較、連続性 | 照合済み |
| `drafts/topological_basis/index.md` | `docs/wiki/topological_basis.md` | 開基の条件、生成する位相、可算開基、開基の比較、有限共通部分による生成 | 照合済み |
| `drafts/closure_operator/index.md` | `docs/wiki/closure_operator.md` | 閉包作用素の公理、触点による特徴付け、閉包作用素と位相の相互復元 | 照合済み |

## 運用規則

各分野の移行前に、草稿の見出し、定義、仮定、例、命題、証明、可換図式、参考文献、内部リンクを一覧化する。
移行先では草稿の内容を削減せず、既存ページとの重複がある場合には情報を統合して参照先を明示する。
移行後には、記号と用語の一貫性、日本語の学術文体、タグ、内部リンク、MkDocs ビルドを確認する。
未対応の草稿を移行済みとして扱わず、この台帳に対応関係と照合結果を追記する。
