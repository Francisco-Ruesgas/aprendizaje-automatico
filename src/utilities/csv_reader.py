import csv


def parse_label(rows: list[list[str]]) -> list[tuple[str | bool, ...]]:
  """ Parse the label found at last position on each row """
  return [(*row[:-1], row[-1] == "True") for row in rows]

def read_csv(file_path: str) -> list[tuple[str | bool, ...]]:
  with open(file_path, newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    return parse_label(list(reader))