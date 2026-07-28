from typing import List

def read_integers() -> List[int]:
    res = []
    user_input = input()
    splitted = user_input.split(",")
    
    for i in splitted:
      res.append(int(i))
    return res


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
