"""
Candidate Elimination Algorithm
Initialize:
  Initialize S
  Initialize G
Repeat until S = G and or not more training examples:
  if positive example:
    specify G (remove hypotheses that do not cover the example)
    generalize S (remove hypotheses that do not cover the example)
  else:
    generalize S (remove hypotheses that cover the example)
    specify G (remove hypotheses that cover the example)
"""

from aprendizaje_automatico.version_spaces.hypothesis import Hypothesis

class CandidateElimination:
  """ Candidate Elimination Algorithm. """

  def __init__(self, atributes_amount: int):
    self._S = {Hypothesis()} # ⊥
    self._G = {Hypothesis(("?",) * atributes_amount)} # ⊤

  def train(self, example: tuple[str, ...], label: bool):
    """ Train the model with a new example """
    if label:
      self.caso_positivo(example)
    else:
      self.caso_negativo(example)

  def caso_positivo(self, example: tuple[str, ...]): # Nombre provisional
    """ Handle positive examples. """
    # Eliminar de G las hipótesis que no cubren el ejemplo.
    self._G = {hypothesis for hypothesis in self._G if hypothesis.covers(example)}
    # Eliminar de S las hipótesis que no sean consistentes con las hipótesis de G.
    new_s = set()
    for s_hypothesis in self._S:
      for g_hypothesis in self._G:
        if g_hypothesis.is_more_general_than(s_hypothesis):
          new_s.add(s_hypothesis)
          break
    self._S = new_s
    # Generalizar mínimamente las hipótesis de S que no cubran el ejemplo.
    new_s = set()
    if self._S == {Hypothesis()}:
      self._S = {Hypothesis(example)}
    for s_hypothesis in self._S:
      new_constraint = ()
      if not s_hypothesis.covers(example):
        for s_atribute, example_atribute in zip(s_hypothesis._constraints, example):
          if s_atribute != "?" and s_atribute != example_atribute:
            new_constraint = new_constraint + ("?",)
          else:
            new_constraint = new_constraint + (s_atribute,)
        new_s.add(Hypothesis(new_constraint))
      else:
        new_s.add(s_hypothesis)
    self._S = new_s
    # Eliminar de S las hipótesis que sean más generales que otras hipótesis de S.
    new_s = set()
    for hypothesis in self._S:
      is_more_general_than_other = False
      for other_hypothesis in self._S:
        if hypothesis != other_hypothesis and hypothesis.is_more_general_than(other_hypothesis):
          is_more_general_than_other = True
          break
      if not is_more_general_than_other:
        new_s.add(hypothesis)
    self._S = new_s

  def caso_negativo(self, example: tuple[str, ...]): # Nombre provisional
    """ Handle negative examples. """
    # Eliminar de S las hipótesis que cubran el ejemplo.
    new_s = set()
    for hypothesis in self._S:
      if not hypothesis.covers(example):
        new_s.add(hypothesis)
    self._S = new_s
    # Separar las hipótesis de G en dos conjuntos: las que cubren el ejemplo y las que no.
    new_g = set()
    not_new_g = set()
    for g_hypothesis in self._G:
      if g_hypothesis.covers(example):
        not_new_g.add(g_hypothesis)
      else:
        new_g.add(g_hypothesis)
    self._G = new_g
    # Generalizar mínimamente las hipótesis de G que cubran el ejemplo.
    new_g == set()
    for g_hypothesis in not_new_g:
      atribute_index = 0
      for g_atribute, example_atribute in zip(g_hypothesis._constraints, example):
        if g_atribute == "?":
          for s_hypothesis in self._S:
            if s_hypothesis._constraints[atribute_index] != "?" and s_hypothesis._constraints[atribute_index] != example_atribute:
              new_constraint = g_hypothesis._constraints[:atribute_index] + (s_hypothesis._constraints[atribute_index],) + g_hypothesis._constraints[atribute_index + 1:]
              new_hypothesis = Hypothesis(new_constraint)
              for other_hypothesis in self._S:
                if new_hypothesis.is_more_general_than(other_hypothesis):
                  new_g.add(new_hypothesis)
        atribute_index += 1
    self._G.update(new_g)
    # Eliminar de G las hipótesis que sean más específicas que otras hipótesis de G.
    new_g = set()
    for hypothesis in self._G:
      is_more_specific_than_other = False
      for other_hypothesis in self._G:
        if hypothesis != other_hypothesis and other_hypothesis.is_more_general_than(hypothesis):
          is_more_specific_than_other = True
          break
      if not is_more_specific_than_other:
        new_g.add(hypothesis)
    self._G = new_g