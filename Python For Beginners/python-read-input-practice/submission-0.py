def add_two_numbers() -> int:
    user_input = input()
    splitted = user_input.split(",")
    res = 0
    for i in splitted:
      res += int(i)
    return res


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
