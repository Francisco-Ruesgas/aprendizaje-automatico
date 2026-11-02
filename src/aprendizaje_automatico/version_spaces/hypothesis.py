"""
Ejemplos:
  ("Japon", "Honda", "azul", 1980, "economico", True)
  ("Japon", "Toyota", "verde", 1970, "deportivo", False)
  ("Japon", "Toyota", "azul", 1990, "economico", True)
  ("EEUU", "Chrysler", "azul", 1980, "economico", False)
  ("Japon", "Honda", "blanco", 1980, "economico", True)

Objetivo:
  ("Japon", "?", "?", "?", "economico")
"""

""" 
Class Hypothesis: Representa una hipótesis en el espacio de versiones.
  Una hipótesis es una tupla de valores que representan las características de un ejemplo.
Atributos:
    - values: Una tupla de valores que representan las características de la hipótesis.
Métodos:
    - __init__: Inicializa una nueva instancia de la clase Hypothesis.
    - __str__: Devuelve una representación en cadena de la hipótesis.
"""

class Hypothesis:
  """ Represent a hypothesis in a version space."""

  def __init__(self, constraints: tuple[str, ...]):
    self._constraints = constraints  

  def covers(self, example: tuple[str, ...]) -> bool:
    """ Check if the hypothesis covers the given example. """
    if len(self._constraints) != len(example):
      raise ValueError("Attribute dimensions must match.")
    for constraint, value in zip(self._constraints, example):
      if constraint != "?" and constraint != value:
        return False
    return True