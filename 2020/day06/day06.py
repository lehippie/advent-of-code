"""Day 6: Custom Customs."""

from pathlib import Path


INPUT_FILE = "groups_answers.txt"


def load_input(filename):
    """Import puzzle input."""
    filepath = Path(__file__).parent / filename
    data = [[]]
    with filepath.open() as f:
        for line in f:
            line = line.strip()
            if line:
                data[-1].append(line)
            else:
                data.append([])
    return data


# --- Part One ---

def anyone_questions(group):
    """Return questions answered "yes" by anyone."""
    return set(''.join(group))


def part_one(groups_answers):
    """Part One solution."""
    questions = [anyone_questions(g) for g in groups_answers]
    yes_count = sum(len(q) for q in questions)
    print(f"{yes_count} questions have been answered 'yes' by anyone.")
    assert yes_count == 6763


# --- Part Two ---

def everyone_questions(group):
    """Return questions answered "yes" by everyone."""
    questions = set(group[0])
    for g in group[1:]:
        questions = questions.intersection(g)
    return questions


def part_two(groups_answers):
    """Part Two solution."""
    questions = [everyone_questions(g) for g in groups_answers]
    yes_count = sum(len(q) for q in questions)
    print(f"{yes_count} questions have been answered 'yes' by everyone.")
    assert yes_count == 3512


# --- Tests ---

def tests():
    """Day tests."""
    # Part One
    test01 = load_input("test_input_01.txt")
    assert anyone_questions(test01[0]) == {"a", "b", "c", "x", "y", "z"}
    test02 = load_input("test_input_02.txt")
    test02_any = [anyone_questions(t) for t in test02]
    assert test02_any == [{"a", "b", "c"}] * 3 + [{"a"}] + [{"b"}]
    assert sum(len(t) for t in test02_any) == 11
    # Part Two
    test02_every = [everyone_questions(t) for t in test02]
    assert test02_every == [{"a", "b", "c"}, set(), {"a"}, {"a"}, {"b"}]
    assert sum(len(t) for t in test02_every) == 6


if __name__ == "__main__":
    tests()
    puzzle_input = load_input(INPUT_FILE)
    part_one(puzzle_input)
    part_two(puzzle_input)
