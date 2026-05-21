---
id: 2
title: 같은 제목의 헤더가 여러 개일 때 앵커가 충돌한다
labels: [bug]
status: open
---

## 재현

```markdown
# 설치
## macOS
# 설치
## Linux
```

현재 출력:

```markdown
- [설치](#설치)
  - [macOS](#macos)
- [설치](#설치)
  - [Linux](#linux)
```

두 번째 "설치" 도 `#설치` 로 가는데, 실제 렌더된 HTML 에서는 GitHub 가 자동으로 `#설치-1` 로 만든다. 그래서 클릭이 잘못된 위치로 점프한다.

## 받아들임 기준

- 같은 제목의 N 번째 등장은 `#슬러그-N-1` 형태로 번호가 붙는다(GitHub 동작 모사).
- 단위 테스트 1개 이상.

## 관련 모듈

- `src/md_toc/formatter.py` 또는 `src/md_toc/slugify.py` — 어디에 카운터를 둘지 토론 거리.
