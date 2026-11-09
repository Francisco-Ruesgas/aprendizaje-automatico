from aprendizaje_automatico.version_spaces.candidate_elimination import CandidateElimination

example = ("japon","honda","azul",1980,"economico")

model = CandidateElimination(5)
model.train(example, True)
print([h._constraints for h in model._G])
print([h._constraints for h in model._S])
