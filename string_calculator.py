import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ",|\n"

    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])  # Extract custom delimiter
        numbers = parts[1]

    num_list = list(map(int, re.split(delimiter, numbers)))

    negatives = [n for n in num_list if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")

    return sum(num_list)



print(add(""))  # 0
print(add("1"))  # 1
print(add("1,5")) #6
print(add("1\n2,3"))  # 6
print(add("//;\n1;2"))  # 3
print(add("1,-2,3,-4"))  # Raises exception: negative numbers not allowed -2, -4