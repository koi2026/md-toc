"""md-toc CLI 진입점."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from md_toc.formatter import render_toc
from md_toc.parser import extract_headers


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="md-toc",
        description="Markdown 파일에서 목차를 추출합니다. '-' 은 표준입력.",
    )
    p.add_argument("path", help="입력 마크다운 파일 경로, 또는 '-' (STDIN)")
    p.add_argument(
        "--max-depth",
        type=int,
        default=6,
        metavar="N",
        help="포함할 최대 헤더 깊이 (기본 6)",
    )
    return p


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.max_depth < 1 or args.max_depth > 6:
        print("error: --max-depth 는 1~6 사이여야 합니다", file=sys.stderr)
        return 2
    text = _read(args.path)
    toc = render_toc(extract_headers(text), max_depth=args.max_depth)
    print(toc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
