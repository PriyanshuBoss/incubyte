import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, re.split(",|\n", numbers)))

print(add(""))  # 0
print(add("1"))  # 1
print(add("1,5")) #6
print(add("1\n2,3"))  # 6