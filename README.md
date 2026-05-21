# md-toc

작은 Markdown 목차(Table of Contents) 추출기. 마크다운 파일을 읽어 헤더 구조를 파악하고, GitHub 스타일 앵커가 달린 중첩 목록을 출력합니다.

KOI 4회차 — *AI를 활용한 오픈소스 기여와 운영 자동화* — 실습용 미니 저장소입니다.

## 설치

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## 사용법

```sh
md-toc examples/sample.md
md-toc examples/sample.md --max-depth 3
cat examples/sample.md | md-toc -
```

출력 예시:

```markdown
- [소개](#소개)
  - [설치](#설치)
  - [빠른 시작](#빠른-시작)
- [API](#api)
```

## 개발

```sh
pytest                # 단위 테스트
ruff check src tests  # 린트
```

## 기여하기

[CONTRIBUTING.md](CONTRIBUTING.md) 를 먼저 읽어 주세요. PR 흐름, 커밋 컨벤션, AI 사용 로그 작성 규칙이 정리되어 있습니다.

미해결 이슈는 [`docs/issues/`](docs/issues/) 폴더에 모여 있습니다. 실습용 저장소라 GitHub Issues 대신 파일로 관리합니다.

## 라이선스

MIT — [LICENSE](LICENSE) 참고.
