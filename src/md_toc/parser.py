"""Markdown 입력에서 헤더만 뽑아낸다.

설계 노트
- 풀 파서가 아니다. 한 줄씩 훑으며 `#` 으로 시작하는 ATX 헤더만 인식한다.
- Setext 헤더(`===`, `---`) 는 지원하지 않는다.
- 반환은 (level, title) 의 리스트. 등장 순서를 보존한다.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# ATX 헤더: `# ` 1~6개 + 공백 + 제목 + (선택)닫는 # + 끝까지
_HEADER_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


@dataclass(frozen=True)
class Header:
    level: int
    title: str


def extract_headers(text: str) -> list[Header]:
    """텍스트에서 ATX 헤더를 등장 순서대로 추출한다.

    >>> [(h.level, h.title) for h in extract_headers("# A\\n## B\\n")]
    [(1, 'A'), (2, 'B')]
    """
    headers: list[Header] = []
    for raw in text.splitlines():
        m = _HEADER_RE.match(raw)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        headers.append(Header(level=level, title=title))
    return headers
