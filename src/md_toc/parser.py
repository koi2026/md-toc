"""Markdown 입력에서 헤더만 뽑아낸다.

설계 노트
- 풀 파서가 아니다. 한 줄씩 훑으며 `#` 으로 시작하는 ATX 헤더만 인식한다.
- Setext 헤더(`===`, `---`) 는 지원하지 않는다.
- 펜스 코드 블록(```` ``` ````, `~~~`) 안의 줄은 헤더로 보지 않는다.
- 반환은 (level, title) 의 리스트. 등장 순서를 보존한다.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# ATX 헤더: `# ` 1~6개 + 공백 + 제목 + (선택)닫는 # + 끝까지
_HEADER_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")

# 펜스 코드 블록: 최대 3칸 들여쓰기 + (` 또는 ~) 3개 이상 + 나머지(정보 문자열)
# CommonMark: 닫는 펜스는 같은 문자 + 같은 개수 이상 + 정보 문자열이 없어야 한다.
_FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


@dataclass(frozen=True)
class Header:
    level: int
    title: str


def extract_headers(text: str) -> list[Header]:
    """텍스트에서 ATX 헤더를 등장 순서대로 추출한다.

    펜스 코드 블록(```` ``` ```` 또는 `~~~`) 내부의 `#` 으로 시작하는 줄은
    헤더로 간주하지 않는다.

    >>> [(h.level, h.title) for h in extract_headers("# A\\n## B\\n")]
    [(1, 'A'), (2, 'B')]
    """
    headers: list[Header] = []
    fence_marker: str | None = None  # 열린 펜스의 실제 문자열(예: "```", "~~~~")
    for raw in text.splitlines():
        fence = _FENCE_RE.match(raw)
        if fence:
            marker, rest = fence.group(1), fence.group(2)
            if fence_marker is None:
                # 펜스 열기 — 정보 문자열(rest) 은 무시
                fence_marker = marker
                continue
            # 닫기 후보: 같은 문자 + 같은 개수 이상 + 정보 문자열 없음
            if (
                marker[0] == fence_marker[0]
                and len(marker) >= len(fence_marker)
                and rest.strip() == ""
            ):
                fence_marker = None
            # 닫지 못한 펜스 라인은 코드 블록 내부로 본다
            continue

        if fence_marker is not None:
            continue

        m = _HEADER_RE.match(raw)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()
        headers.append(Header(level=level, title=title))
    return headers
