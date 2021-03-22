import random
import string


def six_letter_random_str():
    RANDOM_STR_LENGTH = 6
    textbank = string.ascii_lowercase * RANDOM_STR_LENGTH
    return ''.join(random.sample(textbank, RANDOM_STR_LENGTH))

def get_hash_url(hash=None):
    # TODO: get host from the env
    return f'http://localhost/{hash}' if hash else f'http://localhost/{six_letter_random_str()}'
