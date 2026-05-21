---
id: 3
title: 표준입력에 한글이 포함된 경우 일부 환경에서 인코딩 에러
labels: [enhancement]
status: open
---

## 상황

```sh
cat examples/sample.md | md-toc -
```

대부분의 환경에서는 동작하지만, `LANG` 이 `C` 인 컨테이너 등에서 `UnicodeDecodeError` 가 발생할 수 있다.

## 받아들임 기준

- `cli.py` 가 STDIN 을 명시적으로 UTF-8 로 읽도록 한다.
- 환경변수에 의존하지 않는다.
- 단위 테스트로 회귀를 막는다(stdin 모킹).

## 관련 모듈

- `src/md_toc/cli.py`
