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
| `drafts/local_homeomorphism/index.md` | `docs/wiki/local_homeomorphism.md` | 局所同相写像、開写像性、全射性・単射性を要しない点、被覆写像との関係 | 照合済み |
| `drafts/covering_space/index.md` | `docs/wiki/covering_space.md` | 被覆写像、シートへの分解、局所同相、経路・ホモトピー持ち上げ、円周とトーラスの例、分類定理の仮定 | 照合済み |
| `drafts/section/index.md` | `docs/wiki/retraction.md` | 断面、分裂モノ射、直積射影の断面、レトラクションとの関係 | 照合済み |
| `drafts/compact-open_topology/index.md` | `docs/wiki/compact_open_topology.md` | コンパクト開位相、部分基、正しい型の Curry 化と逆 Curry 化、評価写像の連続性に必要な局所コンパクト性条件 | 照合済み |
| `drafts/net/index.md` | `docs/wiki/net.md` | 有向集合、ネット、部分ネット、最終的・しばしば含まれること、普遍ネット、収束、集積点、閉包の特徴付け | 照合済み |
| `drafts/weak_topology/index.md` | `docs/wiki/weak_topology.md` | 始位相、部分基、連続写像による普遍性、積位相、関数解析の弱位相との区別 | 照合済み |
| `drafts/strong_topology/index.md` | `docs/wiki/strong_topology.md` | 終位相、開集合による特徴付け、連続写像による普遍性、商位相、関数解析の強位相との区別 | 照合済み |
| `drafts/nowhere_dense_subset/index.md` | `docs/wiki/nowhere_dense_subset.md` | どこにも稠密でない集合、閉包の内部による定義、非空開集合による同値条件 | 照合済み |
| `drafts/homotopy/index.md` | `docs/wiki/homotopy.md` | ホモトピー、ホモトピー同値、凸集合の変形収縮、基本群・ホモロジーのホモトピー不変性 | 照合済み |
| `drafts/fundamental_group/index.md` | `docs/wiki/fundamental_group.md` | 基本群、端点固定ホモトピー、連結積、球面・トーラスの例、被覆空間との関係 | 照合済み |
| `drafts/homology/index.md` | `docs/wiki/homology.md` | 鎖複体のホモロジー、サイクル・バウンダリー、特異ホモロジー、ホモトピー不変性 | 照合済み |
| `drafts/constant_morphism/index.md` | `docs/wiki/constant_morphism.md` | 左右定値射、零射圏の零射との区別、零対象を通る射の例 | 照合済み |
| `drafts/hom_functor/index.md` | `docs/wiki/hom_functor.md` | Hom 二変数函手、合成による作用、固定変数版、表現可能前層、極限・余極限との関係 | 照合済み |
| `drafts/final_functor/index.md` | `docs/wiki/final_functor.md` | 終函手・始函手、コンマ圏による判定、余極限・極限の添字圏の置換 | 照合済み |
| `drafts/pseudofunctor/index.md` | `docs/wiki/pseudofunctor.md` | 擬函手、Hom 圏上の函手、合成・単位比較2-射、コヒーレンス、厳密2-函手 | 照合済み |
| `drafts/categorification/index.md` | `docs/wiki/categorification.md` | 圏化・脱圏化、集合・関数・等式との対応、有限集合の例、コヒーレンス、高次圏との関係 | 照合済み |
| `drafts/higher_category_theory/index.md` | `docs/wiki/higher_category_theory.md` | 高次圏、準圏・Segal 圏・opetopic/globular モデル、Quillen 同値、2圏・双圏、主要トピック | 照合済み |
| `drafts/traced_monoidal_category/index.md` | `docs/wiki/traced_monoidal_category.md` | 右・左トレース、tightening・sliding・vanishing・strength、公理、有限次元ベクトル空間の例 | 照合済み |
| `drafts/segal_category/index.md` | `docs/wiki/segal_category.md` | Segal 条件、Segal 圏・Segal 空間、通常圏の nerve、ループ空間との接続 | 照合済み |
| `drafts/opetopic_higher_category/index.md` | `docs/wiki/opetopic_higher_category.md` | オペトープ、合成形状、opetopic 高次圏、充填条件によるコヒーレンス | 照合済み |
| `drafts/weighted_colimit_enriched/index.md` | `docs/wiki/weighted_colimit_enriched.md` | 重み付き極限・余極限、通常の余極限、コエンド公式、各点 Kan 拡張との関係 | 照合済み |
| `drafts/enriched_kan_extension/index.md` | `docs/wiki/enriched_kan_extension.md` | 左右豊穣 Kan 拡張、豊穣自然変換の普遍性、重み付き余極限による各点公式 | 照合済み |
| `drafts/enriched_yoneda_lemma/index.md` | `docs/wiki/enriched_yoneda_lemma.md` | 豊穣米田埋め込み、Hom 対象による補題、テンソル表示、余米田型の表現可能前層表示 | 照合済み |
| `drafts/enriched_cauchy_completion/index.md` | `docs/wiki/enriched_cauchy_completion.md` | 絶対重み、小射影前層、Cauchy 完成、普遍性、$`\mathsf{Set}`$ における冪等分解完成 | 照合済み |
| `drafts/enriched_small_projective_morita/index.md` | `docs/wiki/enriched_small_projective_morita.md` | 小射影前層、豊穣前層圏による Morita 同値、Cauchy 完成による判定、$`\mathsf{Set}`$ の場合 | 照合済み |
| `drafts/enriched_density/index.md` | `docs/wiki/enriched_density.md` | 標準重み付き余極限、制限米田函手、充満忠実性による判定、Kan 拡張、米田埋め込みの稠密性 | 照合済み |
| `drafts/enriched_functor_category/index.md` | `docs/wiki/enriched_functor_category.md` | エンドによる Hom 対象、下部圏と豊穣自然変換、内部 Hom としての普遍性、豊穣前層圏 | 照合済み |
| `drafts/enriched_adjoint_equivalence/index.md` | `docs/wiki/enriched_adjoint_equivalence.md` | Hom 対象の自然同型、単位・余単位と三角恒等式、下部圏随伴、豊穣同値、$`\mathsf{Set}`$・$`2`$・$`\mathsf{Cat}`$ の例 | 照合済み |
| `drafts/enriched_free_cocompletion/index.md` | `docs/wiki/enriched_free_cocompletion.md` | 前層圏の豊穣自由余完備性、余極限保存函手の分類、米田拡張のコエンド公式、Kan 拡張、小前層へのサイズ制限 | 照合済み |
| `drafts/universal_property_in_2_category/index.md` | `docs/wiki/universal_property_in_2_category.md` | 2 圏・双圏での随伴、左・右 Kan 拡張、コンマ対象、Hom 圏同値による普遍性、TikZ 図式 | 照合済み |
| `drafts/comma_object_2_category/index.md` | `docs/wiki/universal_property_in_2_category.md` | コンマ対象の Hom 圏による普遍性、2 射レベルの充満忠実性、双圏での擬普遍性、iso-comma 対象 | 照合済み |
| `drafts/enriched_over_bicategory/index.md` | `docs/wiki/enriched_over_bicategory.md` | extent、双圏の 1 射による Hom、単位・合成 2 射、コヒーレンス、1 対象双圏と通常の豊穣圏、$`\mathsf{Prof}`$ の例 | 照合済み |
| `drafts/special_adjoint_functor_theorem/index.md` | `docs/wiki/adjoint_functor.md` | 特殊随伴函手定理、完備性・局所小性・well-powered 性・余生成集合、極限保存性、双対形 | 照合済み |
| `drafts/enriched_strict_2_category/index.md` | `docs/wiki/bicategory.md` | $`\mathcal{V}\text{-}\mathsf{Cat}`$ の 0・1・2 射、垂直・水平合成、交換法則、$`\mathsf{Set}`$ における $`\mathsf{Cat}`$ | 照合済み |
| `drafts/enriched_universal_morphism/index.md` | `docs/wiki/enriched_universal_morphism.md` | 豊穣普遍射、Hom 対象の自然同型、双対形、豊穣随伴の対象ごとの存在判定、通常の普遍射との対応 | 照合済み |
| `drafts/enriched_presheaf_module/index.md` | `docs/wiki/enriched_free_cocompletion.md` | 豊穣前層圏、点ごとの左加群作用、米田埋め込み、自由余完備性、重み付き余極限による拡張 | 照合済み |
| `drafts/benabou_cosmos_enrichment/index.md` | `docs/wiki/benabou_cosmos_enrichment.md` | cosmos の仮定、豊穣函手圏のエンド、コエンドによる重み付き余極限、米田・Kan 拡張、$`\mathsf{Set}`$・$`\mathsf{sSet}`$ の例 | 照合済み |
| `drafts/protocategory/index.md` | `docs/wiki/protocategory.md` | 原射と source-target・合成関係による提示、Hom 集合、通常の圏との情報量の差、関数グラフの例 | 照合済み |
| `drafts/Introduction-to-Category-Theory.md` | `docs/wiki/category_theory_overview.md` | 圏論の目的、基礎概念から普遍性・随伴・極限への学習導線、日本語を含む参考文献 | 照合済み |
| `drafts/Introduction-to-Monoidal-Category-Theory.md` | `docs/wiki/monoidal_category_overview.md` | テンソル積の役割、モノイダル構造・組紐・対称性・閉性・双対性への学習導線、参考文献 | 照合済み |
| `drafts/Introduction-to-Enriched-Categor-over-Monoidal-base-Theory.md` | `docs/wiki/enriched_category_overview.md` | モノイダル基底上の豊穣圏、例、基礎から米田・重み付き余極限・Kan 拡張への学習導線、参考文献 | 照合済み |
| `drafts/measurable_function/index.md` | `docs/wiki/measurable_function.md` | 可測関数、Borel 可測性、連続関数と指示関数の例、点ごとの極限、単関数近似 | 照合済み |
| `drafts/orthonormal_basis/index.md` | `docs/wiki/orthonormal_basis.md` | 正規直交系・基底、ノルム収束による展開、非可算添字の和、Parseval 等式 | 照合済み |
| `drafts/riesz_representation_theorem/index.md` | `docs/wiki/riesz_representation_theorem.md` | Riesz 表現定理、内積の線形変数、等長共役線形同型、実 Hilbert 空間の場合 | 照合済み |
| `drafts/metric_topology/index.md` | `docs/wiki/metric_space.md` | 開球による近傍基と距離位相、位相的同値、可分性・第2可算性・Lindelöf 性、コンパクト性の同値 | 照合済み |
| `drafts/metrizable_topological_space/index.md` | `docs/wiki/metrizable_topological_space.md` | 距離化可能性、同相不変性、必要条件、正則第2可算空間に対する距離化定理 | 照合済み |
| `drafts/operator_norm/index.md` | `docs/wiki/operator_norm.md` | 作用素ノルム、最小の有界定数、基本評価、劣乗法性、作用素空間の完備性 | 照合済み |
| `drafts/compact_operator/index.md` | `docs/wiki/compact_operator.md` | コンパクト作用素、任意の有界集合による特徴付け、有限階作用素、ノルム閉性、スペクトル定理との接続 | 照合済み |
| `drafts/self_adjoint_operator/index.md` | `docs/wiki/self_adjoint_operator.md` | 稠密定義自己共役作用素、有界の場合の内積による特徴付け、実スペクトル、スペクトル定理 | 照合済み |
| `drafts/extension_field/index.md` | `docs/wiki/field_extension.md` | 拡大体・中間体・拡大次数・有限次拡大、塔の法則と基底による説明 | 照合済み |
| `drafts/dedekind_domain/index.md` | `docs/wiki/dedekind_domain.md` | Dedekind 整域、非零イデアルの一意分解、分数イデアル、類群、主イデアル整域と代数体整数環の例 | 照合済み |
| `drafts/extension_field/index.md` | `docs/wiki/field_extension.md` | 拡大体、基礎体、中間体、拡大次数、有限次・無限次拡大、塔の法則 | 照合済み |
| `drafts/affine_connection/index.md` | `docs/wiki/affine_connection.md` | アフィン接続、$`C^\infty(M)`$-線形性と Leibniz 則、Christoffel 記号、捩率、曲率、Levi–Civita 接続 | 照合済み |
| `drafts/geodesic/index.md` | `docs/wiki/geodesic.md` | 測地線方程式、局所座標表示、初期値問題、測地的完備性、Hopf–Rinow 定理の適用範囲 | 照合済み |
| `drafts/complex_manifold/index.md` | `docs/wiki/complex_manifold.md` | 複素多様体、複素アトラスと双正則遷移写像、実次元、複素射影空間と Riemann 面の例 | 照合済み |
| `drafts/symplectic_manifold/index.md` | `docs/wiki/symplectic_manifold.md` | シンプレクティック多様体、閉性と非退化性、偶数次元、標準形式、余接束の標準形式 | 照合済み |
| `drafts/smooth_manifold/index.md` | `docs/wiki/manifold.md` | 滑らかアトラスと最大アトラス、滑らか多様体、射影空間を含む例 | 照合済み |
| `drafts/oppposite_group/index.md` | `docs/wiki/opposite_group.md` | 反対群、積の反転、逆元写像による同型 | 照合済み |

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

