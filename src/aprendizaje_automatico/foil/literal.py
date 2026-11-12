"""
Class Literal
"""

class Literal:
  """ A first order literal. """

  def __init__(self, predicate: str, terms: tuple[str, ...], is_negated: bool = False):
    self._predicate = predicate
    self._terms = terms
    self._is_negated = is_negated

  def __eq__(self, other: 'Literal'):
    return self._predicate == other._predicate and self._terms == other._terms and self._is_negated == other._is_negated

  def __hash__(self):
    return hash((self._predicate, self._terms, self._is_negated))

  def __str__(self):
    sing = "not " if self._is_negated else ""
    return  f"{sing}{self._predicate}({', '.join(self._terms)})"