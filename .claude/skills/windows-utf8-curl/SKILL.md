---
name: windows-utf8-curl
description: >
  Windows環境（Git Bash）でcurlを使い日本語・絵文字などマルチバイト文字を含むJSONペイロードを
  外部APIに送信すると文字化け（mojibake）する問題を回避するスキル。
  「curlで日本語が文字化けする」「APIに日本語を送りたい」「Windowsでcurl」
  「マルチバイト文字をJSONで送る」などの場面で必ずこのスキルを使うこと。
---

# Windows Git Bash での UTF-8 curl リクエスト対策

## 問題

Windows上のGit Bash（Bashツール）で以下のように、日本語などのマルチバイト文字を含む
JSONペイロードを `curl -d '...'` の引数へ直接埋め込むと、シェルの文字コード変換によって
文字が破損（文字化け）した状態でAPIに送信されてしまう。

```bash
# NG例: 文字化けする
curl -X POST -d '{"name":"タスクグループ名"}' https://api.example.com/resource
```

## 対処法

1. **Write** ツールでリクエストボディ（JSON）をUTF-8の一時ファイルとして書き出す
2. curlは `--data-binary @ファイル名` でそのファイルを参照する（`-d`に直接文字列を渡さない）
3. `-H "Content-Type: application/json; charset=utf-8"` を明示する
4. APIのレスポンスに含まれる日本語フィールドが正しく返ってきているか確認する
   - 文字化けしていた場合は、同じファイル経由の方法でPUT等により修正する
5. リクエスト完了後、一時ファイルは `rm` で削除する（後片付け）

### 実行例

```
Write: .tmp_request.json ← {"data":{"name":"タスクグループ名"}}

Bash: curl -X POST \
        -H "Content-Type: application/json; charset=utf-8" \
        --data-binary @".tmp_request.json" \
        "https://api.example.com/resource"

Bash: rm .tmp_request.json
```

## 注意事項

- 一時ファイルに認証情報（トークン等）を含めない。ペイロードは送信先データのみとする。
- Mac/Linuxのbashでは通常この問題は起きないが、ファイル経由の方法は安全なフォールバックとして
  常に使ってよい。
- PowerShellツールを使う場合も同様の文字化けが起きうるため、同じ「ファイル経由」の方針を適用する。
