import random

def generate_random_list(count):
    random_list = [random.randint(5, 1300) for _ in range(count)]
    print(", ".join(map(str, random_list)))

generate_random_list(23)