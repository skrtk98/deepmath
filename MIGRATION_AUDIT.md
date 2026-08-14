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
| `drafts/cone/index.md` | `docs/wiki/cone.md` | 錐と余錐、自然変換による定式化、錐集合、極限・余極限との関係 | 照合済み |
| `drafts/filtered_category/index.md` | `docs/wiki/filtered_category.md` | フィルター付き圏、余フィルター付き圏、有向系、有限極限との可換性 | 照合済み |
| `drafts/monad/index.md` | `docs/wiki/monad.md` | 自己函手、単位と乗法、結合律と単位律、TikZ 図式、随伴、モノイド対象 | 照合済み |
| `drafts/kleisli_category/index.md` | `docs/wiki/kleisli_category.md` | Hom、合成、恒等射、Kleisli 随伴、Eilenberg–Moore 圏との比較 | 照合済み |
| `drafts/eilenberg_moore_category/index.md` | `docs/wiki/eilenberg_moore_category.md` | モナド代数、準同型、自由・忘却随伴、Kleisli 圏との比較 | 照合済み |
| `drafts/coimage/index.md` | `docs/wiki/coimage.md` | エピ射因子化、普遍性、核・余核、アーベル圏での像との関係、可換群の例 | 照合済み |
| `drafts/hom_set/index.md` | `docs/wiki/hom_set.md` | Hom 集合、局所小性、集合・群・前順序の例、豊穣 Hom と内部 Hom の区別 | 照合済み |
| `drafts/presheaf/index.md` | `docs/wiki/presheaf.md` | 前層、前層圏、米田埋め込み、点ごとの極限と余極限、表現可能前層 | 照合済み |
| `drafts/co_yoneda_lemma/index.md` | `docs/wiki/co_yoneda_lemma.md` | 余米田公式、コエンドでの同一視、表現可能前層による前層の標準表示、米田の補題との対応 | 照合済み |
| `drafts/kan_extension/index.md` | `docs/wiki/kan_extension.md` | 左右 Kan 拡張の普遍性、因子化、コンマ圏上の各点極限・余極限公式 | 照合済み |
| `drafts/pointwise_kan_extension/index.md` | `docs/wiki/pointwise_kan_extension.md` | 豊穣左・右各点公式、重みの向き、通常の圏におけるコンマ圏公式、コエンド・エンドとの接続 | 照合済み |
| `drafts/end_and_coend/index.md` | `docs/wiki/end_and_coend.md` | 楔・余楔、エンド・コエンドの普遍性、自然変換のエンド表示、余米田型コエンド、集合値コエンドの余等化子表示 | 照合済み |
| `drafts/dual_object/index.md` | `docs/wiki/dual_object.md` | 右双対の評価・余評価、三角恒等式と TikZ 図式、左双対、双対の一意性、有限次元ベクトル空間の例、剛モノイダル圏 | 照合済み |
| `drafts/monoid_object/index.md` | `docs/wiki/monoid_object.md` | モノイド対象、結合律 TikZ 図式、単位律、余モノイド対象、モノイド射、集合・位相・加群・自己函手圏の例 | 照合済み |
| `drafts/monoid_module_object/index.md` | `docs/wiki/monoid_module_object.md` | 左右加群対象、結合律 TikZ 図式、単位律、逆転モノイダル圏、作用するモノイダル圏上の加群対象 | 照合済み |
| `drafts/module_over_a_monoidal_category/index.md` | `docs/wiki/module_over_a_monoidal_category.md` | 両側加群圏、自己函手圏への強モノイダル函手、加群射、コヒーレンス、加群射の圏、作用圏への還元 | 照合済み |
| `drafts/semicategory/index.md` | `docs/wiki/semicategory.md` | 半圏の始域・終域・合成・結合律、圏との関係、一対象半圏、恒等射の自由付加と左随伴 | 照合済み |
| `drafts/internal_category/index.md` | `docs/wiki/internal_category.md` | 有限極限圏における内部圏、対象・射・合成の内部化、引き戻し、集合・位相・群・圏の例 | 照合済み |
| `drafts/product_category/index.md` | `docs/wiki/product_category.md` | 直積圏の対象・射・成分ごとの合成、射影函手、$`\mathsf{Cat}`$ における積の普遍性 | 照合済み |
| `drafts/coproduct_category/index.md` | `docs/wiki/coproduct_category.md` | 余積圏（直和圏）の対象・射、標準包含函手、$`\mathsf{Cat}`$ における余積の普遍性 | 照合済み |
| `drafts/monoidal_functor/index.md` | `docs/wiki/monoidal_functor.md` | ラックス構造、結合子とのコヒーレンス TikZ 図式、正規・強・厳格モノイダル函手 | 照合済み |
| `drafts/monoidal_natural_transformation/index.md` | `docs/wiki/monoidal_natural_transformation.md` | 構造射との可換条件、単位条件、モノイダル函手の圏、強モノイダル函手 | 照合済み |
| `drafts/closed_monoidal_category/index.md` | `docs/wiki/closed_monoidal_category.md` | 左右閉性、内部 Hom、評価・余評価、集合の例 | 照合済み |
| `drafts/braided_monoidal_category/index.md` | `docs/wiki/braided_monoidal_category.md` | 組紐、六角形公理、TikZ 図式、ベクトル空間の例 | 照合済み |
| `drafts/symmetric_monoidal_category/index.md` | `docs/wiki/symmetric_monoidal_category.md` | 対称性、集合・可換群・ベクトル空間の例、カルテシアン圏 | 照合済み |
| `drafts/enriched_functor/index.md` | `docs/wiki/enriched_functor.md` | Hom 対象の構造射、単位・合成の保存、集合・アーベル群の例、下部圏 | 照合済み |
| `drafts/enriched_natural_transformation/index.md` | `docs/wiki/enriched_natural_transformation.md` | 成分、豊穣自然性、合成、$`\mathcal{V}\text{-}\mathsf{Cat}`$、集合の場合 | 照合済み |

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
| `drafts/flat_module/index.md` | `docs/wiki/flat_module.md` | 平坦性、テンソル積、Tor による特徴付け、自由・射影・局所化の例 | 照合済み |
| `drafts/injective_module/index.md` | `docs/wiki/injective_module.md` | 延長性、Hom の完全性、入射解消、導来関手、可除アーベル群の例 | 照合済み |

