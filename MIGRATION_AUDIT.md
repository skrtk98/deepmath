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

## 運用規則

各分野の移行前に、草稿の見出し、定義、仮定、例、命題、証明、可換図式、参考文献、内部リンクを一覧化する。
移行先では草稿の内容を削減せず、既存ページとの重複がある場合には情報を統合して参照先を明示する。
移行後には、記号と用語の一貫性、日本語の学術文体、タグ、内部リンク、MkDocs ビルドを確認する。
未対応の草稿を移行済みとして扱わず、この台帳に対応関係と照合結果を追記する。
