import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted_basic():
    """Test unikaalsete sorteeritud arvude funktsiooni."""
    assert unique_sorted([3,1,2,2,3]) == [1,2,3]
    assert unique_sorted([]) == []
    assert unique_sorted([5,5,5]) == [5]

def test_count_words_basic():
    """Test sõnade loendamise funktsiooni."""
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!

import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_merge_dicts():
    assert merge_dicts({1: 2, 2: 3}, {3: 4, 5: 6}) == {1: 2, 2: 3, 3: 4, 5: 6}
    assert merge_dicts({}, {}) == {}
    assert merge_dicts({1: 2, 2: 3}, {2: 4, 3: 5}) == {1: 2, 2: 4, 3: 5}

def test_find_max_pair():
    assert find_max_pair([3, 1, 2, 2, 3]) == (3, 2)
    assert find_max_pair([5]) == (5, 1)
    with pytest.raises(ValueError):
        find_max_pair([])

def test_flatten():
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([]) == []
    assert flatten(["hello", "world"]) == ["hello", "world"]

def test_read_file(tmp_path):
    p1 = tmp_path / "file1.txt"
    p1.write_text("tere\n", encoding="utf-8")
    assert read_file(p1) == "tere\n"
    p2 = tmp_path / "file2.txt"
    p2.write_text("", encoding="utf-8")
    assert read_file(p2) == ""
    p3 = tmp_path / "file3.txt"
    p3.write_text("õäöü", encoding="utf-8")
    assert read_file(p3) == "õäöü"

def test_write_file(tmp_path):
    p = tmp_path / "out.txt"
    assert write_file(p, "tere") == 4
    assert p.read_text(encoding="utf-8") == "tere"
    assert write_file(p, "") == 0
    assert p.read_text(encoding="utf-8") == ""
    assert write_file(p, "õäöü") == 4
    assert p.read_text(encoding="utf-8") == "õäöü"

def test_safe_get():
    d = {"a": 1, "b": 2}
    assert safe_get(d, "a") == 1
    assert safe_get(d, "c") is None
    assert safe_get(d, "c", default=0) == 0

def test_top_n():
    assert top_n([5, 3, 4, 1, 2], 3) == [5, 4, 3]
    assert top_n([1], 1) == [1]
    with pytest.raises(ValueError):
        top_n([1, 2], 3)

def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3], 5) == [[1, 2, 3]]
    with pytest.raises(ValueError):
        chunk_list([1, 2], 0)