## 位相の基礎

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- | --- |
| `drafts/neighbourhood_system/index.md` | `docs/wiki/neighbourhood_system.md` | 近傍、フィルター性、近傍系と位相の相互復元、粗細の比較、連続性 | 照合済み |
| `drafts/topological_basis/index.md` | `docs/wiki/topological_basis.md` | 開基の条件、生成する位相、可算開基、開基の比較、有限共通部分による生成 | 照合済み |
| `drafts/closure_operator/index.md` | `docs/wiki/closure_operator.md` | 閉包作用素の公理、触点による特徴付け、閉包作用素と位相の相互復元 | 照合済み |
| `drafts/hausdorff_space/index.md` | `docs/wiki/hausdorff_space.md` | Hausdorff 条件、極限の一意性、コンパクト部分集合、対角の閉性、距離空間 | 照合済み |
| `drafts/dense_subset/index.md` | `docs/wiki/dense_subset.md` | 閉包による定義、非空開集合との交わり、有理数の例 | 照合済み |
| `drafts/interior_point/index.md` | `docs/wiki/interior_point.md` | 内点、内部、最大開集合、近傍系と内部作用素 | 照合済み |
| `drafts/exterior_point/index.md` | `docs/wiki/exterior_point.md` | 外点、補集合の内部、近傍による特徴付け | 照合済み |
| `drafts/boundary_point/index.md` | `docs/wiki/boundary_point.md` | 境界点、境界、閉包による表示、内部との分解 | 照合済み |
| `drafts/cluster_point/index.md` | `docs/wiki/cluster_point.md` | 触点、近傍による定義、閉包との一致 | 照合済み |
| `drafts/accumulation_point/index.md` | `docs/wiki/accumulation_point.md` | 集積点、極限点、導集合、触点による定義 | 照合済み |
| `drafts/isolated_point/index.md` | `docs/wiki/isolated_point.md` | 孤立点、集積点の否定、近傍による特徴付け | 照合済み |
| `drafts/closed_map/index.md` | `docs/wiki/closed_map.md` | 閉写像、合成、ファイバーによる判定、コンパクトから Hausdorff への連続写像との関係 | 照合済み |
| `drafts/neighbourhood_basis/index.md` | `docs/wiki/neighbourhood_basis.md` | 近傍基、生成する近傍系、開基との相互構成、粗細の比較 | 照合済み |
| `drafts/interior_operator/index.md` | `docs/wiki/interior_operator.md` | 開核作用素の公理、位相空間の内部、開核作用素からの位相の復元、閉包作用素との双対 | 照合済み |
| `drafts/open_map/index.md` | `docs/wiki/open_map.md` | 開写像、合成、閉包と逆像による判定 | 照合済み |
| `drafts/homeomorphism/index.md` | `docs/wiki/homeomorphism.md` | 同相写像、開・閉写像による判定、コンパクトから Hausdorff への連続全単射 | 照合済み |
| `drafts/topological_embedding/index.md` | `docs/wiki/topological_embedding.md` | 位相的埋め込み、像への制限、全単射の場合、相互埋め込みから同相性は従わない点の訂正 | 照合済み |
| `drafts/product_topological_space/index.md` | `docs/wiki/product_topological_space.md` | 積位相、部分基と基本開集合、射影の普遍性、近傍基、射影の開性、閉包、積写像 | 照合済み |

