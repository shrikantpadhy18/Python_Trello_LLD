import random
from  helpers import NumericConstants 

def generate_random_number(model_type):
    prefix_value = get_prefix_based_on_model_type(model_type)

    random_value = prefix_value + str(random.randrange(NumericConstants.id_generation_max_range))
    return random_value

def get_prefix_based_on_model_type(model_type):

    prefixes_based_on_model = {
        "board" : "BO-",
        "card":"CA-",
        "user":"UD-",
        "list":"LS-"
    }

    return prefixes_based_on_model[model.value]

