from pathlib import Path

def count_lines(filename):
    path = Path(filename)
    txt = path.read_text()
    lines = txt.split("\n")
    return len(lines)

n_lines = count_lines("spam.txt")
print(f"Number of lines: {n_lines}")