## 既存同名ページの対応確認

| 草稿 | 移行先 | 確認事項 | 状態 |
| --- | --- | --- |
| `drafts/algebraic_extension/index.md` | `docs/wiki/algebraic_extension.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/algebraically_closed_field/index.md` | `docs/wiki/algebraically_closed_field.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/bicategory/index.md` | `docs/wiki/bicategory.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/bilinear_map/index.md` | `docs/wiki/bilinear_map.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/bounded_operator/index.md` | `docs/wiki/bounded_operator.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/compact_space/index.md` | `docs/wiki/compact_space.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/connected_space/index.md` | `docs/wiki/connected_space.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/continuous_map/index.md` | `docs/wiki/continuous_map.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/enriched_category/index.md` | `docs/wiki/enriched_category.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/enriched_module_functor/index.md` | `docs/wiki/enriched_module_functor.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/euclidean_domain/index.md` | `docs/wiki/euclidean_domain.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/field/index.md` | `docs/wiki/field.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/field_extension/index.md` | `docs/wiki/field_extension.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/free_module/index.md` | `docs/wiki/free_module.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/function/index.md` | `docs/wiki/function.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/group_action/index.md` | `docs/wiki/group_action.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/group_homomorphism/index.md` | `docs/wiki/group_homomorphism.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/group_representation/index.md` | `docs/wiki/group_representation.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/hilbert_space/index.md` | `docs/wiki/hilbert_space.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/ideal_in_rings/index.md` | `docs/wiki/ideal_in_rings.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/image/index.md` | `docs/wiki/image.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/integral_domain/index.md` | `docs/wiki/integral_domain.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/inverse_morphism/index.md` | `docs/wiki/inverse_morphism.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/isomorphism/index.md` | `docs/wiki/isomorphism.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/linear_map/index.md` | `docs/wiki/linear_map.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/local_ring/index.md` | `docs/wiki/local_ring.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/localization_of_ring/index.md` | `docs/wiki/localization_of_ring.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/measure_space/index.md` | `docs/wiki/measure_space.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/module_over_a_ring/index.md` | `docs/wiki/module_over_a_ring.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/monoid_action/index.md` | `docs/wiki/monoid_action.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/monoid_homomorphism/index.md` | `docs/wiki/monoid_homomorphism.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/monoidal_category/index.md` | `docs/wiki/monoidal_category.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/natural_isomorphism/index.md` | `docs/wiki/natural_isomorphism.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/noetherian_ring/index.md` | `docs/wiki/noetherian_ring.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/opposite_monoid/index.md` | `docs/wiki/opposite_monoid.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/principal_ideal_domain/index.md` | `docs/wiki/principal_ideal_domain.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/projective_module/index.md` | `docs/wiki/projective_module.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/quasi_category/index.md` | `docs/wiki/quasi_category.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/riemann_curvature_tensor/index.md` | `docs/wiki/riemann_curvature_tensor.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/riemannian_metric/index.md` | `docs/wiki/riemannian_metric.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/ring/index.md` | `docs/wiki/ring.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/ring_homomorphism/index.md` | `docs/wiki/ring_homomorphism.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/spectral_theorem/index.md` | `docs/wiki/spectral_theorem.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/subfield/index.md` | `docs/wiki/subfield.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/submonoid/index.md` | `docs/wiki/submonoid.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/subring/index.md` | `docs/wiki/subring.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/tensor_product_of_modules/index.md` | `docs/wiki/tensor_product_of_modules.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/topological_space/index.md` | `docs/wiki/topological_space.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/topological_subspace/index.md` | `docs/wiki/topological_subspace.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/unique_factorization_domain/index.md` | `docs/wiki/unique_factorization_domain.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |
| `drafts/vector_bundle/index.md` | `docs/wiki/vector_bundle.md` | 同名 Wiki 記事への既存移行を確認。定義、例、性質、タグ、内部リンクは最終監査の対象とする。 | 照合済み |

各分野の移行前に、草稿の見出し、定義、仮定、例、命題、証明、可換図式、参考文献、内部リンクを一覧化する。
移行先では草稿の内容を削減せず、既存ページとの重複がある場合には情報を統合して参照先を明示する。
移行後には、記号と用語の一貫性、日本語の学術文体、タグ、内部リンク、MkDocs ビルドを確認する。
未対応の草稿を移行済みとして扱わず、この台帳に対応関係と照合結果を追記する。
