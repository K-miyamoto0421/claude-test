#!/usr/bin/env python3
"""
char-counter: 文字数カウントスクリプト

Usage:
    python count_chars.py "カウントしたいテキスト"
    echo "テキスト" | python count_chars.py
"""

import sys

NEWLINES = {'\n', '\r'}
SPACES   = {' ', '　', '\t'}


def count_patterns(text: str) -> dict:
    p1 = len(text)
    p2 = len([c for c in text if c not in SPACES])
    p3 = len([c for c in text if c not in NEWLINES])
    p4 = len([c for c in text if c not in NEWLINES | SPACES])
    breakdown = {
        'newlines':    sum(1 for c in text if c in NEWLINES),
        'half_spaces': sum(1 for c in text if c == ' '),
        'full_spaces': sum(1 for c in text if c == '　'),
        'tabs':        sum(1 for c in text if c == '\t'),
    }
    return {'p1': p1, 'p2': p2, 'p3': p3, 'p4': p4, 'breakdown': breakdown}


def format_result(result: dict) -> str:
    b = result['breakdown']
    return "\n".join([
        "## 文字数カウント結果",
        "",
        "| パターン | 改行（\\n \\r） | スペース（半角・全角・タブ） | 文字数 |",
        "|----------|--------------|------------------------------|--------|",
        f"| ①        | 含む         | 含む                         | {result['p1']} 文字 |",
        f"| ②        | 含む         | 除く                         | {result['p2']} 文字 |",
        f"| ③        | 除く         | 含む                         | {result['p3']} 文字 |",
        f"| ④        | 除く         | 除く                         | {result['p4']} 文字 |",
        "",
        f"（内訳）改行: {b['newlines']}文字　半角スペース: {b['half_spaces']}文字　"
        f"全角スペース: {b['full_spaces']}文字　タブ: {b['tabs']}文字",
    ])


if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) >= 2 else sys.stdin.read()
    print(format_result(count_patterns(text)))
