from aprendizaje_automatico.version_spaces.candidate_elimination import (
  CandidateElimination,
)
from utilities.csv_reader import read_csv


def split_features_and_label(raw_examples: list[tuple[str, ...]]) -> list[tuple[tuple[str, ...], bool]]:
    """ Separate example and label"""
    return [(example[:5], example[5]) for example in raw_examples]
     
def main():
  file_path = "data/cars.csv"
  test_examples = split_features_and_label(read_csv(file_path))
  model = CandidateElimination(len(test_examples[0][0]))
  for example in test_examples:
     model.train(example[0], example[1])
  print([h._constraints for h in model._G])
  print([h._constraints for h in model._S])
    
if __name__ == "__main__":
  main()