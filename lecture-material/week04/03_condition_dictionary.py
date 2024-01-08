# As Dictionary, only one of the statements can be true at a time otherwise there is a "unique key" problem.
def get_grade(score):
  return {
    90 <= score <= 100: "A",
    80 <= score < 90: "B",
    70 <= score < 80: "C",
    60 <= score < 70: "D",
    0 <= score < 60: "F"  # I added the condition 0 because otherwise negative inputs won't return "Invalid score"
  }.get(True, "Invalid score")

print(get_grade(85))