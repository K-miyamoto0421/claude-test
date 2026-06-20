# claude-test プロジェクト

田中 蒼空のClaudeCode学習・実験プロジェクト。

## プロジェクト概要

機械学習・AI開発の学習用リポジトリ。SubAgents・Skills・Commandsの実践を通じて
Claude Codeの機能を体系的に習得することを目的とする。

## ファイル構成

```
claude-test/
├── CLAUDE.md               ← このファイル（プロジェクト指示）
├── README.md               ← 自己紹介
├── calculator.py           ← 四則演算モジュール（型バリデーション済み）
├── sample_ml.py            ← 線形回帰の実装（スクラッチ）
└── .claude/
    ├── settings.json       ← プロジェクト設定（SubAgent ツール制限など）
    ├── settings.local.json ← ローカル権限設定（Git管理外推奨）
    ├── skills/
    │   ├── char-counter/   ← 文字数カウントスキル（4パターン出力）
    │   └── seo-blog-writer/ ← SEOブログ記事執筆スキル
    └── commands/
        ├── review.md       ← コードレビュー一括実行
        └── count.md        ← 文字数カウント呼び出し
```

## コーディング規約

- Python: 型ヒント（Type Hints）を付ける
- 関数にはGoogle Style docstringを記述する
- 例外処理は具体的なメッセージを含む `ValueError` / `TypeError` を使う

## SubAgents設定

SubAgentが使用できるツールは `Read・Grep・Glob` の3つに制限されている（`.claude/settings.json`参照）。
ファイルの書き換えを伴う操作はメインセッションで実行すること。

## スキル一覧

| スキル名 | 発動キーワード | 説明 |
|---------|--------------|------|
| `char-counter` | 文字数を数えて、何文字、字数を調べて | テキストの文字数を改行・スペース有無の4パターンで出力 |
| `seo-blog-writer` | ブログを書いて、SEO記事、〇〇文字の記事 | SEO最適化ブログ記事を執筆し、char-counterで文字数管理 |
| `heading-optimizer` | 競合の見出しを調べて、見出し最適化、SEOに強い見出し | 競合URLの見出し構造を分析し最適なH1〜H3案を提案 |
| `seo-content-agent` | 競合を調べてSEO記事を書いて、上位表示できる記事 | **統合エージェント**: heading-optimizer + seo-blog-writer + char-counter を連携 |

## スキル依存関係

```
seo-content-agent
  ├── heading-optimizer   ← PHASE 1: 競合見出し分析
  ├── seo-blog-writer     ← PHASE 3: 記事執筆
  └── char-counter        ← PHASE 4: 文字数計測・調整
```

## よく使うコマンド

```bash
/review    # コードレビュー（doc-writer・code-reviewer・test-runnerを並列実行）
/count     # 文字数カウント（char-counterスキルのショートカット）
```
