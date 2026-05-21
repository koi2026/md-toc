"""헤더 텍스트 → GitHub 스타일 앵커 ID 변환."""

from __future__ import annotations

import re

_NON_ANCHOR = re.compile(r"[^\w\s\-가-힣]", re.UNICODE)
_WHITESPACE = re.compile(r"\s+")


def slugify(title: str) -> str:
    """GitHub 의 markdown 헤더 앵커 규칙에 가깝게 슬러그를 만든다.

    - 소문자로 변환
    - 영숫자/한글/공백/하이픈 외 문자 제거
    - 연속 공백을 단일 하이픈으로
    - 양끝 하이픈 제거

    >>> slugify("Quick Start")
    'quick-start'
    >>> slugify("API 설계")
    'api-설계'
    """
    s = title.strip().lower()
    s = _NON_ANCHOR.sub("", s)
    s = _WHITESPACE.sub("-", s)
    return s.strip("-")
