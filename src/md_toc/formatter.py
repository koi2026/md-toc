"""(level, title) 목록을 중첩된 markdown 목차로 렌더링한다."""

from __future__ import annotations

from collections.abc import Iterable

from md_toc.parser import Header
from md_toc.slugify import slugify

_INDENT = "  "


def render_toc(headers: Iterable[Header], *, max_depth: int = 6) -> str:
    """헤더 목록을 중첩 markdown 목록으로 만든다.

    - 가장 얕은 레벨을 루트로 잡고 상대 들여쓰기.
    - `max_depth` 보다 깊은 헤더는 건너뛴다.
    - 빈 입력이면 빈 문자열을 돌려준다.
    """
    items = [h for h in headers if h.level <= max_depth]
    if not items:
        return ""

    base = min(h.level for h in items)
    lines: list[str] = []
    for h in items:
        depth = h.level - base
        anchor = slugify(h.title)
        lines.append(f"{_INDENT * depth}- [{h.title}](#{anchor})")
    return "\n".join(lines)
