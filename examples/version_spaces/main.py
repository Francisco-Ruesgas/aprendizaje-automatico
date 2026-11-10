from aprendizaje_automatico.version_spaces.candidate_elimination import CandidateElimination

example = ("japon","honda","azul",1980,"economico")
example1= ("japon","toyota","verde",1970,"deportivo")
example2=("japon","toyota","azul",1990,"economico")
example3=("eeuu","chrysler","azul",1980,"economico")
example4= ("japon","honda","blanco",1980,"economico")

model = CandidateElimination(5)
model.train(example, True)
model.train(example1, False)
model.train(example2, True)
model.train(example3, False)
model.train(example4, True)
print([h._constraints for h in model._G])
print([h._constraints for h in model._S])
