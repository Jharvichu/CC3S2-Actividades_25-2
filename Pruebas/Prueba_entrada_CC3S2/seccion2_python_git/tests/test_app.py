import pytest
from app.app import summarize

@pytest.fixture
def sample():
    return ["1", "2", "3"]

def test_ok(sample):
    # Act
    result = summarize(sample)
    
    # Assert
    assert result == {'count': 3, 'sum': 6.0, 'avg': 2.0}
    assert isinstance(result, dict)
    assert 'count' in result and 'sum' in result and 'avg' in result

def test_empty():
    with pytest.raises(ValueError, match="La lista no puede estar vacía"):
        summarize([])

def test_not_a_list():
    with pytest.raises(ValueError, match="nums debe ser una lista"):
        summarize("not a list")

def test_non_numeric():
    with pytest.raises(ValueError, match="Elementos no numéricos encontrado"):
        summarize(["a", "2"])