## 解析学と関数解析

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- | --- |
| `drafts/metric_space/index.md` | `docs/wiki/metric_space.md` | 距離の公理、離散距離、誘導位相、擬距離、距離等化、測度による例 | 照合済み |
| `drafts/normed_space/index.md` | `docs/wiki/normed_space.md` | ノルムの公理、誘導距離、有限次元の例 | 照合済み |
| `drafts/banach_space/index.md` | `docs/wiki/banach_space.md` | 完備性、Cauchy 列、有限次元、$`\ell^p`$、$`L^p`$、$`C(K)`$ の例 | 照合済み |

## 微分幾何

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- | --- |
| `drafts/manifold/index.md` | `docs/wiki/manifold.md` | 位相多様体、滑らかアトラス、球面・トーラス・Lie 群、接束と微分形式 | 照合済み |
| `drafts/tangent_bundle/index.md` | `docs/wiki/tangent_bundle.md` | 接束、ユークリッド空間の自明化、ベクトル場、大域的非自明性 | 照合済み |
| `drafts/cotangent_bundle/index.md` | `docs/wiki/cotangent_bundle.md` | 余接束、ユークリッド空間の自明化、1-形式、標準シンプレクティック形式 | 照合済み |
| `drafts/differential_form/index.md` | `docs/wiki/differential_form.md` | $`k`$-形式、外微分、$`df`$、面積・体積形式、Stokes の定理 | 照合済み |

## 運用規則

各分野の移行前に、草稿の見出し、定義、仮定、例、命題、証明、可換図式、参考文献、内部リンクを一覧化する。
移行先では草稿の内容を削減せず、既存ページとの重複がある場合には情報を統合して参照先を明示する。
移行後には、記号と用語の一貫性、日本語の学術文体、タグ、内部リンク、MkDocs ビルドを確認する。
未対応の草稿を移行済みとして扱わず、この台帳に対応関係と照合結果を追記する。
