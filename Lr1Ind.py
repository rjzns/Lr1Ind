import random

random_list = [random.randint(5, 1300) for _ in range(23)]

print(", ".join(map(str, random_list)))