# Project notes for Claude Code

이 파일은 `claude` 가 이 저장소에서 작업할 때 자동으로 읽는 컨텍스트입니다. 사람이 봐도 짧은 온보딩 노트로 유용합니다.

## 무엇을 만드는가

`md-toc` 는 Markdown 파일의 헤더를 읽어 GitHub 스타일 앵커가 달린 중첩 목차를 출력하는 작은 CLI 입니다. KOI 4회차 실습용 프로젝트라 일부러 작게 유지합니다.

## 모듈 경계

- `src/md_toc/parser.py` — 문자열에서 `(level, title)` 튜플 목록 추출. **유일한 입력 파서**. 이 모듈만 마크다운 형식을 안다.
- `src/md_toc/slugify.py` — 헤더 텍스트 → 앵커 ID. GitHub 알고리즘에 가깝게 구현.
- `src/md_toc/formatter.py` — `(level, title)` 목록을 중첩 markdown 목록 문자열로 렌더. `slugify` 만 의존.
- `src/md_toc/cli.py` — argparse 기반 진입점. 파일/STDIN 입력 처리. 비즈니스 로직 없음.
- `tests/` — pytest. 모듈별로 파일이 1:1.

새 기능은 가능하면 위 경계 안에서 끝내고, CLI 가 비즈니스 로직을 갖지 않도록 합니다.

## 코딩 규칙

- Python 3.10+. 표준 라이브러리만 사용. 추가 의존성은 PR 에서 토론 후 도입.
- 타입 힌트 필수. `ruff check` 통과.
- 함수는 작게, 부수효과는 CLI 계층에서만.
- 커밋은 [Conventional Commits](https://www.conventionalcommits.org/) — `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`.

## 실행 빠르게

```sh
pip install -e ".[dev]"
md-toc examples/sample.md
pytest
```

## 알려진 미해결 이슈

`docs/issues/` 를 보세요. 실습 저장소라 GitHub Issues 대신 파일로 관리합니다. 새 PR 은 해당 이슈 번호를 커밋/PR 본문에 인용해 주세요 (`Closes #1`).
