# DeepMath

DeepMath は、数学ドキュメントを `MkDocs` + `Material for MkDocs` で管理・公開するためのリポジトリです。

## 構成

- `docs/`: ドキュメント本体
- `mkdocs.yml`: 本番用設定（ナビゲーション・プラグイン設定）
- `mkdocs.dev.yml`: 開発用設定
- `plugins/`: カスタム MkDocs プラグイン
- `docs/assets/scss/`, `docs/assets/css/`: スタイル
- `.source/`: 参考資料・ソースデータ

## セットアップ

### 1. Python 依存関係

```bash
uv sync
```

### 2. Node.js 依存関係（CSS ビルド用）

```bash
npm install
```

## ドキュメントのビルド

```bash
mkdocs build
```

生成物は `site/` に出力されます。

## ローカルプレビュー

```bash
mkdocs serve
```

監視モード:

```bash
mkdocs serve --livereload
```

デフォルトでは `http://127.0.0.1:8000` で確認できます。

## CSS の手動ビルド

```bash
npm run build:css
```

監視モード:

```bash
npm run watch:css
```

## 運用メモ

- Python スクリプト実行時は `uv run ...` を使用してください。
- `mkdocs build` の際に警告が出た場合は、`mkdocs.yml` の `nav` と `docs/` 配下の実ファイルの不整合を優先して確認してください。
## ローカルプロジェクトが環境から外れたときの復旧

`uv remove ...` の実行内容によっては、ローカル editable パッケージ
`deepmath` が環境から外れることがあります（例: `- deepmath==0.1.0` と表示される）。

その場合は、プロジェクトルートで次を実行して復旧してください。

```bash
uv pip install -e .
```

確認:

```bash
mkdocs build -q
```

補足:
- 依存関係まで含めて整え直したい場合は `uv sync` でも復旧可能です。
