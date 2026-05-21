# 소개

이 문서는 md-toc 의 동작을 보여 주는 샘플입니다.

## 설치

```sh
# 가상환경 만들고
python -m venv .venv
source .venv/bin/activate

# 설치
pip install -e ".[dev]"
```

## 빠른 시작

명령어 한 줄로 목차를 뽑습니다.

```sh
md-toc examples/sample.md
```

# API

라이브러리로도 쓸 수 있습니다.

## extract_headers

`(level, title)` 튜플 목록을 돌려줍니다.

## render_toc

중첩 markdown 목록 문자열을 만듭니다.

### 옵션

- `max_depth` — 포함할 최대 헤더 깊이.
