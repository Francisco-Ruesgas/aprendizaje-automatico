""" 
Class Hypothesis: 
  Represent a hypothesis in a version space.
Attributes:
    - constraints: A tuple of values that represent the characteristics of the
    hypothesis.
"""

class Hypothesis:
  """ Represent a hypothesis in a version space."""

  def __init__(self, constraints: tuple[str, ...] = ()):
    self._constraints = constraints  

  def covers(self, example: tuple[str, ...]) -> bool:
    """ Check if the hypothesis covers the given example. """
    if self._constraints == ():
      return False
    if len(self._constraints) != len(example):
      raise ValueError("Attribute dimensions must match.")
    for constraint, value in zip(self._constraints, example):
      if constraint != "?" and constraint != value:
        return False
    return True

  def is_more_general_than(self, other: 'Hypothesis') -> bool:
    """ Check if the hypothesis is more general or equal than another hypothesis. """
    if self._constraints == ():
      if other._constraints == ():
        return True
      else:
        return False
    if other._constraints == ():
        return True
    if len(self._constraints) != len(other._constraints):
      raise ValueError("Attribute dimensions must match.")
    for constraint, other_constraint in zip(self._constraints, other._constraints):
      if constraint != "?" and (
        other_constraint == "?" or constraint != other_constraint):
        return False
    return True
