import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ",|\n"

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])  # Extract custom delimiter
        numbers = parts[1]

    return sum(map(int, re.split(delimiter, numbers)))


print(add(""))  # 0
print(add("1"))  # 1
print(add("1,5")) #6
print(add("1\n2,3"))  # 6
print(add("//;\n1;2"))  # 3