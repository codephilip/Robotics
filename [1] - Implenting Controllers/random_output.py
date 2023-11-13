import random

def get_random(output_list):
    return random.choice(output_list)

tmp = ["hi", "hello", "hi there"]
print(get_random(tmp))
