# 기여 가이드

KOI 4회차 실습용 저장소입니다. 실제 OSS 흐름을 그대로 따르되, 학습이 우선이라 친절합니다.

## 워크플로

1. `docs/issues/` 에서 작업할 이슈를 고릅니다.
2. 브랜치를 분기합니다: `git switch -c fix/1-fenced-code-headers`
3. 테스트를 먼저 추가합니다(가능하면 실패하는 형태).
4. 구현을 마치고 `pytest`, `ruff check` 가 통과하는지 확인합니다.
5. Conventional Commits 규칙으로 커밋합니다.
6. PR 본문은 아래 템플릿을 따릅니다.

## 커밋 메시지

```
<type>(<scope>): <subject>

<body — 왜 이 변경이 필요한지>

Closes #<issue-number>
```

`type` 은 `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `perf` 중 하나. `scope` 는 모듈 이름(`parser`, `formatter`, `cli`, `slugify`)을 권장합니다.

예시:

```
fix(parser): 펜스 코드 블록 안의 헤더 무시

```sh
# 같은 라인이 셸 주석인데도 H1 으로 잡혀서
TOC 에 가짜 항목이 들어가던 문제 수정.

Closes #1
```

## PR 본문 템플릿

`.github/PULL_REQUEST_TEMPLATE.md` 를 참고하세요. 다음 항목을 채워 주세요.

- **요약** — 이 PR 이 무엇을 바꾸는지 1–2문장
- **동기 / 이슈** — `Closes #N` 로 연결
- **검증** — 어떤 테스트를 돌렸고 결과는 어떤지
- **위험** — 같이 깨질 수 있는 부분
- **AI 사용 로그** — 아래 형식

### AI 사용 로그

```
- 의도: <무엇을 시키려 했는가>
- 입력 요약: <어떤 컨텍스트를 주었는가>
- 채택 정도: 전체 채택 / 부분 채택 / 폐기
- 변경 이유: <왜 그렇게 결정했는가 — 사람의 판단>
```

마지막 줄이 가장 중요합니다. AI 가 만든 코드라도, **PR 을 올리는 사람이 책임집니다**.
