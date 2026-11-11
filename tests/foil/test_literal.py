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