from md_toc.formatter import render_toc
from md_toc.parser import Header


def test_renders_nested_list_from_levels():
    out = render_toc([Header(1, "A"), Header(2, "B"), Header(2, "C")])
    assert out == "- [A](#a)\n  - [B](#b)\n  - [C](#c)"


def test_indents_relative_to_shallowest_level():
    # H2 부터 시작해도 첫 줄은 들여쓰기 없이
    out = render_toc([Header(2, "X"), Header(3, "Y")])
    assert out == "- [X](#x)\n  - [Y](#y)"


def test_max_depth_filters_deeper_headers():
    headers = [Header(1, "A"), Header(2, "B"), Header(3, "C")]
    out = render_toc(headers, max_depth=2)
    assert "C" not in out
    assert "- [A](#a)" in out


def test_empty_returns_empty_string():
    assert render_toc([]) == ""
