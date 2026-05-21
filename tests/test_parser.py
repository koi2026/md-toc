from md_toc.parser import Header, extract_headers


def test_extracts_levels_and_titles():
    md = "# A\n## B\n### C\n"
    assert extract_headers(md) == [
        Header(1, "A"),
        Header(2, "B"),
        Header(3, "C"),
    ]


def test_ignores_non_header_lines():
    md = "# A\n\nsome paragraph\n## B\n- list item\n"
    assert extract_headers(md) == [Header(1, "A"), Header(2, "B")]


def test_strips_trailing_hashes():
    # ATX closing hashes 는 제목의 일부가 아니다
    md = "## Section ##\n"
    assert extract_headers(md) == [Header(2, "Section")]


def test_empty_input():
    assert extract_headers("") == []


def test_more_than_six_hashes_is_not_a_header():
    md = "####### too deep\n"
    assert extract_headers(md) == []


def test_ignores_headers_inside_backtick_fence():
    md = "# A\n\n```sh\n# 가상환경 만들고\n# 설치\n```\n\n## B\n"
    assert extract_headers(md) == [Header(1, "A"), Header(2, "B")]


def test_ignores_headers_inside_tilde_fence():
    md = "# A\n\n~~~python\n# not a header\n~~~\n\n## B\n"
    assert extract_headers(md) == [Header(1, "A"), Header(2, "B")]


def test_tilde_fence_does_not_close_backtick_fence():
    # 다른 종류의 펜스 문자는 서로를 닫지 않는다 (CommonMark).
    md = "# A\n\n```\n~~~\n# still in code\n```\n\n## B\n"
    assert extract_headers(md) == [Header(1, "A"), Header(2, "B")]


def test_longer_fence_wraps_shorter_one():
    # 4-백틱 펜스는 안의 3-백틱 줄로 닫히지 않는다.
    md = "# A\n\n````\n```\n# still in code\n```\n````\n\n## B\n"
    assert extract_headers(md) == [Header(1, "A"), Header(2, "B")]


def test_indented_fence_up_to_three_spaces():
    # 펜스 앞 최대 3칸 들여쓰기는 허용된다.
    md = "# A\n\n   ```\n# not a header\n   ```\n\n## B\n"
    assert extract_headers(md) == [Header(1, "A"), Header(2, "B")]


def test_closing_fence_must_not_have_info_string():
    # 닫는 펜스에 텍스트가 따라오면 닫히지 않는다.
    md = "# A\n\n```\n# in code\n``` not-a-close\n# still in code\n```\n\n## B\n"
    assert extract_headers(md) == [Header(1, "A"), Header(2, "B")]


def test_unclosed_fence_swallows_rest_of_document():
    # 닫히지 않은 펜스 뒤의 헤더는 무시된다 (CommonMark 와 동일한 동작).
    md = "# A\n\n```\n# inside\n## also inside\n"
    assert extract_headers(md) == [Header(1, "A")]


def test_sample_md_expected_toc():
    # examples/sample.md 회귀 케이스: 펜스 안의 셸 주석이 끼어들지 않는다.
    md = (
        "# 소개\n"
        "\n"
        "## 설치\n"
        "\n"
        "```sh\n"
        "# 가상환경 만들고\n"
        "python -m venv .venv\n"
        "\n"
        "# 설치\n"
        'pip install -e ".[dev]"\n'
        "```\n"
        "\n"
        "## 빠른 시작\n"
        "\n"
        "# API\n"
        "\n"
        "## extract_headers\n"
        "\n"
        "## render_toc\n"
        "\n"
        "### 옵션\n"
    )
    assert extract_headers(md) == [
        Header(1, "소개"),
        Header(2, "설치"),
        Header(2, "빠른 시작"),
        Header(1, "API"),
        Header(2, "extract_headers"),
        Header(2, "render_toc"),
        Header(3, "옵션"),
    ]
