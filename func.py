import random





def is_valid_pin(pin):
    return pin.isdigit() and len(pin) == 4

def generate_unique_id():
    unique_id = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    return unique_id