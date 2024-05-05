import random
from  helpers import NumericConstants 

def generate_random_number():
    random_value = random.randrange(NumericConstants.id_generation_max_range)
    return random_value

