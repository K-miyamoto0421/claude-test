#!/usr/bin/env python3
"""
parse_headings.py — HTML から見出しタグ（H1〜H3）を抽出して構造化する

Usage:
    python parse_headings.py <html_file_or_stdin>

Output:
    JSON形式の見出し構造
"""

import sys
import json
import re
from collections import Counter


def extract_headings(html: str) -> list[dict]:
    """HTMLから H1〜H3 タグを抽出して順序付きリストで返す"""
    pattern = re.compile(
        r'<(h[1-3])[^>]*>(.*?)</\1>',
        re.IGNORECASE | re.DOTALL
    )
    headings = []
    for match in pattern.finditer(html):
        tag = match.group(1).lower()
        # インナーHTMLのタグを除去してプレーンテキストに
        text = re.sub(r'<[^>]+>', '', match.group(2)).strip()
        if text:
            headings.append({"level": tag, "text": text})
    return headings


def analyze_headings(all_headings: dict[str, list]) -> dict:
    """
    複数URLの見出しを横断分析する

    Args:
        all_headings: {url: [{"level": "h2", "text": "..."}, ...]}

    Returns:
        分析結果の辞書
    """
    h2_counter = Counter()
    h3_counter = Counter()
    h2_counts = []
    h3_counts = []

    for url, headings in all_headings.items():
        h2s = [h["text"] for h in headings if h["level"] == "h2"]
        h3s = [h["text"] for h in headings if h["level"] == "h3"]
        h2_counter.update(h2s)
        h3_counter.update(h3s)
        h2_counts.append(len(h2s))
        h3_counts.append(len(h3s))

    n = len(all_headings)
    common_h2 = [text for text, cnt in h2_counter.items() if cnt >= max(2, n // 2)]
    unique_h2  = [text for text, cnt in h2_counter.items() if cnt == 1]

    return {
        "common_h2_topics": common_h2,
        "unique_h2_topics": unique_h2,
        "avg_h2_count": round(sum(h2_counts) / n, 1) if n else 0,
        "avg_h3_count": round(sum(h3_counts) / n, 1) if n else 0,
        "top_h2_keywords": h2_counter.most_common(10),
        "top_h3_keywords": h3_counter.most_common(10),
    }


if __name__ == "__main__":
    html = sys.stdin.read() if len(sys.argv) < 2 else open(sys.argv[1]).read()
    headings = extract_headings(html)
    print(json.dumps(headings, ensure_ascii=False, indent=2))
