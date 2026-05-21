from md_toc.slugify import slugify


def test_lowercases_and_hyphenates():
    assert slugify("Quick Start") == "quick-start"


def test_strips_punctuation():
    assert slugify("API: 설계!") == "api-설계"


def test_collapses_runs_of_whitespace():
    assert slugify("hello   world") == "hello-world"


def test_keeps_korean():
    assert slugify("설치 방법") == "설치-방법"
