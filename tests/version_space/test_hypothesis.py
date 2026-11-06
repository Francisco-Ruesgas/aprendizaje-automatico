import pytest

from aprendizaje_automatico.version_spaces.hypothesis import Hypothesis

# Test cases for the Hypothesis class

## Test the covers method of the Hypothesis class

def test_hypothesis_covers_matching_instance():
  """ Test that a hypothesis covers an instance that matches its constraints. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  example = ("Japon", "Honda", "azul", 1980, "economico")
  assert hypothesis.covers(example)

def test_hypothesis_covers_instance_with_wildcard():
  """ Test that a hypothesis with a wildcard covers an instance that matches its
  constraints. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", "?", "economico"))
  example = ("Japon", "Honda", "azul", 1990, "economico")
  assert hypothesis.covers(example)

def test_hypothesis_does_not_covers_not_matching_instance():
  """ Test that a hypothesis does not cover an instance that does not match its
  constraints. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  example = ("Japon", "Honda", "azul", 1990, "economico")
  assert not hypothesis.covers(example)

def test_hypothesis_with_only_wildcards_covers_any_instance():
  """ Test that a hypothesis with only wildcards covers any instance. """
  hypothesis = Hypothesis(("?", "?", "?", "?", "?"))
  example = ("Japon", "Honda", "azul", 1990, "economico")
  assert hypothesis.covers(example)

def test_hypothesis_different_dimensions_raise_an_error():
  """ Test that a hypothesis with different dimensions than the instance raises
  a ValueError. """
  hypothesis = Hypothesis(("Japon", "Honda"))
  example = ("Japon")
  with pytest.raises(ValueError):
    hypothesis.covers(example)

def test_hypothesis_supports_different_number_of_attributes():
  """ Test that a hypothesis can support different numbers of attributes. """
  hypothesis = Hypothesis(("Japon", "Honda"))
  example = ("Japon", "Honda")
  assert hypothesis.covers(example)

def test_empty_hypothesis_covers_no_instance():
  """ Test that an empty hypothesis does not cover any instance. """
  hypothesis = Hypothesis(())
  example = ("Japon", "Honda", "azul", 1990, "economico")
  assert not hypothesis.covers(example)
  assert not hypothesis.covers(())

## Test the is_more_general_than method of the Hypothesis class

def test_more_general_than_returns_true_for_more_general_hypothesis():
  """ Test that a hypothesis is more general than another hypothesis. """
  hypothesis = Hypothesis(("Japon", "?", "azul", "?", "economico"))
  other_hypothesis = Hypothesis(("Japon", "Honda", "azul", "?", "economico"))
  assert hypothesis.is_more_general_than(other_hypothesis)

def test_more_general_than_returns_true_for_equal_hypotheses():
  """ Test that a hypothesis is more general than itself. """
  hypothesis = Hypothesis(("Japon", "?", "azul", "?", "economico"))
  assert hypothesis.is_more_general_than(hypothesis)

def test_more_general_than_returns_false_for_more_specific_hypothesis():
  """ Test that a hypothesis is not more general than another hypothesis. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", "?", "economico"))
  other_hypothesis = Hypothesis(("Japon", "?", "azul", "?", "economico"))
  assert not hypothesis.is_more_general_than(other_hypothesis)

def test_more_general_than_returns_false_for_incomparable_hypotheses():
  """ Test that a hypothesis is not more general than another hypothesis with
  different concrete values. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", "?", "economico"))
  other_hypothesis = Hypothesis(("Japon", "?", "azul", 1980, "economico"))
  assert not hypothesis.is_more_general_than(other_hypothesis)

def test_all_wildcards_hypothesis_is_more_general_than_any_other():
  """ Test that a hypothesis with all wildcards is more general than any other
  hypothesis. """
  hypothesis = Hypothesis(("?", "?", "?", "?", "?"))
  other_hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  assert hypothesis.is_more_general_than(other_hypothesis)

def test_different_concrete_values_are_not_more_general():
  """ Test that a hypothesis with different concrete values is not more general
  than another hypothesis. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  other_hypothesis = Hypothesis(("Japon", "Toyota", "azul", 1980, "economico"))
  assert not hypothesis.is_more_general_than(other_hypothesis)

def test_more_general_than_with_different_dimensions_raises_an_error():
  """ Test that a hypothesis with different dimensions than another hypothesis
  raises a ValueError. """
  hypothesis = Hypothesis(("Japon", "Honda"))
  other_hypothesis = Hypothesis("Japon")
  with pytest.raises(ValueError):
    hypothesis.is_more_general_than(other_hypothesis)

def test_empty_hypothesis_is_not_more_general_than_normal():
  """ Test that an empty hypothesis is not more general than a normal hypothesis. """
  hypothesis = Hypothesis(())
  other_hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  assert not hypothesis.is_more_general_than(other_hypothesis)

def test_normal_hypothesis_is_more_general_than_empty():
  """ Test that a normal hypothesis is more general than an empty hypothesis. """
  hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  empty_hypothesis = Hypothesis(())
  assert hypothesis.is_more_general_than(empty_hypothesis)

def test_empty_hypothesis_are_equally_general():
  """ Test that two empty hypotheses are equally general. """
  hypothesis = Hypothesis(())
  other_hypothesis = Hypothesis(())
  assert hypothesis.is_more_general_than(other_hypothesis)
  assert other_hypothesis.is_more_general_than(hypothesis)

## Test the equality operator of the Hypothesis class

def test_hypothesis_equality_operator():
  """ Test that two hypotheses with the same constraints are equal. """
  first_hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  second_hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  third_hypothesis = Hypothesis(("Japon", "Toyota", "azul", 1980, "economico"))
  assert first_hypothesis == second_hypothesis
  assert first_hypothesis == first_hypothesis
  assert not first_hypothesis == third_hypothesis

def test_hypothesis_inequality_operator():
  """ Test that two hypotheses with different constraints are not equal. """
  first_hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  second_hypothesis = Hypothesis(("Japon", "Honda", "azul", 1980, "economico"))
  third_hypothesis = Hypothesis(("Japon", "Toyota", "azul", 1980, "economico"))
  assert first_hypothesis != third_hypothesis
  assert not first_hypothesis != second_hypothesis
