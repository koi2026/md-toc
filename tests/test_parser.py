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
