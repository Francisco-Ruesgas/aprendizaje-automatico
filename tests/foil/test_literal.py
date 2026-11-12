import pytest

from aprendizaje_automatico.foil.literal import Literal

# Test cases for the Literal class

## Test equality operator of the Literal class

def test_literal_equality_operator():
  literal = Literal("padre", ("x", "y"))
  other_literal = Literal("padre", ("x", "y"), False)
  another_literal = Literal("madre", ("x", "z"))
  assert literal == other_literal
  assert literal == literal
  assert not literal == another_literal

def test_literal_inequality_operator():
  literal = Literal("padre", ("x", "y"))
  other_literal = Literal("padre", ("x", "y"), False)
  another_literal = Literal("madre", ("x", "z"))
  assert literal != another_literal
  assert not literal != literal
  assert not literal != other_literal

## Test __hash__ method of Literal class

def test_equal_literal_have_same_hash():
  literal = Literal("parent", ("x", "y"))
  other_literal = Literal("parent", ("x", "y"))
  assert literal == other_literal
  assert hash(literal) == hash(other_literal)

def test_literal_can_be_added_to_set():
    literal = Literal("parent", ("X", "Y"))
    literals = {literal}
    assert literal in literals

def test_equal_literals_are_deduplicated_in_set():
    literal = Literal("parent", ("X", "Y"))
    other_literal = Literal("parent", ("X", "Y"))
    assert len({literal, other_literal}) == 1

def test_different_literals_can_coexist_in_set():
    literal = Literal("parent", ("X", "Y"))
    other_literal = Literal("male", ("X",))
    assert len({literal, other_literal}) == 2

## Test string conversion of the Literal class

def test_literal_to_string_conversion():
  literal = Literal("abuelo", ("x", "y"))
  other_literal = Literal("madre", ("y", "x", "z"), True)
  another_literal = Literal("mujer", ("y"))
  assert str(literal) == "abuelo(x, y)"
  assert str(other_literal) == "not madre(y, x, z)"
  assert str(another_literal) == "mujer(y)"