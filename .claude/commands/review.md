# /review — コードレビュー一括実行

このプロジェクトのコードに対して、以下の3つのSubAgentを並列で実行してレビューを行う。

## 実行するSubAgent

1. **doc-writer**: 変更されたコードのdocstringとドキュメントを生成
2. **code-reviewer**: バグ・型エラー・設計上の問題を検出してレポート（最大4件）
3. **test-runner**: pytest形式のテストケースを提案（正常系・異常系を網羅）

## 対象ファイル

プロジェクト内の `.py` ファイルすべてを対象とする。
使用ツールは Read・Grep・Glob のみ（`.claude/settings.json` の設定に従う）。

## 出力形式

各SubAgentの結果をまとめて以下の形式で報告する：

```
## コードレビュー結果

### 📄 ドキュメント提案
[doc-writerの出力]

### 🔍 コードレビュー
[code-reviewerの出力]

### 🧪 テスト提案
[test-runnerの出力]
```
