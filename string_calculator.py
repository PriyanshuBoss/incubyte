
def add(numbers: str) -> int:
    if not numbers:
        return 0
    return sum(map(int, numbers.split(",")))

print(add(""))  # 0
print(add("1"))  # 1
print(add("1,5")) #6