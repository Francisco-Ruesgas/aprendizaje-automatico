import pytest
from aprendizaje_automatico.version_spaces.hypothesis import Hypothesis

# Test cases for the Hypothesis class

## Test the covers method of the Hypothesis class

def test_hypothesis_covers_matching_instance():
  """ Test that a hypothesis covers an instance that matches its constraints. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  example = ("Japon", "Honda", "azul", 1980, "economico")
  assert hypothesis.covers(example) == True

def test_hypothesis_covers_instance_with_wildcard():
  """ Test that a hypothesis with a wildcard covers an instance that matches its constraints. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", "?", "economico"))
  example = ("Japon", "Honda", "azul", 1990, "economico")
  assert hypothesis.covers(example) == True

def test_hypothesis_does_not_covers_not_matching_instance():
  """ Test that a hypothesis does not cover an instance that does not match its constraints. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  example = ("Japon", "Honda", "azul", 1990, "economico")
  assert hypothesis.covers(example) == False

def test_hypothesis_with_only_wildcards_covers_any_instance():
  """ Test that a hypothesis with only wildcards covers any instance. """
  hypothesis = Hypothesis(("?", "?", "?", "?", "?"))
  example = ("Japon", "Honda", "azul", 1990, "economico")
  assert hypothesis.covers(example) == True

def test_hypothesis_different_dimensions_raise_an_error():
  """ Test that a hypothesis with different dimensions than the instance raises a ValueError. """
  hypothesis = Hypothesis(("Japon", "Honda"))
  example = ("Japon")
  with pytest.raises(ValueError):
    hypothesis.covers(example)

def test_hypothesis_supports_different_number_of_attributes():
    """ Test that a hypothesis can support different numbers of attributes. """
    hypothesis = Hypothesis(("Japon", "Honda"))
    example = ("Japon", "Honda")
    assert hypothesis.covers(example) == True
