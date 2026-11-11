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

## Test string conversion of the Literal class

def test_literal_to_string_conversion():
  literal = Literal("abuelo", ("x", "y"))
  other_literal = Literal("madre", ("y", "x", "z"), True)
  another_literal = Literal("mujer", ("y"))
  assert str(literal) == "abuelo(x, y)"
  assert str(other_literal) == "not madre(y, x, z)"
  assert str(another_literal) == "mujer(y)"