import random
import string

def codigo_url():

    allowed_chars = ''.join((string.ascii_letters, string.digits))
    unique_id = ''.join(random.choice(allowed_chars) for _ in range(8))
    return str(unique_id)