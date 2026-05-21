---
id: 1
title: 펜스 코드 블록 안의 `#` 라인이 헤더로 잡힌다
labels: [bug, good-first-issue]
status: open
---

## 재현

`examples/sample.md` 로 `md-toc` 를 실행하면, "설치" 섹션의 펜스 코드 블록 안에 있는 셸 주석이 목차에 들어옵니다.

```sh
md-toc examples/sample.md
```

기대:

```markdown
- [소개](#소개)
  - [설치](#설치)
  - [빠른 시작](#빠른-시작)
- [API](#api)
  - [extract_headers](#extract_headers)
  - [render_toc](#render_toc)
    - [옵션](#옵션)
```

실제: 위 출력에 `- [가상환경 만들고](#가상환경-만들고)` 같은 가짜 H1 항목들이 끼어든다.

## 원인 가설

`parser.py` 의 `extract_headers` 는 줄 단위로 `^(#{1,6})\s+...` 정규식만 매칭한다. 펜스(```` ``` ````, `~~~`) 블록 안인지 여부를 추적하지 않는다.

## 받아들임 기준

- `examples/sample.md` 에 대해 위 "기대" 출력이 나온다.
- 새로운 테스트가 추가되어 회귀를 막는다.
- 닫는 펜스 표기가 다른 경우(`` ``` `` vs `~~~`, 옵션 라벨 `sh`, `python` 등) 도 같이 무시한다.

## 관련 모듈

- `src/md_toc/parser.py`
- `tests/test_parser.py`
